# analysis d120 batch tasks

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d120_batch_tasks_20260520T071242_result.json`
- **Structured JSON:** [`162ea45710ace626426d.json`](../../sessions/16/162ea45710ace626426d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有分析脚本完成。现在编译汇总报告。

---

## 汇总报告

### Task 1: scale_14b_c4_s42_fp32 5-method 分析 ✅

模型: Pythia-1.4B, 数据: C4, α=1.0, seed=42, 11 代

| Method | Fwd sig / Total |
|--------|----------------|
| PermG_fwd (FDR) | **8/8** |
| PermG_rev | 0/8 |
| Diff XCorr (FDR) | **8/8** |
| Naive XCorr | **8/8** |
| Threshold Onset | **0/8** (all None — 无 onset 检测到) |
| TY Granger | **0/8** (all p > 0.45, dmax=1) |

**K≥3 = 8/8**, K≥4 = 0/8

所有 8 pairs 的 consensus 均为 3/5 [naive, diff, perm]。Threshold onset 全部 None（信号太强导致所有 gen 都超阈值，无法确定 onset 时间点）。TY 全部 not significant（dmax=1，df_resid 不足）。

---

### Task 2: Padding Robustness TY 重跑 ✅

目录: `results/padding_robustness/a100_s42_fp32`  
模型: Pythia-410M, α=1.0, seed=42, 11 代

| Method | Fwd sig / Total |
|--------|----------------|
| PermG_fwd (FDR) | **6/8** |
| Diff XCorr (FDR) | **6/8** |
| Naive XCorr | **6/8** |
| Threshold Onset | **0/8** |
| TY Granger | **0/8** (all TY_p > 0.2) |

**K≥3 = 6/8**, K≥4 = 0/8

**TY 仍为 0/8，D120 修复未改变 padding 实验的 TY 结论。** mauve pairs (2/8) 无信号是一致的。TY=0/8 非 bug — 是短序列 T=11 下 TY 检验力不足。

---

### Task 3: TY FPR_null α=0.0 分析 ✅ ⚠️

目录: `results/alpha_sweep/a000_s42_fp32`  
模型: Pythia-410M, α=0.0 (null baseline), seed=42, 11 代

| Method | Fwd sig / Total |
|--------|----------------|
| PermG_fwd (FDR) | **0/8** ✅ |
| Diff XCorr (FDR) | **4/8** ⚠️ |
| Naive XCorr | **2/8** |
| Threshold Onset | **3/8** ⚠️ |
| TY Granger | **1/8** ⚠️ |

**K≥3 = 1/8**（token_entropy→distinct_2, methods: diff+threshold+ty）

**关键发现**: TY 在 α=0.0 null 条件下有 **1 个 false positive**:
- `token_entropy→distinct_2`: TY_p=0.0228, dmax=1

对比旧 m035 CSV 中 α=0.0 的 TY=0/8，D120 修复后 TY 变成 1/8。FPR 从 0% 升至 12.5%（per-pair）。Diff_xcorr 和 threshold_onset 的 FPR 更高（4/8 和 3/8）。**K≥3 consensus 的 null FPR = 1/8 = 12.5%**。

---

### Task 4: v3_d080 变体调查 ✅

对比了以下目录的 config.json:
- `a005_s42_fp32` / `a005_s42_fp32_v3` / `a005_s42_fp32_v3_d080`
- `a060_s42_fp32` / `a060_s42_fp32_v3_d080`
- 标准 `a050_s42_fp32`

**结论: 所有 config.json 完全相同** — 没有 `weight_decay` 字段。

训练脚本 `iterative_train.py` 在 line 180 硬编码 `weight_decay=0.01`，且无 `--weight_decay` CLI 参数。

"d080" 的含义 **只能从命名推断**: 很可能是临时将代码中 `weight_decay` 从 0.01 改为 0.08（或 0.80），运行完后恢复。由于没有 train.log、没有 git 记录在服务器上，**无法 100% 确认实际使用的 decay 值**。

v3_d080 目录没有 train.log，无额外 .sh 或 .cmd 文件。唯一的代码引用在 `aggregate_phase3.py` 和 `run_dose_response_m035.py` 中，仅作为目录名使用。

---

### Task 5: Heatmap CSV model 列检查 ✅

唯一找到的 heatmap CSV: `artifacts/dose_response_m035/consensus_heatmap_data.csv`

**该 CSV 不含 model 列。** 列为: `alpha, dirname, pair, naive_sig, diff_sig, threshold_sig, permG_sig, TY_sig, consensus_votes`

所有条目均为 alpha_sweep 实验（Pythia-410M），通过 dirname 区分（如 `a050_s42_fp32`）。**不存在 `consensus_heatmap_d120_data.csv`** — d120 版本的 heatmap CSV 尚未生成。

因此 GPT-2 vs Pythia-410M 的问题不适用于当前 CSV。

---

### Task 6: 实验进度速查 ✅

找到 **6 个仍在运行** 的实验（非 7 个，部分可能已在查询间完成）：

| 实验名 | 当前gen/总gen | Step进度 | 总体进度 | 速度 | 预估剩余 |
|--------|-------------|---------|---------|------|---------|
| qwen35_08b_wiki_a100_s43_fp32 | 10/10 (resume) | 238/5000 | ~91% | ~1.93 it/s | ~21 min |
| scale_69b_a100_s43 | 10/10 | 1274/5000 | ~93% | ~1.72 it/s | ~36 min |
| alpha_sweep_a025_s44_fp32 | 10/10 | 1190/5000 | ~93% | ~7.69 it/s | ~8 min |
| data_strategy_ablation_s42 | 7/10 | 944/5000 | ~65% | ~7.68 it/s | ~42 min |
| alpha_sweep_a045_s43_fp32 | 4/10 (synth gen) | — | ~36% | ~7.69 it/s | ~66 min |
| qwen35_08b_fp32 | 2/10 | 1092/5000 | ~20% | ~2.12 it/s | ~6.4h |

已完成的近期实验: scale_69b_a100_s42, pythia410m_wiki_a100_s43_fp32, interv_pred_a075_s42_fp32_v4, interv_react_s43_fp32, alpha_sweep_a045_s42_fp32, c4_a025/a050/a075_s42_fp32, a025_s43_fp32, a030/a035_s42_fp32 等。

失败: `alpha_sweep_a060_s43_fp32` (EXIT_CODE=124, timeout)。

---
