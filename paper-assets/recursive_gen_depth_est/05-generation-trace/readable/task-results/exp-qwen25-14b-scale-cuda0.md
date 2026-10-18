# exp qwen25 14b scale cuda0

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_qwen25_14b_scale_cuda0_20260517T174654_result.json`
- **Structured JSON:** [`d874ce62982ae0d73585.json`](../../sessions/d8/d874ce62982ae0d73585.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**问题：cuda:0 已被占用。**

PID 806751 正在 cuda:0 上运行 `qwen25_14b_scale_validation.py`（32302 MiB），当前状态：
- 模型已完整加载（8/8 shards，FP16）
- 正在生成 d0：**411/5000 samples**（刚开始）
- 配置：d0-d3, 5000 samples/depth（与你要求的 d0-d5, 500 samples/depth 不同）
- checkpoints 目录为空

两个冲突点：
1. **cuda:0 不空闲** — 无法直接提交新任务
2. **配置不匹配** — 运行中的实验是 d0-d3/5000 samples，你要求的是 d0-d5/500 samples

选项：
- **A**: 让当前 d0-d3/5000 实验继续跑完（统计效力更强，与之前实验一致）
- **B**: kill 当前进程，改为 d0-d5/500 samples 提交新实验
- **C**: 等当前实验完成后再提交 d0-d5 版本

怎么处理？

---
