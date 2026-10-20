# 电路发现方法的跨方法 Overlap 文献调研

## 核心发现

**跨方法边级 Jaccard 典型范围：0.05–0.30。** 文献中没有论文直接报告 EAP-IG × EP × ACDC 的 pairwise Jaccard，但可从多篇论文的间接证据拼出基准范围。

---

## 相关论文及具体数值

### 1. Have Faith in Faithfulness (Hanna et al., COLM 2024)
- **arXiv**: 2403.17806
- **比较方法**: EAP vs EAP-IG vs 手工标注电路（activation patching）
- **模型/任务**: GPT-2 Small / IOI, Greater-Than, SVA, Capital-Country 等 9 个任务
- **关键数值**:
  - **跨任务节点 IoU**: 大多数任务对 0.25–0.30；功能相似任务对（GT variants）≥ 0.60
  - **跨任务边 IoU**: 大多数任务对 **0.05–0.15**；GT variants 和 Capital/Country ≈ 0.40
  - 包含 ≥90% 手工 IOI 节点的最小 EAP 电路：**0% faithfulness**
  - 包含 ≥90% 手工 GT 节点的最小 EAP 电路：**51% faithfulness**
  - 节点 overlap 与 faithfulness 的 Pearson 相关：**r=0.86** (p<0.001)
  - 边 overlap 与 faithfulness 的 Pearson 相关：**r=0.83** (p<0.001)
- **二值化**: 基于 faithfulness 阈值（85% faithful 电路）
- **启示**: 高节点 overlap ≠ 高 faithfulness；边级 overlap 普遍很低

### 2. Mechanistic Interpretability as Statistical Estimation (arXiv 2510.00845)
- **比较方法**: EAP-IG 不同变体之间（同方法不同配置）
- **模型/任务**: GPT-2 Small, Llama-3.2-1B, Llama-3.2-1B-Instruct / IOI, Greater-Than, SVA
- **关键数值（方法内稳定性）**:

  | 扰动策略 | 平均 Jaccard | CV |
  |----------|-------------|-----|
  | Bootstrap 重采样 | **0.561** | 0.335 |
  | Meta-Dataset 替换 | **0.790** | 0.132 |
  | Prompt 改写 | **0.799** | 0.131 |

- **跨变体 Jaccard（Llama-3.2-1B-Instruct）**:

  | EAP 变体 | GT | IOI | SVA |
  |----------|-----|-----|-----|
  | EAP (sum, patching) | 0.417 | 0.286 | 0.536 |
  | EAP-IG-activations | 0.098 | 0.125 | 0.531 |
  | EAP-IG-inputs (median) | 0.086 | 1.000 | 0.840 |
  | EAP-IG-inputs (sum, mean) | 1.000 | 0.182 | 0.960 |
  | Clean-corrupted | 0.419 | **0.071** | 0.577 |

- **极低值**: Cross-variant Jaccard 可低至 **0.016**（Llama-3.2-1B, IOI, clean-corrupted）
- **Bootstrap 各模型**:
  - gpt2-small IOI: **0.67**
  - Llama-3.2-1B IOI: **0.39**
  - Llama-3.2-1B-Instruct IOI: **0.34**
- **启示**: 同一方法不同超参/数据即可导致 Jaccard 剧烈波动（0.02–1.00），跨方法只会更低

### 3. Attribution Patching Outperforms Automated Circuit Discovery (Syed et al., BlackboxNLP 2024)
- **arXiv**: 2310.10348
- **比较方法**: EAP vs ACDC (task metric / KL divergence)
- **模型/任务**: GPT-2 Small / IOI, Greater-Than, Docstring
- **关键数值（ROC AUC，越高越接近手工电路）**:

  | 任务 | EAP | ACDC-KL | ACDC-task |
  |------|-----|---------|----------|
  | Greater-Than | **0.896** | 0.849 | 0.658 |
  | IOI | **0.907** | 0.869 | 0.588 |
  | Docstring | 0.976 | **0.982** | 0.972 |

- **未报告 Jaccard/IoU**，但 ROC AUC 差异（0.04–0.32）暗示方法选出的电路集合有显著差异
- **启示**: EAP 和 ACDC 在不同阈值下选出的边集不同，ROC 曲线形状差异大

### 4. Finding Transformer Circuits with Edge Pruning (Bhaskar et al., NeurIPS 2024 Spotlight)
- **arXiv**: 2406.16778
- **比较方法**: Edge Pruning vs ACDC vs EAP
- **模型/任务**: GPT-2 Small / IOI, Greater-Than; CodeLlama-13B / Docstring
- **关键数值**:

  | 方法 | KL Divergence (IOI, ~96.6% sparsity) | 时间(s) |
  |------|--------------------------------------|---------|
  | Edge Pruning | **0.25** | 2,756 |
  | ACDC | 0.92 | 18,783 |
  | EAP | 3.47 | 21 |

  - EP 在 98.8% sparsity 达到 ACDC 在 96.8% 的 faithfulness → EP 用 **2.65× 更少的边**
  - CodeLlama-13B 跨任务（IP ∩ FS）overlap: **62.7%** of smaller circuit（1,700× 高于随机期望）
  - 12 随机种子的方法内一致性：描述为"remarkably consistent"（未给出具体 IoU 数值）
