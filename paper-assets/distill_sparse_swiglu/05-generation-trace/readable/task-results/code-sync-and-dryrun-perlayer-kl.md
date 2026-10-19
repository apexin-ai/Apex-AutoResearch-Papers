# code sync and dryrun perlayer kl

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sync_and_dryrun_perlayer_kl_20260521T020437_result.json`
- **Structured JSON:** [`bf21eaacbe49c06b03d5.json`](../../sessions/bf/bf21eaacbe49c06b03d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

DRY-RUN OK.

- 文件已同步（322 行，MD5 匹配：`9dc34eb4c9111f90966476cbabe5ea8f`）
- 2 步 dry-run 通过：`[Step 1/2] layer=7 kl=0.0108 sparsity=0.383` 和 `[Step 2/2] layer=1 kl=0.6641 sparsity=0.371`
- Predictor 参数 75,960,320 (144.9 MB bf16) — 符合 C003 约束（75.9M total）
- Per-layer Lagrangian、随机 layer 采样、checkpoint 保存全部正常
- 总耗时 8.3s（含 gradient checkpointing，cuda:0）

---
