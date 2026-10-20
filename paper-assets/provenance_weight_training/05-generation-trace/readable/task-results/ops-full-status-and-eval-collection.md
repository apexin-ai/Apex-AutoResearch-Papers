# ops full status and eval collection

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full-status-and-eval-collection_20260514T105031_result.json`
- **Structured JSON:** [`d33a6994cb4f138dafa3.json`](../../sessions/d3/d33a6994cb4f138dafa3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。

## GPU 状态

| GPU | 利用率 | 显存占用 | 总显存 |
|-----|--------|----------|--------|
| 0 | 98% | 46523 MiB | 97887 MiB |
| 1 | 99% | 46523 MiB | 97887 MiB |
| 2 | 99% | 46523 MiB | 97887 MiB |
| 3 | 94% | 64845 MiB | 97887 MiB |

4 GPU 全部满载，GPU 3 有 3 个 python 进程（1 个训练 + 2 个小进程 ~9GB 各）。

## Eval Watcher

- PID 74145: **ALIVE**
- 已产出 4 个 eval 文件，最近完成 grid_b1_0_seed123 eval（18:48）

## 已完成训练的模型

| Model | final/ 存在 |
|-------|------------|
| uniform_seed42 | ✓ |
| uniform_seed123 | ✓ |
| uniform_seed456 | ✓ |
| adaptive_seed42 | ✓ |
| adaptive_seed123 | ✓ |
| adaptive_seed456 | ✓ |
| diagnostic_contamination0_seed42 | ✓ |
| grid_b0_5_seed42 | ✓ |
| grid_b0_5_seed123 | ✓ |
| grid_b1_0_seed42 | ✓ |
| grid_b1_0_seed123 | ✓ |

## 正在训练

| 任务 | 进度 | 预计剩余 |
|------|------|----------|
| grid_b1_5_seed42 (batch) | 91% (5561/6103) | ~19 min |
| grid_b1_5_seed123 | 94% (5770/6103) | ~32 min |
| grid_b2_0_seed123 | 7% (410/6103) | ~3h21m |
| grid_b3_0_seed123 | 2% (124/6103) | ~3h31m |

batch 脚本当前在 b=1.5，完成后将依次训练 b=2.0, 3.0, 5.0（seed42）。

`diagnostic_contamination100_seed42` 目录存在（有 config.json + step_metrics.jsonl），但无 final/、无 checkpoint、无 run log，状态不明。

## Eval 结果汇总

| Method | b | Seed | Loss | Eval PPL | 状态 |
|--------|---|------|------|----------|------|
| grid | 0.5 | 42 | 2.8708 | **17.651** | ✅ eval 完成 |
| grid | 0.5 | 123 | 2.8701 | **17.638** | ✅ eval 完成 |
| grid | 1.0 | 42 | 2.8731 | **17.692** | ✅ eval 完成 |
| grid | 1.0 | 123 | 2.8721 | **17.674** | ✅ eval 完成 |
| grid | 1.5 | 42 | — | — | 🔄 训练中 91% |
| grid | 1.5 | 123 | — | — | 🔄 训练中 94% |
| grid | 2.0 | 123 | — | — | 🔄 训练中 7% |
| grid | 3.0 | 123 | — | — | 🔄 训练中 2% |
| grid | 2.0 | 42 | — | — | ⏳ 排队（batch 等 b1.5 完成） |
| grid | 3.0 | 42 | — | — | ⏳ 排队 |
| grid | 5.0 | 42 | — | — | ⏳ 排队 |
| grid | 5.0 | 123 | — | — | ❌ 未启动 |
| uniform | — | 42 | — | — | ✅ 训练完成，未 eval |
| uniform | — | 123 | — | — | ✅ 训练完成，未 eval |
| uniform | — | 456 | — | — | ✅ 训练完成，未 eval |
| adaptive | — | 42 | — | — | ✅ 训练完成，未 eval |
| adaptive | — | 123 | — | — | ✅ 训练完成，未 eval |
| adaptive | — | 456 | — | — | ✅ 训练完成，未 eval |
| diag_contam0 | — | 42 | — | — | ✅ 训练完成，未 eval |
| diag_contam100 | — | 42 | — | — | ❓ 状态不明 |

已有 eval 数据中，b=0.5 的 PPL 略优于 b=1.0（两个 seed 一致）。auto_eval_watcher 运行正常，新完成的 grid_b 模型会自动触发 eval。uniform/adaptive/diagnostic 模型尚无 eval 结果。

---
