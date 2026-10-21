# diag spatial cache fix

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_spatial-cache-fix_20260521T212824_result.json`
- **Structured JSON:** [`76bc737439312f72eeea.json`](../../sessions/76/76bc737439312f72eeea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**问题已自愈，无需修复。** 报告的 `FileNotFoundError` 是历史快照——spatial precompute 在 03:23 完成后训练已重启。

**实际目录结构**（路径完全正确）：
- `/root/autodl-tmp/crm_cache_pi05/spatial/` — 60,250 samples, 1006M, manifest 完整
- `/root/autodl-tmp/crm_cache_pi05/object/` — 69,303 samples, 1.3G

**两个训练都健康运行**：
- Spatial（CUDA:1，03:09 启动）：epoch 17/50, val_loss=0.0077（持续下降）
- Object（PID 800111，CUDA:0，02:21 启动）：epoch 23/50, val_loss=0.0046（持续下降）

**根因**：pipeline 在 spatial precompute shard6 未完成时（耗时 16112s）就启动了 spatial training，触发 FileNotFoundError。后续被重启后正常。

**建议**（针对未来）：在 pipeline orchestrator 中加 `precompute EXIT_CODE=0` + `manifest.json 存在` 的依赖检查，而非按时序触发。

诊断报告：`spatial_cache_diagnosis.md`（artifact id `art_20260521_75ad4a`）。

---
