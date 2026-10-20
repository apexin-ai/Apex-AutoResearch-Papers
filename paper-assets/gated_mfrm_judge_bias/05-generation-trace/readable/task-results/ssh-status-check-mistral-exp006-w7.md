# ssh status check mistral exp006 w7

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_status_check_mistral_exp006_w7_20260523T002011_result.json`
- **Structured JSON:** [`bfb66d9f1801564e908b.json`](../../sessions/bf/bfb66d9f1801564e908b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| 实验 | 进度 | 状态 | ETA |
|---|---|---|---|
| **Mistral judge** (rtx6000-4x) | 9021 行 JSONL | **已完成** — vLLM 已关闭，回到 shell | - |
| **exp-006** (autodl-8gpu) | 50/80 fits (k2✓ k4✓ k6=6/10 k9=0/10) | 运行中，当前 k6_s6 MCMC 59% | ~5-15h（k9 未知） |
| **W7 ablation** (autodl-8gpu) | 19/20 seeds，当前 seed=18 binary_gating | 运行中 | ~25 min |

备注：
- Mistral：tmux `vllm-mistral` 里 vLLM 进程已正常退出，收集应已完成
- exp-006：k2/k4 很快（~2min/seed），k6 ~40min/seed，k9 尚未开始且规模更大，预计耗时较长；LOOCV 也还没跑
- W7：还剩 seed 18 的 2 个 variant + seed 19 全部 4 个 variant

---
