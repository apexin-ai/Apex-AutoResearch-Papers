# eval teal 30pct downstream

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_teal_30pct_downstream_20260516T025452_result.json`
- **Structured JSON:** [`4c1e89dbe5ce8c7149a5.json`](../../sessions/4c/4c1e89dbe5ce8c7149a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已提交并注册为 RUNNING。

**总结：**
- **实验**: `lm_eval_teal_30pct`，PID 194814，tmux session `teal30`
- **服务器**: westd-34887, cuda:0
- **模型**: Llama-3.1-8B（已验证 config.json，registry 中 TEAL 50% 标记 `model="Qwen2.5-7B-Instruct"` 是 registry 错误）
- **命令**: `python -u src/lm_eval_teal.py --sparsity_target 0.3 --tasks arc_challenge,winogrande,mmlu,gsm8k --gpu 0 --output_path results/lm_eval_teal_30pct`
- **Few-shot**: 未指定 `--num_fewshot`，与 TEAL 50% 一致（使用 lm-eval 各 task 默认值：ARC 25-shot, WinoGrande 5-shot, MMLU 5-shot, GSM8K 5-shot）
- **离线模式**: `HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1`
- **日志**: `~/runs/distill_sparse_swiglu/lm_eval_teal_30pct.log`
- **输出**: `results/lm_eval_teal_30pct/`
- 预计运行 30-40 分钟（参考 50% 用了 ~37 分钟）

---
