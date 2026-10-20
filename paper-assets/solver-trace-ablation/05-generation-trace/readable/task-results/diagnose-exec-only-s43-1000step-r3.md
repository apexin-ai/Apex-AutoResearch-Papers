# diagnose exec only s43 1000step r3

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exec-only-s43-1000step-r3_20260516T232834_result.json`
- **Structured JSON:** [`1169b85e53568fdf965b.json`](../../sessions/11/1169b85e53568fdf965b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**OOM 位置**: Step 9 的 forward pass（计算 per-token logps），step 8 正常完成后崩溃。

**根因: 无 gradient checkpointing + 内存碎片化**

关键证据:
- `gradient_checkpointing=False`（代码 L573，config 中未设置）
- OOM 时 PyTorch 已分配 90.67 GiB，另有 **3.58 GiB reserved but unallocated**（碎片化标志）
- 每步 logps forward 处理 batch_size(4) × num_generations(4) = 16 条序列，序列长度可达 prompt + 512 tokens
- Full-param 4B + AdamW: model(~8GB) + optimizer(~48GB) + gradients(~8GB) = ~64GB 固定开销，仅剩 ~31GB 给 activations
- 之前 plan001-exec-only-s43-1000 存活到 step 150（后因 disk full 死），说明该配置在 95GB GPU 上处于内存边界，偶发碎片化/长序列批次即可触发 OOM

**为什么 r3 比之前更早崩溃**: step 9 的序列组合 + PyTorch 分配碎片化模式刚好超限。3.58 GiB 空间存在但因碎片化无法被使用。

## 修复建议

**首选**（影响最小，效果最大）:
```bash
# 在启动命令中加参数或修改代码 default
--gradient_checkpointing True
```
加上环境变量:
```bash
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
```

这将 activation 内存降低 ~80%，同时解决碎片化问题。训练速度约慢 10-20%，但 95GB GPU 跑 4B full-param GRPO 会非常安全。

**备选**（如不想加 gradient checkpointing）:
- `per_device_batch_size` 从 4 降到 2（effective batch 不变可以把 gradient_accumulation_steps 从 2 改 4）

---
