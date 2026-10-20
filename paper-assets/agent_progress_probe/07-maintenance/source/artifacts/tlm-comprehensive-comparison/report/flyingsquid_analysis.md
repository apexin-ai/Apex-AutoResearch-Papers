# FlyingSquid Detailed Analysis

## Overview

FlyingSquid (triplet-based generative label model) fitted on 54,809 windows with 3 LFs.

- **MV agreement**: 82.04% (9,841 disagreements)
- **All disagreements are progress→stagnation**: FlyingSquid systematically over-predicts stagnation
- **Label distribution**: MV: 71.5% progress / 28.5% stag → FS: 53.6% progress / 46.4% stag

## Agreement by Confidence Level

| Confidence | N windows | Agreement | FS→stag | FS→prog |
|---|---|---|---|---|
| 1 (low) | 39,408 | 79.0% | 8,276 | 0 |
| 2 (medium) | 14,609 | 89.3% | 1,565 | 0 |
| 3 (high) | 792 | 100% | 0 | 0 |

Key: FlyingSquid never flips stagnation to progress. All divergence is unidirectional.

## Top Disagreement LF Vote Patterns

These are the LF vote patterns where FS disagrees with MV (all cases: MV=progress, FS=stagnation):

| Pattern (file_diff / cmd_rep / outcome_bp) | Count | % of disagree |
|---|---|---|
| abstain / progress / stagnation | 3,461 | 35.2% |
| progress / stagnation / abstain | 3,131 | 31.8% |
| progress / abstain / stagnation | 1,684 | 17.1% |
| progress / progress / stagnation | 1,529 | 15.5% |
| progress / stagnation / progress | 28 | 0.3% |
| stagnation / progress / progress | 8 | 0.1% |

**Pattern**: FS flips to stagnation primarily when outcome_backpropagation abstains or votes stagnation, regardless of file_diff_delta signal. FS appears to weight the abstain-heavy outcome_bp LF more than MV does.

## Downstream Probe Results

Probe trained on FS labels vs MV labels (cross-eval on MV conf≥2 test set):

| Metric | MV Probe | FS Probe | Delta |
|---|---|---|---|
| Conf≥2 Macro-F1 | 0.8946 | 0.7816 | −11.3pp |
| MV-All Macro-F1 | 0.8468 | 0.7343 | −11.3pp |
| Self Macro-F1 | 0.8468 | 0.8186 | −2.8pp |

## Conclusion

FlyingSquid is a negative baseline. Its triplet-based method treats LF votes as i.i.d., ignoring temporal structure. This leads to systematic stagnation bias, especially when outcome_backpropagation abstains (which is common in our data). The downstream probe trained on FS labels loses 11pp on the gold-proxy evaluation.
