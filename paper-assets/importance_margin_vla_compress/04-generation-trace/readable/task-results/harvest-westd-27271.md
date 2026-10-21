# harvest westd 27271

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_westd-27271_20260523T154349_result.json`
- **Structured JSON:** [`fda24e1a024a5fbde855.json`](../../sessions/fd/fda24e1a024a5fbde855.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the summary:

## 收割结果

### 已完成: eval_e5_xvla_attn_last_obj_k03
- **SR: 84.2%** (421/500), Wilson CI [80.7%, 87.1%]
- 15/50 tokens 保留 (k=0.3)
- Registry → DONE (success)

**X-VLA Object k=0.3 三种 attention 模式对比：**
| Mode | SR |
|------|-----|
| attention_mean | **96.0%** |
| attention_rollout | **92.0%** |
| attention_last | **84.2%** |

attention_last 在极端剪枝下退化最严重，但仍保持 84.2%，远好于 attention_last k=0.5 的 74.4%——说明 k=0.5→k=0.3 结果反升，可能存在数据波动或之前 k=0.5 数据有问题。

### 仍在运行

| 实验 | 进度 | GPU |
|------|------|-----|
| eval_openvla_baseline_goal_seed42_v3 (PID 263442) | Task 3/10, ~130/500 ep (~26%) | GPU 0 |
| eval_openvla_baseline_long_seed42 (PID 291098) | Task 1/10, 刚启动 (~5min) | GPU 2 |

还有 PID 257941 在 GPU 0 跑了 1.5h，是一个没带 `--model_path` 和 `--unnorm_key` 的旧 Goal baseline（可能是 v1），与 v3 并行占用资源。两个 OpenVLA Goal baseline 预计还需 ~4-5 小时完成。

---
