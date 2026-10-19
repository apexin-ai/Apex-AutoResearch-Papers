# ops westd start ragen eval gpu123

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_start_ragen_eval_gpu123_20260522T091558_result.json`
- **Structured JSON:** [`04ab2b5e46118c8206a8.json`](../../sessions/04/04ab2b5e46118c8206a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 GPUs now running successfully:
- **GPU 0**: 90467 MiB, 100% util
- **GPU 1**: 90467 MiB, 100% util
- **GPU 2**: 90469 MiB, 100% util
- **GPU 3**: 89747 MiB, 52% util (vLLM just finished preallocation!)

## 最终状态报告

### 4 个 RAGEN OOD Eval 运行状态

| GPU | tmux session | 模型/实验 | Config | W&B Run ID | GPU Memory | 状态 |
|-----|-------------|-----------|--------|------------|------------|------|
| 0 | `ragen_eval_gpu0` | SFT baseline (`qwen3_exp021_ragen_sft_v4`) | `_alfworld_sft_baseline_ood_eval_v2` | `9dgcusr8` | 90467 MiB | 运行中 |
| 1 | `ragen_eval_gpu1` | seed8 step5 (`qwen_exp029_seed8_step5_hf`) | `_alfworld_exp029_seed8_ood_precollapse` | `iayaluzg` | 90467 MiB | 运行中 |
| 2 | `ragen_eval_gpu2` | seed2048 step5 (`qwen_seed2048_step5_hf`) | `_alfworld_seed2048_step5_ood_eval` | `xmjg12o1` | 90469 MiB | 运行中 |
| 3 | `ragen_eval_gpu3` | intervention_c step5 (`qwen_intervention_c_hard_cap_step5_hf`) | `_alfworld_intervention_c_step5_ood_eval` | `nzdwgvcg` | 89747 MiB | 运行中 |

### GPU 3 重启说明

GPU 3 初次启动时 Ray 因 `pthread_create failed: Resource temporarily unavailable` 崩溃（4个 Ray 集群各自尝试预启动 88 个 worker 超出系统线程限制）。通过添加 `+ray_kwargs.ray_init.num_cpus=20` 限制 CPU 资源后成功启动。

### 启动命令

- **GPU 0**: `CUDA_VISIBLE_DEVICES=0 python train.py --config-name _alfworld_sft_baseline_ood_eval_v2 system.CUDA_VISIBLE_DEVICES='0'`
- **GPU 1**: `CUDA_VISIBLE_DEVICES=1 python train.py --config-name _alfworld_exp029_seed8_ood_precollapse system.CUDA_VISIBLE_DEVICES='1' trainer.experiment_name=seed8-step5-ood-eval`
- **GPU 2**: `CUDA_VISIBLE_DEVICES=2 python train.py --config-name _alfworld_seed2048_step5_ood_eval system.CUDA_VISIBLE_DEVICES='2'`
- **GPU 3**: `CUDA_VISIBLE_DEVICES=3 python train.py --config-name _alfworld_intervention_c_step5_ood_eval system.CUDA_VISIBLE_DEVICES='3' '+ray_kwargs.ray_init.num_cpus=20'`

### 日志文件

- GPU 0: `/root/autodl-tmp/logs/ragen_sft_ood_eval_restart.log`
- GPU 1: `/root/autodl-tmp/logs/ragen_seed8_ood_eval_v2.log`
- GPU 2: `/root/autodl-tmp/logs/ragen_seed2048_ood_eval_v4.log`
- GPU 3: `/root/autodl-tmp/logs/ragen_intervention_c_ood_eval_v3.log`

### 预估完成时间

134 个 ALFWorld OOD 任务，max_turn=50，单 GPU 评估通常需要 **3-6 小时**。GPUs 0-2 从 17:32 开始，GPU 3 从 17:42 开始。

---
