# research plan 010 live check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_plan_010_live_check_20260516T053036_result.json`
- **Structured JSON:** [`20b072b0bf9ce2064f68.json`](../../sessions/20/20b072b0bf9ce2064f68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## plan_010 LIBERO-Spatial Extraction 状态

### GPU
| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| 0 | RTX PRO 6000 Blackwell | 84% | 16.5 / 95.6 GB |
| 1 | RTX PRO 6000 Blackwell | 83% | 16.5 / 95.6 GB |

两块 GPU 都在正常工作。

### 提取进度

| 条件 | 已完成 h5 | 当前任务 | 当前进度 | 速度 | 磁盘 |
|------|-----------|----------|----------|------|------|
| **Trained** (GPU 0) | 2 done + 1 in progress | [3/10] pick_up_black_bowl_in_top_drawer | 3282/7479 (44%) | ~40 step/s | 6.3G |
| **Untrained** (GPU 1) | 2 done + 1 in progress | [3/10] pick_up_black_bowl_in_top_drawer | 3454/7479 (46%) | ~39 step/s | 6.3G |

### 预估剩余时间
- 当前 task 3 剩余：~1.7 min
- 剩余 7 个 task，每个 ~2.6 min（按平均 ~6000 steps、~38 step/s 估算）
- **总预估剩余：~20 min**（两条件并行，同时完成）

### 错误
无。两个进程都在正常运行，无报错。只有 transformers 版本不匹配的 warning（不影响提取）。

---
