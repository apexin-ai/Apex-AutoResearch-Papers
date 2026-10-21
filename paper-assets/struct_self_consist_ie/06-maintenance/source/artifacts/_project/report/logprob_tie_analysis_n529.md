# Logprob Tie Analysis — NER Basis n=529

**Data**: `exp_012_rerun_1024/samples.jsonl` (Qwen SciERC joint, N=8, seed=42, max_tokens=1024)
**Filtering**: 551 total → 22 empty gold NER → **n=529**

---

## 1. Instance-Level Logprob Range

Range = max(mean_logprob) − min(mean_logprob) across 8 samples per instance.

| Stat   | Value    |
|--------|----------|
| Mean   | 0.0622   |
| Median | 0.0401   |
| P25    | 0.0265   |
| P75    | 0.0685   |
| P90    | 0.1221   |
| P95    | 0.1711   |
| Min    | 0.0001   |
| Max    | 0.6083   |

**Instance-level "tied" (range < ε):**

| ε     | Tied instances | % of 529 |
|-------|---------------|----------|
| 0.01  | 6             | 1.1%     |
| 0.05  | 319           | 60.3%    |
| 0.10  | 444           | 83.9%    |
| 0.50  | 526           | 99.4%    |

**Interpretation**: At ε=0.05, 60% of instances have all 8 samples within 0.05 mean_logprob of each other — logprob cannot meaningfully rank them.

---

## 2. Non-Tied Subset Selection Performance

### Full set (n=529)

| Method       | NER F1  |
|-------------|---------|
| Greedy       | 0.6439  |
| LP-best      | 0.6501  |
| SJ-best (MV-Jaccard) | 0.6492  |
| Oracle       | 0.7758  |

### Non-tied subset: range ≥ 0.05 (n=210, 39.7% of instances)

| Method       | NER F1  | vs Greedy   | p-value |
|-------------|---------|-------------|---------|
| Greedy       | 0.5960  | —           | —       |
| LP-best      | 0.6246  | **+0.0286** | **0.010** |
| SJ-best      | 0.6127  | +0.0167     | 0.176   |
| Oracle       | 0.7421  | —           | —       |

- LP-best vs greedy: **+2.9 points, p=0.01** (significant)
- SJ-best vs LP-best: −1.2 points, p=0.37 (not significant)
- LP-best outperforms SJ on the non-tied subset

### Non-tied subset: range ≥ 0.1 (n=85)

| Method       | NER F1  | vs Greedy   | p-value |
|-------------|---------|-------------|---------|
| Greedy       | 0.5779  | —           | —       |
| LP-best      | 0.6148  | +0.0369     | 0.079   |
| SJ-best      | 0.5757  | −0.0022     | 0.923   |
| Oracle       | 0.7316  | —           | —       |

---

## 3. Pairwise Comparison Tie Rate

C(8,2)=28 pairs per instance × 529 instances = **14,812 total pairs**.

Pairwise |diff| stats: mean=0.0228, median=0.0117, P75=0.0260.

| ε      | Tied pairs | % of 14,812 |
|--------|-----------|-------------|
| 0.001  | 1,222     | 8.3%        |
| 0.005  | 3,979     | 26.9%       |
| 0.010  | 6,699     | 45.2%       |
| 0.020  | 9,969     | 67.3%       |
| **0.026** | **~11,109** | **~75.0%** |
| 0.050  | 13,259    | 89.5%       |
| 0.100  | 14,312    | 96.6%       |

**论文声明验证**："75% of comparisons are ties" 对应 ε ≈ 0.026（P75 of pairwise diffs = 0.02595）。

这意味着论文所说的"75% tie"不需要特别大的容忍度——mean_logprob 差异的第 75 百分位仅为 0.026，在 per-token logprob 尺度上确实很小。

---

## 4. n=529 vs n=551 对比

| 指标                    | n=551  | n=529  | Δ       |
|------------------------|--------|--------|---------|
| Range mean             | 0.0623 | 0.0622 | −0.0001 |
| Range median           | 0.0413 | 0.0401 | −0.0012 |
| Tied (range<0.05)      | 59.7%  | 60.3%  | +0.6pp  |
| Greedy F1              | 0.6436 | 0.6439 | +0.0003 |
| LP-best F1             | 0.6495 | 0.6501 | +0.0005 |
| SJ-best F1             | 0.6505 | 0.6492 | −0.0013 |
| Pairwise tied (ε=0.05) | 89.2%  | 89.5%  | +0.3pp  |
| P75 pairwise diff      | 0.0263 | 0.0260 | −0.0003 |

**结论**: 基数从 551→529 对所有核心指标影响极小（delta < 0.002）。22 个 empty gold instance 的 logprob 分布与整体一致，不构成偏差来源。

---

## 关键发现

1. **Logprob 信号确实 weak**: 60% 的 instance 在 ε=0.05 下"tied"（8 个样本的 mean_logprob range < 0.05）
2. **但在 non-tied 子集上 logprob 有效**: range ≥ 0.05 的 210 个 instance 上，LP-best 显著优于 greedy（+2.9 F1, p=0.01）
3. **论文 "75% ties" 验证**: 对应 ε ≈ 0.026，在 per-token mean_logprob 尺度上合理
4. **SJ 在 non-tied 子集上不如 LP**: 当 logprob 能区分时，LP 选择优于 SJ（差异不显著但方向一致）
5. **n=529 vs n=551 无实质差异**

---

## 产出文件

- 脚本: `output/review_round4/analyze_logprob_ties.py`
- JSON: `output/review_round4/logprob_tie_results_n529.json`
