# ops check m16 seed44 eval

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-m16-seed44-eval_20260520T094946_result.json`
- **Structured JSON:** [`10d0f298e6917927c049.json`](../../sessions/10/10d0f298e6917927c049.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**eval 实际上已成功完成，不是失败。**

```
eval 失败原因: 误报。eval 实际已正常完成（500 eps × 10 tasks = 5000 eps 全部跑完）。
             监控系统在进程退出后检测不到 sentinel/W&B 信号，误判为失败。
             日志最后一行时间 17:15:39，结果文件已写入。

checkpoint 状态: 完好（1.48GB, checkpoint.pt 存在）
checkpoint 路径: /root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m16_seed44/checkpoint.pt

eval 结果:
  suite: libero_object, M=16, seed=44
  Overall SR: 56.5% [95% CI: 55.1%-57.8%]
  Per-task: 38% / 70% / 55% / 42% / 65% / 33% / 73% / 64% / 87% / 38%

cqa1 可用 GPU: 全部 4 张 RTX 4090D 空闲（0/1/2/3, 均 0 MiB used, 0% util）

建议: 无需重新 eval，结果已完整。直接使用 eval_results/eval_smart_compress_m16_seed44.json。
```

---
