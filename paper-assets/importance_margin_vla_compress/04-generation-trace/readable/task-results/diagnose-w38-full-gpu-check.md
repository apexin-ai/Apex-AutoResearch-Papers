# diagnose w38 full gpu check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_w38_full_gpu_check_20260528T043630_result.json`
- **Structured JSON:** [`c3c5ef758a9683ee56cb.json`](../../sessions/c3/c3c5ef758a9683ee56cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-38929 GPU 诊断汇总

| GPU | 实验 | 状态 | 结果 |
|-----|------|------|------|
| **cuda:0** | eval_pi05_attn_k085_long_seed45_strict_w38 | **已完成** ✓ | SR=**52.0%**, 172min, EXIT_CODE=0 |
| **cuda:1** | eval_pi05_l2norm_k095_long_seed45_strict_w38 (PID 106960) | **运行中** | 已跑 37min，刚部署 |
| **cuda:2** | eval_pi05_l2norm_k085_long_seed45_strict_w38 | **已完成** ✓ | SR=**79.2%**, 138min, EXIT_CODE=0 |
| **cuda:3** | eval_pi05_attn_k05_long_seed45_strict_w38 (PID 990330) | **运行中** | 已跑 2h18m |

### 已完成实验 Per-task 详情

**Attn k=0.85 seed45 → SR=52.0%** (s42=50.0%, s43=52.4%, s44=49.4%, **s45=52.0%**, 4-seed mean≈50.9%)
| T0 | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 |
|----|----|----|----|----|----|----|----|----|-----|
| 18 | 60 | 38 | 56 | 44 | 84 | 64 | 58 | 10 | 88 |

**L2norm k=0.85 seed45 → SR=79.2%** (s42=78.6%, s43=77.6%, s44=76.6%, **s45=79.2%**, 4-seed mean≈78.0%)
| T0 | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 |
|----|----|----|----|----|----|----|----|----|-----|
| 98 | 96 | 82 | 100 | 80 | 96 | 6 | 90 | 52 | 92 |

**cuda:0 和 cuda:2 空闲，可部署新实验。** Registry 已更新为 DONE。

---
