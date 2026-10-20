# paper compile and audit

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_compile-and-audit_20260515T045634_result.json`
- **Structured JSON:** [`2cc9d82a431cc211f72e.json`](../../sessions/2c/2cc9d82a431cc211f72e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。核心发现：

**编译阻塞**: `acl.sty` 缺失，4 个 section 被注释掉，`references.bib` 需 build.sh 复制。图片文件均存在。

**数字不一致（P0 级）**:
- **results.tex 内联 LOGO 表**: 6/7 个数字与 registry 偏差（如 Qwen3-1.7B 写 0.809 实为 0.805，avg 写 0.790 实为 0.789）。table1.tex 有正确值但未被 \input。
- **Feature Importance**: results.tex 文本写 hapax 0.271/TTR 0.165/entropy_mean 0.156，registry 为 0.269/0.159/0.164。table2.tex caption 正确。
- **Spearman 四舍五入**: TTR -0.543（应 -0.542）、entropy_mean -0.476（应 -0.475）、tail_decay 0.087（应 0.089）。
- **introduction.tex**: per-gen range 写 "0.69 to 0.85"，其他位置和 registry 均为 "0.68 to 0.86"。

**全部匹配**: baselines（5-gen LOGO）、downstream perplexity、cross-ref models 数字全部正确。

报告已注册为 artifact `art_20260515_205e9a`。

---
