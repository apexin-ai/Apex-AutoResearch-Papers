# code dryrun v3 and submit

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dryrun-v3-and-submit_20260519T213942_result.json`
- **Structured JSON:** [`3f8e5832f064c8c14090.json`](../../sessions/3f/3f8e5832f064c8c14090.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## DRY-RUN V3 验证报告

### Log 文件
- 路径: `/root/afford_invar/results/dryrun_v3.log`
- 大小: 11,444 bytes
- 时间: 2026-05-20 05:42:18

### 检查项

| # | 检查项 | 结果 |
|---|--------|------|
| 1 | `NUM_PATCHES = 256` | **PASS** |
| 2 | ≥5 步 L_act/L_con/H_ent/L_tot 非 NaN | **PASS** (全部 11 步均有值) |
| 3 | lora_gnorm/dec_gnorm 非零 | **PASS** (step 0: 4.87/1.69, step 10: 1.83/0.08) |
| 4 | 无 OOM/CUDA error | **PASS** |
| 5 | Step 0 GRAD MONITOR | **PASS** |

### 每步 Loss 表格

| Step | L_act | L_con | H_ent | L_tot |
|------|-------|-------|-------|-------|
| 0 | 0.5156 | 0.351835 | -8.9226 | 0.4616 |
| 1 | 5.4688 | 0.385445 | -8.5990 | 5.4213 |
| 2 | 2.3750 | 0.350824 | -7.7351 | 2.3327 |
| 3 | 2.2344 | 0.177459 | -8.3709 | 2.1684 |
| 4 | 1.2031 | 0.042440 | -8.2100 | 1.1253 |
| 5 | 1.2891 | 0.024715 | -8.4156 | 1.2074 |
| 6 | 0.6055 | 0.018008 | -8.6025 | 0.5212 |
| 7 | 0.8359 | 0.010060 | -8.6892 | 0.7501 |
| 8 | 0.6992 | 0.012078 | -8.7789 | 0.6126 |
| 9 | 0.3359 | 0.004866 | -8.8611 | 0.2478 |
| 10 | 0.9531 | 0.004527 | -8.9411 | 0.8642 |

### GRAD MONITOR (Step 0)
```
[GRAD MONITOR step 0] L_consist=0.351835 | consist_grad_norm=1.576595 | total_grad_norm=34.131474 | grad_ratio=0.0462
```

数值合理：consistency loss 梯度占总梯度的 4.6%，符合 alpha=0.1 的预期权重。

### 注意事项
- 任务指定的 `--paraphrase_file` / `--save_steps` / `--output_hidden_states` 参数名与代码不匹配，已修正为 `--paraphrases_path` / `--save_freq`，去掉了 `--output_hidden_states`（非 CLI 参数）
- 脚本需要 `torchrun` 启动（内部使用 DDP + `dist.barrier()`）
- 正式全训练启动命令需用 `torchrun --nproc_per_node=1 --master_port=29501`

**DRY-RUN V3 PASSED**

---
