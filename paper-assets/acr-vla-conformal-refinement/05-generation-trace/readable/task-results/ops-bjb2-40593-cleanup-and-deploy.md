# ops bjb2 40593 cleanup and deploy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb2-40593-cleanup-and-deploy_20260516T071715_result.json`
- **Structured JSON:** [`7737fa27dffcf0475614.json`](../../sessions/77/7737fa27dffcf0475614.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 清理
- killed 残留 scalar 评估进程 PID 310859（`crm_scalar --benchmark object --seed 44`），释放 5609 MiB VRAM
- GPU 释放后：0 MiB / 24564 MiB, 0% utilization

## 系统内存
- Total: 503 GiB, Available: 445 GiB — 充足

## 部署
- **exp_id**: eval-perdof-object-default-seed44
- **PID**: 316387 (GPU process) / 316382 (tmux)
- **VRAM**: 5609 MiB / 24564 MiB
- **GPU Util**: 9%
- **状态**: RUNNING，模型加载完成，正在评估
- **参数**: `--mode crm_perdof --benchmark object --seed 44 --K 10`，未传 `--max_correction_norm`（使用默认值 ~1.42）

## 问题
无

---
