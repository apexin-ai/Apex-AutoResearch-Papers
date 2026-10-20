# code exp45 eval fix

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp45_eval_fix_20260522T065355_result.json`
- **Structured JSON:** [`f71578e042102007db22.json`](../../sessions/f7/f71578e042102007db22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results JSON 已经包含全部 7 个 N 值的完整数据，无需修复。

当前 `exp45_benign_adaptation_curve.json` 内容：

| N | wildchat_fpr | ood_dd_f1 | ood_aa_f1 | ood_fitd_f1 | train_size | time_min |
|---|---|---|---|---|---|---|
| 0 | 0.653 | 1.000 | 0.981 | 1.000 | 350 | 3.0 |
| 5 | 0.163 | 0.990 | 0.981 | 1.000 | 355 | 3.0 |
| 10 | 0.000 | 1.000 | 1.000 | 1.000 | 360 | 2.4 |
| 25 | 0.000 | 1.000 | 0.953 | 1.000 | 375 | 1.7 |
| 50 | 0.000 | 1.000 | 1.000 | 1.000 | 400 | 1.9 |
| **100** | **0.000** | **1.000** | **1.000** | **1.000** | **450** | **2.1** |
| **150** | **0.000** | **1.000** | **0.981** | **1.000** | **500** | **2.1** |

N=100 和 N=150 的数据完整存在，checkpoint 路径也已记录（在 `/root/autodl-tmp/persuasion_turn_jailbreak_detect/checkpoints/` 下）。可能之前已有人补跑过了。

---
