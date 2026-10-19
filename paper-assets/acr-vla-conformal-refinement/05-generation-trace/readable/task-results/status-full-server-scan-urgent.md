# status full server scan urgent

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_full-server-scan-urgent_20260522T112041_result.json`
- **Structured JSON:** [`e833ef80c78ea42795f1.json`](../../sessions/e8/e833ef80c78ea42795f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。汇总如下：

---

## 全局 GPU + 进程状态报告 (2026-05-22 19:21 UTC)

### bjb1-18228 — 4× RTX 4090

| GPU | 显存占用 | 利用率 | PID | 进程 |
|-----|---------|--------|-----|------|
| 0 | 11800/24564 MiB | 91% | 883211 | `python src/train_crm.py --precompute --benchmark long --K 10 --model pi05 --cache_dir .../crm_cache_pi05/ --shard_id 0 --num_shards 1` |
| 0 | (共享) | — | 907623 | `python -m lerobot.scripts.lerobot_eval --policy.path=.../smolvla_libero --env.task=libero_object --eval.n_episodes=20` |
| 1 | 10365/24564 MiB | 68% | 905254 | **进程已结束**（检查时消失） |
| 2 | 10365/24564 MiB | 24% | 905879 | `python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 43 --n_rollouts 20 --K 10` |
| 3 | 10365/24564 MiB | 13% | 906429 | `python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 44 --n_rollouts 20 --K 10` |

**空闲 GPU: GPU 1（进程 905254 刚结束，显存可能正在释放）**

---

### bjb1-32546 — 6× RTX 4090

| GPU | 显存占用 | 利用率 | PID | 进程 |
|-----|---------|--------|-----|------|
| 0 | 11802/24564 MiB | 26% | 218144 | `python src/evaluate.py --model pi05 --mode acr_vla --crm_checkpoint .../crm_pi05_full/object/crm_best.pt --benchmark object --seed 42` |
| 1 | 11802/24564 MiB | 62% | 218433 | 同上，`--seed 43` |
| 2 | 12265/24564 MiB | 25% | 218713 | 同上，`--seed 44` |
| 3 | 2/24564 MiB | 0% | — | **空闲** |
| 4 | 2/24564 MiB | 0% | — | **空闲** |
| 5 | 2/24564 MiB | 0% | — | **空闲** |

**空闲 GPU: GPU 3, 4, 5**

---

### bjb2-28827 — 6× RTX 4090

| GPU | 显存占用 | 利用率 | PID | 进程 |
|-----|---------|--------|-----|------|
| 0 | 12054/24564 MiB | 21% | 148761 | `python src/evaluate.py --model pi05 --mode acr_vla --crm_checkpoint .../spatial/crm_best.pt --benchmark spatial --seed 42` |
| 1 | 12054/24564 MiB | 22% | 149038 | 同上，`--seed 43` |
| 2 | 12054/24564 MiB | 22% | 149320 | 同上（推测 `--seed 44`） |
| 3 | 9883/24564 MiB | 20% | 206132 | `python src/train_crm.py --precompute --benchmark goal --K 10 --model pi05 --cache_dir .../crm_cache_pi05/ --shard_id 0 --num_shards 3` |
| 4 | 9883/24564 MiB | 21% | 206279 | 同上，`--shard_id 1 --num_shards 3` |
| 5 | 9883/24564 MiB | 22% | 206558 | 同上（推测 `--shard_id 2`） |

**空闲 GPU: 无**

---

### bjb2-40593 — 1× RTX 4090 D

| GPU | 显存占用 | 利用率 | PID | 进程 |
|-----|---------|--------|-----|------|
| 0 | 16436/24564 MiB | 57% | 952457 | `python experiments/robot/libero/run_libero_eval.py --pretrained_checkpoint .../openvla-oft/object --task_suite_name libero_object --num_trials_per_task 50 --seed 7` |

**空闲 GPU: 无**

---

## 实验汇总

| 实验类型 | 服务器 | GPU | 详情 |
|---------|--------|-----|------|
| **Pi05 CRM precompute (long, K=10)** | bjb1-18228 | GPU 0 | 单 shard，正在运行 |
| **Pi05 CRM precompute (goal, K=10)** | bjb2-28827 | GPU 3-5 | 3 shards 并行 |
| **SmolVLA eval (libero_object)** | bjb1-18228 | GPU 0 | lerobot_eval，20 episodes |
| **Pi05 vla_only eval (object)** | bjb1-18228 | GPU 2-3 | seed 43/44，各 20 rollouts |
| **Pi05 ACR-VLA eval (object)** | bjb1-32546 | GPU 0-2 | crm_pi05_full/object，seed 42/43/44 |
| **Pi05 ACR-VLA eval (spatial)** | bjb2-28827 | GPU 0-2 | crm_pi05_full/spatial，seed 42/43/44 |
| **OpenVLA-OFT eval (object)** | bjb2-40593 | GPU 0 | 50 trials/task，seed 7 |

## Cache 数据完整性

| 路径 | bjb1-18228 | bjb1-32546 |
|------|-----------|-----------|
| crm_cache_v5/object/manifest.json | ✓ May 14 | ✓ May 15 |
| crm_cache_v5/spatial/manifest.json | ✓ May 14 | ✓ May 15 |
| crm_cache_v5/goal/manifest.json | ✓ May 22 15:32 | ✓ May 22 19:19 |
| crm_cache_v5/long/manifest.json | ✓ May 22 16:51 | ✓ May 22 15:28 |
| crm_cache_k10/ | **不存在** | — |

4 个 suite 的 v5 cache manifest 在两台服务器上都完整。goal 和 long 的 manifest 今天刚更新。K10 cache 目录在 bjb1-18228 不存在。

## Unified CRM Checkpoint (bjb1-18228)

```
checkpoint_epoch0001.pt  — May 22 17:35
checkpoint_epoch0002.pt  — May 22 18:00
checkpoint_epoch0003.pt  — May 22 18:25
checkpoint_epoch0004.pt  — May 22 18:50
crm_best.pt              — May 22 18:50 (1.3MB)
```

每 epoch ~25 分钟，epoch 4 保存于 18:50。crm_best.pt 同时更新。

## 空闲 GPU 总计

- **bjb1-18228**: GPU 1（刚释放）
- **bjb1-32546**: GPU 3, 4, 5
- **bjb2-28827**: 无
- **bjb2-40593**: 无
- **总计可用: 4 张 RTX 4090**

---
