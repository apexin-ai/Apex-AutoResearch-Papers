# urgent gpu recovery and next batch

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_gpu_recovery_and_next_batch_20260521T155303_result.json`
- **Structured JSON:** [`27543090db9900cb0950.json`](../../sessions/27/27543090db9900cb0950.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. GPU 状态 — 两卡均被占用

| GPU | 利用率 | 显存 | 进程 |
|-----|--------|------|------|
| cuda:0 | 0% (CPU-bound Phase 2) | 15.2 / 97.9 GB | `openvla_long_pipeline_v1` |
| cuda:1 | 0% (CPU-bound Phase 2) | 8.6 / 97.9 GB | `tracvla_spatial_untrained_v1` |

两个实验都在运行，处于 Phase 2（Ridge probing），此阶段 CPU 密集，GPU 利用率显示 0% 是正常的。

### 2. 上一轮实验进度

**openvla_long_pipeline_v1 (cuda:0)** — 正在跑 trained 条件的 Phase 2
- Phase 1 完成: 5000 samples / 524.5s
- Phase 2 部分结果 (trained):
  - L0: img_mean=0.8762, last_pre=0.6539
  - L8: img_mean=0.8849, last_pre=0.8549
  - L16: img_mean=0.8815, last_pre=0.8627
  - L24: img_mean=0.8743, last_pre=0.8683
- 还需完成剩余层 + untrained 全条件，预计 1.5-2h

**tracvla_spatial_untrained_v1 (cuda:1)** — 正在跑 Phase 2
- Phase 1 完成: 5000 samples / 310.4s
- Phase 2 部分结果:
  - L0: img_mean=0.7761, last_pre=0.5911
  - L8: img_mean=0.7892, last_pre=0.6942
- 还需完成剩余层 + Phase 3-5，预计 1-1.5h

### 3. 新实验脚本就绪情况 — 两个都不存在

| 脚本 | 状态 | 可用模板 | Checkpoint |
|------|------|----------|------------|
| `nora_object_full_pipeline.py` | ❌ 不存在 | `nora_spatial_full_pipeline.py` | ❌ 无 `nora-libero-object` checkpoint |
| `tracvla_long_full_pipeline.py` | ❌ 不存在 | `tracvla_spatial_full_pipeline.py` + `libero_long_full_pipeline.py` | ✅ `tracevla-phi3v` 可用 |

### 4. 结论

**无需恢复实验——两个实验都在正常运行中。** GPU 并非空闲，只是处于 CPU 密集的 probing 阶段。

下一轮实验需要 Agent 决策：
1. **NORA Object**: 缺脚本 + 缺 checkpoint（checkpoints 目录无 `nora-libero-object`）
2. **TraceVLA Long**: 缺脚本（可从模板创建），checkpoint 可能可用

建议等当前两个实验完成后再提交新实验。

---
