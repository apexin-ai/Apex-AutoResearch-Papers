# research bib verification

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_bib_verification_20260514T183737_result.json`
- **Structured JSON:** [`bfa8a6c17e1d39e50c79.json`](../../sessions/bf/bfa8a6c17e1d39e50c79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。

---

### 1. zhong2021frustratingly — ✅ 真实

- **标题**: A Frustratingly Easy Approach for Entity and Relation Extraction
- **作者**: Zexuan Zhong, Danqi Chen (Princeton)
- **Venue**: NAACL 2021, pages 50–61
- **ACL Anthology**: https://aclanthology.org/2021.naacl-main.5/
- **SciERC Rel F1**: ~48.6% (boundaries), ~35.7% (strict/Rel+)

```bibtex
@inproceedings{zhong2021frustratingly,
  title     = {A Frustratingly Easy Approach for Entity and Relation Extraction},
  author    = {Zhong, Zexuan and Chen, Danqi},
  booktitle = {Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},
  pages     = {50--61},
  year      = {2021},
  address   = {Online},
  publisher = {Association for Computational Linguistics},
  url       = {https://aclanthology.org/2021.naacl-main.5}
}
```

### 2. ye2022packed — ✅ 真实

- **标题**: Packed Levitated Marker for Entity and Relation Extraction
- **作者**: Deming Ye, Yankai Lin, Peng Li, Maosong Sun (Tsinghua/THUNLP)
- **Venue**: ACL 2022, pages 4904–4917
- **ACL Anthology**: https://aclanthology.org/2022.acl-long.337/
- **SciERC Rel F1**: ~53.2% (boundaries), improvement over PURE by ~2.8–4.0%

```bibtex
@inproceedings{ye2022packed,
  title     = {Packed Levitated Marker for Entity and Relation Extraction},
  author    = {Ye, Deming and Lin, Yankai and Li, Peng and Sun, Maosong},
  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  pages     = {4904--4917},
  year      = {2022},
  address   = {Dublin, Ireland},
  publisher = {Association for Computational Linguistics},
  url       = {https://aclanthology.org/2022.acl-long.337}
}
```

---

### Claim 校验: "40–50% F1"

| 模型 | Rel F1 (boundaries) | Rel+ F1 (strict) |
|------|---------------------|-------------------|
| PURE | ~48.6% | ~35.7% |
| PL-Marker | ~53.2% | ~38% |

**问题**: claim 说 "40–50% F1"，但 PL-Marker 的 Rel F1 达到 ~53%，超出了 50% 上界。两个修正方案：

1. **调整范围**: 改为 `"achieve approximately 49--53\% relation F1"` 
2. **如果有意指 strict Rel+**: 两者都在 35–38%，低于 40%

建议改为 `"achieve 48--53\% relation F1 (boundaries evaluation)"` 或更宽泛的 `"achieve roughly 50\% F1"`，这样更准确地覆盖两篇论文的实际数字。

Sources:
- [PURE - ACL Anthology](https://aclanthology.org/2021.naacl-main.5/)
- [PURE - GitHub](https://github.com/princeton-nlp/PURE)
- [PL-Marker - ACL Anthology](https://aclanthology.org/2022.acl-long.337/)
- [PL-Marker - GitHub](https://github.com/thunlp/PL-Marker)
- [PL-Marker - ar5iv](https://ar5iv.labs.arxiv.org/html/2109.06067)

---
