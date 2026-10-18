# ssh exp3c pairwise confusion

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp3c-pairwise-confusion_20260515T023600_result.json`
- **Structured JSON:** [`39cd1d906aecedd90e62.json`](../../sessions/39/39cd1d906aecedd90e62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果汇总：

## 相关性结果

| 条件 | n pairs | 非零 confusion pairs | Pearson r (p) | Spearman ρ (p) |
|------|---------|---------------------|---------------|----------------|
| **ALL** | 1953 | 358 | **0.156** (4.6e-12) | **0.160** (1.3e-12) |
| **count_6** | 1770 | 122 | 0.078 (1.0e-3) | 0.088 (2.2e-4) |
| **count_12** | 1953 | 282 | **0.147** (6.7e-11) | **0.142** (2.7e-10) |

非零 confusion pairs only（排除无混淆的 pair）：

| 条件 | Pearson r (p) | Spearman ρ (p) |
|------|---------------|----------------|
| ALL | **0.206** (8.8e-5) | **0.254** (1.1e-6) |
| count_6 | 0.158 (0.082) | **0.315** (4.0e-4) |
| count_12 | **0.212** (3.4e-4) | **0.211** (3.7e-4) |

## Top-10 most confused type pairs

| Rank | Type A | Type B | Confusion | Rate | BCS |
|------|--------|--------|-----------|------|-----|
| 1 | person-other | person-politician | 156 | 0.040 | **0.934** |
| 2 | person-other | person-actor | 65 | 0.019 | 0.895 |
| 3 | person-other | person-athlete | 61 | 0.016 | **0.922** |
| 4 | person-other | person-artist/author | 47 | 0.012 | **0.918** |
| 5 | location-GPE | location-other | 41 | 0.009 | 0.859 |
| 6 | building-other | location-road/railway... | 27 | 0.022 | 0.762 |
| 7 | org-government | org-other | 26 | 0.014 | **0.902** |
| 8 | building-other | location-GPE | 24 | 0.005 | 0.848 |
| 9 | location-GPE | org-other | 20 | 0.004 | 0.828 |
| 10 | org-other | org-company | 19 | 0.011 | 0.883 |

## 关键发现

- **BCS 与 confusion rate 显著正相关**（所有条件 p < 0.001），但效应量中等偏弱（r ≈ 0.15-0.25）
- 限制到有实际混淆的 pairs 后相关性更强（Spearman ρ 从 0.16 提升到 0.25）
- **Top confused pairs 几乎全是语义相近类型**：person-other ↔ person-{politician/actor/athlete/artist}（BCS 0.89-0.93）占主导，location 和 organization 子类间也高
- count_12 比 count_6 产生更多混淆（1212 vs 421），更多 type 暴露在混淆中
- 图片已保存：
  - `/root/schema-dag-extraction/results/pairwise_confusion_analysis.png`
  - `/root/schema-dag-extraction/results/pairwise_confusion_count6.png`
  - `/root/schema-dag-extraction/results/pairwise_confusion_count12.png`
  - JSON：`/root/schema-dag-extraction/results/pairwise_confusion_correlation.json`

---
