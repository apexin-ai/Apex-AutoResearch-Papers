# research llm asp citation verify

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_llm_asp_citation_verify_20260514T042632_result.json`
- **Structured JSON:** [`122763921e9d186c79c7.json`](../../sessions/12/122763921e9d186c79c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：**"LLM+ASP (ICLP 2025)" 作为引用不准确，需要修正。**

### 不存在的内容

没有一篇以 "LLM+ASP" 为简称、发表在 ICLP 2025 主会议、且核心方法为 **post-hoc ontology validation** 的论文。

### 实际存在的最近匹配

**1. LLMASP — ICLP 2025 Doctoral Consortium（非主会）**
- Title: *LLMASP: A Framework for Mitigating Hallucinations and Supporting Symbolic Reasoning in Large Language Models*
- Author: Lorenzo Grillo
- Venue: ICLP-WS-DC 2025, CEUR-WS Vol-4117
- 方法：LLM 提取结构化事实 → ASP 推理，**不是 ontology validation**

**2. LLMASP 完整版 — IJCAI 2025（不是 ICLP）**
- Title: *Integrating Answer Set Programming and Large Language Models for Enhanced Structured Representation of Complex Knowledge in Natural Language*
- Authors: Mario Alviano, Lorenzo Grillo, Fabrizio Lo Scudo, Luis Angel Rodriguez Reiners
- Venue: IJCAI 2025, pp. 4330–4338
- DOI: `10.24963/ijcai.2025/482`
- 方法：YAML 配置 prompt → LLM 抽取结构化事实 → ASP solver 推理。**核心是 structured representation，不是 post-hoc ontology validation**

**3. STAR — ICLP 2023**
- Title: *Reliable Natural Language Understanding with Large Language Models and Answer Set Programming*
- Authors: Rajasekharan, Zeng, Padalkar, Gupta
- arXiv: `2302.03780`
- Venue: ICLP 2023
- 方法：LLM 抽取谓词 → goal-directed ASP 推理

### 问题诊断

引用 "LLM+ASP (ICLP 2025)" 存在三个错误：
1. **Venue 错误** — 最相关的完整论文发表在 IJCAI 2025，不是 ICLP 2025（ICLP 2025 只有一篇 DC 摘要）
2. **方法描述不符** — 这些论文的核心是 "LLM 抽取 + ASP 推理"，不是 "post-hoc ontology validation"
3. **简称不规范** — 没有论文以 "LLM+ASP" 作为正式简称

### 建议替代方案

如果 Claim 2 需要一篇 post-hoc ontology validation 的代表工作：
- 将引用修正为 **Alviano et al. (IJCAI 2025)**，但需调整描述为 "ASP-based symbolic reasoning for structured knowledge validation"，而非 "ontology validation"
- 或者寻找真正做 ontology constraint checking 的工作（如 SHACL/DL reasoner-based validation 方向的论文）

Sources:
- [IJCAI 2025 Paper #482](https://www.ijcai.org/proceedings/2025/482)
- [ICLP 2025 Workshops & DC Proceedings (CEUR-WS Vol-4117)](https://ceur-ws.org/Vol-4117/)
- [STAR: Reliable NLU with LLMs and ASP (arXiv 2302.03780)](https://arxiv.org/abs/2302.03780)
- [ICLP 2025 Main Proceedings (EPTCS 439)](https://dblp.org/db/series/eptcs/eptcs439.html)
- [Alviano & Grillo Preliminary Report (CEUR-WS Vol-3876)](https://ceur-ws.org/Vol-3876/paper3.pdf)

---
