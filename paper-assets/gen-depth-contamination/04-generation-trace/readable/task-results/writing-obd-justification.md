# writing obd justification

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_obd-justification_20260514T084302_result.json`
- **Structured JSON:** [`471b43c6cca9a6a7c270.json`](../../sessions/47/471b43c6cca9a6a7c270.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

段落已插入 `experiments_c1.tex` 第 5.1 节末尾（K* boundary 与 Cross-Model Transfer 之间），约 130 词，覆盖了：

- OBD 在 3 个 model families 上一致的 accuracy 优势（38.2–42.3%），对比 random baseline 16.7%（+21.5–25.6pp）和 LLM zero-shot ~33%（+5.2–9.3pp）
- Ordinal-logreg MAE 最低但 pairwise AUC 近 chance（0.49 vs 0.61）——collapse to center 而非真正区分
- Multiclass LightGBM pairwise AUC 与 OBD 持平但 accuracy 和 MAE 均差
- OBD 三指标 balance 最优的结论
- 交叉引用 Section method 和 Appendix Table S3（LLM zero-shot）

---
