# code plan 701 download libero full train

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_701-download-libero-full-train_20260517T145454_result.json`
- **Structured JSON:** [`e3c74044538e2f23f928.json`](../../sessions/e3/e3c74044538e2f23f928.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Precompute 稳定运行，14.3 samples/s。1000/72507 (~1.4%)。预计 ~84 min 完成。训练正常推进，无需继续密集监控。

汇报总结：

---

### Part 1: LIBERO Object HDF5 数据下载 — 完成

- **下载方式**: HuggingFace `yifengzhu-hf/LIBERO-datasets` via `hf-mirror.com`（huggingface.co 和 utexas.box.com 均不可达）。先用 `huggingface_hub.snapshot_download` 并行下载，后用 `aria2c` 多线程加速剩余文件
- **数据路径**: `/root/autodl-tmp/libero_data/libero_object/`
- **数据量**: 10 个 HDF5 文件，共 7.0 GB，每个 50 demos（500 trajectories total）
- **遇到问题**: xet CDN 从中国访问慢/不稳定导致超时；`tomato_sauce` 文件首次下载损坏，重新下载后验证通过
- **全部 10 个文件 h5py 验证通过**

### Part 2: 多阶段 K=1 CRM 训练 — 已启动

- **训练任务 ID**: `train-crm-k1-accg-object-seed42-v2`
- **GPU**: bjb2-28827 cuda:0 (RTX 4090, 3.5GB 占用)
- **tmux session**: `train-crm-k1-accg-object-seed42-v2`
- **当前阶段**: Precompute (Phase 1) — SmolVLA 多阶段特征提取
  - 72507 training samples from 500 trajectories
  - 速度 ~14 samples/s, 预计 ~84 min 完成 precompute
  - 之后自动进入 Phase 2 训练 (50 epochs, batch_size=512)
- **参数**: `--loss_mode multi --lambda_dir 0.1 --lambda_tri 0.05 --lambda_mag 0.01 --max_correction_norm 0.2 --seed 42`
- **W&B run**: `crm-k1-v2-accg-multistage-object` in project `acr-vla-conformal-refinement`
- **日志**: `/root/acr-vla-conformal-refinement/logs/train_crm_k1_full.log`

---
