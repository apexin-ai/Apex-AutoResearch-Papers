# code plan 013 model expansion

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_013_model_expansion_20260521T080609_result.json`
- **Structured JSON:** [`84d7e127c1279bb3012e.json`](../../sessions/84/84d7e127c1279bb3012e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成总结

**模型探测结果**：

| Model | Status | Tool Calling |
|---|---|---|
| google/gemini-2.5-flash | OK | OK |
| google/gemini-2.5-pro | OK | No (text only) |
| meta-llama/llama-4-maverick | OK | No (proxy不支持) |
| meta-llama/llama-4-scout | OK | OK |
| mistralai/mistral-large-2411 | OK | 未测 |
| 其余候选 | 不可用 | - |

**选定模型**：Gemini-2.5-Flash (Google) + LLaMA-4-Scout (Meta)

**实验结果**（各 500 episodes = 250 clauses × 2 conditions，judge = GPT-5.4）：

| | Gemini-2.5-Flash | LLaMA-4-Scout |
|---|---|---|
| Amb violation rate | 37.6% | 37.6% |
| Unamb violation rate | 4.0% | 17.6% |
| Delta (pp) | **+33.6** | **+20.0** |
| p-value | <0.0001 | <0.0001 |
| **C1 replicates** | **YES** | **YES** |
| **C2 rank correlation** | **0.700** | -0.200 |
| Top types | lexical > incompleteness > scopal | incompleteness > auth_scope > lexical |

**结论**：
- **C1（二元歧义效应）在两个新模型家族上均成功复现**，效应显著（p<0.0001），Gemini 效应更强（+33.6pp vs +20.0pp）
- **C2（类型层级）**：Gemini 与参考排序有较强正相关（ρ=0.700），LLaMA 的类型排序与参考排序不一致（ρ=-0.200），表明类型层级的泛化性有限

输出文件位于 `artifacts/model_expansion/{gemini-2.5-flash,llama-4-scout}/` 下，含 `episodes.jsonl`、`judgments.jsonl`、`analysis.json`。

---
