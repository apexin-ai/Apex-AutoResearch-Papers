# eval exp9 bootstrap ci v2

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp9-bootstrap-ci-v2_20260518T164825_result.json`
- **Structured JSON:** [`c633faa013ccd8813122.json`](../../sessions/c6/c633faa013ccd8813122.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Exp9 Bootstrap CI 完成。结果汇总：

## Bootstrap 95% CI (BCa, 10K resamples)

### DD OOD (Deceptive Delight)
| Variant | K=1 | K=2 | K=3 | K=5 | Full |
|---------|-----|-----|-----|-----|------|
| 9class | .991 [.919,1.00] | .981 [.884,1.00] | .971 [.827,1.00] | .997 [.943,1.00] | .997 [.943,1.00] |
| binary | 1.00 [1.00,1.00] | .997 [.951,1.00] | .984 [.921,1.00] | 1.00 [1.00,1.00] | 1.00 [1.00,1.00] |
| scrambled | .997 [.937,1.00] | .981 [.882,1.00] | .975 [.848,1.00] | .997 [.953,1.00] | .997 [.942,1.00] |
| jb_mlm | .973 [.908,1.00] | .994 [.936,1.00] | .997 [.949,1.00] | .997 [.949,1.00] | .913 [.645,1.00] |
| wiki_mlm | .912 [.717,1.00] | .910 [.694,.991] | .936 [.731,.990] | .922 [.669,.990] | .903 [.588,.991] |
| topic | .590 [.299,.723] | .592 [.247,.743] | .568 [.234,.730] | .572 [.204,.762] | .541 [.186,.737] |
| vanilla | .441 [.258,.643] | .339 [.244,.532] | .296 [.236,.407] | .270 [.202,.341] | .270 [.202,.341] |

### ActorAttack
| Variant | K=1 | K=5 | Full |
|---------|-----|-----|------|
| 9class | .772 [.650,.863] | .966 [.840,1.00] | .972 [.855,1.00] |
| binary | .735 [.542,.841] | .987 [.894,1.00] | .990 [.926,1.00] |
| scrambled | .718 [.576,.921] | .936 [.757,.991] | .950 [.792,1.00] |
| jb_mlm | .734 [.492,.960] | .928 [.831,.990] | .893 [.671,.980] |
| vanilla | .336 [.226,.452] | .261 [.208,.325] | .257 [.203,.314] |

### RoBERTa DD OOD
| Variant | K=1 | Full |
|---------|-----|------|
| rob_9class | .987 [.885,1.00] | .994 [.943,1.00] |
| rob_mlm | .796 [.615,1.00] | .906 [.784,1.00] |
| rob_vanilla | .912 [.610,.991] | .981 [.883,1.00] |

## Paired Permutation Tests (p-values)

| Comparison | DD OOD (all K) | ActorAttack (all K) |
|------------|---------------|---------------------|
| **9class vs vanilla** | **p=0.0000** (all seeds, all K) | **p=0.0000** (all seeds, all K) |
| 9class vs jb_mlm | max_p=1.0 (not significant) | max_p≥0.40 (not significant) |
| 9class vs scrambled | max_p=1.0 (not significant) | max_p=1.0 (not significant) |

**核心结论**：9class 显著优于 vanilla（p<0.0001），与 jb_mlm 和 scrambled 无显著差异。CIs 因小样本（n=118）较宽，但 9class 与 vanilla 的 CI 完全不重叠。结果已保存至 `results/exp9_bootstrap_ci.json`，registry 已更新为 DONE (success)。

---
