# Reference Audit Report

**Date**: 2026-05-15

## 统计
- 总 bib 条目数: 43
- 被引用条目数: 43（主 tex 文件）
- 未引用条目数: 0

## 完整性检查

| Key | 缺失字段 | 问题 |
|-----|---------|------|
| `diveye` | — | author 缺少名（"Basani and Chen"），应为 "Basani, Advik Raj and Chen, Pin-Yu" |
| `ood_baseline` | — | author 缺少名（"Hendrycks and Gimpel"），应为 "Hendrycks, Dan and Gimpel, Kevin" |
| `aaronson_watermark` | — | author 缺少名（"Aaronson and Kirchner"），应为 "Aaronson, Scott and Kirchner, Jan Hendrik" |
| `writing_diversity` | — | author 缺少名（"Padmakumar and He"），应为 "Padmakumar, Vishakh and He, He" |
| `stamatatos_survey` | — | author 缺少名（"Stamatatos"），应为 "Stamatatos, Efstathios" |

**备注**: 所有条目均具备 author/title/year/venue 四个核心字段。上述 5 个条目 author 字段仅有姓氏，缺少名字，会导致 BibTeX 引用格式异常（如 \citet 只显示姓氏，无法正确生成缩写）。

## 真实性抽查

| Key | 标题 | 验证结果 |
|-----|------|---------|
| `detectgpt` | DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature | ✅ 确认。Mitchell et al., ICML 2023，标题/作者/会议/年份均匹配 |
| `binoculars` | Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text | ✅ 确认。Hans et al., ICML 2024，标题/作者/会议/年份均匹配 |
| `broken_telephone` | LLM as a Broken Telephone: Iterative Generation Distorts Information | ✅ 确认。Mohamed et al., ACL 2025，标题/作者/会议/年份均匹配 |
| `chainwash` | Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks | ✅ 确认。arXiv 2605.05503，标题匹配 |
| `ld_score` | Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection | ✅ 确认。arXiv 2605.01647，Narayanasamy et al.，标题/作者匹配 |
| `diveye` | Diversity Boosts AI-Generated Text Detection | ✅ 确认。Basani & Chen, TMLR 2026。但 bib 中作者应补全为 Advik Raj Basani, Pin-Yu Chen |
| `curse_of_recursion` | The Curse of Recursion: Training on Generated Data Makes Models Forget | ✅ 确认。Shumailov et al., Nature 2024（vol. 631），标题/作者/期刊/年份均匹配 |
| `markovian_chains` | Markovian Generation Chains in Large Language Models | ✅ 确认。Geng et al., arXiv 2603.11228，标题/作者匹配 |

**抽查 8/43 条目，全部为真实论文，无伪造引用。**

## 问题汇总

### 需修复（5 项）
1. **`diveye`** — author 补全为 `Basani, Advik Raj and Chen, Pin-Yu`
2. **`ood_baseline`** — author 补全为 `Hendrycks, Dan and Gimpel, Kevin`
3. **`aaronson_watermark`** — author 补全为 `Aaronson, Scott and Kirchner, Jan Hendrik`
4. **`writing_diversity`** — author 补全为 `Padmakumar, Vishakh and He, He`
5. **`stamatatos_survey`** — author 补全为 `Stamatatos, Efstathios`

### 次要注意
- 备份文件 `method_01fe38.tex` 中存在 6 处 `\cite{placeholder}`，对应 bib 中无 `placeholder` 条目。当前主文件 `method.tex` 已修复，此为历史版本残留，不影响编译。
- 多数条目缺少 volume/pages/DOI 字段，不影响编译但投稿时可能需要补全。
- 2026 年条目共 6 篇（ld_score, diveye, generator_barrier, feat_aug_transformer, chainwash, markovian_chains），均为当前 arXiv preprint 或 2026 会议/期刊论文，年份合理。
