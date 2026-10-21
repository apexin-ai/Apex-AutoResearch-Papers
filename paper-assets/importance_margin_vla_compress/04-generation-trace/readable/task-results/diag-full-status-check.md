# diag full status check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_full_status_check_20260518T172618_result.json`
- **Structured JSON:** [`5b93259fc6822e485dcd.json`](../../sessions/5b/5b93259fc6822e485dcd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态总览

### westd-27271 (Eval)

| exp_id | GPU | status | result | 
|---|---|---|---|
| eval_official_smolvla_prune_k09 | cuda:0 | **完成** | overall SR = **0.0%** (0/500) |
| eval_official_smolvla_prune_k095 | cuda:1 | **完成** | overall SR = **0.0%** (0/500) |

两个 eval 的 10 个 task SR 全部为 0.0%，所有 episode 均跑满 280 步超时。random prune k=0.9 和 k=0.95（移除 90%/95% token）对 pretrained SmolVLA 完全致命。

### cqa1-33015 (Training)

| exp_id | GPU | status | step/total | loss | speed | ETA |
|---|---|---|---|---|---|---|
| train_baseline_control_100k_v2 | cuda:0 | running | 67700/100000 | 0.056 | 3.9 sps | ~2.3h |
| train_smart_compress_m64_seed43 | cuda:1 | running | 8700/100000 | 0.115 | 4.1 sps | ~6.2h |
| train_smart_compress_m96_seed43 | cuda:2 | running | 68400/100000 | 0.051 | 4.0 sps | ~2.2h |
| train_smart_compress_m32_seed43 | cuda:3 | running | 16000/100000 | 0.060 | 4.1 sps | ~5.7h |

m96 和 baseline 进度接近（~68%），预计约 2h 完成。m32 约 16%，m64 约 8.7%，这两个还需 ~6h。

---
