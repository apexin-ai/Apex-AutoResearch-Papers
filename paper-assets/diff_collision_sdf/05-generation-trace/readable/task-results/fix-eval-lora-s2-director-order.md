# fix eval lora s2 director order

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_eval_lora_s2_director_order_20260527T140441_result.json`
- **Structured JSON:** [`7076079ff2aab92de7f6.json`](../../sessions/70/7076079ff2aab92de7f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

eval_lora_s2_30k_v2 已正常启动并进入 eval 阶段。

---

## 报告

| 项目 | 状态 |
|------|------|
| **PID 512147** (eval_lora_baseline_30k_s2 原始进程) | 已 kill (force_killed) |
| **PID 512155/512156** (eval_lora_baseline_30k_s2 残留子进程) | 已 kill — 原进程被杀后子进程仍在运行，额外清理 |
| **PID 514115** (eval_lora_s2_30k_v2 原始进程) | 已死 — 被之前的错误 Worker 终止 (EXIT_CODE=129) |
| **eval_lora_s2_30k_v2 重新提交** | 已启动，PID 519125，tmux session `eval_lora_s2_30k_v2`，conda `base` 环境 |
| **当前进度** | 模型加载完成，Task 0 开始 eval（Safety level II, 50 episodes） |
| **GPU 使用** | cuda:0 = 8623 MiB (eval_lora_s2_30k_v2)，cuda:1 = 27088 MiB (train_pi05_a1_obj_s2_l01_high) |

**Registry 更新：**
- `eval_lora_baseline_30k_s2` → DONE, conclusion=killed
- `eval_lora_s2_30k_v2` → RUNNING, PID=519125, tmux=eval_lora_s2_30k_v2

---
