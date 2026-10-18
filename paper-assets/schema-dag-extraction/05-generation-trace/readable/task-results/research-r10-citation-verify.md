# research r10 citation verify

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_r10-citation-verify_20260517T075934_result.json`
- **Structured JSON:** [`1c31fd5f42afe8f29fcd.json`](../../sessions/1c/1c31fd5f42afe8f29fcd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

### 1. NuNER (Bogdanov et al., 2024) ✅ 确认存在

- **完整标题**: NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data
- **作者**: Sergei Bogdanov, Alexandre Constantin, Timothée Bernard, Benoit Crabbé, Etienne Bernard
- **年份**: 2024
- **Venue**: EMNLP 2024 (Main Conference)
- **BibTeX**:
```bibtex
@inproceedings{bogdanov2024nuner,
  title={NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data},
  author={Bogdanov, Sergei and Constantin, Alexandre and Bernard, Timoth{\'e}e and Crabb{\'e}, Benoit and Bernard, Etienne},
  booktitle={Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
  pages={11586--11600},
  year={2024}
}
```

---

### 2. Self-Improving LLM IE (Zhang et al., 2024) ⚠️ 作者归属错误

- **完整标题**: Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models
- **作者**: Tingyu **Xie**, Qi Li, Yan Zhang, Zuozhu Liu, Hongwei Wang
- **年份**: 2024
- **Venue**: NAACL 2024 (Short Papers)
- **问题**: 第一作者是 **Xie**，不是 Zhang。Zhang 只是第三作者。引用应写为 **(Xie et al., 2024)**，不是 (Zhang et al., 2024)。
- **BibTeX**:
```bibtex
@inproceedings{xie2024selfimproving,
  title={Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models},
  author={Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},
  booktitle={Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 2: Short Papers)},
  pages={583--593},
  year={2024}
}
```

---

### 3. LLMaAA (Zhang et al., 2024) ⚠️ 年份错误

- **完整标题**: LLMaAA: Making Large Language Models as Active Annotators
- **作者**: Ruoyu Zhang, Yanzeng Li, Yongliang Ma, Ming Zhou, Lei Zou
- **年份**: **2023**（不是 2024）
- **Venue**: Findings of EMNLP 2023
- **问题**: 引用年份应为 **2023**。正确写法为 **(Zhang et al., 2023)**。
- **BibTeX**:
```bibtex
@inproceedings{zhang2023llmaaa,
  title={LLMaAA: Making Large Language Models as Active Annotators},
  author={Zhang, Ruoyu and Li, Yanzeng and Ma, Yongliang and Zhou, Ming and Zou, Lei},
  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2023},
  year={2023}
}
```

---

### 4. Lakens (2017) ✅ 确认存在

- **完整标题**: Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses
- **作者**: Daniël Lakens
- **年份**: 2017
- **Venue**: *Social Psychological and Personality Science*, 8(4), 355–362
- **DOI**: 10.1177/1948550617697177
- **BibTeX**:
```bibtex
@article{lakens2017equivalence,
  title={Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses},
  author={Lakens, Dani{\"e}l},
  journal={Social Psychological and Personality Science},
  volume={8},
  number={4},
  pages={355--362},
  year={2017},
  doi={10.1177/1948550617697177}
}
```

---

### 5. Wellek (2010) ✅ 确认存在

- **完整标题**: Testing Statistical Hypotheses of Equivalence and Noninferiority (2nd Edition)
- **作者**: Stefan Wellek
- **年份**: 2010
- **Venue**: Chapman & Hall/CRC (书籍)
- **ISBN**: 978-1439808184, 431 pages
- **BibTeX**:
```bibtex
@book{wellek2010testing,
  title={Testing Statistical Hypotheses of Equivalence and Noninferiority},
  author={Wellek, Stefan},
  edition={2nd},
  year={2010},
  publisher={Chapman \& Hall/CRC},
  isbn={978-1439808184}
}
```

---

## 总结

| # | 引用 | 状态 | 问题 |
|---|------|------|------|
| 1 | NuNER (Bogdanov et al., 2024) | ✅ | — |
| 2 | Self-Improving (Zhang et al., 2024) | ⚠️ | 应为 **Xie et al., 2024** |
| 3 | LLMaAA (Zhang et al., 2024) | ⚠️ | 年份应为 **2023** |
| 4 | Lakens (2017) | ✅ | — |
| 5 | Wellek (2010) | ✅ | — |

**需修正**：引用 #2 的作者归属和引用 #3 的年份。

---
