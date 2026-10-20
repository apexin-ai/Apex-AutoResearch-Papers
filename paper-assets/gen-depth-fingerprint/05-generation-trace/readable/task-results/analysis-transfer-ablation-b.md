# analysis transfer ablation B

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_transfer_ablation_B_20260519T072523_result.json`
- **Structured JSON:** [`578ffb25684f5e5271d1.json`](../../sessions/57/578ffb25684f5e5271d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个文件全部生成。结果摘要：

- **Mean cross-generator transfer F1 = 0.810** [95% CI: 0.796, 0.822]，远超 chance (0.5)，t=46.58, p<1e-10
- **对角线 (within-gen) 平均 F1 = 0.985**，off-diagonal 平均 = 0.810
- 最强 transfer: Py-2.8B → Py-1B (0.87)；最弱: Py-1B → Mi-7B (0.62)，仍超过 baseline
- 结论：depth signal 跨 generator 泛化，不是 generator identity confound

---
