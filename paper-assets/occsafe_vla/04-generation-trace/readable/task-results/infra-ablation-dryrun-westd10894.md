# infra ablation dryrun westd10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_ablation_dryrun_westd10894_20260521T020051_result.json`
- **Structured JSON:** [`13e47ccca09232bede41.json`](../../sessions/13/13e47ccca09232bede41.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成，磁盘恢复到 21G 可用。

---

## run_occ_detach.sh dry-run
- **脚本路径**: `/root/occsafe_vla/scripts/run_occ_detach.sh`
- **实际执行命令**: `WANDB_MODE=disabled CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py ... --occ_detach true --max_steps 5 --save_freq 3 --run_root_dir /root/autodl-tmp/checkpoints/dryrun_occ_detach --seed 42`
- **结果**: 成功
- **训练 log**: `Max step 5 reached! Stopping training...`
- **Checkpoint 产出**: 是（step 3 checkpoint 完整保存，含 model safetensors、action_head、occ_head、lora_adapter、proprio_projector）
- **注意**: 所有 occ label 加载均返回 `Failed to load occ label: Unable to synchronously open file (bad object header version number)` 警告，训练本身不受阻

## run_random_occ.sh dry-run
- **脚本路径**: `/root/occsafe_vla/scripts/run_random_occ.sh`
- **实际执行命令**: 同上，`--occ_detach true` 替换为 `--random_occ True`
- **结果**: 训练执行成功（跑完 5 步），但 checkpoint 保存失败
- **失败原因**: `SafetensorError: I/O error: No space left on device (os error 28)` — 第一个 dry-run 的 ~15GB checkpoint 占满了数据盘（250G 盘 92% 已用）
- **Checkpoint 产出**: 部分（step 3 checkpoint 写入中断，仅完成 5.5GB/~15GB）
- **结论**: 脚本逻辑正确，训练可正常启动和执行，磁盘空间是唯一阻碍

## 清理
- **已 kill 进程**: 无残留进程
- **已删除 checkpoint**: `dryrun_occ_detach/`、`dryrun_random_occ/`、两个 log 文件
- **磁盘恢复**: 21G 可用

**关键发现**: occ_data HDF5 文件全部无法读取（`bad object header version number`），正式跑之前需要排查 HDF5 版本兼容性问题。磁盘空间也需要在正式实验前清理出足够余量（两个 ablation 实验各需 ~15GB/checkpoint × 多个 save 点）。

---
