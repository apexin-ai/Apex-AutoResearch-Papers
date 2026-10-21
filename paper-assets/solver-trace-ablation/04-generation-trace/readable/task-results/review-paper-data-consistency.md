# review paper data consistency

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_paper-data-consistency_20260514T214424_result.json`
- **Structured JSON:** [`cb511a2dd8a7a0146c60.json`](../../sessions/cb/cb511a2dd8a7a0146c60.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/data_consistency_report.md`。

**核心结论：PASS（无 critical 错误）**

- 所有数字（ISR 崩塌轨迹 0.642→0.132→0.003、3-seed β=0.1 ISR/Random、SFT 92.9%、Prolog 3-seed、1000-step 18.55 components 等）均与 registry 一致
- 所有硬约束遵守：0 处 "2.4x"、0 处 "six modes"、s44 query-as-fact gaming 正确标 0% genuine、plan013 vs plan017 未简化为 additive/convex 对照、ISR β=0.1 未误标 "no hacking"
- "near-zero hacking" 仅用于 SFT（92.9% genuine），不用于 ISR β=0.1
- proved-only ISR* 约定全文一致（registry 中部分 mean_isr 数学换算后吻合）

**3 处 minor 建议修改：**
1. Appendix line 414 把 `−99.6%` 改为 `−99.5%`（与 abstract 对齐）
2. Table 1 caption 或 §3.2 footnote 说明 H7/H1 是 simple mean across seeds（H1=17% 用 simple mean，H7=65% 用 pooled，口径差异 ~0.8pp）
3. 可选：Prolog STA s44 的 Gen=0 在表内更显眼标注，避免读者忽略 footnote $^b$ 中的 strict classifier 100% genuine 误报

---
