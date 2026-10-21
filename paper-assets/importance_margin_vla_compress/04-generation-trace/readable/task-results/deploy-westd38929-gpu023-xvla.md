# deploy westd38929 gpu023 xvla

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy-westd38929-gpu023-xvla_20260523T235350_result.json`
- **Structured JSON:** [`28b2ee69fe30092a3dc7.json`](../../sessions/28/28b2ee69fe30092a3dc7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。汇总：

## westd-38929 GPU 状态

| GPU | 实验 | 状态 |
|-----|------|------|
| 0 | eval_xvla_l2norm_k05_spatial_seed43 | 🔄 运行中 (PID 330589) |
| 1 | eval_xvla_l2norm_k05_long_seed43 | 🔄 运行中 (PID 432791, 另一 Worker) |
| 2 | — | 空闲 |
| 3 | **eval_xvla_random_k05_goal_seed43_v4** | ✅ 刚启动 (PID 469773, tmux: xvla_random_goal_s43_v4) |

## GPU 2 情况说明

任务指定的两个 fallback 都无法执行：
1. **`eval_xvla_random_k05_object_seed43`** — 已完成 (SR=71.0%)，无需重跑
2. **`eval_xvla_attention_k05_goal_seed43`** — X-VLA 脚本只支持 `l2_norm` 和 `random`，不支持 `attention` 模式

R6-C1 X-VLA CV seed43 实验已全部覆盖（4 running/done + Goal v4 刚部署），GPU 2 暂无明确的 X-VLA CV 实验可部署。需要指示。

---
