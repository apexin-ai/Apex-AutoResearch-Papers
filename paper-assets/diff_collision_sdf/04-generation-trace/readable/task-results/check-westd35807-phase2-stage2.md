# check westd35807 phase2 stage2

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd35807_phase2_stage2_20260527T184738_result.json`
- **Structured JSON:** [`c17e24a68b5b10526c76.json`](../../sessions/c1/c17e24a68b5b10526c76.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Stage 1 仍在运行，尚未完成。

**GPU 状态汇总：**

| GPU | PID | 运行时间 | 任务 | 状态 |
|-----|-----|---------|------|------|
| cuda:1 | 856552 | 4h 22m | Phase 2 Stage 1 (seed0, λ=0.005, 10K) | 7068/10000 (71%), ETA ~3h 46m |
| cuda:2 | 856471 | 4h 22m | Phase 2 s2_v4 (seed2, λ=0, 30K, resume) | 运行中 |
| cuda:3 | 341425 | 1d 6h 20m | spatial_bowl LoRA control (seed0, 30K) | 运行中 |
| cuda:0 | — | — | 空闲 | — |

**Stage 1 详情：**
- 当前 step 7068/10000，速度 ~4.63s/it（前期 ~1.21s/it，后期明显减速，可能是 eval/checkpoint 开销）
- 预估剩余 ~3h 46min，预计约 4 小时后完成
- loss 稳定在 0.03-0.04 区间，sdf ~0.03，ee ~0.02-0.03

**Stage 2 暂不启动**，等 Stage 1 跑完 10K 步后再提交。

---
