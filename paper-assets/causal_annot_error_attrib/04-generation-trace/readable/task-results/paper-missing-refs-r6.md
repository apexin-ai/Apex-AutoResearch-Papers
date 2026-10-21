# paper missing refs r6

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_missing_refs_r6_20260522T180857_result.json`
- **Structured JSON:** [`4bf4afbc3dd78b0ba809.json`](../../sessions/4b/4bf4afbc3dd78b0ba809.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**references.bib** 新增 4 个条目（按 verified 元数据）：
- `neuhaus1999` — Biometrika 86(4):843–855, DOI 10.1093/biomet/86.4.843
- `shu_yi2019a` — Statistics in Medicine 38(10):1835–1854, DOI 10.1002/sim.8073
- `shu_yi2019b` — Statistical Methods in Medical Research 28(7):2049–2068, DOI 10.1177/0962280217743777
- `cadei2025` — arXiv:2502.06343

**related_work.tex** 引用插入位置：
- Measurement error 段：`\citet{neuhaus1999}` 跟在 "biases toward the null" 后面，附量化语；`\citet{shu_yi2019a, shu_yi2019b}` 接在 `\citet{edwards_lessler_naimi2021}` 之后，描述 IPW 下联合处理 covariate+outcome 误测的加权估计
- Correction 段：`\citet{cadei2025}` 接在 `\citet{zrnic_candes2024}` 之后，描述 deconfounded risk 目标对 PPI 在处理效应上的适配

**编译结果**：`main.pdf` 27 页输出成功，`main.bbl` 已包含全部 4 个 `\bibitem`，`main.log` 无 undefined citation / undefined reference 警告（仅 `h→ht` float specifier 与 hyperref Unicode 提示，与本次改动无关）。

Sources:
- [Shu & Yi 2019a — Statistics in Medicine](https://onlinelibrary.wiley.com/doi/10.1002/sim.8073)
- [Shu & Yi 2019b — SMMR](https://journals.sagepub.com/doi/10.1177/0962280217743777)
- [Cadei et al. 2025 — arXiv:2502.06343](https://arxiv.org/abs/2502.06343)
- [Neuhaus 1999 — Biometrika](https://academic.oup.com/biomet/article-abstract/86/4/843/276226)

---
