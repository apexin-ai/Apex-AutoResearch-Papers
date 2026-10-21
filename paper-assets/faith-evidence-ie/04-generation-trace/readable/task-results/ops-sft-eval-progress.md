# ops sft eval progress

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_sft-eval-progress_20260514T124134_result.json`
- **Structured JSON:** [`f315a4b06fc7691d8d7a.json`](../../sessions/f3/f315a4b06fc7691d8d7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 当前进度

| 指标 | 值 |
|------|-----|
| 进度 | **34/247 batches (14%)** |
| 已运行 | 52 min 56 sec（自 19:48 开始） |
| 平均速度 | ~95s/batch |
| 剩余预估 | **5h 38m**（约 02:20 完成） |

### 运行参数

```
--batch_size 4
--max_new_tokens 1024
--quantize (4-bit NF4)
CUDA_VISIBLE_DEVICES=1
```

### GPU 状态

GPU 1 显存：**10,666 MiB / 32,607 MiB (33%)**，利用率 88%。

### 加速分析

**瓶颈在哪：** 4-bit Qwen3-4B (~2.5GB weights) 在 RTX 5090 上做 autoregressive decoding 是 memory-bandwidth bound。batch_size=4 时每个 decode step 只生成 4 个 token，GPU 内存带宽远未饱和。

**batch_size 4 → 16 的可行性：**
- KV cache 估算：batch=4 约 720MB，batch=16 约 2.9GB，总显存约 12.8GB — 32GB 卡完全放得下
- Decode 阶段，权重读取开销不变（~2GB/step），但每 step 产出从 4 token 增至 16 token → 理论上 **~3-4x 加速**
- Batch 数从 247 降至 62
- 保守估计总耗时（含模型加载）：**1.5-2h**

**Restart 成本 vs 收益：**

| 方案 | 剩余耗时 | 说明 |
|------|----------|------|
| 继续跑 (batch_size=4) | **~5h 38m** | 无风险 |
| 重启 (batch_size=16) | **~1.5-2h**（从头） | 丢 53min 已完成进度，净省 ~3.5-4h |
| 重启 (batch_size=32) | **~1-1.5h** | 更激进，显存约 ~16GB 仍可行 |

**max_new_tokens 1024：** greedy decoding 遇到 EOS 会自动停止，1024 只是上限。除非大量 doc 被截断（需看最终 n_truncated），否则缩小这个值影响不大。代码里没有中间结果保存，无法 resume。

### 建议

**重启，batch_size=16**。净省约 3.5h，风险极低（显存充裕、代码已支持 batched generation）。如果想更激进可以试 32。

需要我执行重启吗？

---
