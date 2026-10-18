# research dont waste bits citation

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_dont_waste_bits_citation_20260515T052854_result.json`
- **Structured JSON:** [`6d001c969b219de2ddc6.json`](../../sessions/6d/6d001c969b219de2ddc6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：论文**真实存在**

**完整信息：**
- **标题**: Don't Waste Bits! Adaptive KV-Cache Quantization for Lightweight On-Device LLMs
- **作者**: Sayed Pedram Haeri Boroujeni, Niloufar Mehrabi, Patrick Woods, Gabriel Hillesheim, Abolfazl Razi
- **arXiv ID**: 2604.04722 (April 2026)
- **会议**: Accepted at CVPR 2026
- **核心方法**: 基于 token-level features（频率、质量分数、attention variance、entropy）的 learned controller，动态为每个 token 选择 KV 精度 {2-bit, 4-bit, 8-bit, FP16}
- **目标场景**: 轻量级 on-device LLMs（SmolLM 系列）

---

### 与我们工作的关系

两篇论文都做 KV cache mixed-precision quantization，但**粒度和方法完全不同**：

| | Don't Waste Bits | Ours (RateKV) |
|---|---|---|
| 粒度 | **token-level** | **per-head** |
| 决策方式 | learned controller, **动态** (runtime) | MCKP + cardinality constraint, **静态** |
| 目标模型 | 小模型 (SmolLM-360M) | 大模型 (Qwen2.5-7B 等) |
| 理论基础 | data-driven | rate-distortion, polymatroid |

互补而非竞争——他们按 token 调精度，我们按 head 调精度。

---

### BibTeX

```bibtex
@article{haeriboroujeni2026dontwaste,
  title   = {Don't Waste Bits! {Adaptive} {KV}-Cache Quantization for Lightweight On-Device {LLMs}},
  author  = {Haeri Boroujeni, Sayed Pedram and Mehrabi, Niloufar and Woods, Patrick and Hillesheim, Gabriel and Razi, Abolfazl},
  journal = {arXiv preprint arXiv:2604.04722},
  year    = {2026},
  note    = {Accepted at CVPR 2026}
}
```

---

### 引用位置

建议加在 `related_work.tex` 第 22 行的 mixed-precision KV-cache 列表中，紧接 `\cite{zhang2025mixkvq}` 之后。引用 context：

> token-level adaptive precision via a learned controller~\cite{haeriboroujeni2026dontwaste}

在现有句子末尾的分号列表中追加即可，因为该段已经在按粒度（layer/block/channel/memory-budget/dynamic）列举 mixed-precision KV cache 方法，token-level 是一个自然的新粒度类别。

Sources:
- [arXiv: Don't Waste Bits!](https://arxiv.org/abs/2604.04722)
- [ResearchGate](https://www.researchgate.net/publication/403562001_Don't_Waste_Bits_Adaptive_KV-Cache_Quantization_for_Lightweight_On-Device_LLMs)

---
