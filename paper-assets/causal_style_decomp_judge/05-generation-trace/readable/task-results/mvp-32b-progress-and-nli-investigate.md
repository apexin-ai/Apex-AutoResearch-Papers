# mvp 32b progress and nli investigate

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_mvp_32b_progress_and_nli_investigate_20260520T142517_result.json`
- **Structured JSON:** [`a1f8ef2b2fefb6ee2ddc.json`](../../sessions/a1/a1f8ef2b2fefb6ee2ddc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已获取。汇总如下：

---

## 任务 1: Qwen3-32B 下载进度

**进行中，约 59%**

| 指标 | 值 |
|------|-----|
| 总大小 | 61GB（目标约 65GB） |
| 已完成 shards | 10/17（#1-8, #13, #16） |
| 下载中 shards | 7 个（#9-12, #14-15, #17，在 `._____temp/` 目录） |
| 下载进程 PID 12163 | 仍在运行，已耗时 4h26m |
| config/tokenizer | 已存在 |

预计还需 ~3 小时。完成后可运行 tokenizer 验证。

---

## 任务 2: mvp_0002 NLI 异常分析

**mvp_0002 全文对比：**

| 字段 | 内容 |
|------|------|
| Original | "There was an independence referendum." |
| Counterfactual | "There was a vote on independence." |
| Double Rewrite | "There was a vote on independence."（与 CF 完全相同） |
| BERTScore_cf | 0.9164（正常） |
| **NLI_cf** | **0.0352（极低）** |

**原因分析：这是 NLI 模型的已知弱点，不是改写质量问题。**

"independence referendum" → "vote on independence" 在语义上几乎等价，BERTScore 0.916 也证实了这一点。但 NLI 模型（通常是 MNLI-trained）对这类**政治/法律领域的近义替换**非常敏感——"referendum" 是一个具有精确法律含义的词（公民投票的正式制度），而 "vote on independence" 更宽泛（可以是议会投票、全民公投、非正式投票等）。NLI 模型倾向于判定后者不能蕴含前者（entailment 方向失败），因此给出极低分。

此外，这条文本极短（仅 36 字符），NLI 模型在短文本上的置信度分布更极端，容易出现接近 0 或 1 的极端值。

---

## 全部 NLI_cf < 0.90 记录（5 条）

| ID | NLI_cf | BS_cf | 问题类型 |
|----|--------|-------|---------|
| mvp_0099 | 0.0002 | 0.465 | **内容完全替换**（`/user` → overfitting 讨论），改写彻底跑偏 |
| mvp_0084 | 0.0052 | 0.958 | "as radiant as" → "brighter than"，比喻→直述，NLI 判定语义不等价 |
| mvp_0002 | 0.0352 | 0.916 | "referendum" → "vote on independence"，领域术语近义替换 |
| mvp_0088 | 0.1022 | 0.912 | 诗歌："warming" → "illuminating"，NLI 对意象变化敏感 |
| mvp_0058 | 0.1895 | 0.787 | 正式邮件 → 口语化改写，语域变化大，NLI 对语气变化敏感 |

**结论：** mvp_0099 是改写质量问题（应当剔除或重新改写）；其余 4 条（包括 mvp_0002）是 NLI 模型对短文本/近义词/修辞手法变化的过度敏感，改写本身质量没有问题。建议在数据清洗管线中对 BERTScore > 0.85 但 NLI < 0.10 的记录做人工复核或使用多 NLI 模型投票。

---
