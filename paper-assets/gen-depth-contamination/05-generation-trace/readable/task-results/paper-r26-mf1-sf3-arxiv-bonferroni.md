# paper r26 mf1 sf3 arxiv bonferroni

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230_result.json`
- **Structured JSON:** [`6041d5a3b4efac0f5d9d.json`](../../sessions/60/6041d5a3b4efac0f5d9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 结果汇总

### Part 1: MF-1 — arXiv 2v3 CI

**JSON 验证**（均正确）：
- Qwen arXiv 2v3: AUC=0.6427, CI=[0.6275, 0.6575], perm_p=0.0001
- Pythia arXiv 2v3: AUC=0.6544, CI=[0.6401, 0.6688], perm_p=0.0001

**修改**：
1. `appendix.tex` Table S12 arXiv 2v3 行：`.6436` → `$.6436\;[.628,\,.658]$` + 脚注（p<0.001, CI lower > θ）
2. `experiments_c1.tex` Section 4.6：arXiv 讨论句添加了两个模型的 2v3 CI 和 "CI lower bounds above θ" 措辞

### Part 2: SF-3 — Bonferroni 99.5% CI

α_corr = 0.005, z = 2.807

| Config | Boundary | AUC | σ_boot | 99.5% CI | Pass θ |
|---|---|---|---|---|---|
| Qwen-rw | 1v2 | .6955 | .0046 | [.683, .708] | ✓ |
| Pythia-1.4B | 1v2 | .6539 | .0046 | [.641, .667] | ✓ |
| Qwen-base | 1v2 | .6260 | .0047 | [.613, .639] | ✓ |
| Qwen-7B | 1v2 | .6168 | .0046 | [.604, .630] | ✓ |
| **LLaMA-8B** | **1v2** | **.6123** | **.0048** | **[.599, .626]** | **✗** |
| **Qwen-cont** | **1v2** | **.6112** | **.0049** | **[.598, .625]** | **✗** |
| OLMo-1B | 0v1 | .9860 | .0009 | [.983, .989] | ✓ |
| Mistral-7B | 0v1 | .9842 | .0009 | [.982, .987] | ✓ |
| Pythia-6.9B | 0v1 | .9599 | ~.0015† | [.956, .964] | ✓ |
| Gemma-2-2B | 0v1 | .9530 | .0018 | [.948, .958] | ✓ |

**2/10 CI lower bound 跌破 θ=0.60**：
- **Qwen-cont**：CI_lower = 0.5976 < 0.60（符合预期）
- **LLaMA-8B**：CI_lower = 0.5988 < 0.60（额外发现）

Bonferroni 表已添加到 `appendix_extended.tex` Section "Bonferroni-Corrected Confidence Intervals"。正文 6/10 计数未修改。

†Pythia-6.9B 无单独 bootstrap JSON，σ_boot 从同类配置估计。

---
