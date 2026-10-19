# research next experiment prep

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_next-experiment-prep_20260516T032018_result.json`
- **Structured JSON:** [`77c10490475c4684bfb2.json`](../../sessions/77/77c10490475c4684bfb2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

方案已写入 `artifacts/next_experiment_plan.md` 并注册。

核心结构：

- **Phase 1** (Day 0): seed1 eval 4 suites，双卡并行 ~6h，这是 gate decision
- **Phase 2** (Day 0.5-2): ACIB-H k=0.8 训练 + seed2 重训并行，各 ~11h
- **Phase 3** (Day 2.5-5): 消融 A1(复用v4,0h训练) + A2 VIB-only + A3 Consistency-only
- **Phase 4** (Day 2.5-4): ACIB-S on smolvla_libero_plus（论文最关键互补性实验）

总 GPU 预算 ~85-103h，2 卡并行 wall-clock ~5-6 天，留 4-5 天 buffer 给补跑和论文写作。消融 A1 复用 v4 已有 collapse 数据省 11h 训练。消融只跑 libero_spatial 单 suite 节省时间。

---
