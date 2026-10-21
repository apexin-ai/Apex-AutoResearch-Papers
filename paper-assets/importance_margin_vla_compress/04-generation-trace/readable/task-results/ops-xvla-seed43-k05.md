# ops xvla seed43 k05

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_xvla-seed43-k05_20260520T115837_result.json`
- **Structured JSON:** [`8e5ea169e5e586ce04a0.json`](../../sessions/8e/8e5ea169e5e586ce04a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

k=0.5 eval 已在 GPU 3 上成功启动并运行 (PID 894191)，已完成 2/50 episodes。

**汇总：**

| GPU | 任务 | PID | 状态 |
|-----|------|-----|------|
| 0 | OpenVLA SC m128 eval (seed42) | 858906 | 运行中 (~43min) |
| 1 | X-VLA k=0.9 seed43 | 866924 | 运行中 |
| 2 | X-VLA k=0.7 seed43 | 868193 | 运行中 |
| 3 | **X-VLA k=0.5 seed43** | **894191** | **刚启动，2/50 ep** |

**注意事项：**
- GPU 0 未释放，被 OpenVLA SC eval 占用，k=0.5 改到 GPU 3 启动
- OFT CV (PID 869442) 已崩溃，错误：`RuntimeError: expected mat1 and mat2 to have the same dtype, but got: float != c10::BFloat16`（linear 层输入 float32 vs 权重 bfloat16 不匹配）

---
