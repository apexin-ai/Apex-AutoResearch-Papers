# code multiseed lambada eval

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_multiseed_lambada_eval_20260518T181921_result.json`
- **Structured JSON:** [`e94b5b78a3fd0f8ec355.json`](../../sessions/e9/e94b5b78a3fd0f8ec355.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

**Multi-seed 评测结论：lambada_openai 对 seed 完全不敏感**

| 模型 | acc | ppl | acc_stderr (bootstrap) |
|------|-----|-----|----------------------|
| GDN-pure | 0.5440 | 8.261 | 0.00694 |
| GDN-h24-1 | 0.5412 | 8.552 | 0.00694 |

所有已跑的 seed（0, 1, 4）对同一模型产生**完全相同**的结果（acc 和 ppl 一致到小数点后 16 位）。

**原因**：lambada_openai 是 0-shot 评测任务（无 few-shot 采样），seed 只控制 few-shot example 的随机选取。0-shot 下没有随机性，评测是完全确定性的。

**关于 GDN-pure vs GDN-h24-1 的差异**：
- acc 差值 = 0.0027（GDN-pure 略高）
- 根据 lm_eval 的 bootstrap stderr (~0.0069)，差值仅 0.39 个标准误，**不显著**
- 按原定判断标准（差值 > 2×std），由于 cross-seed std = 0，判据退化

**建议**：
1. Multi-seed 方案对 0-shot 任务无效，不需要继续跑剩余模型的多 seed
2. 如需统计显著性，应使用 lm_eval 自带的 bootstrap stderr（已有），或对 few-shot 任务（如 hellaswag、arc）做 multi-seed
3. GDN-pure 和 GDN-h24-1 在 lambada 上差异不显著

是否需要对 few-shot 任务（如 hellaswag 5-shot）做 multi-seed 评测？

---
