# ops check gradient analysis and start

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_gradient_analysis_and_start_20260524T114843_result.json`
- **Structured JSON:** [`1715d779178701340e46.json`](../../sessions/17/1715d779178701340e46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**gradient_analysis_mixed_seed 已成功完成，无需重启。**

- pid 821589 已退出，EXIT_CODE=0
- 5 个条件全部跑完（Vanilla_s0, Full_OCC_s0, Detach_LN_s0, Detach_BN_s2, Random_s2），200 batches each
- 产出在 `/root/occsafe_vla/artifacts/gradient_analysis_mixed_seed/`（每条件一个 `*_gradient_stats.json` + `*_gradient_norms.pdf`）
- 耗时 ~25 分钟（wall_clock 1480s, 0.41 GPU-hours）
- Registry 已更新为 DONE/success

GPU 状态备注：GPU 0 当前被 pid 823309 占用（16.7GB），GPU 1 空闲，GPU 2/3 被训练任务占用。

---
