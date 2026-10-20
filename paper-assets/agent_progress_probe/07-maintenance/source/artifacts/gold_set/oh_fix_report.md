# OH Annotation Matching Fix Report

## Problem
Gold set evaluation only matched 132/199 annotations. 63 OpenHands (OH) windows were unmatched because OH data was never merged into the main `data/windows_labeled.jsonl`.

## Root Cause
- `data/windows_labeled.jsonl` contained only SWE-agent windows (59,496 entries)
- OH windows existed separately at `/root/autodl-tmp/openhands_data/windows_labeled.jsonl` (154,743 entries)
- The `prepare_openhands_data.py` pipeline generated OH windows but never merged them
- Additionally, both SWE-agent and OH use `row_index` 0-4999 (referencing different trajectory files), requiring source-aware trajectory lookup for structural features

## Fix Applied
1. **Merged OH windows** into `data/windows_labeled.jsonl` (59,496 + 154,743 = 214,239 total)
2. **Patched `evaluate_gold_set.py`** to load OH trajectory file separately (`--oh_trajectories`) and route structural feature extraction by source
3. **Backed up** original files: `data/windows_labeled.jsonl.bak`, `evaluate_gold_set.py.bak`

## Verification
- **Before fix**: 132/199 matched (all SWE-agent, 0 OH)
- **After fix**: 195/199 matched (132 SWE-agent + 63 OH)
- **4 unmatched**: All SWE-agent entries with confidence=0 (all LFs abstained -> majority_label=-1 -> excluded from non-abstain set)
  - `horejsek__python-fastjsonschema-140__swe-agent-llama-70b__r1841__w1`
  - `just-work__fffw-64__swe-agent-llama-70b__r3549__w4`
  - `beetbox__beets-3869__swe-agent-llama-70b__r2190__w17`
  - `openstack-charmers__zaza-36__swe-agent-llama-70b__r2306__w18`

## Impact on Results

### MV-Gold Agreement (n=195)
| Metric | Before (n=132) | After (n=195) | Delta |
|--------|----------------|---------------|-------|
| Agreement rate | 0.7348 | 0.7487 | +0.014 |
| Macro-F1 | 0.7304 | 0.7184 | -0.012 |
| Accuracy | 0.7348 | 0.7487 | +0.014 |

### Structural RF (n=195 vs 132)
| Metric | Before (n=132) | After (n=195) | Delta |
|--------|----------------|---------------|-------|
| Macro-F1 | 0.7928 | 0.7564 | -0.036 |
| Accuracy | 0.7955 | 0.7795 | -0.016 |

### Structural GB (n=195 vs 132)
| Metric | Before (n=132) | After (n=195) | Delta |
|--------|----------------|---------------|-------|
| Macro-F1 | 0.7847 | 0.7595 | -0.025 |
| Accuracy | 0.7879 | 0.7846 | -0.003 |

### GRU Probe (unchanged, n=132 -- SWE-agent embeddings only)
| Metric | Value |
|--------|-------|
| Macro-F1 | 0.7348 |
| Accuracy | 0.7348 |

## Notes
- GRU Probe and TWV Probe still evaluate on SWE-agent only (n=132) since OH embeddings are in a separate file
- OH gold set is heavily imbalanced: 62 progress / 1 stagnation (98.4% progress)
- The macro-F1 decrease is expected: OH adds many easy-to-classify progress windows but also introduces 14 false negatives where MV labeled OH progress windows as stagnation
