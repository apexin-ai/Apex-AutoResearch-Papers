# research write paper framing

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_write-paper-framing_20260514T214222_result.json`
- **Structured JSON:** [`8be760e2031a38d96238.json`](../../sessions/8b/8be760e2031a38d96238.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`paper_framing.md` 已保存。

核心 framing：**"Error Injection Helps Tool-Use but Hurts Planning"** — 以 PALADIN 对比为主线，论证 error injection 的有效性取决于任务结构（error observability、local recoverability、bounded action space），而非 taxonomy 质量。

文档包含：
- **6 条 Claims**，每条都追溯到具体实验数据（多种子 clean eval、recovery eval、per-operator breakdown）
- **7 条 Reviewer Concerns** 及预回应策略
- **PALADIN 对比分析**：4 个结构性差异维度解释为什么 tool-use 成功但 embodied planning 失败
- **3 级补充实验清单**：P1 必须做（更多 seed + injection ratio 消融 + loss 曲线），P2 强化（第二环境 + 定性分析），P3 锦上添花

推荐投 **Insights from Negative Results @ EMNLP 2026** (Budapest, Oct)，短论文 track，专为严谨负面发现设计。

---
