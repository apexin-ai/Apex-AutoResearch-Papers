# research citation verification

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_citation_verification_20260520T173215_result.json`
- **Structured JSON:** [`a2bf580aab27b45c7125.json`](../../sessions/a2/a2bf580aab27b45c7125.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。结果写入 `artifacts/citation_verification.json`。

## 核心发现

**3 条高危（疑似虚构）：**

| 引用 | 问题 |
|------|------|
| **DRIP-R** | 实际 Borkakoty et al., **2026** (arXiv 2605.07699)。bib 中的 Murthy/Li et al. 2024、NeurIPS/EMNLP venue 全部是编造的 |
| **PhantomPolicy** | 实际 Jie Wu & Ming Gong, **2026** (arXiv 2604.12177)。bib 中 Wang et al. ACL 2024 是编造的 |
| **AgentPex** | 实际 Sharma, Barke, Zorn (Microsoft Research), **2026** (arXiv 2603.23806)。bib 中 Zhang et al. NeurIPS 2024 是编造的 |

**5 条需修正：**

| 引用 | 问题 |
|------|------|
| **τ-bench / τ²-bench** | 正确标题 "τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains"（Yao et al., NeurIPS 2024, arXiv 2406.12045）。τ²-bench 是另一篇论文（Barres et al., 2025） |
| **Toolformer** | NeurIPS **2023**，不是 2024 |
| **Massey** | 标题错——bib 中是另一篇 Massey 论文。正确标题 "Identifying and Classifying Ambiguity for Regulatory Requirements"，RE 2014 |
| **Berry & Kamsties** | 缺第三作者 Michael M. Krieger |
| **Wasow (2005)** | bib1 标题 "Intuitions and Models of Vagueness and Ambiguity" 查无此文。实际论文标题 "The Puzzle of Ambiguity"（CSLI Publications） |

**3 条已验证：** Kennedy (2007)、Ferreira et al. (2002)、PolicyBank（但需确认是否已加入 References）。

---
