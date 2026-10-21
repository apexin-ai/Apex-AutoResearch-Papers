# ops exp002v3 precheck readiness

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp002v3-precheck-readiness_20260519T133259_result.json`
- **Structured JSON:** [`35943b58c20d71e6340c.json`](../../sessions/35/35943b58c20d71e6340c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-002v3 部署就绪状态检查

| # | 检查项 | 状态 | 备注 |
|---|--------|------|------|
| 1 | **launch_exp002v3.sh 存在且正确** | **PASS** | `unset CUDA_VISIBLE_DEVICES` ✓, 绝对路径 `/root/miniconda3/bin/deepspeed` ✓, `--include localhost:0,3` ✓ |
| 1b | **超参数 (Python 脚本)** | **PASS** | `R1_SCALE_FACTOR=5.0` ✓, `R1_WEIGHT=0.4` ✓, `R3_WEIGHT=0.6` ✓, `R2_WEIGHT=0.0` |
| 2 | **DeepSpeed config** | **PASS** | 脚本实际引用 `ds_config_exp002v3.json`（非 `ds_config_zero2.json`），已存在，ZeRO stage 2 ✓, bf16 ✓, grad_accum=16 ✓ |
| 3 | **recalib bug fix** | **PASS** | `_DCRewardCallable.__call__` 中使用 `step = t.state.global_step` 做 recalibration 判断 ✓, `t._reward_step` 仅作计数器 |
| 3b | **备份文件** | **PASS** | `dcgrpo_trainer.py.bak_pre_recalib_fix` 存在 (May 19 19:39) |
| 4 | **directions.pt** | **PASS** | 脚本引用 `/root/contrastive_entrain_calib/results/exp001/directions.pt` ✓ 存在 |
| 4b | **probe 文件** | **PASS** | `probe_module.py` 存在, 多个 `probe.pt` checkpoint 存在 |
| 5 | **训练数据** | **PASS** | `/root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl` (367KB) ✓ |
| 5b | **模型权重** | **PASS** | Qwen3-8B 5 个 shard 全在 `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/` |
| 6 | **磁盘空间 (根分区)** | **WARN** | `/` 仅剩 **4.9GB** (84% used)，DeepSpeed checkpoint 会写到根分区的 `checkpoints/` 目录，500 step 保存一次可能不够 |
| 6b | **磁盘空间 (数据盘)** | **PASS** | `/root/autodl-tmp` 剩 305GB (14% used) |

### 需要处理的问题

**根分区仅 4.9GB，checkpoint 存储空间不足。** `OUTPUT_DIR` 设为 `/root/contrastive_entrain_calib/checkpoints/exp002v3_dcgrpo_scaled_cosine/`，位于根分区。LoRA checkpoint (r=64, 4 target modules) 每个约 500MB-1GB，加上 DeepSpeed optimizer states，save_steps=500 会快速耗尽空间。

建议：将 `OUTPUT_DIR` 改为 `/root/autodl-tmp/checkpoints/exp002v3_dcgrpo_scaled_cosine/`，或在根分区建软链接指向数据盘。

其余检查项全部通过，可以启动。

---
