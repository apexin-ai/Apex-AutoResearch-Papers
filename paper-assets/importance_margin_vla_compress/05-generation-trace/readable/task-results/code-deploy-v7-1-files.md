# code deploy v7 1 files

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_deploy-v7_1-files_20260515T182219_result.json`
- **Structured JSON:** [`400c44a82b86a0a74faa.json`](../../sessions/40/400c44a82b86a0a74faa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件部署成功，验证全部通过：

- **`configs/imm_anchor_v7_1.yaml`** — 内容正确，`lambda_margin=0.2`, `grad_clip=30.0`
- **`train.py`** — split-loss logging 已更新，IMM 模式下会打印 `action=`, `margin_loss=`, `Δ=` 分项；语法检查通过

---
