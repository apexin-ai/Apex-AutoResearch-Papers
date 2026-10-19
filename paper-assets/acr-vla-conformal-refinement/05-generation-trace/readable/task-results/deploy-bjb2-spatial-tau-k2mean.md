# deploy bjb2 spatial tau k2mean

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-spatial-tau-k2mean_20260526T142211_result.json`
- **Structured JSON:** [`804937de9043b02f720d.json`](../../sessions/80/804937de9043b02f720d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**STOP — C001 violation. 任务描述与服务器实际状态不符。**

GPU 实测占用情况：

**bjb2-28827** (任务声称"6 卡全空"):
| GPU | memory.used | util | PID |
|-----|-------------|------|-----|
| 0 | 14663 MiB | 21% | 443692 |
| 1 | 14663 MiB | 21% | 444363 |
| 2 | 13966 MiB | 61% | 445988 |
| 3 | 13966 MiB | 21% | 448295 |
| 4 | 14741 MiB | 19% | 450041 |
| 5 | 14741 MiB | 17% | 451711 |

**bjb2-24035** (任务声称"1 卡空"):
| GPU | memory.used | util | PID |
|-----|-------------|------|-----|
| 0 | 14694 MiB | 20% | 63656 |

**所有 7 张目标 GPU 均 > 500 MiB，全部不可用。** 7 个独立进程，每个 ~14 GB，符合 VLA rollout 评测的显存特征——很可能已经有别的 worker 在跑实验，或之前提交的实验仍在进行。

按 C001 禁止启动，需要先排查这些进程是什么。下一步建议：

1. 检查 tmux 会话和 registry，确认这些 PID 对应哪些实验
2. 如果是本项目正在跑的合法实验 → 不能启动新的，等待这批结束
3. 如果是僵尸/残留进程 → 经确认后 kill 再启动

要不要我先拉 tmux session 列表和 registry 中 RUNNING 状态的实验做交叉比对？

---
