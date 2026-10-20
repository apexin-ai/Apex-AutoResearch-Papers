# ops westd cleanup and prep math500

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_cleanup_and_prep_math500_20260517T225849_result.json`
- **Structured JSON:** [`941583e54a878a98a313.json`](../../sessions/94/941583e54a878a98a313.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. PID 59866 kill 结果
已成功 kill。PID 59408 仍在运行：
```
python src/eval_gsm8k.py --model_path pruned_cka_only_30 --max_samples 200 (cuda:2, 启动于 05:59)
```

### 2. eval_math500_unpruned 完整信息
- **PID**: 2506 (tmux session，已完成)
- **状态**: **已完成** (EXIT_CODE=0)
- **结果**: MATH-500 Accuracy = **0.7360 ± 0.0197** (368/500)
- **完成时间**: 2026-05-17 19:09:23 (昨天已结束)
- **GPU 影响**: 当前 **不再占用 GPU 显存**，不影响其他任务
- **结果文件**: `/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_unpruned.json`

### 3. sft_cka_only_20 模型确认
存在，大小 **12GB**，路径 `/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20/`

### 4. eval_math500.py 参数
```
--model_path MODEL_PATH (必选)
--output_path OUTPUT_PATH
--max_new_tokens MAX_NEW_TOKENS
--max_samples MAX_SAMPLES
--seed SEED
--dtype DTYPE
```

### 5. eval_sft_cka_only_20_n1319 进度
- **PID**: 49480 (cuda:0, 启动于 03:17)
- **进度**: **1083/1319 (82%)**，运行约 3h38m
- **当前 acc**: 0.6333 (截至 1050 样本)
- **速度**: ~5-7s/it
- **预计剩余**: ~20-25 min 完成

### GPU 当前分配总览
| GPU | 显存占用 | 任务 |
|-----|----------|------|
| cuda:0 | 41GB/98GB | eval_sft_cka_only_20_n1319 (82%) |
| cuda:1 | 35GB/98GB | eval_math500_grpo_standard_20 |
| cuda:2 | 12GB/98GB | eval_postprune_cka_only_30 (PID 59408) |
| cuda:3 | 33GB/98GB | eval_postprune_standard_30 |

---
