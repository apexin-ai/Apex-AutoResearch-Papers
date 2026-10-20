# paper auroc full recalculation

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_auroc_full_recalculation_20260524T085347_result.json`
- **Structured JSON:** [`17736cc401f9108a31c5.json`](../../sessions/17/17736cc401f9108a31c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All clean. Here's the complete report:

---

## 1. 完整 NVE 数据表

### B1/B2 (n=11, nve_raw 表)
| Experiment | NVE | B1 | B2 |
|---|---|---|---|
| 006 | 4.83 | + | + |
| **059** | **4.72** | **-** | **+** |
| 008d | 4.12 | + | + |
| 008e_v3_s3 | 4.02 | + | + |
| 008e_v3_s2 | 3.78 | - | - |
| 009b | 1.62 | - | + |
| 001 | 1.00 | - | - |
| 008e_v3_s4 | 0.99 | - | - |
| 008f | 0.97 | - | - |
| 008e_v3_s1 | 0.94 | - | - |
| 008a | 0.93 | - | - |

### Main ROC (n=30): 13 pos, 17 neg — 059 added as CIVO+ (NVE=4.72)

## 2. AUROC 新旧值对比

| Metric | Old | **New** | Change |
|---|---|---|---|
| B1 AUROC (n=11) | 1.000 | **0.917** | -0.083 |
| B2 AUROC (n=11) | 0.958 | **0.967** | +0.009 |
| B2 full AUROC (n=17) | 0.969 | **0.972** | +0.003 |
| Main ROC AUROC (n=30) | 0.953 | **0.957** | +0.004 |
| Main ROC 95% CI | [0.867, 1.000] | **[0.875, 1.000]** | — |
| LOEO Walker AUROC | 0.944 | **0.963** | +0.019 |
| LOEO mean AUROC | 0.981 | **0.988** | +0.007 |
| LOEO Walker accuracy | 13/14 (0.929) | **14/15 (0.933)** | +0.004 |
| LOEO mean accuracy | 0.976 | **0.978** | +0.002 |

B1 AUROC 下降因为 059 (NVE=4.72, B1-negative) 排名高于两个 B1 正例 (4.12, 4.02)，破坏了原有的完美分离。其余 AUROC 均上升，因为 059 作为正确分类的正例增加了 concordant pairs。

## 3. 论文更新位置

| 文件 | 行号 | 旧 → 新 |
|---|---|---|
| abstract_body.tex:1 | AUROC=0.953 → 0.957 |
| introduction.tex:6,11 | AUROC=0.953 → 0.957 |
| methodology.tex:38 | AUROC=0.953 → 0.957, LOEO=0.981 → 0.988 |
| methodology.tex:39 | 删除 n=29 注释 |
| results.tex:73 | AUROC=0.953 → 0.957 |
| analysis.tex:8 | AUROC=0.953 → 0.957 |
| conclusion.tex:4 | AUROC=0.953 → 0.957 |
| conclusion.tex:10 | LOEO AUROC=0.981 → 0.988 |
| appendix.tex:152 | B1 文字：删除 "perfect rank separation"，改写为 059 导致 AUROC=0.917 |
| appendix.tex:156 | B1 表 caption: AUROC=1.000 → 0.917 |
| appendix.tex:166-171 | B1 表 θ≥1.5/1.7/2.0/3.9 行：FP/TN/accuracy 全部修正 |
| appendix.tex:178 | B2 表 caption: AUROC=0.958 → 0.967 |
| appendix.tex:199 | B2 full caption: AUROC=0.969 → 0.972 |
| appendix.tex:228 | B1 最优阈值文字：100% → 90.9% |
| appendix.tex:233 | n=16 → n=17 |
| appendix.tex:238 | ROC 图 caption: AUROC=0.953 → 0.957 |
| appendix.tex:274 | Limitations 段: n=16→17, AUROC 值更新 |
| appendix.tex:279 | LOEO Walker n=14 → 15 |
| appendix.tex:292-296 | LOEO 表：N_train/N_test/accuracy/AUROC 全行更新 |
| appendix.tex:301 | LOEO 文字段 mean accuracy/AUROC 更新 |

## 4. 编译验证

pdflatex 编译通过，无 Error 或 undefined reference。无残留 TODO。旧值 (0.953, 0.958, 0.969, 0.981, 0.944, 0.976) 全部从 sections/*.tex 中清除。

---
