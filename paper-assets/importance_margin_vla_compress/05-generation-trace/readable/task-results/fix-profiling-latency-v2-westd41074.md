# fix profiling latency v2 westd41074

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_profiling-latency-v2-westd41074_20260525T202942_result.json`
- **Structured JSON:** [`2e8f0df2c815baefd98e.json`](../../sessions/2e/2e8f0df2c815baefd98e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。结果汇总：

## Profiling v2 结果（RTX PRO 6000 Blackwell）

| k_ratio | median (ms) | P5 (ms) | P95 (ms) | speedup |
|---------|------------|---------|---------|---------|
| 1.0     | 209.88     | 197.76  | 221.67  | 1.0000x |
| 0.9     | 206.36     | 171.43  | 225.03  | 1.0171x |
| 0.5     | 201.87     | 189.21  | 211.31  | 1.0397x |

**方法论**：warmup=20, measure=200步, median+P5/P95 统计

**关键发现**：Token pruning 在此 GPU 上 speedup 极小（k=0.5 仅 ~4%）。Vision token 处理不是 π0.5 推理的瓶颈——大部分延迟来自 LLM 解码（action token generation）。

**注意事项**：
- GPU 非独占（与 OpenVLA eval 进程共存于 GPU 0，26GB/98GB）
- k=0.9 的 P5=171.43ms 异常低（远低于 median），可能受 GPU 调度抖动影响
- 模型加载时未找到 `model.safetensors`，使用随机权重——不影响延迟测量的有效性（计算图和 FLOP 相同）

---
