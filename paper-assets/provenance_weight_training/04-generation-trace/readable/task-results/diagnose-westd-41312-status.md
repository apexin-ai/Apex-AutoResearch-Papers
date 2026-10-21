# diagnose westd 41312 status

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd-41312-status_20260518T165033_result.json`
- **Structured JSON:** [`03a2673662211a904db1.json`](../../sessions/03/03a2673662211a904db1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 eval 完成。汇总报告：

---

## 诊断结果

**4 个实验全部已完成训练（6102 步），原始 PID 已死。GPU 上正在运行新实验。**

| 实验 | PID 存活 | Final checkpoint | 完成时间 | Train loss (unweighted, last 100 steps avg) | Eval Loss | Eval PPL |
|---|---|---|---|---|---|---|
| `qwen06b_uniform_seed42` (实际目录 `_v2`) | 否 (PID 125995 死) | 有 (`qwen06b_uniform_seed42_v2/final/`) | May 18 05:51 | 1.9882 | 2.8733 | 17.69 |
| `ess_only_seed456` | 否 (PID 115525 死) | 有 (`ess_only_seed456/final/`) | May 18 07:07 | 1.9364 | 2.8770 | 17.76 |
| `ess_only_seed123` | 否 (PID 115021 死) | 有 (`ess_only_seed123/final/`) | May 18 07:25 | 2.0421 | 2.8747 | 17.72 |
| `random_reweight_seed456` | 否 (PID 125367 死) | 有 (`random_reweight_seed456/final/`) | May 18 08:29 | 1.9176 | 2.8779 | 17.78 |

**关键观察：**
- 4 个方法的 eval PPL 非常接近（17.69 ~ 17.78），差异很小
- uniform 略优（17.69），ess_only_seed123 次之（17.72），其余在 17.76-17.78
- ess_only 的 weighted_loss（2.39/2.55）远高于 unweighted_loss（1.94/2.04），反映了重要性加权的效果
- GPU 当前运行 4 个新实验：`uniform_1_7b_seed42_resumed`（GPU 0）、`adaptive_1_7b_seed42`（GPU 1）、`ngram_adaptive_seed42`（GPU 2）、`ngram_uniform_seed42`（GPU 3）

---
