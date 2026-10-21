# paper writing introduction

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_introduction_20260517T164308_result.json`
- **Structured JSON:** [`b10cae5597de7d62bb8b.json`](../../sessions/b1/b10cae5597de7d62bb8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Introduction 已写入 `docs/paper/sections/introduction.tex`，约 1200 words，5 段结构：

1. **P1** — LLM DocRE 进展但无证据：GenRES/LMRC/DocKS-RAG 逼近 encoder SOTA，但只输出裸三元组，部署场景无法验证
2. **P2** — 可验证证据的必要性：RE 输出进入 KG 和决策流程，encoder 方法 (SAIS/DREEAM) 有证据但精度已落后
3. **P3** — Encoder retrieval ≠ generative production：encoder 证据是辅助信号（helps extraction），生成式证据是额外负担（costs capacity）
4. **P4** — 核心发现：decoupling spectrum、scale-dependent evidence tax、RSFT+CED 方案
5. **P5** — 5 条贡献列表（enumerate 格式）

风格检查通过：无 em-dash、无解释性 en-dash、无 -ing 短语结尾、无连续过渡词、无黑名单用词。

---
