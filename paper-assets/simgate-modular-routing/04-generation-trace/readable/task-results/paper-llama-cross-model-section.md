# paper llama cross model section

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_llama-cross-model-section_20260515T095427_result.json`
- **Structured JSON:** [`1c0d7ad9d3f60abd12ae.json`](../../sessions/1c/1c0d7ad9d3f60abd12ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两处修改完成：

1. **experiments.tex** — 在 §4.3 Router Training as Diagnostic 之后新增 §4.4 Cross-Model Verification，包含：
   - Llama-3.1-8B pilot 定位（mechanism verification, N=20）
   - 坦承 Llama 能力弱但方向一致
   - freeze 和 find-non-living-thing 两个 task 的具体数据
   - 对比表格（Table `cross-model`）列出两个模型的 death rate 和 label 分布
   - 结尾定位为 preliminary directional evidence

2. **main.tex** — Limitations 段首句后插入一句，引用 §cross-model 并明确 full-scale validation 是 future work。

---
