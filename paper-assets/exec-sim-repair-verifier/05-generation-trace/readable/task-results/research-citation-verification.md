# research citation verification

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_citation-verification_20260515T122933_result.json`
- **Structured JSON:** [`af108947ccb6fc18644c.json`](../../sessions/af/af108947ccb6fc18644c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

核查完成。关键发现：

**Part A — 24 条 bib 中有 8 条 first author 错误**（全部是近期 arXiv 论文，疑似 LLM 生成时产生的幻觉）：

| bib key | 错误 author | 实际 author |
|---------|-----------|-----------|
| `ding2025selfexecution` | Ding, Yangruibo | **Maimon, Gallil** |
| `ye2025demystifying` | Ye, Yanzhuo | **Abdollahi, Mohammad** |
| `chen2025solidcoder` | Chen, Xinyun | **Lee, Woojin** |
| `zhang2025swerm` | Zhang, Jiayi | **Shum, KaShun** |
| `wu2025patchreasoner` | Wu, Zuxin | **Xu, Junjielong** |
| `wang2025vgsearch` | Wang, Jinghan | **Chen, Hao Mark** |
| `zhang2025sstar` | Zhang, Dacheng | **Li, Dacheng** |
| `aleithan2025survey` | Aleithan, Reem | **Yang, Boyang** |

**Part B** — 5 篇补充论文的完整 BibTeX 已生成（LEVER, CodeT, Andrews 2005, Just 2014, VG-Search 修正版）。

**Qwen3** — 有独立技术报告（arXiv:2505.09388, 2025-05-14），如论文使用 Qwen3 模型应增加引用。

完整报告已写入 `artifacts/_project/report/citation_verification_w6_w9.md`。修正后的 bib key 会变化（如 `ding2025selfexecution` → `maimon2025selfexecution`），需同步更新 .tex 中的 `\cite{}`。

---
