# research reference expansion

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_reference-expansion_20260521T062633_result.json`
- **Structured JSON:** [`e88c0f05b42ea7e2658d.json`](../../sessions/e8/e88c0f05b42ea7e2658d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。文件已写入：

- **BibTeX**: `artifacts/references/references.bib` — 30 条 verified entries
- **摘要表**: `artifacts/references/references_summary.md`

### 需要注意的问题

**1 条 UNVERIFIED：**
- **Yin, Shi, Wu, Chang (2024)** — 多次搜索未找到匹配 NeurIPS 2024 + IRT + LLM 的论文，已在 bib 文件中标注

**3 条作者不匹配（已用最接近的替代）：**
- 用户指定 "Li, Zhang, et al. (2024)" contamination survey → 实际匹配为 `Xu2024contamination`（Xu, Guan, Greene, Kechadi, arXiv:2406.04244）
- 用户指定 "Xu, Jain, et al. (2024)" benchmark self-evolving → 实际匹配为 `Wang2024selfevolving`（Wang, Long, Fan, Wei, Huang, arXiv:2402.11443）
- 用户指定 "Polo, Choshen, Sun, Xu, **Flamary**" → 实际作者列表为 Maia Polo, Weber, Choshen, Sun, Xu, **Yurochkin**（Flamary 不在作者列表中）

**1 条年份修正：**
- 用户指定 "Byrd & Srivastava (2024)" → 实际找到的是 ACL 2022 短文

---
