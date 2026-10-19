# analysis cqa1 long analyzing

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cqa1-long-analyzing_20260526T102824_result.json`
- **Structured JSON:** [`753df190a6c09cba896e.json`](../../sessions/75/753df190a6c09cba896e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均失败 → status=DONE, conclusion=failed。

## 汇总报告

| 实验 | GPU | success | trigger | 结论 |
|---|---|---|---|---|
| pi05-adaptive-long-s43-cqa1-r2 | cuda:4 | 0/200 (0.0%) | N/A | **failed** |
| pi05-adaptive-long-s44-cqa1-r2 | cuda:5 | 0/200 (0.0%) | N/A | **failed** |

**失败原因**：两个实验在每个 rollout 的 step 0 立即抛 `torch.AcceleratorError: CUDA error: out of memory`（栈在 `pi05_wrapper.py:163 torch.flip` / `evaluate.py:458 select_action_conformal_crm`）。脚本对 per-rollout 异常做了 try/except，所以最终 EXIT_CODE=0，但所有 10 个任务 × 20 rollouts 全部失败，per-task success rate 全部 0.0%，trigger_rate 因从未进入正常推理路径无统计值。

OOM 发生在第一帧图像 preprocess 阶段（不是模型采样阶段），暗示 GPU 在脚本启动时就已被其他进程占满 / cuda:4 与 cuda:5 上有残留显存。建议下一步：
1. 重跑前用 `nvidia-smi` 确认 cuda:4/5 空闲，必要时清残留进程
2. 这次再跑的 r2 跟原 r1 不是同节点问题，是 GPU 显存争用，不是 tmux 残留

---
