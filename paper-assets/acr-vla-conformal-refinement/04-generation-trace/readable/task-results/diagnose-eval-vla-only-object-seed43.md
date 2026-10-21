# diagnose eval vla only object seed43

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-vla-only-object-seed43_20260515T184816_result.json`
- **Structured JSON:** [`910a583f78211562f84c.json`](../../sessions/91/910a583f78211562f84c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**实验没有失败，已正常完成。** 

JSON 输出文件 `eval_object_vla_only_seed43.json` 包含全部 10/10 tasks 的结果：

| Task | Success Rate |
|------|-------------|
| alphabet_soup | 0.0 (0/10) |
| cream_cheese | 0.1 (1/10) |
| salad_dressing | 0.1 (1/10) |
| bbq_sauce | 0.3 (3/10) |
| ketchup | 0.0 (0/10) |
| tomato_sauce | 0.0 (0/10) |
| butter | 0.0 (0/10) |
| milk | 0.1 (1/10) |
| chocolate_pudding | 0.4 (4/10) |
| orange_juice | 0.2 (2/10) |
| **Overall** | **0.12 (12/100)** |

**失败原因**：监控系统误报。进程已正常退出（跑完全部 100 个 rollouts 后自然结束），但监控连续 5 次检测不到已退出的进程，错误地标记为 failed。不存在 OOM、GPU 错误或崩溃。tmux 中也没有残留 session。

**是否需要重跑**：否。实验已完成，结果完整。

**GPU 状态**：当前 6 张 4090 全部有进程在跑，无空闲 GPU。GPU 4 负载最重（99% util, 2 个进程占 11.3GB），其余 GPU 各有 1 个进程占约 5GB。

---
