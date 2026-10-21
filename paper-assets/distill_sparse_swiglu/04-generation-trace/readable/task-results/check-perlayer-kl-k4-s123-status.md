# check perlayer kl k4 s123 status

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_perlayer_kl_k4_s123_status_20260522T150528_result.json`
- **Structured JSON:** [`75ea985c0a0e5c41ef9f.json`](../../sessions/75/75ea985c0a0e5c41ef9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Status: Pipeline 仍在跑（Phase 3 进行中）

**进程状态**
- Bash wrapper PID 59565: 存活
- 进程链: 59565 → 59569 → 59570 (run_k4_s123_pipeline.sh) → 65980 (benchmark_eval.py downstream)
- GPU 0: 98% util, 48GB
- Python 训练进程 59575 退出是正常的——Phase 1 训练已完成，pipeline 已进入下一阶段

**Phase 进度**
| Phase | 状态 | 结果 |
|-------|------|------|
| Phase 1: K=4 训练 (2700 steps) | DONE @ 23:04 | predictor_perlayer_kl_k4.pt 已落盘 (152MB) |
| Phase 2: PPL eval (wikitext2) | DONE @ 23:04 | **wikitext2_ppl = 8.8897** |
| Phase 3: Downstream 7-task | RUNNING | 当前在跑 loglikelihood requests, ~23% (1082/4687) |
| Phase 4: Sparsity 分析 | PENDING | — |

**已知 metrics**
- wikitext2_ppl = 8.8897
- Per-layer sparsity (训练后从 predictor 计算的 TEAL-global mask): Layer 0-31 全部在 [0.293, 0.301] 范围, model-level = **0.297**（接近 target 0.3）
- 训练收敛: avg_kl 从 0.095 (step 1) → 0.045 (step 2000)，最终 avg_sp=0.300 (step 2000)

**Downstream eval 任务顺序**: arc_challenge → winogrande → mmlu → gsm8k → hellaswag → piqa → boolq。当前在跑前几个 task 之一（4687 requests 与 arc_challenge 1172×4=4688 高度吻合，可能仍在 ARC 收尾或已切到 winogrande）。

**结论**: Pipeline 健康运行，**不更新 registry**。预计 Phase 3 还需 1-2 小时（MMLU + GSM8K 较慢），Phase 4 sparsity 分析很快。

---
