# deploy westd 49937 p0 vla only

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd-49937-p0-vla-only_20260526T064335_result.json`
- **Structured JSON:** [`0dd3e6fc25e0eeefd7a9.json`](../../sessions/0d/0dd3e6fc25e0eeefd7a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-49937 报告

### Harvest
- westd-pi05-k2mean-goal-s42: SR=**0.995** → registry DONE
  - log: `logs/eval_goal_k2mean_pi05_seed42.log`
  - json: `logs/eval_goal_k2mean_pi05_seed42.json`

### 新部署
- **westd-pi05-vla-only-goal-s42** on cuda:4: ✅ 启动成功
  - tmux session 已创建, PID 144256 运行中, VRAM 10.2GB
  - 命令: `vla_only --baseline_mode single --K 1 --benchmark goal --seed 42`
  - hypothesis 已设置（D158 paired comparison）

### GPU 状态 (服务器时间 14:47, 启动 12:41~12:47)

| GPU | 实验 | 进度 | VRAM | ETA |
|-----|------|------|------|-----|
| 0 | westd-pi05-adaptive-goal-s42 | task 10/10 (wine_bottle 5/20) | 10.3G | ~15:00 |
| 1 | westd-pi05-adaptive-goal-s43 | task 10/10 (wine_bottle 5/20) | 10.3G | ~15:00 |
| 2 | westd-pi05-adaptive-goal-s44 | task 10/10 (wine_bottle 5/20) | 10.3G | ~15:00 |
| 3 | westd-pi05-adaptive-object-s42 | task 6/10 (butter_basket 15/20) | 11.0G | ~15:30 |
| 4 | **westd-pi05-vla-only-goal-s42** (NEW) | 加载模型完毕，开始 rollout | 10.0G | ~16:45 (~2h) |
| 5 | westd-pi05-crm-k2-goal-s42 | task 10/10 (wine_bottle 已显示) | 10.4G | ~15:00 |

### 备注
- GPU 0/1/2/5 均在最后一个 task (`put_the_wine_bottle_on_the_rack`)，~15 分钟内陆续完成
- GPU 3 (object) 进度稍慢，约 14:30 进入第 7 个任务
- 没有新 JSON 完成（旧的 `eval_goal_adaptive_pi05_seed42.json` 时间戳为昨日 16:50，本次完成会覆盖）

---
