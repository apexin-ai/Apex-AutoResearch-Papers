# paper ref audit a13

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_ref-audit-a13_20260522T234649_result.json`
- **Structured JSON:** [`3399ad63618ba4003bb7.json`](../../sessions/33/3399ad63618ba4003bb7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### Step 1: 两篇论文已添加

**Lanham et al., 2023**
- 完整引用: Tamera Lanham, Anna Chen, Ansh Radhakrishnan, ... Ethan Perez. "Measuring Faithfulness in Chain-of-Thought Reasoning." arXiv:2307.13702, 2023.
- bib key: `lanham2023faithfulness`
- 已添加到 `references.bib`
- 已在 `related_work.tex` L15 (process rewards 段落末尾) 添加引用

**Turpin et al., 2023**
- 完整引用: Miles Turpin, Julian Michael, Ethan Perez, Samuel R. Bowman. "Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting." NeurIPS 2023. arXiv:2305.04388.
- bib key: `turpin2023unfaithful`
- 已添加到 `references.bib`
- 已在同一句中引用

添加的句子:
> Parallel work on CoT faithfulness finds that stated reasoning steps are often not causally necessary for model predictions (Lanham et al., 2023; Turpin et al., 2023); STA tests component necessity analogously but operates on solver-input clauses rather than natural-language CoT.

### Step 2: arXiv ID 验证

| arXiv ID | 状态 | 标题 |
|----------|------|------|
| 2509.22047 | **存在** | "MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems" (Ichihara et al., 2025) |
| 2603.28063 | **存在** | "Reward Hacking as Equilibrium under Finite Evaluation" (Wang & Huang, 2026) |

两个 arXiv ID 均真实存在，等 Director 决定是否添加到 bib。

`docs/paper/` 和 `paper/` 两个目录已同步，diff 验证一致。

---
