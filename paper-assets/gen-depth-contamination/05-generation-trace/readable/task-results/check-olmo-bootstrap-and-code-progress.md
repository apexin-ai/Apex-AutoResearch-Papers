# check olmo bootstrap and code progress

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_olmo_bootstrap_and_code_progress_20260520T055154_result.json`
- **Structured JSON:** [`b3c178897d16d20acebb.json`](../../sessions/b3/b3c178897d16d20acebb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

### OLMo 10k Bootstrap
状态: **运行中**
- Pipeline 今日 12:43 启动，配置: OLMo-1B, C4 continuation, 5000 samples, max depth 5
- **Step 3 (Depth Chain) ✅ 完成** — 5 个 depth 全部生成完毕 (12:43→13:48, 每 depth ~13 min)
- **Step 4 (Feature Extraction) 🔄 进行中** — 13:48 开始，当前在 VocabDiv d=1 (~5%)
- 剩余: 完成 depths 1-5 的特征提取 (~20 min) + 后续 bootstrap 步骤
- 预计完成: ~14:20-14:30 (北京时间)

注意: 日志显示 `Samples: 5000`，不是 10000。如果需要 10k samples 需要确认配置是否正确（可能 "10k" 指的是 bootstrap iterations B=10000 而非 sample 数）。

### Code DeBERTa (cuda:3)
状态: **运行中**
- PID 285392 存活，已运行 21h11m
- 进度: **Fold 1/5, Epoch 1/3, Step 400/1650**
  - Fold 0 已完成 (3 epochs)
  - 每 200 steps ≈ 45s → 每 fold ≈ 18.5 min
- 剩余: fold 1 剩余 ~17 min + folds 2-4 ~58 min = **~75 min**
- 预计完成: ~15:07 (北京时间)
- GPU: cuda:3 utilization **97%**, memory **19427/24564 MiB** (79%)

---
