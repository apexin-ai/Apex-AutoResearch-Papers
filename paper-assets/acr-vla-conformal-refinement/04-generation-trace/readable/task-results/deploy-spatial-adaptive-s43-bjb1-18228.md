# deploy spatial adaptive s43 bjb1 18228

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_spatial-adaptive-s43-bjb1-18228_20260523T033610_result.json`
- **Structured JSON:** [`7db2dce68e2030237b3c.json`](../../sessions/7d/7db2dce68e2030237b3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个问题：

1. **cuda:3 不空闲** — PID 114507 正在跑 `π0.5 precompute`（`train_crm.py --precompute --model pi05 --benchmark long`），占用 9874 MiB。四张 GPU 全被 π0.5 precompute 占满（cuda:0-3 各一个进程）。

2. **checkpoint `crm_smolvla_3suite_v1` 不存在** — 可能的匹配：
   - `/root/autodl-tmp/checkpoints/crm_unified_4suite/crm_best.pt`（unified 4suite）
   - `/root/autodl-tmp/checkpoints/crm_pi05/spatial/crm_best.pt`（pi05 spatial）
   - `/root/autodl-tmp/checkpoints/crm_pi05_full/spatial/crm_best.pt`（pi05 full spatial）

**无法在 cuda:3 上部署**，因为该 GPU 正在被 π0.5 precompute 占用。需要你确认：

1. 是否等 precompute 完成后再部署？或者要 kill 掉 cuda:3 上的 precompute 进程（PID 114507）？
2. 用哪个 checkpoint？指定的 `crm_smolvla_3suite_v1` 不存在，上面列出了可用的 checkpoint。

---
