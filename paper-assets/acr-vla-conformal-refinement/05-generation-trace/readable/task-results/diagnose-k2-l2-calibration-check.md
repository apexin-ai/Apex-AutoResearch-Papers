# diagnose k2 l2 calibration check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_k2-l2-calibration-check_20260519T205631_result.json`
- **Structured JSON:** [`5094ad1290dca638eb2f.json`](../../sessions/50/5094ad1290dca638eb2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态：运行中

| 项目 | 状态 |
|------|------|
| PID 995736 | **存活**，已运行 23m57s |
| JSON 输出 | 尚未生成 |
| GPU 1 | 21% 利用率，5236/24564 MiB |

**进度**：10 个任务 × 5 episodes = 50 episodes 总计
- Task 1 `pick_up_alphabet_soup`: 5/5 done
- Task 2 `pick_up_cream_cheese`: 4/5 done (当前)
- 已完成 **9/50 episodes (18%)**

**速度**：每 episode ~151s，剩余 41 episodes ≈ **103 分钟**（预计 ~1.7 小时后完成）。

目前全部 episode 都是 FAIL (300 steps)，这是预期行为——calibration 脚本在收集 FMVD 分数，不依赖 success rate。进程正常运行，无需干预，等待 JSON 输出即可。

---
