# analysis qwen3 thinking data integrity

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen3-thinking-data-integrity_20260520T181825_result.json`
- **Structured JSON:** [`fa2f51b970fd863bd878.json`](../../sessions/fa/fa2f51b970fd863bd878.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

核查完成。结果：

**根因**：Dir-L 只读了 westd-25068 上的 exp028b intermediates（folio_0-165，166题），漏掉了 westd-16639 上的 remaining38（folio_166-203）。**不存在数据损坏或默认值填充问题。**

**关键数字**：
| | n | SC Correct | SC Accuracy |
|---|---|---|---|
| Dir-L | 166 | 139 | 83.73% |
| Dir-I3 | 204 | 176 | 86.27% |
| 166-subset 交叉验证 | 166 | 139 vs 139 | **完全一致** |
| remaining38 | 38 | 37 | 97.37% |

- remaining38 只有 `folio_203` 答错
- remaining38 正确率异常高（97.37%），显著拉升了 204 题的总平均

**论文建议**：
- Dir-I3 的 n=204, SC=86.27%, SICA=86.76% 是正确的全集数值
- Dir-L 的 83.73% 是 166-subset 上的正确结果，但不应作为完整 FOLIO 结果引用
- Dir-L 的 Table 需要补齐 remaining38 数据后重跑，或标注 n=166

报告已写入 `/root/symb_invariant_consensus/results/qwen3_thinking_data_integrity/report.json` 和 `report.md`。

---
