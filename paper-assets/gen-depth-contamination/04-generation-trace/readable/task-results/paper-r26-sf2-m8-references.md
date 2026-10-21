# paper r26 sf2 m8 references

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_r26_sf2_m8_references_20260522T082246_result.json`
- **Structured JSON:** [`465031b583d350bed3c5.json`](../../sessions/46/465031b583d350bed3c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修改已完成，验证通过。

---

## SF-2 结果

**references.bib** 追加两条：

```bibtex
@article{geng2026markovian,
  title={Markovian Generation Chains in Large Language Models},
  author={Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry},
  journal={arXiv preprint arXiv:2603.11228},
  year={2026},
  url={https://arxiv.org/abs/2603.11228}
}

@article{shahriar2025erosion,
  title={The Erosion of {LLM} Signatures: Can We Still Distinguish Human and {LLM}-Generated Scientific Ideas After Iterative Paraphrasing?},
  author={Shahriar, Sadat and Ayoobi, Navid and Mukherjee, Arjun},
  journal={arXiv preprint arXiv:2512.05311},
  year={2025},
  url={https://arxiv.org/abs/2512.05311}
}
```

**related_work.tex** 插入位置：

1. **Geng** → `\paragraph{Model collapse and recursive degradation.}` 段，`wang2025unveiling}.` 之后、`Suresh et al.` 之前：
   > Geng et al.~\cite{geng2026markovian} study the Markov chain convergence behavior of successive generation; our work complements this by quantifying the empirical discrimination boundary.

2. **Shahriar** → `\paragraph{Beyond binary detection.}` 段，`cross-mode transfer` 之后、`CoDeC` 之前，作为分号链的一环：
   > ...Shahriar et al.~\cite{shahriar2025erosion} measure detection accuracy erosion (${\sim}25.4\%$) across generation depths; CoDeC...
   
   末句扩展为：
   > None estimates recursive generation depth; we instead characterize the precise depth at which discrimination becomes impossible.

---

## m8 结果

**Preprint 格式审计**（5 条 `@article` 含 arXiv）：

| 条目 | 格式 | 状态 |
|------|------|------|
| `briesch2023selfconsuming` | `journal = {arXiv preprint arXiv:2311.16822}` | ✓ 一致 |
| `sadasivan2023detect` | `journal = {arXiv preprint arXiv:2303.11156}` | ✓ 一致 |
| `mehta2025beyond` | `journal = {arXiv preprint arXiv:2511.17602}` | ✓ 一致 |
| `spennemann2025quantifying` | `journal = {arXiv preprint arXiv:2504.08755}` | ✓ 一致 |
| `suresh2024rate` | `journal = {arXiv preprint arXiv:2412.17646}` | ✓ 一致 |

所有 preprint 均使用 `@article` + `journal = {arXiv preprint arXiv:XXXX.XXXXX}` 格式，**无不一致项**。新增两条也遵循此格式。

**修复的问题**：
- `suresh2024rate`：缺失 `url` 字段 → 已补充 `url={https://arxiv.org/abs/2412.17646}`

**已发表但仍标为 preprint？**：未发现。`sadasivan2023detect` 曾提交 OpenReview 但未确认被某会议正式接收，保持 preprint 状态。

---
