# analysis llama docred dr residual

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama_docred_dr_residual_20260515T063059_result.json`
- **Structured JSON:** [`cef5092dc2e7fcc4d4f2.json`](../../sessions/ce/cef5092dc2e7fcc4d4f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成并注册。核心发现：

**418 residual DR violations (2.55%)** 的结构化分析：

1. **Top-10 relations 占 63.9% violations** — P1001 (jurisdiction, 45), P31 (instance of, 37), P607 (conflict, 30) 居前三
2. **Tightness 与残余 DR 无相关性** — Spearman rho=0.069, p=0.52。约束系统在松紧不同的 relation 上均有效，残余 violation 不是 schema 太紧导致的
3. **三类残余成因**：entity type ambiguity (forward coreference)、temporal role confusion、type granularity mismatch — 均为 greedy left-to-right decoding 的天然局限
4. **Llama 大幅优于 Qwen** — 91.7% vs 53.3% 相对降幅，42/94 relations 零违规
5. **Rebuttal 核心论点**：残余 2.55% 是 non-local dependency 的结构性下界，不可通过 local constraint 消除；tau(r) 无相关证明约束系统 uniformly effective

报告路径：`artifacts/llama_docred_full_s1/report/dr_residual_analysis.md`

---
