# diagnose smollm3 3b s43 17855

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_smollm3_3b_s43_17855_20260520T183818_result.json`
- **Structured JSON:** [`b6df6609774ff2a51892.json`](../../sessions/b6/b6df6609774ff2a51892.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验没有失败。** 结果如下：

- **EXIT_CODE = 0**（成功）
- **训练进度：全部 11 代完成**（gen_0 ~ gen_10），all_metrics.json 包含完整的 11 条记录
- **完成时间：2026-05-21 02:28**
- **总耗时：约 18.5 小时**（gen_0 始于 05-20 08:28，gen_10 完成于 05-21 02:28）

### Metrics 摘要（α=1.0, seed=43, SmolLM3-3B）

| Gen | PPL | Token Entropy | Eff Rank | MAUVE |
|-----|-----|--------------|----------|-------|
| 0 | 13.25 | 2.56 | 45.5 | 0.032 |
| 1 | 81.83 | 0.96 | 84.3 | 0.033 |
| 5 | 296.5 | 0.95 | 102.2 | 0.033 |
| 10 | 449.3 | 1.17 | 78.7 | 0.034 |

PPL 从 13→449 单调上升，token_entropy gen0→gen1 骤降（2.56→0.96 然后平稳），符合 α=1.0 的强 collapse 预期。

**结论：westd-17855 上的实验已成功完成，不存在失败。** 如果之前的监控系统报告了失败，可能是因为 EXIT_CODE=129 (SIGHUP) 的误判（参考 C005 约束），或者是在实验仍在运行时检查了状态。

---
