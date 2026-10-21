# code plan 701 fallback immediate

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_701-fallback-immediate_20260517T151403_result.json`
- **Structured JSON:** [`7f723b70a43f8936362a.json`](../../sessions/7f/7f723b70a43f8936362a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

1. **Bug 修复**：`train_crm_k1.py` 第 559 行的 `--auto` 逻辑未检查 `--reuse_k10_cache`，导致仍尝试 precompute（缺 LIBERO HDF5 数据而崩溃）。已修复为 `if needs_precompute and not args.reuse_k10_cache:`
2. **训练成功**：50 epochs 在 bjb1-32546 GPU 4 上完成，约 15 分钟。Best val_loss=0.006505 (epoch 43)
3. **Checkpoint**：`/root/autodl-tmp/checkpoints/crm_k1/`
4. **Registry**：已标记 DONE/success

---
