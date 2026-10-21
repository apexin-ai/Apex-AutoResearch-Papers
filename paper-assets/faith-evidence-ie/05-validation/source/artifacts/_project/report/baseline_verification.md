# External Baseline Verification

Verified 2026-05-25. Numbers cited in Table 8 (Appendix, `tab:encoder_comparison`) and related_work.tex.

## ATLOP (Zhou et al., 2021)

- **引用**: Ign-F1=61.32, Rel-F1=63.18
- **原论文**: Table 3, DocRED dev, RoBERTa-large
- **交叉验证**: DREEAM paper Table 2a reports ATLOP as 61.32/63.18; SAIS paper Table 1 reports ATLOP as 61.32/63.18
- **原论文数字**: Ign-F1=61.32, F1=63.18
- **匹配**: ✓
- **备注**: EIDER paper reports slightly different numbers (61.30±0.22 / 63.15±0.21), likely due to different random seeds. Our citation uses the most commonly reported values which match ATLOP's own paper.

## EIDER (Xie et al., 2022)

- **引用**: Ign-F1=62.34, Rel-F1=64.27, Evi-F1=52.54
- **原论文**: Table 1 (RE) + Table 3 (Evidence), DocRED dev, RoBERTa-large
- **原论文数字**: Ign-F1=62.34±0.14, F1=64.27±0.10, Evi-F1=52.54 (dev)
- **匹配**: ✓
- **Evi-F1 协议**: Binary sentence classification over all entity pairs. "Evi F1" = evidence F1 on all pairs (distinct from "PosEvi F1" which is positive-only). Evaluated as sentence-level retrieval F1 for all ground-truth triples.
- **备注**: SAIS paper independently confirms EIDER as 62.34/64.27/52.54.

## SAIS (Xiao et al., 2022)

- **引用**: Ign-F1=62.23, Rel-F1=65.17, Evi-F1=55.84
- **原论文**: Table 1, DocRED dev, RoBERTa-large (NAACL 2022)
- **原论文数字**: Ign-F1=62.23±0.15, F1=65.17±0.08, Evi-F1=55.84±0.23
- **匹配**: ✓
- **Evi-F1 协议**: Evidence retrieval evaluates "how accurately the supporting sentences are identified for predicted relations". Sentence-level retrieval precision and recall over ground-truth triples.

## DREEAM (Ma et al., 2023)

- **引用**: Ign-F1=61.71, Rel-F1=63.49, Evi-F1=54.15
- **原论文**: Table 2(a), DocRED dev, RoBERTa-large, without distantly-supervised data (EACL 2023)
- **原论文数字**: Ign-F1=61.71±0.09, F1=63.49±0.10, Evi-F1=54.15±0.11
- **匹配**: ✓
- **Evi-F1 协议**: "official evaluation metrics of DocRED: Ign F1 and F1 for RE and Evi F1 for ER". Uses DocRED official evaluation script with all ground-truth triples in denominator (joint protocol).

## AutoRE (related_work.tex comparison)

- **引用**: Ign-F1=52.14 (footnote: "AutoRE Ign-F1 from the LLaMA3-8B reproduction by wang2025relprior; the original paper reports only F1.")
- **原论文**: RelPrior (Wang et al., 2025), Table 2, **RE-DocRED dev** (NOT DocRED dev!)
- **RelPrior Table 2 实际数字**:
  - AutoRE_LLaMA3-8B on **DocRED dev**: Ign-F1=45.22, F1=45.76
  - AutoRE_LLaMA3-8B on **RE-DocRED dev**: Ign-F1=52.14, F1=52.28
  - RelPrior_LLaMA3-8B on **DocRED dev**: Ign-F1=47.70, F1=47.82
  - RelPrior_LLaMA3-8B on **RE-DocRED dev**: Ign-F1=55.50, F1=55.94
- **匹配**: ❌ **跨数据集比较错误**
- **问题分析**:
  - related_work.tex 写: "At 8B, our RSFT model (54.33 Ign-F1) outperforms AutoRE (52.14) and is slightly below RelPrior (−1.17pp)"
  - 54.33 来自 Table 2 (tab:scaling) = Qwen3-8B RSFT on **DocRED dev**
  - 52.14 来自 RelPrior Table 2 = AutoRE on **RE-DocRED dev**
  - 55.50 - 54.33 = 1.17 = RelPrior on **RE-DocRED dev**
  - 三个数字来自两个不同数据集，比较无效
- **正确比较 (DocRED dev)**:
  - Our 8B RSFT: 54.33 vs AutoRE: 45.22 → **outperforms by +9.11pp**
  - Our 8B RSFT: 54.33 vs RelPrior: 47.70 → **outperforms by +6.63pp**
- **建议修复**: 要么 (a) 用 DocRED dev 数字 (AutoRE=45.22, RelPrior=47.70)，要么 (b) 在 Re-DocRED dev 上评估我们的 8B 模型做公平比较。

## 总结

| Baseline | Ign-F1 | Rel-F1 | Evi-F1 | 状态 |
|----------|--------|--------|--------|------|
| ATLOP | 61.32 | 63.18 | -- | ✓ |
| EIDER | 62.34 | 64.27 | 52.54 | ✓ |
| SAIS | 62.23 | 65.17 | 55.84 | ✓ |
| DREEAM | 61.71 | 63.49 | 54.15 | ✓ |
| AutoRE | 52.14 | -- | -- | ❌ 数据集错误 |

4/5 baseline 数字验证通过。AutoRE 引用存在跨数据集比较错误，需要修复。
