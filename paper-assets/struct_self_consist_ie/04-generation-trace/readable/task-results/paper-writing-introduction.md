# paper writing introduction

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_introduction_20260514T200845_result.json`
- **Structured JSON:** [`2fe0a7afcb7da90de77c.json`](../../sessions/2f/2fe0a7afcb7da90de77c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Introduction 已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex`。

结构概要：
- **段落1 (Hook)**: Self-consistency 在推理任务上的成功 → IE 的结构化输出本质不同 → 核心问题
- **段落2 (Gap)**: Quality estimation vs sample selection 被混为一谈；Nédellec & Xia 2026 的 surface matching 局限；现有工作缺乏系统比较
- **段落3 (Insight + Approach)**: Correlation-selection gap 核心发现预告；5 signals × 3 families × 3 datasets × 2 models；引用 Figure~\ref{fig:overview}
- **段落4 (Contributions)**: C1 首次系统比较 (ρ=0.50, AUROC=0.73)；C2 correlation-selection gap (NER 无信号超越 greedy，RE logprob +2.3pp)；C3 task-complexity boundary (EM>SJ easy tasks, SJ>EM hard tasks, 收敛于 WNUT-17)
- **过渡**: 指向 §method, §experiments, §related

所有数字与 experiments.tex 一致，引用仅使用 references.bib 中已有的 keys，未违反任何 FORBIDDEN 规则。

---
