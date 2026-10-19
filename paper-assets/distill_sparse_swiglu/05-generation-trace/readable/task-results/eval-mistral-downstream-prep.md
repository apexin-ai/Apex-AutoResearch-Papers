# eval mistral downstream prep

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_mistral_downstream_prep_20260515T231938_result.json`
- **Structured JSON:** [`cdbd48132aee10c88e69.json`](../../sessions/cd/cdbd48132aee10c88e69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

**eval_benchmark.py 修改完成**：
- 新增 `mistral_dense` 和 `mistral_kl_s42` conditions（自动使用 Mistral 模型路径）
- 新增 `--model_path` CLI 参数（conditions 自动检测 model_path）
- 语法检查通过，`--list_conditions` 正常显示

**GPU 状态**：
| GPU | tmux session | 任务 | 进度 | 预计剩余 |
|-----|-------------|------|------|---------|
| cuda:0 | lm_eval_kl_s42 | Llama kl_s42 GSM8K generate_until | 11% (141/1319) | ~28 min |
| cuda:1 | lm_dense | Llama dense GSM8K generate_until | 51% (673/1319) | ~10 min |

**GPU 1 约 10 分钟后释放**。

**准备好的提交命令**（等 GPU 1 空闲后执行）：

```bash
# Mistral KL sparse downstream eval
CUDA_VISIBLE_DEVICES=1 python -u src/eval_benchmark.py \
  --condition mistral_kl_s42 \
  --tasks lm_eval \
  --skip_ppl \
  --gpu 0 \
  --batch_size 4 \
  --output_dir results/plan_009_mistral

# Mistral dense baseline (接着跑)
CUDA_VISIBLE_DEVICES=1 python -u src/eval_benchmark.py \
  --condition mistral_dense \
  --tasks lm_eval \
  --skip_ppl \
  --gpu 0 \
  --batch_size 4 \
  --output_dir results/plan_009_mistral
```

可以合并为一个 submit_training_job 顺序执行。要现在设定监控等 GPU 1 释放后自动提交，还是手动触发？

---
