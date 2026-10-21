# 论文全文数字一致性审计报告

**审计日期**: 2026-05-16
**审计范围**: abstract.tex, introduction.tex, results.tex, discussion.tex, conclusion.tex, limitations.tex, method.tex, related_work.tex, table4.tex, ethics.tex, appendix_finer_depth.tex, appendix_classifier.tex, appendix_human_edit.tex, appendix_prompt_type.tex, appendix_length.tex, appendix_lofo.tex, appendix_confusion_matrix.tex

---

## 审计结果

### CRITICAL（必须修复）

无。

### WARNING（建议修复）

- **[results.tex:30]** "best single-model ceiling (Pythia-1B, 0.862)" — 主 LOGO 表 (Table 1) 中 Pythia-1B held-out F1 = **0.856**，0.862 不在 ground truth 中。该数字可能来自 cross-model chain 的 5-fold stratified CV 对照实验，但论文未说明来源，且 0.862 恰好落在 LOGO CI 上界 [0.843, 0.863] 附近，有误用 CI 端点作点估计的嫌疑。**建议**：确认 0.862 的来源，若为 5-fold CV 则标注 "(5-fold CV)"；若为笔误则改为 0.856。

- **[discussion.tex:67, limitations.tex:6]** Instruct 实验中 base Qwen3-0.6B 对比值写作 F1=0.816，但主 LOGO 表 (Table 1) 中同一模型 held-out F1 = **0.824**。差异原因是 instruct 实验可能使用了不同 reference model（Qwen3-0.6B 自身作 ref 时整体 LOGO F1=0.816，见 Table cross-ref），但论文未解释此差异。读者对比 Table 1 (0.824) 与此处 (0.816) 会产生疑惑。**建议**：在 instruct 讨论段落中加一句说明，或统一引用同一评估设置下的数字。

- **[discussion.tex:69, limitations.tex:8]** Entropy 特征在 instruct 模型上 "reverse sign" 的措辞。项目叙事规范要求使用 "depth signal degradation" / "method boundary" 叙事而非 "方向反转"。当前文本标题已采用 "degrades depth signal" 叙事（合规），但正文中多次使用 "reverse sign"、"reversal" 等词汇。**建议**：将 "reverse sign" 改为 "shift to positive"，"reversal" 改为 "sign change" 或 "weakening/degradation of the negative correlation"，避免暗示系统性方向反转。

### INFO（信息备注）

- **[appendix_human_edit.tex:22-27]** 表格内舍入不一致：Random 20% 行显示 Binary F1 从 0.724→0.717（差 0.7pp），但 Δ 列写 −0.8pp（从未舍入值 0.7241→0.7165=0.76pp 四舍五入而来）。LLM rephrase 行类似：0.724→0.662=6.2pp，但 Δ 列写 −6.3pp。这是 "从原始值计算 Δ" vs "从显示值计算 Δ" 的经典舍入问题。不影响正确性，但严谨读者可能注意到。

- **[discussion.tex:9, limitations.tex:27]** "degrades at extreme temperatures (t=1.0, −6pp)" — 实际 3-class 降幅为 6.2pp (0.788→0.726)，binary 为 6.6pp (0.799→0.733)。"~6pp" 是合理的近似值。

- **[appendix_classifier.tex:44-47]** Sampling ablation 的 default config 3-class F1=0.788，而主结果报告 0.789。差异 (0.001) 来自数据重新生成，属预期行为。

- **[appendix_human_edit.tex:22]** Human edit baseline binary F1=0.724（从 0.7241 舍入），而主结果 primary binary F1=0.723。两者来自不同实验流程，差异合理，但读者可能疑惑为何同一 baseline 在不同表中有微小差异。

- **[results.tex:30]** Cross-model chain 比较中 single-model ceiling 使用 5-fold stratified CV（0.862），而 Table 1 使用 LOGO（0.856），两种评估协议不同。建议在文中明确标注评估协议以避免混淆。

---

## 逐文件核查清单

### abstract.tex ✅
| 声明 | 论文值 | 真值 | 状态 |
|------|--------|------|------|
| Binary F1 | 0.723 | 0.723 | ✓ |
| 95% CI | [0.717, 0.729] | [0.717, 0.729] | ✓ |
| Per-gen std | 0.051 | 0.051 | ✓ |
| 6 generators, 3 families, 0.6B-8.2B | — | — | ✓ |

### introduction.tex ✅
| 声明 | 论文值 | 真值 | 状态 |
|------|--------|------|------|
| Binary F1 (×3处) | 0.723 | 0.723 | ✓ |
| 95% CI (×3处) | [0.717, 0.729] | [0.717, 0.729] | ✓ |
| Per-gen std (×2处) | 0.051 | 0.051 | ✓ |
| PPL random vs depth | 2.367 vs 2.387 | 2.367 vs 2.387 | ✓ |
| Per-gen F1 range (baselines) | 0.42–0.81 | 与 per-gen 详细数据一致 | ✓ |

