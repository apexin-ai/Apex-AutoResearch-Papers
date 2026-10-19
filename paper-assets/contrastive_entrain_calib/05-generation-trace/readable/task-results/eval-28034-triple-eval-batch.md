# eval 28034 triple eval batch

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_28034-triple-eval-batch_20260523T005351_result.json`
- **Structured JSON:** [`629a6956224a41acf518.json`](../../sessions/62/629a6956224a41acf518.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 eval 全部启动确认完毕，15 分钟后回来检查结果。

**当前状态汇总：**

```
=== 之前 ACT s2 结果（已完成）===
ckpt-6500: SYCONScore=0.2543, ToF=0.1492, NoF=0.8619
ckpt-7000: SYCONScore=0.2858, ToF=0.1713, NoF=0.8619

=== 本轮 eval 启动 ===
GPU0: reduced-lora ckpt-2500, PID=146135 (之前已在跑)
GPU2: reduced-lora ckpt-3000, PID=146802
GPU3: reduced-lora ckpt-3500, PID=147325
GPU1: reduced-lora 训练中 (不动)

=== 备注 ===
- ACT s2 ckpt-7500 在 29046 已产出，但 28034→29046 SCP 失败（无 SSH key），需后续安排
- 预计 09:20 左右全部完成
```

---
