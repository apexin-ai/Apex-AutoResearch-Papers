# research plan b literature

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_plan-b-literature_20260526T095830_result.json`
- **Structured JSON:** [`e5ae0afa5878dd7ae62e.json`](../../sessions/e5/e5ae0afa5878dd7ae62e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成，已追加到 memory.md。核心发现总结：

**最相关的论文**:
- **QDepth-VLA** (2025) — 明确指出 naïve depth auxiliary supervision 对 VLA 有害的三个机制（监督噪声、冗余信号、干扰预训练表征），但缺乏 controlled experiment。我们的 2×2 factorial design 填补这个空白。
- **ForkMerge** (NeurIPS 2023) — 负迁移的 optimization + generalization 双层解释，直接对应我们的 Full OCC vs Detach vs Vanilla 结果。

**形成清晰对比的模式**: 成功的 VLA 空间增强方法（SpatialVLA, GeoVLA, Spatial Forcing）都把 3D 信息作为 **input 或 alignment target**，而非让 shared backbone 去 predict dense spatial output。AuxVLA 的成功辅助任务是 action-relevant sparse 任务（joint config, grasp affordance），而非 dense spatial prediction。

**VLA Safety 竞品**: VLSA/AEGIS（post-hoc constraint, SafeLIBERO benchmark）和 SafeVLA（constrained RL）都不走 auxiliary supervision 路线——我们的负面结果解释了为什么。

**论文 framing 建议**: 定位为 "mechanism analysis" 而非 "failure report"，核心叙事是两层干扰机制（梯度冲突 + capacity competition），用正面结果论文做对比论证。

---