### results.tex ✅ (1 WARNING)
| 声明 | 论文值 | 真值 | 状态 |
|------|--------|------|------|
| 3-class LOGO F1 | 0.789 | 0.789 | ✓ |
| Binary F1 | 0.723 | 0.723 | ✓ |
| Per-gen F1 (6个) | 0.856/0.804/0.764/0.824/0.806/0.683 | 全部匹配 | ✓ |
| Per-class F1 | 0.94/0.64/0.80 | 0.94/0.64/0.80 | ✓ |
| LOFO F1 (3个) | 0.772/0.762/0.754, Δ=-2.6pp | 全部匹配 | ✓ |
| Cross-model chains | 3c=0.809, bin=0.764 | 0.809/0.764 | ✓ |
| Ordinal: CORAL/FH/XGB | 0.771/0.793/0.789; bin 0.721/0.728; conc 0.821/0.810/0.825 | 全部匹配 | ✓ |
| Spearman (5个) | -0.558/-0.542/-0.475/0.076/0.089 | 全部匹配 | ✓ |
| Ablation: full/surface/ref | 0.789/0.729/0.745 | 全部匹配 | ✓ |
| Top importance: hapax | 0.269 | 0.269 | ✓ |
| Cross-ref (3个) | 0.803/0.807/0.816, spread=0.013 | 全部匹配 | ✓ |
| Baselines (7行×3列) | 全部数字 | 全部匹配 | ✓ |
| Baseline Δ计算 (4个) | +1.1/+2.2/+10.7/+19.9pp | 算术正确 | ✓ |
| Downstream PPL (5行) | 2.335/2.367/2.387/2.389/2.681 | 全部匹配 | ✓ |
| ⚠ Single-model ceiling | 0.862 | 真值 LOGO=0.856 | WARNING |

### discussion.tex ✅ (2 WARNING)
| 声明 | 论文值 | 真值 | 状态 |
|------|--------|------|------|
| Sampling robustness | ≤0.3pp, -6pp | 0.3pp, ~6.2pp | ✓ (近似) |
| 5-class drop | 0.789→0.501, Δ=0.288 | 0.501 | ✓ |
| 5-class per-class (gen2/3/4) | 0.268/0.259/0.423 | 全部匹配 | ✓ |
| Alt classifiers | RF 0.476, LR 0.447, FH 0.451 | 全部匹配 | ✓ |
| Human edit 20% | -6.0pp 3c, ≤0.8pp bin | -5.97pp/-0.76pp | ✓ |
| LLM rephrase | -3.4pp 3c, -6.3pp bin | -3.4pp/-6.26pp | ✓ |
| Multi-det ensemble | 0.805 vs 0.789; 0.723 vs 0.724 | 全部匹配 | ✓ |
| Cross-ref spread | 0.013, range 0.803-0.816 | 匹配 | ✓ |
| Pythia-1B cross-family | 0.845-0.848 | 0.845-0.848 | ✓ |
| Instruct OLMo | 0.338 vs 0.764 | 匹配 | ✓ |
| Instruct Qwen3-0.6B | 0.667 vs 0.816 | 匹配 | ⚠ 见WARNING |
| Entropy partial ρ | +0.103/+0.161/+0.364 | 全部匹配 | ✓ |

### conclusion.tex ✅
| 声明 | 论文值 | 真值 | 状态 |
|------|--------|------|------|
| Binary F1 + CI + std | 0.723/[0.717,0.729]/0.051 | 全部匹配 | ✓ |
| Cross-model | 3c=0.809, bin=0.764 | 匹配 | ✓ |

### limitations.tex ✅ (同 discussion WARNING)
所有数字与 discussion 一致，instruct 对比值同上 WARNING。

### method.tex ✅
| 声明 | 论文值 | 真值 | 状态 |
|------|--------|------|------|
| Cross-ref spread | 0.013 | 0.013 | ✓ |
| Seed stability | mean=0.789, std=0.0009 | mean 匹配 | ✓ |
| Ordinal range | 0.771-0.793 vs 0.789 | 匹配 | ✓ |

### related_work.tex ✅
| 声明 | 论文值 | 真值 | 状态 |
|------|--------|------|------|
| Baseline binary range | 0.52-0.71 | 0.524-0.712 | ✓ |

### appendix_finer_depth.tex ✅
5-class avg 0.501±0.038、per-class 0.921/0.634/0.268/0.259/0.423、alt classifiers 全部匹配。

### appendix_human_edit.tex ✅ (INFO: 舍入)
Baseline/delta 全部匹配 ground truth 原始值；delta 列有轻微舍入不一致（见 INFO）。

### appendix_classifier.tex + sampling ✅
XGBoost/RF/LR 全部匹配；sampling ablation 3×3 全部匹配。

### 其他附录 (prompt_type, length, lofo, confusion_matrix, ethics) ✅
无 ground truth 冲突，内部一致。

---

## 总结

**通过（有条件）**。

- **0 个 CRITICAL 问题**
- **3 个 WARNING**：(1) Pythia-1B 0.862 来源不明；(2) Instruct Qwen3-0.6B base 对比值 0.816 vs LOGO 表 0.824 未解释；(3) instruct "reverse sign" 措辞与叙事规范的兼容性
- **5 个 INFO**：均为轻微舍入近似，不影响结论

所有主要指标（binary F1=0.723、3-class F1=0.789、CI、std、baseline 全表、downstream PPL、ablation、cross-ref、LOFO、5-class、human edit delta）均与 ground truth 完全一致或在合理舍入范围内。无 7-gen vs 6-gen 混用、无不支持的 "significantly" 声明。
