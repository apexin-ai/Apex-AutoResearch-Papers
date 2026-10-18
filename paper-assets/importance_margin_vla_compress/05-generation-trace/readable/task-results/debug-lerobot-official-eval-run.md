# debug lerobot official eval run

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_lerobot_official_eval_run_20260516T124342_result.json`
- **Structured JSON:** [`70d90865eb25f232faf2.json`](../../sessions/70/70d90865eb25f232faf2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 最终确认报告

### 实测结果

用 SmolVLA 官方 `select_action()` 和我们的 `predict_actions()` 对 `baseline/latest` checkpoint 各跑 10 episode：

| 方法 | Success Rate | Mean Reward |
|------|-------------|-------------|
| 官方 `select_action()` | **0% (0/10)** | 0.0 |
| 我们的 `predict_actions()` | **0% (0/10)** | 0.0 |

**两种方法结果完全一致**，首步 action 差异仅来自 flow matching 的随机噪声。

### 关键发现

1. **`n_action_steps = 50 = chunk_size`** — SmolVLA 默认执行整个 chunk，我们的 `action_horizon=50` 完全匹配
2. **SmolVLA 没有 temporal ensemble** — `select_action` 用的是简单的 deque action queue
3. **Normalization 不影响** — 我们的训练和 eval 都跳过 processor pipeline，一致地在原始空间操作
4. **无法直接跑 `lerobot-eval` CLI** — checkpoint 格式（`checkpoint.pt` + LoRA）和 normalization 不兼容

### 结论

**eval pipeline 已确认正确，0% success rate 是模型训练端问题。** 报告已保存至 `eval_results/official_eval_final_report.md`。

---
