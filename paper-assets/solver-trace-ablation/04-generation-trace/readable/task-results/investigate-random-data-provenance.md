# investigate random data provenance

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_random-data-provenance_20260515T141005_result.json`
- **Structured JSON:** [`e5f39be7d620109de4f9.json`](../../sessions/e5/e5f39be7d620109de4f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the full report:

---

## plan018-random-b01-s42
- **output_dir**: `plan018_additive_random_b01_s42/` → **DELETED**
  - Alternative: `_1000/` (16MB, metadata only) and `_1000_r3/` (16MB, metadata only) exist but are **different model runs**
- **checkpoint**: **NOT_FOUND** — no .safetensors in any dir (all 3 dirs are 16MB = tokenizer + config only, weights stripped)
- **eval_sta_results.json**: **EXISTS** — standalone at `/root/autodl-tmp/outputs/eval_sta_plan018_additive_random_b01_s42.json`
  - prove_rate=0.79, mean_isr=0.1038, n_proved=79, model_path points to original (deleted) dir
  - Contains full per-sample STA details (100 problems)
- **_1000/eval/sta_results.json**: EXISTS but **WRONG MODEL** — degenerate collapse (prove_rate=1.0, ISR=0.3333 for ALL samples, all formalizations are `∀x (Person(x, "Google", x))`)
- **_1000_r3/eval_results.json**: EXISTS but **DIFFERENT MODEL** — prove_rate=0.97, mean_isr=0.6892
- **H7 taxonomy files**: **NOT_FOUND**
- **H8 audit file**: **NOT_FOUND** (the only H8 file on disk is for plan002/ISR side)
- **Backup**: EXISTS in both `eval_results_backup/` and `eval_backups/` — same content as standalone eval_sta file
- **genuine_count 可验证**: **PARTIALLY** — eval file has per-sample STA data, but no H7/H8 classification file on disk. Registry's genuine_count=23 cannot be independently reproduced from files alone (needs rerunning H7/H8 taxonomy pipeline on the eval file).

## plan018-random-b01-s43-r2
- **output_dir**: **NOT_FOUND**
- **checkpoint**: **NOT_FOUND**
- **eval_sta_results.json**: **NOT_FOUND**
- **eval_results.json**: **NOT_FOUND**
- **H7 taxonomy files**: **NOT_FOUND**
- **Backup**: **NOT_FOUND** (nothing in either backup dir)
- **Training log only**: `/root/runs/solver-trace-ablation/plan018-additive-random-b01-s43-r2.log` — training completed 500 steps, final reward stats: prove_rate=0.5925, mean_isr=0.0988 (⚠️ training log metrics, NOT eval_sta — per C004 不可用于跨 run 对比)
- **Config**: `/root/solver-trace-ablation/configs/plan018_random_b01_s43.yaml`
- **genuine_count 可验证**: **NO** — zero eval artifacts on disk. Registry's genuine_count=6 has no supporting evidence.

## plan018-random-b01-s44
- **output_dir**: **NOT_FOUND**
- **checkpoint**: **NOT_FOUND** (registry 记录的 `checkpoint-500` 已删除)
- **eval_sta_results.json**: **NOT_FOUND**
- **eval_results.json**: **NOT_FOUND**
- **H7 taxonomy files**: **NOT_FOUND**
- **Backup**: **NOT_FOUND**
- **Training log only**: `/root/runs/solver-trace-ablation/plan018-additive-random-b01-s44.log` — training completed 500 steps, final reward stats: prove_rate=0.64675, mean_isr=0.08092 (training log only)
- **Config**: `/root/solver-trace-ablation/configs/plan018_random_b01_s44.yaml`
- **genuine_count 可验证**: **NO** — no eval file, no genuine_count in registry (18 is pooled 推算值), no checkpoint to re-eval.

## ISR 侧 eval 文件
- **plan002 ISR β=0.1 s42**: `/root/autodl-tmp/outputs/plan002_additive_b01_s42_1000/eval/eval_sta_results.json` — prove_rate=0.90, mean_isr=0.7892
  - Backup: `/root/autodl-tmp/eval_results_backup/plan002_additive_b01_s42_eval_sta_results.json`
  - H8 audit: `/root/autodl-tmp/outputs/h7_classification/plan002_additive_b01_s42_h8.json` — genuine_count=14
  - Model weights: **NOT_FOUND** (dir 16MB, metadata only)
- **plan002 ISR β=0.1 s43/s44**: **NOT_FOUND** — no files anywhere
- **plan018 ISR (non-random) dirs**: **NOT_FOUND**

## 备份目录状态
| 目录 | 文件数 | 内容 |
|------|--------|------|
| `eval_results_backup/` | 3 | plan002_s42, plan016_s42, plan018_random_s42 |
| `eval_backups/` | 1 | plan018_random_s42 (same content) |

## 磁盘
47G / 250G used (19%)

---

## 结论

| 实验 | Eval 可溯源 | Checkpoint 可重评 | genuine_count 来源 |
|------|------------|-------------------|-------------------|
| s42 | **YES** — standalone eval_sta file exists | **NO** — weights deleted | Registry only (需重跑 H7/H8 pipeline 验证) |
| s43-r2 | **NO** — 完全丢失 | **NO** — 完全丢失 | Registry only, 无任何证据 |
| s44 | **NO** — 完全丢失 | **NO** — 完全丢失 | 推算值, 无原始数据 |

**Critical**: s43-r2 和 s44 的 eval 数据、checkpoint 全部丢失，无法溯源也无法重评。论文中使用的 genuine_count（s43=6, s44=18推算）仅存于 registry 记录中。如需论文数据可验证，这两个实验必须重训+重评。

---
