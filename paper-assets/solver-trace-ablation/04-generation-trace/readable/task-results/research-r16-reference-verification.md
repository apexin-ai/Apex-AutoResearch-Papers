# research r16 reference verification

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_r16-reference-verification_20260520T054756_result.json`
- **Structured JSON:** [`66b4020f89ff83671c69.json`](../../sessions/66/66b4020f89ff83671c69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

| # | 引用 | 验证 | 已在 bib | 需操作 |
|---|------|------|----------|--------|
| 1 | Ng et al. 1999 | ✅ 正确 | ✅ `ng1999policy` | 无 |
| 2 | Sullivan 2025 | ✅ 正确（单作者，非 et al.） | ❌ | **需添加** `sullivan2025grpo` |
| 3 | Wang et al. 2025 | ✅ 正确 | ✅ `wang2025trace` | 无 |
| 4 | "Luo et al." 2026 | ⚠️ 作者错误：实际是 Pronesti, Belz, Hou | ❌ | **需添加** `pronesti2026beyond`；引用时注意作者修正 |
| 5 | "Pan et al." 2026 | ⚠️ 第一作者是 Cao（Pan 是第4作者） | ✅ `cao2026pushing` | 无（bib 正确） |

2 篇新 BibTeX 条目已保存到 `artifacts/new_references.bib`。

Sources:
- [Ng 1999 - ACM DL](https://dl.acm.org/doi/10.5555/645528.657613)
- [Sullivan 2025 - arXiv:2509.21154](https://arxiv.org/abs/2509.21154)
- [Wang et al. 2025 - arXiv:2510.01367](https://arxiv.org/abs/2510.01367)
- [Pronesti et al. 2026 - arXiv:2601.17223](https://arxiv.org/abs/2601.17223)
- [Cao et al. 2026 - arXiv:2601.22642](https://arxiv.org/abs/2601.22642)

---
