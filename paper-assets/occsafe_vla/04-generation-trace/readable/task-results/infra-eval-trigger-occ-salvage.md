# infra eval trigger occ salvage

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_eval-trigger-occ-salvage_20260521T061839_result.json`
- **Structured JSON:** [`2cb333ce080de45f8171.json`](../../sessions/2c/2cb333ce080de45f8171.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行正常：

- **PID**: 85512
- **状态**: 正在每 120 秒轮询，等待 `*--50000_chkpt` 或 `*--7500_chkpt` 出现
- s0/s2 当前最新 checkpoint 为 47500，最终 checkpoint 尚未生成
- 脚本检测到 final checkpoint 后会等训练 PID 退出，然后自动在对应 GPU 上启动 eval
- eval 结果将保存为 `/root/occsafe_vla/eval_results/occ_s0_salvage.json` 和 `occ_s2_salvage.json`
- 日志: `/root/occsafe_vla/scripts/eval_occ_salvage.log`

---
