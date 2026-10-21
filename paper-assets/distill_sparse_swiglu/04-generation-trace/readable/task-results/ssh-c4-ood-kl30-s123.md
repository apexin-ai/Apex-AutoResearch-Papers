# ssh c4 ood kl30 s123

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_c4_ood_kl30_s123_20260520T132752_result.json`
- **Structured JSON:** [`8824e7e913dbe9dce377.json`](../../sessions/88/8824e7e913dbe9dce377.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**C4 OOD KL30 s123 实验** — westd-41718:cuda:0
- PID 259363，tmux session `c4_ood_kl30_s123`
- 模型已加载，正在计算 TEAL global masks (calibration=C4)
- 日志：`~/runs/distill_sparse_swiglu/c4_ood_kl30_s123.log`
- Registry 状态为 DEPLOYED（从之前 failed 重启，state machine 不允许直接回 RUNNING）
- 注意：benchmark_eval.py 无 `--seed` 参数，s42 也没用 seed。本次使用相同 checkpoint (kl_sparsity30_s42_v3) + 相同配置，lm-eval-harness 默认 random_seed=0，loglikelihood 类任务结果应与 s42 一致

**westd-34887 Mistral 状态**：
- **s123** (cuda:0, PID 212473)：训练已完成，进入 eval 阶段。loglikelihood requests 进度 ~27% (11169/40168)，正在跑 MMLU
- **s456** (cuda:1, PID 215424)：训练已完成，进入 eval 阶段。generate_until requests 进度 ~23% (305/1319)，正在跑 GSM8K

---
