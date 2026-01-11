from enum import Enum


class Field(Enum):
    # PARCELLE
    IDU = "idu"
    COMMUNE = "commune"
    ADRESSE = "adresse"
    SUF = "SUF"
    NAT_CAD = "nature"
    CONTENANCE = "contenance"
    CONTENANCE_SUF = "contenance_suf"

    # DROITS
    CODE_DROIT = "droit"
    LBL_DROIT = "droit_long"
    MAJIC = "MAJIC"
    SIREN = "SIREN"
    CLASSEMENT_PPT = "groupe"
    FORME_JURIDIQUE_ABR = "forme"
    FORME_JURIDIQUE = "forme_longue"
    DENOMINATION = "dénomination"

def plot_fields() -> list[Enum]:
    return [
        Field.IDU,
        Field.SUF,
        Field.CONTENANCE,
        Field.CONTENANCE_SUF,
        Field.ADRESSE,
        Field.NAT_CAD,
        Field.COMMUNE,
    ]

def right_fields() -> list[Enum]:
    return [f for f in Field if f not in plot_fields()]
