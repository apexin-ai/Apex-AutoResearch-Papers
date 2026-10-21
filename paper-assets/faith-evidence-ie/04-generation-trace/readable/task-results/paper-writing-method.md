# paper writing method

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_method_20260517T162426_result.json`
- **Structured JSON:** [`b07ec30960321b238ced.json`](../../sessions/b0/b07ec30960321b238ced.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Method section 写入 `docs/paper/sections/method.tex`，~1243 words，5 个子节：

- **3.1 Task** — 形式化定义 evidence-grounded DocRE，区分 encoder-based 方法（SAIS/DREEAM 无生成开销）与 LLM 生成式方法（scale-dependent cost）
- **3.2 SFT Baseline** — LoRA r=64/α=128，含 no-evidence upper bound 变体
- **3.3 Optimization Paradigms** — GRPO (QLoRA G=4, bf16 G=8)、DPO (1ep/3ep)、RSFT (N=8, top-k=1, 9042/24216=37.3%)
- **3.4 CED** — NLI entailment + entity-sharing hard negatives 对比评分，含 flat-NLI baseline 对比（p=0.44），`\label{sec:ced}` 已设置
- **3.5 EDCR** — 诊断指标定义 Evi-Recall\_TP / Rel-Recall，method-level ρ=-0.965，per-relation ρ=-0.064，阈值 0.70/0.65

所有参数与 experiments.tex 一致。无 em-dash、无 -ing 短语结尾、无黑名单词。

---
