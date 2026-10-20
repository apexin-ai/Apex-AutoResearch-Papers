# knowledge literature map update

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_literature_map_update_20260514T160129_result.json`
- **Structured JSON:** [`9eee31753179052f7ea3.json`](../../sessions/9e/9eee31753179052f7ea3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`literature_map.yaml` 已创建，包含 8 篇论文的完整条目：

| 论文 | Role | 核心差异 |
|------|------|----------|
| **VeriCoT** (ICLR 2026) | direct-competitor | binary step-level, 单链+反思, LLM-gen premises, 15-45% pass rate |
| **PC-CoT** (ICLR 2026) | direct-competitor | binary filter + SC (Certified Self-Consistency), 仅 GSM8K |
| **VERGE** (arXiv 2026) | direct-competitor | MCS error localization + 生成引导, online 介入 vs SVS post-hoc |
| **PRoSFI** (ICML 2026) | method-component | graded reward for RL training, 不用于 inference |
| **LogicReward** (ICLR 2026) | evaluation | Isabelle-based graded reward for SFT/DPO |
| **LINC** (EMNLP 2023) | background | Prover9, problem-level binary |
| **LOGIC-LM** (EMNLP 2023) | background | symbolic solver, problem-level binary + self-refinement |
| **SatLM** (NeurIPS 2023) | background | SAT solver, 声明式编程 |

每篇都包含 `svs_relevance` 字段，说明与 SVS 的差异化定位。底部 `landscape_summary` 总结了 binary→graded 趋势、chain selection 空白、autoformalization 瓶颈三个关键观察。

---
