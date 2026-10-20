# diagnose ablation occ detach s3 v2

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_ablation_occ_detach_s3_v2_20260525T202800_result.json`
- **Structured JSON:** [`ba77038228ec73403a5e.json`](../../sessions/ba/ba77038228ec73403a5e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因**：两个实验同一原因 —— `/root/autodl-tmp` 磁盘 250GB 100% 占满（checkpoints 占 229GB）。两个实验都成功训练了 step 20000→30000 的 10k 步，但在 step 30000 保存 checkpoint 时 `safetensors` 序列化因磁盘空间不足报 `os error 28` 失败。

**关键发现**：
- 两个实验的 30000 checkpoint 均不完整（损坏），需要删除
- 20000 checkpoint 完好，可以重新 resume
- 重试前必须清理磁盘，建议至少释放 30-50GB

报告已写入 `artifacts/diagnose_s3_v2_failures.md`。

---
