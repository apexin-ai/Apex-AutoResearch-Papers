# ACIB: Action-Conditioned Information Bottleneck for VLA robustness.
# Soft-reweights or hard-prunes visual tokens before VLM processing,
# guided by language/state conditioning to retain action-relevant information.

from acib.config import ACIBConfig
from acib.scorer import ACIBScorer
from acib.losses import ACIBLoss
