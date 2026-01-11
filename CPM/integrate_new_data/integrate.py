import os
import pandas as pd


def split_excel_to_max_size(
    input_filepath: str,
    output_dir: str | None = None,
    max_mb: int = 5,
    sample_rows: int = 5000,
    base_output_name: str | None = None,
) -> list[str]:
    """
    Split an Excel file into multiple Excel files, each <= max_mb (approximately enforced by checking actual file size).
    Works best for "data table" sheets (values). Formatting/objects are not preserved.

    Args:
        input_filepath: path to the source .xlsx
        output_dir: directory where parts are written (default: alongside input in "<name>_split")
        sheet_name: sheet index or name to split (default: first sheet)
        max_mb: max size per output file in MB (default: 5)
        sample_rows: rows used to estimate bytes/row (default: 5000)
        base_output_name: base name for output files (default: input filename without extension)

    Returns:
        List of output filepaths created.
    """
    if not os.path.isfile(input_filepath):
        raise FileNotFoundError(f"Input file not found: {input_filepath}")

    max_bytes = max_mb * 1024 * 1024

    in_dir = os.path.dirname(os.path.abspath(input_filepath))
    in_stem = os.path.splitext(os.path.basename(input_filepath))[0]
    if base_output_name is None:
        base_output_name = in_stem

    if output_dir is None:
        output_dir = os.path.join(in_dir, f"{in_stem}_split")
    os.makedirs(output_dir, exist_ok=True)

    # Read the sheet (values)
    df = pd.read_csv(input_filepath, sep=';', encoding='utf-8', dtype=object)
    n = len(df)
    if n == 0:
        return []

    def _write_chunk(df_chunk: pd.DataFrame, part_idx: int) -> tuple[str, int]:
        out_path = os.path.join(output_dir, f"{base_output_name}_part_{part_idx:03d}.csv")
        df_chunk.to_csv(out_path, index=False, sep=';', encoding='utf-8')
        return out_path, os.path.getsize(out_path)

    # Estimate bytes/row using a sample file
    sr = min(sample_rows, n)
    tmp_path, tmp_size = _write_chunk(df.iloc[:sr].copy(), part_idx=0)
    os.remove(tmp_path)

    bytes_per_row = max(1.0, tmp_size / max(1, sr)) * 1.05
    est_rows_per_file = max(1, int(max_bytes / bytes_per_row))

    outputs: list[str] = []
    part = 1
    start = 0

    while start < n:
        # Initial guess
        end = min(n, start + est_rows_per_file)
        out_path, size = _write_chunk(df.iloc[start:end].copy(), part_idx=part)

        # If too large, refine with binary search to fit under max_bytes
        if size > max_bytes and (end - start) > 1:
            os.remove(out_path)

            lo = start + 1
            hi = end
            best_end = lo

            while lo <= hi:
                mid = (lo + hi) // 2
                trial_path, trial_size = _write_chunk(df.iloc[start:mid].copy(), part_idx=part)

                if trial_size <= max_bytes:
                    best_end = mid
                    os.remove(trial_path)
                    lo = mid + 1
                else:
                    os.remove(trial_path)
                    hi = mid - 1

            # Write final chunk (<= max_bytes)
            out_path, _ = _write_chunk(df.iloc[start:best_end].copy(), part_idx=part)
            outputs.append(out_path)
            start = best_end
        else:
            outputs.append(out_path)
            start = end

        part += 1

    return outputs

def integrate_new_data(folder: str, new_data_folder: str) -> None:
    file_names = os.listdir(folder)
    if not os.path.exists(new_data_folder):
        os.mkdir(new_data_folder)


    for file_name in file_names:
        file_path = f"{folder}{os.sep}{file_name}"
        split_excel_to_max_size(file_path, output_dir=new_data_folder)


if __name__ == '__main__':
    base_folder = ""
    folder = rf"{base_folder}{os.sep}new_ppm_data"
    new_data_folder =  rf"{base_folder}{os.sep}new_ppm_data_integrated"
    integrate_new_data(folder, new_data_folder)
