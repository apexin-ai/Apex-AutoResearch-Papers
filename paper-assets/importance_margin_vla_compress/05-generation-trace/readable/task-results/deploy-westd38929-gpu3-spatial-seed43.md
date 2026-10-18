# deploy westd38929 gpu3 spatial seed43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy-westd38929-gpu3-spatial-seed43_20260523T222059_result.json`
- **Structured JSON:** [`72118e17a335c746bb72.json`](../../sessions/72/72118e17a335c746bb72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**发现**：前一个 v3 worker 在被取消前已经自行部署了 `eval_xvla_random_k05_spatial_seed43`。v3 goal 进程已死（log 停在 task 1 ep 4），spatial 实验已在 GPU 3 上运行（PID 155546）。

**已执行**：
1. **GPU 3 无需清理** — v3 goal 进程已自然死亡，spatial 已接管 GPU 3
2. **无 v3 goal tmux session** — 只有 spatial session 存在
3. **Registry 更新**：
   - `eval_xvla_random_k05_goal_seed43_v3` → DONE, conclusion=killed, failure_reason 已记录
   - `eval_xvla_random_k05_goal_seed43_v2` → 已是 DONE/failed（无需操作）
4. **Spatial 实验已注册**：`eval_xvla_random_k05_spatial_seed43` → RUNNING, PID 155546, GPU 3
5. **实验健康**：Task 0 已完成 100% SR，正在跑 Task 1

**westd-38929 四 GPU 状态**：
| GPU | PID | 实验 |
|-----|-----|------|
| 0 | 994436 | eval_xvla_l2norm_k05_goal_seed43 |
| 1 | 994512 | eval_xvla_l2norm_k05_object_seed43 |
| 2 | 994651 | eval_xvla_random_k05_long_seed43 |
| 3 | 155546 | eval_xvla_random_k05_spatial_seed43 ✓ |

---
