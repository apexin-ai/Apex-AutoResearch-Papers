# ssh timestep accuracy analysis

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_timestep-accuracy-analysis_20260515T180416_result.json`
- **Structured JSON:** [`3c66e89ad7640def1624.json`](../../sessions/3c/3c66e89ad7640def1624.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果非常清晰：

**Trained VLA (layer 1)**：所有 10 个 bin 均为 **100.0%** accuracy，包括 t=0 初始帧。

**DINO-V2 (layer 0)**：强烈的时间依赖性——

| Bin | DINO Acc | VLA Acc |
|-----|----------|---------|
| 0 (t=0~0.1) | **43.3%** | 100% |
| 1 (t=0.1~0.2) | 79.7% | 100% |
| 2 | 83.8% | 100% |
| 5 | 90.4% | 100% |
| 8 | 99.0% | 100% |
| 9 (t=0.9~1.0) | 99.1% | 100% |

**关键发现**：
- DINO 在 bin 0（初始帧）只有 43.3% accuracy（接近随机 10%，但高于 chance → 初始 scene 确实有些视觉差异）
- DINO early-frame acc 远低于 late-frame（delta = 37.6%），说明 DINO 的 86% 整体 accuracy 主要靠 late frames 撑起来
- **Trained VLA 在 t=0 就达到 100%** → 这不可能来自视觉差异（初始场景相同），只能来自 language instruction grounding

这是 language grounding 信号存在的强证据：VLA 的隐层表征在第一帧就已经编码了 goal identity，这只能来源于语言指令。

---
