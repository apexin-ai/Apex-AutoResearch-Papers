# ops spon eval retry check

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_spon_eval_retry_check_20260515T200322_result.json`
- **Structured JSON:** [`9806b66c77813f70c080.json`](../../sessions/98/9806b66c77813f70c080.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已无残留。

## 报告

**(1) 日志关键内容**

`eval_spon_supp_retry.log`（32 行，4.5KB）完成了 5 步评估中的前 3 步：
- [1/5] True Dense PPL: **6.1173**
- [2/5] Dense with SPON biases folded: **6.1823**（degradation +0.0651）
- [3/5] TEAL sparsity: **0.4993**
- [4/5] TEAL sparse (no SPON): 开始后日志出现重复输出，**无 PPL 值**
- [5/5] 完全缺失

EXIT_CODE=0 来自 wrapper 脚本，但 Python 进程实际未完成全部评估。

**(2) 结果：部分失败**

步骤 4-5 的 TEAL sparse PPL 指标未产出。

**(3) 指标**

本次 retry 无新增指标。之前 worker (`worker_eval_spon_2048_supplementary`) 已成功获取的完整指标仍然有效：
| 指标 | 值 |
|------|-----|
| teal_sparse_no_spon_ppl | 12.0776 |
| teal_sparse_with_spon_ppl | 11.7907 |
| spon_recovery_teal | 4.8% |
| dense_with_spon_ppl | 6.1823 |

本次 retry 的步骤 1-2 结果与之前一致（dense PPL 6.1173/6.1823），确认数据无偏差。

**(4) Cron 状态**

`spon_supp_eval_retry` 在 MCP cron 和 session cron 中均不存在，无需删除。Registry 中也无此实验条目（非独立实验），无需更新。

**结论**：retry 部分失败但无影响——所需指标已由先前 worker 完整获取，无需重跑。

---
