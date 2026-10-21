# review paper consistency

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_paper-consistency_20260514T112531_result.json`
- **Structured JSON:** [`3c3e7a951b9b5372c68f.json`](../../sessions/3c/3c3e7a951b9b5372c68f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审查完成。报告已写入 `artifacts/_project/paper/review_report.md`。

**核心发现摘要**:

**🔴 Critical (4)**:
1. **Logit/Generation 准确率混源** — 74.5% logit 来自 plan-004-v5 (GA=1)，65.36% generation 来自 plan-004-ablation-b (GA=8)，是两个不同模型。v5 的 generation 实际只有 53.3%（degenerate），ablation-b 的 logit-generation gap 为 0。论文制造了一个不存在的"中等 gap"。
2. **缺 main.tex** — 无法编译
3. **`\ref{fig:decomposition}` 悬空** — 无对应 Figure
4. **页数超限** — 估算 ~5.0 页，超 4 页限制约 1 页

**🟡 Important (6)**: Limitations 重复出现两次、Method/Experiments 数值重复、DAgger gap 未讨论（paper_framing 明确要求）、bib 条目不完整（2 条缺 venue、2 条 Anonymous）、96.2% 可能应为 96.3%、98.2% tie rate 无 registry 支撑

**🟢 Minor (5)**: Abstract 过密、C2 贡献混入 router 细节、-100 惩罚泛化性讨论不足、CogRouter 82.3% 与本文 metric 不可比、Future Work 可压缩

**好消息**: 所有核心数字（Δ_full、Δ_nd、DAF、r、p、Table 1 全部数字）跨 section 一致且与 registry 匹配。Framing 一致性合规（Option B），无违禁表述，强度词使用合理。

---
