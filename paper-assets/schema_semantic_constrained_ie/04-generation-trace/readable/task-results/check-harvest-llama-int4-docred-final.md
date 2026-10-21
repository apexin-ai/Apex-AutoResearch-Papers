# check harvest llama int4 docred final

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_harvest-llama-int4-docred-final_20260523T071020_result.json`
- **Structured JSON:** [`6376072eda523ba44a5b.json`](../../sessions/63/6376072eda523ba44a5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总报告：

---

## 实验状态汇总

### 1. sf2_llama_int4_docred_s1 — ✅ DONE

| 指标 | 值 |
|------|-----|
| DR% | **0.00** |
| CF% | 0.22 (8 violations) |
| ET% | 0.00 |
| RV% | 0.00 |
| R-F1 | **48.04** (P=44.79, R=51.80) |
| E-F1 | **84.18** (P=85.50, R=82.90) |
| #pred | 3669 entities, 2997 relations |
| Parse Fail | 5/200 (2.5%) |

Registry 已更新到 DONE (conclusion=success)。

### 2. sf2_qwen_int4_docred_s1 — 🔄 Running

- 进度：**123/200** docs (61.5%)
- 服务器：westd-16980, cuda:0
- 运行时间：~1h17m
- 模型刚加载完成（log 显示 AWQ Marlin kernel 加载），正在推理中

### 3. eval_70b_lora_docred_200_full_s2 — 🔄 Running

- 进度：**178/200** docs (89%)
- 服务器：westd-21461, cuda:1
- 运行时间：~6h30m
- 预计剩余：~50min（按当前速度）

### 4. sf2_70b_prompt_sensitivity — 🔄 Running

- 结构：2 prompt variants (minimal, detailed) × 2 modes (constrained, unconstrained) = **4 runs**，每 run 551 SciERC samples
- 当前：第 1/4 run (minimal_constrained) **544/551** (98.7%)
- 服务器：westd-21461, cuda:0
- 运行时间：~1h29m
- 预计总时间：~6h（4 runs × ~1.5h each）

---
