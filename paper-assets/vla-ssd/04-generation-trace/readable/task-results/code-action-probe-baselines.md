# code action probe baselines

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_action-probe-baselines_20260515T141645_result.json`
- **Structured JSON:** [`16975fe0ae49460bf313.json`](../../sessions/16/16975fe0ae49460bf313.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行完成。结果：

### Action Prediction Baselines

| Metric | Copy Baseline | Random-Frame Baseline |
|---|---|---|
| **Global Overall R²** | **0.9751** | **-0.9100** |
| **Per-Task Mean R²** | **0.9720** | **-0.9771** |

**Per-dim R² (Copy baseline):**

| dx | dy | dz | drx | dry | drz | grip |
|---|---|---|---|---|---|---|
| 0.979 | 0.988 | 0.982 | 0.971 | 0.966 | 0.991 | 0.949 |

**关键结论：**

1. **Copy baseline R² = 0.975** — 极高，证实 Director 的担忧：LIBERO 轨迹 action 自相关非常强，相邻帧 action 几乎相同。这意味着 **action prediction probe 的 R² 必须显著超过 0.975 才能说明 hidden state 编码了超越简单时序自相关的信息**。
2. **Random-frame baseline R² ≈ -0.9** — 如预期，随机帧毫无预测力（负 R² 说明比 predict-mean 还差）。
3. 所有 10 个 task 的 copy baseline R² 都在 0.96–0.98 之间，非常一致。

结果已保存到 `/root/autodl-tmp/vla-ssd/results/action_baselines.json`，脚本在 `/root/vla-ssd/action_baselines.py`。

---
