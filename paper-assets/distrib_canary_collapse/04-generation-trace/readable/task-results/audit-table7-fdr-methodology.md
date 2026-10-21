# audit table7 fdr methodology

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_table7_fdr_methodology_20260518T002359_result.json`
- **Structured JSON:** [`35c1f3f2a957a439bff7.json`](../../sessions/35/35c1f3f2a957a439bff7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。以下是完整报告。

---

## Table 7 (tab:generalization) FDR 方法论审计报告

### 论文声明

| 参数 | 声明位置 | 声明值 |
|------|---------|--------|
| FDR 方法 | experiments.tex:25 | Benjamini-Hochberg (BH) at q=0.05 |
| FDR scope | experiments.tex:342 caption | "reaching BH-corrected FDR significance" |
| n_perm | method.tex:55, experiments.tex:26 | 5,000 |
| max_lag (xcorr) | method.tex:53 | 5 |
| max_lag (granger) | method.tex:55 | 1 (隐含，first-differenced series) |

---

### 各行实际来源与参数

| Row | 来源脚本 → 结果文件 | n_perm | max_lag_xcorr | FDR scope |
|-----|---------------------|--------|---------------|-----------|
| **Baseline (Pythia-410M)** | 无可追溯的分析 JSON | **不确定 (推测1000)** | 不确定 | 不确定 |
| **GPT-2-medium** | `leadlag_gpt2m_s42.py` | 5000 ✓ | 5 ✓ | per-direction (6 pairs/pool) |
| **OPT-1.3B** | `analyze_opt1b_full.py` → `opt1b_6method_full.json` | **1000 ✗** | **1 ✗** | per-method |
| **Scale (Pythia-1.4B)** | `pythia14b_8pair_analysis.py` → `pythia14b_8pair_6method_analysis.json` | 5000 ✓ | 5 (params) / 3 (code default) | per-method |
| **Domain (C4)** | `c4_full_8pair_analysis.py` → `c4_8pair_6method_analysis.json` | **1000 ✗** | **3 ✗** (not 5) | pooled (all methods+pairs) |

---

### 严重问题 1：n_perm 不一致

论文声明 5000 permutations，但：
- **OPT-1.3B**: n_perm=1000 (confirmed `opt1b_6method_full.json` → `"n_perm": 1000`)
- **C4**: n_perm=1000 (confirmed `c4_8pair_6method_analysis.json` → `"n_perm": 1000`)
- **Baseline**: `reverse_permg_results.json` 用 n_perm=1000，无 5000 perm 分析存在

---

### 严重问题 2：Scale 行 PermG 使用 RAW p-values 而非 FDR

**证据链**：
- `pythia14b_8pair_6method_analysis.json` (`method_sig_counts`):
  - **PG_fwd = 2** (FDR-corrected, per-method BH)
  - Naive = 4
- `run_unified_generalize.py` 输出 (`unified_5method.json`):
  - PermG: raw_sig = **5/8**, fdr_permethod_sig = **2/8**
  - Naive: raw_sig = 7/8, fdr_permethod_sig = 7/8
- **论文 Table 7 报告 PermG_fwd = 5/8** → 匹配 RAW，不匹配 FDR

结论：**Scale 行的 PermG(fwd) 和 K≥4 列使用了 raw p-values，与 caption 声称的 "BH-corrected FDR" 矛盾。**

---

### 问题 3：FDR scope 跨脚本不一致

| 脚本 | FDR scope |
|------|-----------|
| `run_5method_analysis.py` (alpha sweep) | per-method + per-direction (8 pairs/pool) |
| `method_ablation.py` (Phase 1) | per-method across pair×seed |
| `analyze_opt1b_full.py` | per-method (8 pairs per method) |
| `c4_full_8pair_analysis.py` | **pooled across ALL methods** (most conservative) |
| `leadlag_gpt2m_s42.py` | per-direction (6 fwd/6 rev) |
| `run_unified_generalize.py` (audit) | reports both per-method and pooled |

论文未明确声明 scope 是 per-method 还是 pooled。不同 scope 对 borderline p-values 有实质影响。

---

### 问题 4：xcorr max_lag 不一致

| 脚本 | xcorr max_lag | 论文声明 |
|------|---------------|---------|
| OPT-1.3B (`analyze_opt1b_full.py`) | **1** | 5 |
| C4 (`c4_full_8pair_analysis.py`) | **3** | 5 |
| Pythia-1.4B (result params) | 5 ✓ (code default=3, discrepancy) | 5 |
| GPT-2-medium | 5 ✓ | 5 |

---

### 风险评估

| Row | 受影响列 | 当前值 → 纠正后最坏情况 |
|-----|---------|------------------------|
| **Scale (Pythia-1.4B)** | PermG_fwd, K≥4 | **5/8 → 2/8** (FDR per-method), K≥4 也会下降 |
| **OPT-1.3B** | 全部 | n_perm 5000 重跑: PermG 仍为 6/8 (stable); 但 xcorr max_lag=5 会改变 Naive/Diff |
| **C4** | 全部 | n_perm 5000 + max_lag_xcorr=5 重跑: PermG 仍 8/8 (stable); Naive/Thresh 可能变 |
| **Baseline** | 全部 | 不可验证——无源文件 |

---

### 最关键风险

**Scale 行 PermG_fwd**: 论文报 5/8（raw），实际 FDR 应为 2/8。这直接影响 K≥4 consensus 列（paper 报 5/8，纠正后可能降到 2-3/8）。如果审稿人要求复现，此不一致会被发现。

**OPT + C4 的 n_perm=1000**：permutation test 在 1000 perms 下 p-value resolution 为 0.001，而 5000 perms 下为 0.0002。对于 borderline cases（p≈0.04-0.06），perm 数量差异可能翻转 significance。但对于 strong signals（OPT PermG p<0.01），影响可能有限。

---
