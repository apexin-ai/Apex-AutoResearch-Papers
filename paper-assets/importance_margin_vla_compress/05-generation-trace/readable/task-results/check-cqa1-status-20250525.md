# check cqa1 status 20250525

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cqa1_status_20250525_20260525T224932_result.json`
- **Structured JSON:** [`01b2873a0ffb70ba65e8.json`](../../sessions/01/01b2873a0ffb70ba65e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

```
GPU0: [running] 进度 5.5/10 tasks, 表现优异
  - zeromask_random k=0.9 Object (v2)
  - T0=100%, T1=100%, T2=100%, T3=100%, T4=96%, T5 进行中(ep10: 90%)
  - Log 持续更新 (06:50), 预估再 ~50min 完成

GPU1: [⚠️ STUCK] Log 冻结 55 分钟，GPU 利用率 0%
  - l2norm k=0.75 Long (v3)
  - 最后输出: T0 ep10=100% (05:55:38)，之后无任何新输出
  - 进程仍占 9780MiB 显存但 GPU-Util=0%
  - 诊断: 进程挂起，可能死锁或等待 I/O

GPU2: [running] 进度 1.8/10 tasks
  - random k=0.75 Long
  - T0=84%, T1 进行中(ep40: 75%)
  - Log 持续更新 (06:47), 正常运行

GPU3: [running but 0% SR] 确认异常 — 不是 bug 而是模型失效
  - OpenVLA Attn k=0.9 Goal seed43
  - T1: 0/50=0%, T2 进行中(ep30: 0/30=0%)
  - 无 crash/error，GPU 70% 利用率正常推理
  - 根因: transformers==5.5.3 vs 模型期望 4.40.1
    模型加载时有明确警告 "there might be inference-time regressions"
    attention pruning 在新版 transformers 下可能选错 token 或 attention 计算异常
```

**需要处理**:
1. **GPU1**: 进程卡死，需要 kill 并重启
2. **GPU3**: transformers 版本不匹配导致 0% SR。两种方案：
   - (a) 降级 transformers 到 4.40.1 后重跑
   - (b) 如果其他 OpenVLA 实验（不带 prune）在同环境下也 0%，说明是全局环境问题

要我执行修复操作吗？

---
