from .s1_embedding import compute as compute_s1
from .s2_minkpp import compute as compute_s2
from .s3_constat import compute as compute_s3
from .s4_selfcritique import compute as compute_s4

SIGNAL_MAP = {
    "s1": compute_s1,
    "s2": compute_s2,
    "s3": compute_s3,
    "s4": compute_s4,
}
