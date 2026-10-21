# paper writing related work

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_related_work_20260515T093527_result.json`
- **Structured JSON:** [`4b5c8c30d0a0b82f7520.json`](../../sessions/4b/4b5c8c30d0a0b82f7520.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Related Work 章节已写入 `docs/paper/section_related_work.tex`，约 600 words，严格遵循 4 段结构：

1. **Model Collapse Theory** — 从 Shumailov (Nature 2024) 的 tail erosion 出发，覆盖 Dohmatob scaling laws、MAD framework、accumulation/detection mitigation，以及 non-monotonic dynamics、heat death、contamination guarantees 等扩展工作。定位语：这些工作假设深度已知，我们估计深度本身。

2. **AI Text Detection** — DetectGPT → Fast-DetectGPT → Binoculars → DivEye → GLTR 的方法线，加 paraphrasing limits 和 distribution shift 的局限性分析。定位语：binary classification 丢弃 ordinal depth information。

3. **Adjacent Tasks** — EditLens（单次编辑程度）、attribution（哪个模型）、LOKI（benchmark）。定位语：互补维度，无一估计 recursive depth。

4. **Decoding Strategy Effects** — nucleus/temperature/top-k/Mirostat 的文献基础，收束到我们的 Depth Degradation Atlas 揭示 strategy-dependent degradation trajectories。

---
