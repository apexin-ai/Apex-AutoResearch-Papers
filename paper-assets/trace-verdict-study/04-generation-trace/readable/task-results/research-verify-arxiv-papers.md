# research verify arxiv papers

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_verify_arxiv_papers_20260515T135212_result.json`
- **Structured JSON:** [`59f1904f0e9783322b60.json`](../../sessions/59/59f1904f0e9783322b60.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

### 论文 1: arXiv 2509.16596
| 项目 | 结果 |
|------|------|
| 页面状态 | ✅ 存在 |
| 标题 | ✅ 完全匹配："Analyzing the Effects of Supervised Fine-Tuning on Model Knowledge from Token and Parameter Levels" |
| 作者 | ✅ 匹配 — Junjie Ye, Yuming Yang, Yang Nan, Shuo Li, Qi Zhang, Tao Gui, Xuanjing Huang, Peng Wang, Zhongchao Shi, Jianping Fan |
| 日期 | 2025-09-20 提交，2026-02-10 更新 v2 |
| 会议 | ✅ 页面明确标注 "Accepted by EMNLP 2025 Main Conference" |

**结论：✅ REAL — 信息全部匹配。**

---

### 论文 2: arXiv 2605.03686
| 项目 | 结果 |
|------|------|
| 页面状态 | ✅ 存在 |
| 标题 | ✅ 完全匹配："From Code to Prediction: Fine-Tuning LLMs for Neural Network Performance Classification in NNGPT" |
| 作者 | ⚠️ 不匹配 — 实际作者为 **Mahmoud Hanouneh, Radu Timofte, Dmitry Ignatov**，而非所声称的 "NNGPT Team" |
| 日期 | 2026-05-05 提交，2026-05-06 更新 v2 |
| 会议 | 页面无会议录用信息，与声称的 "arXiv preprint" 一致 |

**结论：⚠️ MISMATCH — 论文真实存在，标题匹配，但作者信息不准确。"NNGPT Team" 是笼统描述，实际作者是 Hanouneh, Timofte, Ignatov 三人。**

---
