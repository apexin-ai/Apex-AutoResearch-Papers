# data trajectory collection api

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_trajectory-collection-api_20260514T062125_result.json`
- **Structured JSON:** [`e697dd37d0c1d554e10c.json`](../../sessions/e6/e697dd37d0c1d554e10c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

traj_0002 完成（4 步 SUCCESS），traj_0005 已启动。收集运行正常，无错误。

汇报：

**1. API 可用性确认**
- API endpoint `http://47.94.22.126/v1` 正常可用
- Model `openai/gpt-5.2` 可用，chat completion 响应 ~5s
- min max_tokens 限制为 16（脚本用 512，无影响）

**2. 测试 3 条轨迹结果**
| 轨迹 | 任务类型 | 步数 | 结果 |
|------|---------|------|------|
| traj_0001 | look_at_obj_in_light | 35/50 | SUCCESS/FAILED（两次测试不同） |
| traj_0002 | pick_clean_then_place_in_recep | 7 | SUCCESS |
| traj_0003 | pick_and_place_simple | 6 | SUCCESS |

- 1 线程测试 cost: $0.1284，318s
- 4 线程测试 cost: $0.1779，344s（env_lock 修复后零 crash）

**3. 正式收集启动确认**
- **PID: 11045**
- 575 episodes sampled（含 15% 冗余），目标 500 条成功
- 4 workers 并行
- 输出目录: `data/trajectories/`
- 日志: `/tmp/collect_500.log`
- 预计 3-5 小时完成

**4. 配置调整**
- 发现 textworld gym 不线程安全，脚本 4 workers 会大量 crash
- 修复：在 `collect_trajectories.py` 添加 `env_lock = threading.Lock()`，对 `register_games`/`make`/`reset`/`step`/`close` 加锁
- 修复后 4 线程运行稳定，零 crash

---
