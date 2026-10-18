# probe westd41074 westd27271 status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_probe_westd41074-westd27271-status_20260521T233225_result.json`
- **Structured JSON:** [`8b26b6bb59d8f0c1a3d1.json`](../../sessions/8b/8b26b6bb59d8f0c1a3d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。以下是结构化报告：

---

## GPU 进程探测报告（2026-05-22 07:33 UTC+8）

### 服务器概览

| 服务器 | GPU | 型号 | 显存占用 | GPU利用率 | 占用进程 |
|--------|-----|------|----------|-----------|----------|
| westd-41074 | 0 | RTX PRO 6000 Blackwell (96GB) | 10.3/95.6 GB | 32% | PID 715307 (eval_pi05_random_k0925) |
| westd-41074 | 1 | 同上 | 10.3/95.6 GB | 34% | PID 730309 (eval_pi05_random_k095) |
| westd-41074 | 2 | 同上 | 27.9/95.6 GB | 74% | PID 68539 (train_m96) |
| westd-41074 | 3 | 同上 | 26.9/95.6 GB | 0% | PID 59671 (train_m64_v6) |
| westd-27271 | 0 | 同上 | 31.3/95.6 GB | 91% | PID 362168 + PID 369092 (两个eval共享) |
| westd-27271 | 1 | 同上 | 41.2/95.6 GB | 0% | PID 921279 (train_m32) |

---

### 实验详情

#### 1. `train_openvla_sc_m96_seed42` — **ALIVE**
| 字段 | 值 |
|------|------|
| PID | 68539 |
| 服务器/GPU | westd-41074 / GPU 2 |
| 启动时间 | 2026-05-20 11:40（已运行 ~44h） |
| 进度 | step 77100/100000（77.1%）|
| 速度 | 0.5 sps（~100 sec/50步）|
| Loss | ~2.5-2.8 |
| VRAM | 28546 MiB |
| 预计完成 | ~May 22 20:00（剩余 ~12.7h）|
| 启动命令 | `CUDA_VISIBLE_DEVICES=2 HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 WANDB_MODE=offline python -u train_openvla_smart_compress.py --config configs/openvla_smart_compress_m96.yaml` |
| 日志 | `logs/train_openvla_sc_m96_seed42.log` |
| 启动方式 | nohup |

#### 2. `train_openvla_sc_m32_vtconly_seed42` — **ALIVE**
| 字段 | 值 |
|------|------|
| PID | 921279 |
| 服务器/GPU | westd-27271 / GPU 1 |
| 启动时间 | 2026-05-20 18:47（已运行 ~37h）|
| 进度 | step 79200/100000（79.2%）|
| 速度 | 0.5 sps |
| Loss | ~2.1-2.9 |
| VRAM | 42180 MiB |
| 预计完成 | ~May 22 18:00（剩余 ~10.5h）|
| 启动命令 | `CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 WANDB_MODE=offline python -u train_openvla_smart_compress.py --config configs/openvla_smart_compress_m32.yaml --resume checkpoints/openvla_sc_m32_seed42` |
| 日志 | `logs/train_openvla_sc_m32_seed42_resume.log` |
| 启动方式 | tmux session `train_openvla_sc_m32_seed42` |
| ⚠️ 注意 | Cron 标签含 "vtconly" 但实际 config 是 `openvla_smart_compress_m32.yaml`（非 vtconly），且带 `--resume` |

#### 3. `train_openvla_sc_m64_seed42_v6` — **ALIVE**
| 字段 | 值 |
|------|------|
| PID | 59671 |
| 服务器/GPU | westd-41074 / GPU 3 |
| 启动时间 | 2026-05-21 17:16（已运行 ~14h）|
| 进度 | step 29100/100000（29.1%）|
| 速度 | 0.6 sps |
| Loss | ~2.6-3.2 |
| VRAM | 27526 MiB |
| 预计完成 | ~May 23 17:30（剩余 ~34h）|
| 启动命令 | `CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 WANDB_MODE=offline python -u train_openvla_smart_compress.py --config configs/openvla_smart_compress_m64.yaml --wandb-run openvla_sc_m64_seed42_v6` |
| 日志 | `logs/train_m64v6.log` |
| 启动方式 | tmux（通过 bash -c pipe tee）|

#### 4. `eval_openvla_baseline_spatial_seed42_v3` — **ALIVE**
| 字段 | 值 |
|------|------|
| PID | 369092 |
| 服务器/GPU | westd-27271 / GPU 0（与 PID 362168 共享）|
| 启动时间 | 2026-05-22 06:43（已运行 ~50min）|
| 进度 | Task 3/10 进行中，Task1 SR=86%, Task2 SR=96% |
| 速度 | ~2.1 eps/min |
| 预计完成 | ~May 22 10:20（剩余 ~2.8h）|
| 启动命令 | `CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode baseline --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-spatial --unnorm_key libero_spatial --suite libero_spatial --num_episodes 50 --gpu 0 --seed 42` |
| 日志 | `logs/eval_openvla_baseline_spatial_seed42_v3.log` |
| 启动方式 | nohup |

#### 5. `eval_pi05_random_k0925_object_seed42` — **ALIVE**
| 字段 | 值 |
|------|------|
| PID | 715307 |
| 服务器/GPU | westd-41074 / GPU 0 |
| 启动时间 | 2026-05-22 05:53（已运行 ~1.7h）|
| 进度 | Task 8/10 完成，Total SR=27.8%（125/450）, 耗时 98min |
| 预计完成 | ~May 22 07:55（剩余 ~22min）|
| 启动命令 | `python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.925 --suite libero_object --n_episodes 50 --seed 42 --gpu 0` |
| 日志 | `logs/eval_pi05_random_k0925_object_seed42.log` |

#### 6. `eval_pi05_random_k095_object_seed43` — **ALIVE**
| 字段 | 值 |
|------|------|
| PID | 730309 |
| 服务器/GPU | westd-41074 / GPU 1 |
| 启动时间 | 2026-05-22 06:14（已运行 ~1.3h）|
| 进度 | Task 8/10 完成，Total SR=73.8%（332/450）, 耗时 77min |
| 预计完成 | ~May 22 07:50（剩余 ~16min）|
| 启动命令 | `python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.95 --suite libero_object --n_episodes 50 --seed 43 --gpu 0` |
| 日志 | `logs/eval_pi05_random_k095_object_seed43.log` |

#### 7. `eval_pi05_l2norm_k0925_object_seed42` — **DEAD ❌**
| 字段 | 值 |
|------|------|
| PID | 985039 |
| 状态 | 两台服务器均不存在此 PID |
| 日志 | 未找到 `*l2norm_k0925*` 日志文件 |
| 结论 | 已崩溃或完成，无残留痕迹 |

---

### 额外发现：未追踪的活跃进程

| PID | 服务器/GPU | 命令 | 进度 |
|-----|-----------|------|------|
| 362168 | westd-27271 / GPU 0 | `python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.5 --suite libero_object --num_episodes 50 --seed 42` | Task 2/10 进行中 (T1 SR=56%) |

此进程不在 Cron 追踪列表中，但占用 westd-27271 GPU 0 共 15961 MiB 显存，与 PID 369092 共享同一 GPU。

---
