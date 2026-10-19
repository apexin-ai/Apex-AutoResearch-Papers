# deploy cqa1 gpu012 pi05 staggered

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1-gpu012-pi05-staggered_20260526T064419_result.json`
- **Structured JSON:** [`828b214b565ab38b26ea.json`](../../sessions/82/828b214b565ab38b26ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 3 个新实验已注册为 RUNNING。任务完成。

## cqa1-32758 报告

### Harvest
- tau_sweep τ=0.50: SR=0.870, trigger_rate=2.06% (565/27431 steps) → registry DONE
- tau_sweep τ=0.70: SR=0.870, trigger_rate=1.04% (283/27265 steps) → registry DONE
- tau_sweep τ=0.90: SR=0.890, trigger_rate=0.35% (94/26628 steps) → registry DONE

τ-sweep 关键发现：τ 从 0.25→0.90，SR 几乎不变（87-89%），但 trigger_rate 从 ~2% 降到 0.35%。τ=0.90 在极少触发 CRM 的情况下仍保持 89% SR，说明 π0.5 基础能力很强，CRM 修正在 Goal 上边际收益有限。

### 新部署
| GPU | 实验 | 状态 |
|-----|------|------|
| 0 | pi05-crm-k2-long-s44-cqa1 | 启动成功（14731 MiB, 已加载环境） |
| 1 | pi05-adaptive-object-s42-cqa1 | 启动成功（14042 MiB, 已加载环境） |
| 2 | pi05-adaptive-goal-s42-cqa1 | 启动成功（13920 MiB, 已加载环境） |

注：3 个实验在本次任务执行前已被部署（tmux sessions 创建于 14:52-14:57），本次补注册 registry 并更新为 RUNNING。残留 pi05-tau050 tmux session 已清理。

### OOM 事件
无。6 GPU 并发 π0.5 稳定运行，总 VRAM 使用 ~84 GiB / 147 GiB (57%)。

### GPU 3-5 状态
| GPU | 实验 | 进度 | VRAM |
|-----|------|------|------|
| 3 | pi05-adaptive-object-s44-cqa1 | 3/10 tasks (当前: salad_dressing 10/20) | 13113 MiB |
| 4 | pi05-adaptive-long-s43-cqa1 | 2/10 tasks (当前: cream_cheese_box 5/20) | 14018 MiB |
| 5 | pi05-adaptive-long-s44-cqa1 | 2/10 tasks (当前: cream_cheese_box 5/20) | 14018 MiB |

---
