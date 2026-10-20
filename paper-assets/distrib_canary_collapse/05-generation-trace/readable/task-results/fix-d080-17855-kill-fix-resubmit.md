# fix d080 17855 kill fix resubmit

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_d080_17855_kill_fix_resubmit_20260519T001837_result.json`
- **Structured JSON:** [`df770e0f8c9a90ffa3a1.json`](../../sessions/df/df770e0f8c9a90ffa3a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D080 执行摘要

**Step 1-2**: 原始 PID 已不存在。发现 GPU 3 上有旧代码启动的 a005_s42_fp32_v3 (PID 69317)，已 kill。`iterative_train.py` 两处 `else None` → `else torch.float32` 修复完成（MD5: `a51bddbed6f1bdf79051283d5238fd19`）。

**Step 3**: 清理完成：
- `a005_s42_fp32_v3/gen_1` 已删除
- `a060_s42_fp32_v2/gen_1+gen_2` 已删除（含 810MB NaN checkpoint）
- `predictive_te_a075_s42_fp32/gen_1+gen_2` 已删除（含 810MB NaN checkpoint）

**Step 4**: Registry 已更新：a005_s42 → failed+notes, a060_fp32_v2 → notes, a060_fp32 → notes, interv_pred_fp32 → notes。

**Step 5**: 三个实验已提交到新 output_dir（`*_d080` 后缀）。

**Step 6**: Qwen3.5 config `torch_dtype=None`，但训练正常（loss=0.71-0.89, grad_norm=14-18），**不受影响**。

**Step 7**: 已设置 15 分钟后自动检查 NaN。

---
