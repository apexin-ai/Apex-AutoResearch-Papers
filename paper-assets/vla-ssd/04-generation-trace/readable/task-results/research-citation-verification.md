# research citation verification

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_citation_verification_20260516T042149_result.json`
- **Structured JSON:** [`fa32b7429101e8ecbeda.json`](../../sessions/fa/fa32b7429101e8ecbeda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。结果如下：

---

### 引用 1: grant2026

```
引用 ID: grant2026
状态: VERIFIED
真实信息:
  Title: "Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models"
  Authors: Bryce Grant, Xijia Zhao, Peng Wang
  ArXiv ID: 2603.19233
  Year: 2026 (March)
  Venue: arXiv preprint (also on OpenReview)
与当前 bib 差异: 当前 bib 为占位符，需替换为真实信息
建议修正: 更新 bib 条目为上述真实信息。arXiv ID 是 2603.19233。
  关键发现与引用描述一致："the visual pathway dominates action generation across all architectures"
```

---

### 引用 2: fang2025

```
引用 ID: fang2025
状态: VERIFIED（但引用描述需微调）
真实信息:
  Title: "DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action"
  Authors: Zhen Fang et al.
  ArXiv ID: 2511.22134
  Year: 2025
与当前 bib 差异: bib 条目本身正确。
  但 paper_framing.md 引用为 "fine-tuning erodes VLM reasoning"，
  而论文实际讨论的是双向问题：
  (1) 将 VLM 微调为 VLA 会丢失推理能力（catastrophic forgetting）——这是论文动机
  (2) 给 specialist VLA 加回推理训练会导致 action degeneration——这是论文解决的问题
建议修正: 引用描述可保留，但更精确的表述是
  "fine-tuning VLMs into VLAs precipitates catastrophic forgetting of reasoning (Fang et al., 2025)"
  而非笼统的 "fine-tuning erodes VLM reasoning"
```

---

### 引用 3: rizzardo2026

```
引用 ID: rizzardo2026
状态: MISMATCH — 第一作者错误
真实信息:
  Title: "Observing and Controlling Features in Vision-Language-Action Models"
  Authors: Hugo Buurmeijer, Carmen Amo Alonso, Aiden Swann, Marco Pavone
  ArXiv ID: 2603.05487 ✓（正确）
  Year: 2026 (March)
与当前 bib 差异: cite key 为 rizzardo2026，但论文第一作者是 Buurmeijer，不是 Rizzardo。
  论文中无 Rizzardo 此人。
建议修正:
  1. cite key 改为 buurmeijer2026
  2. author 字段改为 {Hugo Buurmeijer and Carmen Amo Alonso and Aiden Swann and Marco Pavone}
  3. 全文搜索替换所有 \cite{rizzardo2026} → \cite{buurmeijer2026}
```

---

### 总结

| 引用 | 状态 | 阻塞? |
|------|------|-------|
| grant2026 | **VERIFIED** — 论文存在，arXiv:2603.19233，需更新占位符 bib | 更新 bib 后解除阻塞 |
| fang2025 | **VERIFIED** — bib 正确，引用描述可微调更精确 | 不阻塞 |
| rizzardo2026 | **MISMATCH** — 第一作者是 Buurmeijer 非 Rizzardo，需改 cite key | 需修正 |

Sources:
- [Grant et al. 2026 - arXiv](https://arxiv.org/abs/2603.19233)
- [Grant et al. 2026 - OpenReview](https://openreview.net/forum?id=w8Mw9zJt1y)
- [Fang et al. 2025 - DualVLA](https://arxiv.org/abs/2511.22134)
- [Buurmeijer et al. 2026 - arXiv](https://arxiv.org/abs/2603.05487)

---
