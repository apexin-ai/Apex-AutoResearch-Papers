# cpu e4 deepseek parse filter

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_e4_deepseek_parse_filter_20260521T122251_result.json`
- **Structured JSON:** [`6dd5750cd367affc8df8.json`](../../sessions/6d/6dd5750cd367affc8df8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**"正交性"是 parse failure 伪信号。** 关键证据：

| 条件 | DeepSeek vs 其他3模型 Pearson r |
|------|------|
| 全集 (n=200) | 0.23–0.28 |
| DS parse-success (n=99) | 0.15–0.24（反降，因为去掉了 both-zero 锚点）|
| **所有模型 F1>0 (n=81)** | **0.60–0.70** |

- DeepSeek 50.5% 的 zero-F1 率（vs 其他模型 18-22%）产生了双峰分布，系统性压低 Pearson r
- 在所有模型都有有效输出的 81 个实例上，DeepSeek 与其他模型的相关性 r≈0.60-0.70，与三强模型之间的互相关（0.69-0.82）处于可比范围
- DeepSeek 的 ensemble 边际收益在 filtered 子集上加倍（+0.049→+0.099），说明它在成功 parse 时确实有价值，但这是 **error pattern diversity**（不同实例上失败），不是 capability orthogonality
- **Conclusion 3 需要重写**：应表述为"互补的失败模式"而非"正交的抽取能力"

报告已注册为 `e4_deepseek_parse_filter.md`（artifact ID: `art_20260521_58e9b0`）。

---
