# analysis inverse scaling status

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_inverse-scaling-status_20260523T194751_result.json`
- **Structured JSON:** [`ba9322889d66f3fc2c89.json`](../../sessions/ba/ba9322889d66f3fc2c89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

计算已完成，状态报告写入 `artifacts/inverse_scaling_server_status.md`。

核心结果：
- 全部 9 个配置运行成功，无活跃进程
- Inverse scaling 跨种子可复现：Qwen N=8 的 4 个种子中，4/21 transitions 在所有种子上都显著 inverse（lp_weighted/theta2n/uniform 在高 N 时）
- LLaMA 跨种子一致性更高（90%）
- `majority_vote` 和 `lp_best` 在所有种子/模型上都不出现 inverse scaling
- "40 of 58 transitions" claim 无需更新，但可补充 cross-seed reproducibility 的论据
- 完整分析已在本地 `artifacts/multiseed_inverse_scaling_report.md`

---
