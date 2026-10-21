# diag k16 eval progress

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_k16_eval_progress_20260523T131836_result.json`
- **Structured JSON:** [`9dd0ed0eefa21e66a00f.json`](../../sessions/9d/9dd0ed0eefa21e66a00f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**两个 eval 均在运行中**，已运行约 38 分钟。

| 实验 | PID | 状态 | 当前任务 | 进度 |
|------|-----|------|---------|------|
| K=16 s123 | 141289 | Running | MMLU (tokenizing) | 46% (18556/40168) |
| K=16 s456 | 141430 | Running | GSM8K (generate_until) | 94% (1241/1319) |

**GPU 状态**：
- GPU 0: 0% util, 66.1/97.9 GB（s123 模型已加载，当前在 tokenize 阶段）
- GPU 1: 62% util, 66.1/97.9 GB（s456 正在跑 GSM8K 生成）

s456 比 s123 快，GSM8K 快跑完了，后面还有 hellaswag 和 piqa。两个预计还需 15-25 分钟完成全部 7 个 task。

---
