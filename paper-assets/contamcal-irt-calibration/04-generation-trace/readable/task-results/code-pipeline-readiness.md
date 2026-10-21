# code pipeline readiness

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pipeline_readiness_20260514T123858_result.json`
- **Structured JSON:** [`c11f212941bae521c335.json`](../../sessions/c1/c11f212941bae521c335.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks complete. Here's the readiness report:

---

## Pipeline Readiness Report

### 1. exp-003 RRF Aggregation (CPU)

| 检查项 | 状态 |
|--------|------|
| `aggregate_rrf.py` 存在 | ✅ 12KB, 今天 18:44 更新 |
| `--generate-exposure` 标志 | ✅ 存在 |
| `--signal-dir`, `--benchmarks`, `--k`, `--normalize` 参数 | ✅ 全部存在 |
| 输出目录 `/root/autodl-tmp/exp003/` | ❌ **不存在，需创建** |
| 0.5B signal 文件 | ⚠️ 进行中（见下） |

**当前 0.5B signal 完成度：**
- `d000_s42`: embedding×3 + minkpp_mmlu = 4/12 文件
- `d005_s42`: embedding_mmlu = 1/12 文件
- 缺失：minkpp (gsm8k, arc), constat (全部), selfcritique (全部)

### 2. exp-006 IRT Calibration + 7 Baselines

| 检查项 | 状态 |
|--------|------|
| Stan 模型已编译 | ✅ 4个 (2pl_gamma, 4pl, 4pl_simple, vanilla_4pl) |
| CmdStanPy | ✅ v1.3.0, cmdstan-2.38.0 |
| baselines.py (B0-B6) | ✅ 7个基线全部实现 (Raw, Remove-rescore, Single-signal 2PL+γ, Vanilla 4PL, Linear regression, Emperor, DCR fuzzy) |
| `run_exp006.py` | ✅ 有 `--dry-run` 和 `--skip-stan` 标志 |
| `evaluate_calibration.py` | ✅ 存在 |
| `baselines/` 独立目录 | ⚠️ 无独立目录，baselines 统一在 `baselines.py`（`_baselines_v1/` 是旧版模块化代码） |

### 3. exp-002 后续 (1.5B/3B Signals)

| 检查项 | 状态 |
|--------|------|
| `compute_signals.py` | ✅ 8KB, 今天 18:04 更新 |
| selfcritique `BATCH_SIZE=32` 热修复 | ✅ `signal_selfcritique.py` 中硬编码 `BATCH_SIZE = 32`，不受 args.batch_size 影响 |
| 1.5B eval 结果 | ✅ 6个变体 (d000_s42, d000_s123, d100_s42, aligned, para_aligned, d005_s42_aligned) |
| 3B eval 结果 | ✅ 5个变体 (d000_s42, d000_s123, raw, d000_s42_aligned, d100_s42_aligned) |

---

### Blockers

1. **❌ `/root/autodl-tmp/exp003/` 目录不存在** — 需要在 exp-003 启动前创建（`mkdir -p /root/autodl-tmp/exp003`），或确认 `aggregate_rrf.py` 会自动创建。

### 无 Blocker 项

整个 pipeline 代码和依赖就绪。exp-002 0.5B signals 完成后，exp-003 和 exp-006 可立即启动，唯一需要的预操作是创建 exp003 输出目录。

---
