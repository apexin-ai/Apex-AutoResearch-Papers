# ops openvla k05 final result

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_openvla_k05_final_result_20260518T000432_result.json`
- **Structured JSON:** [`14c3988d94240ba2e02e.json`](../../sessions/14/14c3988d94240ba2e02e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

k=0.7 已在 GPU 0 上运行（15.6GB，90% util）。

## 结果汇总

### k=0.5 Random Prune 完整结果（500 episodes）

| Task | SR | Baseline SR |
|---|---|---|
| alphabet soup | 0.60 | 0.78 |
| cream cheese | 0.08 | 0.80 |
| salad dressing | 0.36 | 0.82 |
| bbq sauce | 0.44 | 0.46 |
| ketchup | 0.50 | 0.96 |
| tomato sauce | 0.38 | 0.78 |
| butter | 0.02 | 0.58 |
| milk | 0.24 | 0.72 |
| chocolate pudding | 0.40 | 0.68 |
| orange juice | 0.72 | 0.82 |
| **Overall** | **0.374** | **0.740** |

随机裁剪 50% vision tokens → SR 从 74.0% 降至 37.4%（相对下降 49.5%）。cream cheese 和 butter 几乎完全失败。

### k=0.7 启动确认
- **PID**: 755666 (子进程 755671 on GPU 0)
- 参数: `--mode random_prune --k_ratio 0.7 --suite libero_object --num_episodes 50 --seed 7`
- 预计运行约 4.5 小时（参考 k=0.5 的 267 分钟）

---
