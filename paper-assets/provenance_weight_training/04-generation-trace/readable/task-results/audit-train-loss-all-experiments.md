# audit train loss all experiments

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_train_loss_all_experiments_20260514T144356_result.json`
- **Structured JSON:** [`09f19181e021aa9d7751.json`](../../sessions/09/09f19181e021aa9d7751.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部提取成功。对比结果：

| exp_id | registry_train_loss | verified_train_loss | match? |
|--------|--------------------|--------------------|--------|
| grid_b0_5_seed123 | 9.601 | 9.6009 | ✓ |
| grid_b1_0_seed123 | 10.218 | 10.2183 | ✓ |
| grid_b1_5_seed123 | 10.4776 | 10.4776 | ✓ |
| grid_b2_0_seed123 | 10.61 | 10.6104 | ✓ |
| grid_b3_0_seed123 | 10.7422 | 10.7422 | ✓ |
| uniform_seed42 | 7.3104 | 7.3104 | ✓ |
| uniform_seed123 | 7.3121 | 7.3121 | ✓ |
| uniform_seed456 | 7.2895 | 7.2895 | ✓ |
| adaptive_seed42 | 9.2665 | 9.2665 | ✓ |
| adaptive_seed123 | 9.2665 | 9.2665 | ✓ |
| adaptive_seed456 | 9.2354 | 9.2354 | ✓ |

**结论：全部 11 个已完成实验的 registry train_loss 与 HF Trainer 日志摘要一致，无误录。**

之前报告的 3 个 bug 案例（grid_b3_0_seed123, grid_b2_0_seed123, grid_b_seed42_batch）中，grid_b3_0_seed123 和 grid_b2_0_seed123 的 registry 值现在是正确的——说明已经被修正过了。grid_b_seed42_batch 当前 RUNNING，未在本次审计范围内。

---
