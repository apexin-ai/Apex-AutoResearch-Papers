# Citation Verification Report

Date: 2025-05-17

---

### diverseaware2025
**Status**: VERIFIED
**Search queries tried**:
- "diversity-aware training test-time scaling LLM 2025"
- "RePrism Diversity-aware Training for Test-time Scaling arXiv 2025"
- OpenReview page fetch (UVL10ozjtl)

**Result**: 论文真实存在。
- **Title**: Diversity-aware Training for Test-time Scaling
- **Authors**: Bohan Lyu, Qixin Xu, Zihan Zhu, Yesai Wu, Zhong Zhang, Haotian Chen, Xin Cong, Xiaojiang Liu, Zhiyuan Liu, Maosong Sun
- **Venue**: Submitted to ICLR 2026 (OpenReview ID: UVL10ozjtl)
- **arXiv ID**: 未找到独立 arXiv 预印本
- **OpenReview**: https://openreview.net/forum?id=UVL10ozjtl

**注意**: bib key 标注为 2025，但该论文实际提交至 ICLR 2026。建议将 bib key 中的年份修正为 2026，并确认论文 acceptance 状态（目前显示为 submitted，未确认 accepted）。如论文尚未被接收，引用时应标注为 preprint。

---

### satbench2025
**Status**: VERIFIED
**Search queries tried**:
- "SATBench LLM Boolean satisfiability benchmark 2025"
- "SATBench Benchmarking LLMs' Logical Reasoning Anjiang Wei arXiv 2505.14615"

**Result**: 论文真实存在。
- **Title**: SATBench: Benchmarking LLMs' Logical Reasoning via Automated Puzzle Generation from SAT Formulas
- **Authors**: Anjiang Wei, Yuheng Wu, Yingjia Wan, Tarun Suresh, Huanmi Tan, Zhanke Zhou, Sanmi Koyejo, Ke Wang, Alex Aiken
- **Venue**: EMNLP 2025 (ACL Anthology: 2025.emnlp-main.1716)
- **arXiv ID**: 2505.14615
- **Code**: https://github.com/Anjiang-Wei/SATBench

**BibTeX**:
```bibtex
@inproceedings{satbench2025,
  title={SATBench: Benchmarking LLMs' Logical Reasoning via Automated Puzzle Generation from SAT Formulas},
  author={Wei, Anjiang and Wu, Yuheng and Wan, Yingjia and Suresh, Tarun and Tan, Huanmi and Zhou, Zhanke and Koyejo, Sanmi and Wang, Ke and Aiken, Alex},
  booktitle={Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
  year={2025}
}
```

**注意**: 论文中描述为 "benchmarks LLMs on Boolean satisfiability problems"，实际论文是通过 SAT 公式自动生成逻辑谜题来测试 LLM，描述基本准确但略有简化。无需修改。

---

### llmmeets_cp2025
**Status**: VERIFIED
**Search queries tried**:
- "LLM constraint propagation solver hybrid 2025"
- "Large Language Model Meets Constraint Propagation IJCAI 2025 authors arXiv GenCP"
- arXiv page fetch (2505.24012)

**Result**: 论文真实存在。
- **Title**: Large Language Model Meets Constraint Propagation
- **Authors**: Alexandre Bonlarron, Florian Regin, Elisabetta De Maria, Jean-Charles Regin
- **Venue**: IJCAI 2025 (Special Track on AI, the Arts and Creativity)
- **arXiv ID**: 2505.24012
- **IJCAI Proceedings**: https://www.ijcai.org/proceedings/2025/1115

**BibTeX**:
```bibtex
@inproceedings{llmmeets_cp2025,
  title={Large Language Model Meets Constraint Propagation},
  author={Bonlarron, Alexandre and R{\'e}gin, Florian and De Maria, Elisabetta and R{\'e}gin, Jean-Charles},
  booktitle={Proceedings of the Thirty-Fourth International Joint Conference on Artificial Intelligence (IJCAI)},
  year={2025}
}
```

**注意**: 论文中描述为 "hybrid architectures where the LLM generates candidate assignments and a CP solver enforces hard constraints"。实际论文 (GenCP) 是将文本生成建模为 CSP，用 CP 推理来约束 LLM 输出，应用场景偏向受约束文本生成而非通用约束求解。描述方向正确但应用场景有偏差，建议核实论文中引用该工作时的上下文是否准确。

---

## Summary

| bib_key | Status | Venue | 需要修正 |
|---------|--------|-------|---------|
| diverseaware2025 | VERIFIED | ICLR 2026 (submitted) | 年份 2025->2026；确认 acceptance 状态 |
| satbench2025 | VERIFIED | EMNLP 2025 | 无 |
| llmmeets_cp2025 | VERIFIED | IJCAI 2025 | 核实引用上下文是否准确 |

**结论**: 3 篇引用均为真实论文，不存在 AI 虚构引用。但 `diverseaware2025` 的年份标注需修正。
