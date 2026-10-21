# paper writing cosine failure

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_cosine_failure_20260520T074932_result.json`
- **Structured JSON:** [`e0bac0e80f8b34d45cef.json`](../../sessions/e0/e0bac0e80f8b34d45cef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

§4 已写入 `docs/paper/sections/cosine_failure.tex`，约 700 words。

结构：
- **开头**：从 §3 的 discriminability 结果过渡，预告 4-experiment diagnostic chain
- **Table 1** (`tab:cosine_chain`)：4 行总结 F1a--F1d 的配置、公式、outcome、root cause
- **F1a**：tanh gate saturation，norm mismatch 导致梯度消失
- **F1b**：raw cosine gap 仅 0.098，信号被 R3 方差淹没
- **F1c**：recalibration 把 AUROC 提到 0.91 但引入 reward discontinuity，导致 mode collapse
- **F1d**：5x scaling 放大 noise，R3 step 100 饱和后 R1 独撑但 oscillate，终端 collapse
- **Unified diagnosis**：cosine projection 把 warranted revision 和 unwarranted capitulation 混为一谈，方向编码 belief change direction 但不编码 warrant；过渡到 §5 binary probe

---