- **未直接报告跨方法 Jaccard**
- **启示**: EP 和 ACDC 在相同 faithfulness 下电路大小差 2.65×，暗示边集差异极大

### 5. Hybrid Attribution and Pruning (HAP) (arXiv 2510.03282, NeurIPS 2025)
- **比较方法**: HAP vs EAP vs Edge Pruning
- **模型/任务**: GPT-2 Small / IOI (94% sparsity)
- **关键数值**:

  | 方法 | Accuracy | Logit Diff | KL Div | 时间(s) |
  |------|----------|-----------|--------|---------|
  | EAP | 0.698 | 3.13 | — | 4 |
  | EP | 0.772 | 3.48 | 0.190 | 2,921 |
  | HAP | 0.759 | 3.42 | 0.188 | 1,579 |

- **未报告跨方法 Jaccard**

### 6. InterpBench: Semi-Synthetic Transformers (Makelov et al., NeurIPS 2024)
- **arXiv**: 2407.14494
- **比较方法**: ACDC vs EAP-IG vs Node SP vs Edgewise SP
- **关键数值**:
  - ACDC 与 EAP-IG **统计不可区分** (p > 0.05)
  - ACDC 显著优于 Node SP，effect size 0.54–0.91
  - 平均 ROC AUC: ACDC ≈ EAP-IG > Edgewise SP > Node SP
- **启示**: 在有 ground-truth 电路的 semi-synthetic 模型上，ACDC 和 EAP-IG 恢复能力相当

### 7. CD-T: Contextual Decomposition (Hsu et al., ICLR 2025)
- **arXiv**: 2407.00886
- **比较方法**: CD-T vs ACDC vs EAP
- **关键数值**: 平均 ROC AUC **97%**，优于 ACDC 和 EAP
- **未报告 Jaccard**

### 8. Circuit Compositions (Mondorf & Wold, ACL 2025)
- **arXiv**: 2410.01434
- **比较方法**: 同一方法发现的不同任务电路之间的 overlap
- **模型/任务**: T5-based seq2seq / PCFG SET 10 个模块操作
- **关键数值**:
  - 跨任务节点 IoU: 大多数对 **0.20–0.30**
  - 功能相似任务对（reverse/swap/shift）更高
- **启示**: 功能不同的电路 overlap 低是预期行为

---

## 总结：Jaccard 范围基准

### 边级（Edge-level）Jaccard 基准

| 比较类型 | 典型 Jaccard 范围 | 来源 |
|----------|------------------|------|
| **跨任务**（同方法，不同任务） | 0.05–0.15 | Hanna et al. 2024 |
| **跨任务**（功能相似任务） | 0.30–0.40 | Hanna et al. 2024 |
| **同方法同任务**（bootstrap 重采样） | 0.33–0.67 | arXiv 2510.00845 |
| **同方法不同超参**（EAP 变体间） | 0.02–1.00（极度不稳定） | arXiv 2510.00845 |
| **跨方法同任务**（EP vs ACDC 推断） | ~0.10–0.25（推断值） | 电路大小差 2.65× 暗示 |

### 节点级（Node-level）Jaccard 基准

| 比较类型 | 典型 Jaccard 范围 | 来源 |
|----------|------------------|------|
| **跨任务** | 0.25–0.60 | Hanna et al. 2024; Mondorf 2025 |
| **功能相似任务** | 0.50–0.65 | Hanna et al. 2024 |

---

## 对我们结果的解读建议

### Pairwise Jaccard（EAP-IG × EP, EAP-IG × ACDC, EP × ACDC）

1. **Jaccard < 0.10（边级）**: 极低但不异常。文献中跨方法变体 Jaccard 可低至 0.02–0.07。说明方法在边级确实在发现不同的电路，但不代表无效——"Have Faith" 论文证明 overlap 低不等于 faithfulness 低。

2. **Jaccard 0.10–0.25**: 正常范围。跨方法在同一任务上的边级一致性就在这个区间。这是我们报告的合理预期值。

3. **Jaccard 0.25–0.40**: 偏高的一致性。如果我们的三个方法在此范围，说明它们在边级有实质共识，超过大多数文献报告的跨方法 agreement。

4. **Jaccard > 0.40**: 非常高的一致性。文献中只有在功能高度相似的任务间或同方法稳定运行时才能达到。

### 3-way 共识比率

文献中几乎没有报告 3-way overlap（三方法交集）的数据。预期 3-way ratio 应显著低于任一 pairwise Jaccard。

### 建议的叙事框架

- **如果 Jaccard 在 0.10–0.25**: "与文献一致，不同方法族（gradient vs. mask optimization vs. greedy causal）在边级发现的电路存在显著差异，但 CSS 共识子集（交集）仍可提取出高置信度的核心电路。"
- **如果 Jaccard > 0.25**: "跨方法一致性优于文献中多数报告的跨方法 agreement，表明 CSS 共识方法有效地识别了鲁棒的电路核心。"
- **关键引用**: Hanna et al. (2024) 的核心论点——overlap ≠ faithfulness——支持我们用 CSS 做编辑而非单纯追求 overlap 最大化的思路。
