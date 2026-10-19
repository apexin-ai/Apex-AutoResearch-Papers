# writing related work v1 round2

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_related-work-v1-round2_20260515T101954_result.json`
- **Structured JSON:** [`eb08aa18edcf9f3e35e0.json`](../../sessions/eb/eb08aa18edcf9f3e35e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修改完成。修改摘要：

**修正 1 — §2.3 CoCoHaNeRe gap 表述**：替换了模糊的 "More broadly..." 句，改为明确指出 CoCoHaNeRe 的评估针对 NL→code search setting，在 structural code retrieval（repo-level/file-level localization）下 static embedding-distance mining 是否同样受限尚未被测试。同时覆盖了 BM25 和 embedding-based 两种非梯度策略的局限性，消除 Intro/RW 不一致。

**修正 2 — §2.3 StructFuse 定位扩充**：从 1 句扩展为 3 句，涵盖：(1) systematic comparison of three mining strategies across encoders with distinct representation geometries；(2) static embedding-distance mining 提供 consistent gains 作为 strong baseline，无需 gradient computation；(3) data-flow structure 作为 orthogonal signal，基于 inter-procedural program semantics。无 hedge 语言。

**修正 3 — 补充 RepoFusion + GRACE**：
- RepoFusion `\cite{shrivastava2023repofusion}` 加入 §2.4，紧接 CrossCodeEval 后，描述 cross-file context 训练对 code completion 的提升
- GRACE `\cite{wang2025grace}` 加入 §2.4 inference-time graph methods 段落，描述 multi-level code graph（repo/module/function 粒度）
- 两条新 bib 条目已加入 references.bib

**修正 4 — Sentence-BERT + Ding et al. 2022**：
- Sentence-BERT `\cite{reimers2019sentencebert}` 加在 §2.2 开头作为从 NLP 到代码对比学习的过渡桥梁（bib 条目已存在）
- Ding et al. `\cite{ding2022programcontrasts}` 加在 §2.2 ContraBERT 之后，描述 structure-guided code transformations 用于合成对比样本对（bib 条目已存在）

---
