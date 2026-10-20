# research fix literature authors

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_fix_literature_authors_20260515T134235_result.json`
- **Structured JSON:** [`904861f9f56f807f02bf.json`](../../sessions/90/904861f9f56f807f02bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有编辑已正确应用。汇总报告：

---

## 汇总

### 作者信息修复（5 篇）

| 论文 | 原始 authors | 修复后 |
|---|---|---|
| TraceCoder | "ICSE 2026 Research Track" | Jiangping Huang, Wenguang Ye, Weisong Sun, Jian Zhang, Mingyue Zhang, Yang Liu |
| APSG+Graph-LoRA | "arXiv 2505.02629" | Zhenyu Yang, Jingwen Wu, Zhen Yang, Zhongxing Yu |
| InspectCoder | "arXiv 2510.18327" | Yunkun Wang, Yue Zhang, Guochang Li, Chen Zhi, Binhua Li, Fei Huang, Yongbin Li, Shuiguang Deng |
| ET-CoT | "ICML 2025 Workshop PRAL" | Koshi Eguchi, Takuya Akiba |
| arXiv 2512.00215 | "arXiv 2512.00215" | Mohammad Abdollahi, Khandaker Rifah Tasnia, Soumit Kanti Saha, Jinqiu Yang, Song Wang, Hadi Hemmati |

### 额外作者补全（2 篇）

- **Seeker**: "Xuanming Zhang et al." → Xuanming Zhang, Yuxuan Chen, Yuan Yuan, Minlie Huang
- **FisherSFT**: "Rohan Deb, Kiran Koshy Thekumparampil, et al." → 补全全部 6 位作者
- **Runtime Traces + Multi-Agent Debate**: "Jiaqing Wu et al." → 补全全部 5 位作者

### arXiv ID / OpenReview ID 补全（17 篇 2025-2026 论文）

全部已添加。其中 ET-CoT 无 arXiv 预印本，添加了 `openreview_id: pFyBdPyOCQ`。

### 真实性验证

| 论文 | 结果 |
|---|---|
| **TraceCoder** (ICSE 2026) | **confirmed** — arXiv 2602.06875，conf.researchr.org 有 ICSE 2026 收录记录 |
| **Runtime Traces + Multi-Agent Debate** (arXiv 2604) | **confirmed** — arXiv 2604.02647，Jiaqing Wu 等 5 人，2026-04-03 提交 |

**26 篇论文全部确认真实存在，无需标注 `verified: false`。**

---
