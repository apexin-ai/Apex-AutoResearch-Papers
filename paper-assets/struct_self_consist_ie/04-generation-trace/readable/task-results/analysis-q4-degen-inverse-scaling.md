# analysis q4 degen inverse scaling

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_q4_degen_inverse_scaling_20260523T090138_result.json`
- **Structured JSON:** [`8356edbe03cb06f4344f.json`](../../sessions/83/8356edbe03cb06f4344f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果写入 `artifacts/q4_degen_inverse_scaling.md`。

**核心发现**：

| 分组 | Transitions | Inverse 比例 |
|------|------------|-------------|
| Degenerate | 54,411 | **1.3%** |
| Non-degenerate | 141,264 | **11.1%** |

Fisher exact: OR=0.109, p≈0 (***)

**结论**：Degenerate instances 几乎不会出现 inverse scaling（1.3% vs 11.1%，~9× 差异）。5/6 数据集 p<0.001 显著，唯一不显著的 SciERC-PT 是因为 degenerate 实例太少（81个）导致 underpowered。

关键 pattern：
- N≥4 时 degenerate inverse scaling 接近 0%（只有 2→4 transition 有少量，因为 N=2 时 degeneracy 信号弱）
- Pretrained 比 finetuned 效应更强（OR=0.066 vs 0.166），因为 pretrained 整体 inverse scaling 更高
- 这强力支持 diagnostic framework：degeneracy = model certainty → 免疫 inverse scaling

---
