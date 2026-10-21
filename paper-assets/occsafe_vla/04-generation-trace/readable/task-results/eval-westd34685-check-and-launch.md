# eval westd34685 check and launch

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_westd34685_check_and_launch_20260522T234214_result.json`
- **Structured JSON:** [`1ff76ddc17557279bdc3.json`](../../sessions/1f/1ff76ddc17557279bdc3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部仍在训练，尚无 `50000_chkpt`，暂不启动 eval。

## 训练状态汇总

| 实验 | 最新 step | 进度 | 最新 checkpoint | 预估剩余 |
|------|-----------|------|----------------|---------|
| cutoff_s0 | 46258/50005 | 92% | 40000_chkpt | ~60 min |
| cutoff_s1 | 48326/50005 | 97% | 40000_chkpt | ~28 min |
| depth_s0 | 48299/50005 | 97% | 40000_chkpt | ~28 min |
| depth_s1 | 48164/50005 | 96% | 40000_chkpt | ~31 min |

**最新 loss（来自日志）**：
- cutoff_s0 (step 46200): occ=0.0102, depth=0.0000, action=0.0371
- cutoff_s1 (step 48300): occ=0.0090, depth=0.0000, action=0.0598
- depth_s0 未在可见范围内打印 AUX
- depth_s1 (step 48100): occ=0.0000, depth=0.0163, action=0.0520

所有实验运行正常，~1 it/s（偶有 IO 抖动导致慢 step）。cutoff_s1/depth_s0/depth_s1 约 30 分钟内完成，cutoff_s0 约 1 小时。需要我稍后回来检查并启动 eval 吗？

---
