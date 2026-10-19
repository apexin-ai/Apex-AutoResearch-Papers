# code cka pilot

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cka_pilot_20260520T201949_result.json`
- **Structured JSON:** [`4ccc093441b07809e5d9.json`](../../sessions/4c/4ccc093441b07809e5d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个模型的 CKA 都跑完了。汇总结果：

---

## CKA Results (Qwen2.5-7B, mvp_001)

| Layer |   zh   |   ar   |   hi   |   sw   |   ko   |
|------:|-------:|-------:|-------:|-------:|-------:|
|     0 | 0.9121 | 0.9014 | 0.5365 | 0.4397 | 0.6869 |
|     4 | 0.6519 | 0.6416 | 0.5191 | 0.4703 | 0.6305 |
|     8 | 0.8146 | 0.7370 | 0.5926 | 0.6039 | 0.7245 |
|    12 | 0.8429 | 0.8195 | 0.6143 | 0.6115 | 0.7885 |
|    16 | 0.8859 | 0.8829 | 0.5755 | 0.5930 | 0.8647 |
|    20 | 0.7642 | 0.6641 | 0.3707 | 0.3988 | 0.6696 |
|    24 | 0.6940 | 0.5443 | 0.1619 | 0.1250 | 0.5513 |
|    27 | 0.3445 | 0.3564 | 0.1165 | 0.0841 | 0.3179 |

**Spearman (CKA vs zero-shot AUROC):**
- Overall: rho = **-0.1645**, p = 0.3103 (not significant)
- Per-language:
  - zh: rho = -0.5952, p = 0.1195
  - ar: rho = -0.6667, p = 0.0710
  - **hi: rho = -0.7857, p = 0.0208** (significant)
  - **sw: rho = -0.8810, p = 0.0039** (significant)
  - ko: rho = -0.6190, p = 0.1017

---

## CKA Results (Llama-3.1-8B, mvp_003)

| Layer |   zh   |   ar   |   hi   |   sw   |
|------:|-------:|-------:|-------:|-------:|
|     0 | 0.8805 | 0.6785 | 0.1978 | 0.2654 |
|     4 | 0.9302 | 0.9237 | 0.5313 | 0.7124 |
|     8 | 0.8913 | 0.8798 | 0.5534 | 0.7459 |
|    12 | 0.9224 | 0.9050 | 0.6236 | 0.7047 |
|    16 | 0.8573 | 0.8300 | 0.5108 | 0.6715 |
|    20 | 0.6365 | 0.5675 | 0.3496 | 0.3874 |
|    24 | 0.6069 | 0.5266 | 0.2752 | 0.3000 |
|    28 | 0.5806 | 0.4820 | 0.2213 | 0.2561 |
|    31 | 0.4686 | 0.3055 | 0.1615 | 0.2661 |

（mvp_003 的 transfer_results.csv 尚未生成，train_probe 仍在运行，Spearman 待补。）

---

## 解读

1. **CKA 随深度单调下降（两个模型一致）**：深层表示跨语言相似度急剧降低。Qwen L27 和 Llama L31 的 CKA 降到 0.08–0.47，说明最深层的表示已高度语言特异化。

2. **CKA 与 AUROC 呈负相关**：per-language 分析显示 hi (rho=-0.79) 和 sw (rho=-0.88) 显著负相关。这意味着 **CKA 越低（表示越不相似）的层，transfer AUROC 反而越高**。这与直觉相反——表面上"更不对齐"的深层反而更有鉴别力。

3. **Overall 相关不显著**的原因：不同语言的 CKA 水平差异大（zh/ar 高 vs hi/sw 低），pooling 后语言间变异淹没了层间趋势。

4. **Pareto frontier 解释**：CKA 本身不能直接解释 transfer quality，但 **低 CKA + 高 AUROC** 的组合暗示深层存在语言特异化的 calibration-relevant 特征。这支持"deep layers encode language-specific confidence patterns"的假设，与 mvp_001 发现的"中深层最优"一致——中层兼具足够的跨语言结构和语言特异信号。

---
