# probe westd 27271 gpu status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_probe_westd-27271-gpu-status_20260521T231343_result.json`
- **Structured JSON:** [`7f1569f5633a9ef970d6.json`](../../sessions/7f/7f1569f5633a9ef970d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态总结

| GPU | 状态 | PID | 实验 | 显存占用 | GPU 利用率 |
|-----|------|-----|------|----------|-----------|
| 0 | 占用 | 362168 | `eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.5 --suite libero_object --seed 42` | 15961 MiB / 97887 MiB | 11% |
| 0 | 占用 | 369092 | `eval_openvla_l2norm_libero.py --mode baseline --model_path openvla-7b-finetuned-libero-spatial --suite libero_spatial --seed 42` | 16064 MiB / 97887 MiB | |
| 1 | 占用 | 921279 | `train_openvla_smart_compress.py --config configs/openvla_smart_compress_m32.yaml --resume checkpoints/openvla_sc_m32_seed42` | 42180 MiB / 97887 MiB | 47% |

**空闲 GPU：无。** 两块 GPU 均被占用。

**PID 921279 状态：仍在运行。** 训练进程 `train_openvla_sc_m32_seed42` 在 GPU 1 上活跃（47% 利用率），对应 tmux session `train_openvla_sc_m32_seed42`（创建于 May 20）。最新日志 `train_openvla_sc_m32_seed42_resume.log` 最后更新于 07:12（2 分钟前），确认训练正在推进。

**Tmux sessions：**
- `train_openvla_sc_m32_seed42` — 1 window

**GPU 0 上同时跑了 2 个 eval 任务**（random_prune k=0.5 object + baseline spatial），共占 ~32 GiB，还剩 ~65 GiB 空闲显存。

---
