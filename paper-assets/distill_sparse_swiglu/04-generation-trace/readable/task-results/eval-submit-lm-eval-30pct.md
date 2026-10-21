# eval submit lm eval 30pct

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_submit_lm_eval_30pct_20260516T003918_result.json`
- **Structured JSON:** [`b816972767667a8822c6.json`](../../sessions/b8/b816972767667a8822c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

提交确认：

| 项目 | 值 |
|------|-----|
| **exp_id** | `lm_eval_kl_30pct_s42` |
| **PID** | 186674 (tmux wrapper)，实际 python 进程已出现在 GPU 0 |
| **GPU** | cuda:0，当前显存 73703/97887 MiB |
| **日志** | `~/runs/distill_sparse_swiglu/lm_eval_kl_30pct_s42.log` |
| **命令** | `python -u src/lm_eval_sparse.py --tasks arc_challenge,winogrande,mmlu,gsm8k --sparsity_target 0.3 --predictor_path checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --output_path results/lm_eval_kl_30pct` |

nvidia-smi 确认 GPU 0 上三个 python 进程共存：
- PID 181121 (Mistral dense eval): 21246 MiB
- PID 186226 / 186410 (新 eval 相关): ~18GB each

模型正在加载中（log: `Loading model from .../llama-3.1-8b`），显存充足，两组 eval 安全并行。

---
