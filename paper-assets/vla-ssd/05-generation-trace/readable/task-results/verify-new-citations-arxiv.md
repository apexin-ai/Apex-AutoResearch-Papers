# verify new citations arxiv

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_new_citations_arxiv_20260524T013515_result.json`
- **Structured JSON:** [`c3dc331a8db8a004e5c0.json`](../../sessions/c3/c3dc331a8db8a004e5c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两篇论文均已验证完毕。

---

## 论文 1: "Pretrained VLAs are Surprisingly Resistant to Forgetting"
- **arXiv ID 有效**: 是 — [2603.03818](https://arxiv.org/abs/2603.03818) 存在
- **标题准确**: 部分 — 实际标题为 "Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning"（声称标题是缩写版）
- **作者匹配**: 是 — Huihan Liu, Changyeon Kim, Bo Liu, Minghuan Liu, Yuke Zhu
- **内容摘要**: Pretrained VLAs 在 continual learning 中对遗忘有极强抵抗力；简单的 Experience Replay (ER) 即可实现接近零遗忘；在 Pi0、GR00T N1.5 等多种 VLA 上一致成立
- **发表时间**: 2026年3月17日 ✓
- **结论**: **真实论文** ✓

---

## 论文 2: "Enhancing Generalization in VLA Models by Preserving Pretrained Representations"
- **arXiv ID 有效**: 是 — [2509.11417](https://arxiv.org/abs/2509.11417) 存在
- **标题准确**: 部分 — 实际标题为 "Enhancing Generalization in **Vision-Language-Action** Models by Preserving Pretrained Representations"（声称标题用了缩写 VLA）
- **作者匹配**: 是 — Shresth Grover, Akshay Gopalkrishnan, Bo Ai, Henrik I. Christensen, Hao Su, Xuanlin Li（声称的姓氏列表匹配，缺了 Xuanlin Li）
- **内容摘要**: VLM→VLA fine-tuning 会破坏 pretrained representations，提出 (1) dual-encoder（一个 frozen + 一个 trainable）, (2) string-based action tokenizer, (3) co-training strategy 结合 robot demo 和 VL 数据集
- **发表时间**: 2025年9月14日 ✓
- **结论**: **真实论文** ✓（作者列表少列了 Li，其余准确）

---

两篇均为真实论文，可安全引用。建议在正式引用时使用完整标题和完整作者列表。

Sources:
- [arXiv 2603.03818](https://arxiv.org/abs/2603.03818)
- [arXiv 2509.11417](https://arxiv.org/abs/2509.11417)
- [Continual VLAs project page](https://continual-vlas.github.io/forget-me-not/)
- [Gen-VLA project page](https://gen-vla.github.io/)

---
