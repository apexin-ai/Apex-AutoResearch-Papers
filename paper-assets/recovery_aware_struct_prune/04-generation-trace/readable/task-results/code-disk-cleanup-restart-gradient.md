# code disk cleanup restart gradient

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_disk_cleanup_restart_gradient_20260517T091327_result.json`
- **Structured JSON:** [`d6d437ca269925a654b5.json`](../../sessions/d6/d6d437ca269925a654b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 报告

### Top 20 目录（删除前）
| 大小 | 目录 |
|------|------|
| 15G | pruned_unstructured_20 |
| 12G | sft_standard_20, sft_rasp_rlvr_20, sft_rasp_20, pruned_rasp_rlvr_20, pruned_rasp_alpha_1.0, pruned_rasp_alpha_0.0, pruned_random_20, **pruned_magnitude_20**, pruned_gradient_20, grpo_stage2_standard_20_v8, grpo_stage2_rasp_20_v9 |
| 11G | sft_standard_25, sft_rasp_25, pruned_standard_30, pruned_standard_25, pruned_rasp_30, pruned_rasp_25, grpo_rasp_25 |
| 5.5G | **sft_gradient_20**（之前磁盘满中断的残留） |

### 删除结果
- `pruned_magnitude_20` (12G) — 已删除
- `sft_magnitude_20` — 不存在（之前未跑到 SFT 阶段）
- `sft_gradient_20` (5.5G) — 已删除

释放约 **17G** 空间。

### 磁盘状态
```
/dev/md0  250G  234G  17G  94%  /root/autodl-tmp
```

### Gradient SFT 启动状态
- **PID**: 697500
- **Session**: scoring_ablation_v2
- **GPU**: cuda:0 (12.5GB VRAM)
- **进度**: 16/1870 steps, loss=1.703, ~35min 预估完成
- **命令**: `CUDA_VISIBLE_DEVICES=0 python src/sft_recovery.py --model_path pruned_gradient_20 --output_dir sft_gradient_20 --gpu 0 --learning_rate 2e-5 --num_train_epochs 2 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --seed 42`

### Random Eval 进度
- **Session**: scoring_ablation_random
- **GPU**: cuda:1 (12.9GB VRAM)
- **进度**: 33/200 samples (16%), ~1.5h 剩余

---
