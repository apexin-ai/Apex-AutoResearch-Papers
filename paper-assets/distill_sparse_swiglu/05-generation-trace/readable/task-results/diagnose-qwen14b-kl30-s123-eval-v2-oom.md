# diagnose qwen14b kl30 s123 eval v2 oom

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_qwen14b_kl30_s123_eval_v2_oom_20260519T112324_result.json`
- **Structured JSON:** [`87d609ba59efd3971bac.json`](../../sessions/87/87d609ba59efd3971bac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### GPU 占用

| GPU | PID | 进程 | 显存占用 | GPU利用率 |
|-----|-----|------|---------|----------|
| 0 | 93142 | `qwen14b_kl30_s123_eval`（原始） | 94074 MiB / 97887 MiB (96%) | 76% |
| 1 | 100070 | `qwen14b_kl30_s456_eval_v2` | 72658 MiB / 97887 MiB (74%) | 100% |

### 旧进程状态

| PID | 状态 | 说明 |
|-----|------|------|
| 93137 | **已死** | 不存在 |
| 93142 | **仍在运行** | 原始 s123_eval，在 GPU 0 上跑 GSM8K generate_until，进度 ~33% (433/1319) |
| 93278 | **已死** | 不存在 |

### OOM 根因

**GPU 冲突。** PID 93142（原始 `qwen14b_kl30_s123_eval`）仍占据 GPU 0 的 91.87 GiB。`qwen14b_kl30_s123_eval_v2` 也尝试在 GPU 0 加载 Qwen2.5-14B 模型（需要 27.51 GiB），但 GPU 0 仅剩 2.55 GiB 可用，直接 OOM。

### tmux sessions

仅一个活跃 session：`qwen14b_kl30_s456_eval_v2`（GPU 1，刚启动）。

### GPU 0 是否可用于重试

**不可用。** PID 93142 仍在运行且占满 GPU 0。需要等它跑完（GSM8K 进度 33%，按速度估计还需 ~2 小时）或手动 kill 后才能重试。

---
