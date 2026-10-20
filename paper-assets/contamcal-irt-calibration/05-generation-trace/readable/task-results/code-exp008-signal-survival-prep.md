# code exp008 signal survival prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp008-signal-survival-prep_20260514T080035_result.json`
- **Structured JSON:** [`f98af002f1de5193e998.json`](../../sessions/f9/f98af002f1de5193e998.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## exp-008 Signal Survival Analysis 调研报告

### 1. 目录/代码现状

exp008/ 已有 3 个完整脚本，代码已升级到 **v2 N-regime** 架构：

| 文件 | 功能 |
|------|------|
| `signal_survival_analysis.py` (14KB) | 核心分析：AUC matrix + pairwise 统计检验（Cohen's d, Spearman, Wilcoxon） |
| `run_signal_survival.py` (8KB) | 执行入口：`--regime-dirs base=/path SFT=/path RL=/path`，有 dry-run |
| `plot_survival.py` (7KB) | 可视化：AUC heatmap + delta-AUC heatmap (PDF) |

`exp008_output/survival_report.json` 是 **mock data 的 dry-run 结果**（n=10, 2 regime），非真实数据。

### 2. 可用 RL-trained 模型

HF cache 中 **无 Instruct 模型**。已有：
- Qwen2.5-0.5B / 1.5B / 3B (base only)
- Qwen3-14B-AWQ, Qwen3-8B（不适用）

**Qwen2.5-0.5B-Instruct 缺失**，需下载。

### 3. 缺失项

| 缺失项 | 说明 | 解决方案 |
|--------|------|---------|
| **Qwen2.5-0.5B-Instruct** | Regime 4 唯一模型 | ModelScope 下载，~30 min |
| **d000 contamination labels** | d000 = 0% contamination，无 label 文件 | 程序生成全 0 labels |
| **exp-002 信号数据** | 仅完成 d000_s42/embedding/mmlu | 需对 4 个 regime 全量计算 |

已有 contamination labels：d005/d025/d050/d100 × mmlu/gsm8k/arc_challenge

### 4. exp-002 信号脚本兼容性

| Regime | 调用方式 | 兼容性 |
|--------|---------|--------|
| **base** (raw Qwen2.5-0.5B) | `--model-path BASE` 不传 adapter | ✅ adapter_path=None 时直接用 base model |
| **SFT-clean** (d000_s42) | `--model-path BASE --adapter-path d000_s42/lora_adapter` | ✅ |
| **SFT-contaminated** (d100_s42) | `--model-path BASE --adapter-path d100_s42/lora_adapter` | ✅ |
| **RL-post-trained** (Instruct) | `--model-path Instruct` 不传 adapter | ✅ 理论兼容 |

Min-K%++ 的 ref_model：所有 regime 统一用 base Qwen2.5-0.5B（或 d000 adapter）。

### 5. 建议的实验设计

**Regime 矩阵** (聚焦 0.5B)：

```
Regime 1: base         → Qwen2.5-0.5B (no adapter)
Regime 2: SFT-clean    → Qwen2.5-0.5B + d000_s42 LoRA
Regime 3: SFT-contam   → Qwen2.5-0.5B + d100_s42 LoRA  
Regime 4: RL-aligned   → Qwen2.5-0.5B-Instruct (需下载)
```

**信号 × benchmark**：4 signals × 3 benchmarks (mmlu/gsm8k/arc_challenge) = 12 runs/regime

**Labels**：用 d100 的 contamination labels（标记了哪些 benchmark items 被注入 SFT 训练集）。base 和 SFT-clean 虽未被 contaminate，但用同一份 labels 能比较检测 AUC 的 baseline。

**执行架构**：写一个 `run_exp008.sh`，对 4 regimes 各调用 `exp002/compute_signals.py` 生成信号文件，输出到 `/root/autodl-tmp/exp008/signals/{regime_name}/`，然后调用 `run_signal_survival.py --regime-dirs base=... SFT_clean=... SFT_contam=... RL=...`。

### 6. 时间估算

**硬件**：6 × RTX 4090D 24GB

| 阶段 | 时间 |
|------|------|
| 下载 Qwen2.5-0.5B-Instruct (ModelScope) | ~30 min |
| 信号计算/regime (~40 min × 4，可并行 4 GPU) | ~40 min wall |
| 分析 + 可视化 | ~5 min |
| **总计** | **~1.5 h** |

单 GPU 信号计算分解：S1 embedding ~2 min + S2 Min-K%++ ~5 min + S3 ConStat ~1 min + S4 Self-Critique ~5 min = ~13 min/benchmark × 3 benchmarks = ~40 min/regime。

---
