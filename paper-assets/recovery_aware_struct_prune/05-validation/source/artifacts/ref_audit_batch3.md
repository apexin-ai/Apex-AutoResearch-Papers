# 引用核对清单 — Batch 3

| # | bib key | 存在? | 标题正确? | 作者正确? | 年份正确? | Venue正确? | arXiv ID正确? | 问题 |
|---|---------|-------|----------|----------|----------|-----------|-------------|------|
| 27 | restorelcc_2025 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 无 |
| 28 | boiling_frog_2026 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 无 |
| 29 | hendrycks2021math | ✅ | ✅ | ✅ | ✅ | ⚠️ | N/A | Venue 应为 NeurIPS 2021 Datasets and Benchmarks Track，bib 写的 NeurIPS 可接受但不够精确 |
| 30 | opsd2026 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 无 |
| 31 | mukherjee2025rlsubnetworks | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 无 |
| 32 | shrestha2026layerpruninglimits | ✅ | ✅ | ✅ | ✅ | ✅ | N/A | 无 |
| 33 | davari2023cka | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 无 |
| 34 | li2025reasoning_compression | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | bib key 为 "li2025" 但第一作者姓 Zhang（Nan Zhang），非 Li；bib 中作者列表正确（Zhang 等），仅 key 命名误导 |
| 35 | canpruning2025 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 无 |
| 36 | wang2026linearity | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 无 |
| 37 | deng2025grpocollapse | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | bib 中只列了 4 位作者（Deng, Li, Gong, Ren），实际有 6 位，缺 Christos Thrampoulidis 和 Xiaoxiao Li |
| 38 | suk2025rlvrdynamics | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 无 |
| 39 | mroueh2025grpodynamics | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 无 |

## 详细问题

### #29 hendrycks2021math — Venue 精度
- **bib 中**: `booktitle={Advances in Neural Information Processing Systems (NeurIPS)}`
- **实际**: 该论文发表于 NeurIPS 2021 **Datasets and Benchmarks Track**（不是主会议）。从 `datasets-benchmarks-proceedings.neurips.cc` 可确认。
- **严重程度**: 低。写 NeurIPS 2021 不算错误，但如果要精确，应标注为 Datasets and Benchmarks Track。当前写法在学术引用中普遍可接受。

### #34 li2025reasoning_compression — bib key 命名与第一作者不符
- **bib key**: `li2025reasoning_compression`（暗示第一作者姓 Li）
- **实际第一作者**: Nan Zhang（bib 中 author 字段正确写了 `Zhang, Nan`）
- **严重程度**: 低。bib key 不影响引用渲染，但会给维护者造成困惑。建议改为 `zhang2025reasoning_compression`。

### #37 deng2025grpocollapse — 作者不完整
- **bib 中**: `Deng, Wenlong and Li, Yushu and Gong, Boying and Ren, Yi`（4 位）
- **arXiv 实际**: Wenlong Deng, Yushu Li, Boying Gong, Yi Ren, **Christos Thrampoulidis**, **Xiaoxiao Li**（6 位）
- **严重程度**: 中。缺少两位合著者，可能引发学术礼仪问题。建议补全。
- **建议修正**:
  ```bibtex
  author={Deng, Wenlong and Li, Yushu and Gong, Boying and Ren, Yi and Thrampoulidis, Christos and Li, Xiaoxiao},
  ```
