# paper related work citations

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_related_work_citations_20260519T154045_result.json`
- **Structured JSON:** [`8863ab9a86873104ec17.json`](../../sessions/88/8863ab9a86873104ec17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 7 个新 key 在 tex 和 bib 中均有对应，无 orphan。

**总结：**

| 方向 | 新增引用 | 融入位置 |
|------|---------|---------|
| Code agents w/ execution feedback | `yang2024sweagent`, `wang2025openhands` | Trace Compression 段落 (line 22) |
| Build log / test result parsing | `he2021loganalysis` | Trace Compression 段落 (line 23) |
| Selective context / input pruning | `jiang2023llmlingua`, `li2023selectivecontext` | Trace Compression 段落 (line 24) |
| Test oracle survey | `barr2015oracle` | Code Verdict 段落 (line 13) |
| Mutation testing | `papadakis2019mutation` | Code Verdict 段落 (line 14) |

**替换说明：** Compresso (Guo et al., 2023) 是模型结构化剪枝论文，与"input pruning"不符。改用 Selective Context (Li et al., EMNLP 2023)，该论文研究通过剪除低信息 token 压缩 LLM 输入，直接支持"less is more"叙事。

注意：根据 C001 约束，这些改动在本地 `docs/paper/`，需同步到服务器 `/root/trace-verdict-study/docs/paper/`。

---
