# ops unified baselines pipeline

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_unified_baselines_pipeline_20260517T164317_result.json`
- **Structured JSON:** [`9ea28bcc51af361ba1e5.json`](../../sessions/9e/9ea28bcc51af361ba1e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完整 Baseline 对比表

**Ground truth** = per-scale d=0 model accuracy, MAE = mean|calibrated - GT|, τ = Kendall(calibrated, GT), * = p<0.05

### MMLU + ARC: J=16 (1.5B+3B, 300 items)

| Method | MMLU MAE | MMLU τ | ARC MAE | ARC τ |
|--------|----------|--------|---------|-------|
| B0: Raw Accuracy | 0.0056 | 0.767* | 0.0067 | 0.695* |
| B1: DRC (oracle) | 0.1955 | 0.178 | 0.2605 | 0.217 |
| B1b: Remove & Rescore | 0.0258 | 0.783* | 0.0143 | 0.673* |
| B3: Vanilla 2PL | 0.0080 | 0.731* | 0.0145 | 0.597* |
| B4: Linear Regression | 0.0096 | 0.751* | 0.0123 | 0.731* |
| B5: Threshold | 0.0373 | -0.030 | 0.0177 | 0.628* |
| B5b: Emperor | 0.0060 | 0.789* | 0.0067 | 0.674* |
| B6: DCR Fuzzy | 0.1081 | 0.654* | 0.3138 | 0.173 |
| ContamCal (2PL+γ) | 0.0091 | 0.731* | 0.0196 | 0.609* |

### GSM8K (excl 3B): J=16 (0.5B+1.5B, 300 items)

| Method | GSM8K MAE | GSM8K τ |
|--------|-----------|---------|
| B0: Raw Accuracy | 0.0213 | 0.647* |
| B1: DRC (oracle) | 0.1456 | 0.415* |
| B1b: Remove & Rescore | 0.0306 | 0.705* |
| B3: Vanilla 2PL | 0.0246 | 0.635* |
| B4: Linear Regression | 0.0702 | 0.654* |
| B5: Threshold | 0.0298 | 0.725* |
| B5b: Emperor | 0.0218 | 0.654* |
| B6: DCR Fuzzy | 0.1575 | 0.654* |
| ContamCal (2PL+γ) | 0.0233 | 0.635* |

### 关键发现

1. **Contamination 对 aggregate accuracy 的影响很小** — MMLU/ARC 上 d=100 模型与 d=0 模型的 accuracy 差异仅 ~0.01，因此 Raw Accuracy 已是强 baseline（MAE=0.006）。这说明 aggregate accuracy 不是衡量 contamination 严重程度的好指标。

2. **ContamCal 的 MAE 未优于 Raw** — 因 contamination 对 aggregate score 的影响太小，IRT 校准反而轻微 overcorrect。ContamCal 的价值在于 γ 估计（检测 contamination 存在）和 per-item 分析，而非 aggregate MAE 改善。

3. **GSM8K 3B d000 异常** — 3B d000 模型 GSM8K accuracy 仅 0.11-0.16（LoRA damage），使 ground truth 无效。排除 3B 后 GSM8K 结果正常（MAE ~0.02）。

4. **γ 值**: MMLU γ=0.698 [-0.42, 1.81], ARC γ=0.727 [0.02, 1.44] (CI excludes 0), GSM8K γ=0.064 (接近 0)

5. **B1 DRC 和 B6 DCR 系统性高估** contamination 影响，MAE > 0.1。

**结果已保存**: `/root/autodl-tmp/exp006/unified_baselines_n16/`
- `all_results.json` — 完整结果含 per-model data
- `final_summary.json` — 汇总表
- 脚本: `exp006/compute_all_baselines_unified.py`

---
