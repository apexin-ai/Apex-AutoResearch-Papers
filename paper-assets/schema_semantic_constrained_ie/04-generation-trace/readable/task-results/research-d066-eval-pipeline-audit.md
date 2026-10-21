# research d066 eval pipeline audit

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_d066_eval_pipeline_audit_20260520T135155_result.json`
- **Structured JSON:** [`a7462f21322c8004780b.json`](../../sessions/a7/a7462f21322c8004780b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。下面是审计报告。

---

## d066 Beam Sweep Eval 管道审计报告

### 1. 已有 eval 结果用的是哪个管道？

**westd-21461** 上的 8 个 `eval_beam*.json` 文件（Qwen SciERC beam 1/2/4/8 × con/unc）**全部由 eval_d064.py 生成**。判断依据：
- JSON 结构匹配 eval_d064.py 输出格式（`CF_pct`, `cf_violations`, `avg_inference_time` 等字段）
- CF 数字一致：beam1 con CF=0.5% (9 violations) — 和 eval_d064.py 的 per-unique-entity 计数匹配

**westd-16980 上无任何 eval JSON 文件**——DocRED 输出尚未跑 eval。

两台服务器的 `violations/` 目录下有 violation_checker 的输出（westd-21461: 8 个 SciERC 文件，westd-16980: 4 个 Qwen DocRED 文件），但这些**仅供参考，不应用于论文数据**。

### 2. beam_sweep_table.tex 数据来源验证

表中所有数字与 eval_d064.py 输出**完全吻合**：

| 配置 | 表 E-F1 | eval E-F1 | 表 R-F1 | eval R-F1 | 表 DR | eval DR | 表 CF | eval CF |
|------|---------|-----------|---------|-----------|-------|---------|-------|---------|
| k=1 unc | 66.88 | 66.88 | 42.95 | 42.95 | 2.11 | 2.11 | 0 | 0.0 |
| k=1 con | 66.88 | 66.88 | 42.95 | 42.95 | 0 | 0.0 | 0.50 | 0.5 |
| k=2 unc | 67.79 | 67.79 | 44.75 | 44.75 | 1.54 | 1.54 | 0 | 0.0 |
| k=2 con | 67.71 | 67.71 | 44.60 | 44.60 | 0 | 0.0 | 0.11 | 0.11 |
| k=4 unc | 67.49 | 67.49 | 43.72 | 43.72 | 1.89 | 1.89 | 0 | 0.0 |
| k=4 con | 67.22 | 67.22 | 43.60 | 43.60 | 0 | 0.0 | 0 | 0.0 |
| k=8 unc | 66.40 | 66.40 | 43.17 | 43.17 | 1.77 | 1.77 | 0 | 0.0 |
| k=8 con | 66.36 | 66.36 | 43.65 | 43.65 | 0 | 0.0 | 0 | 0.0 |

**表数据来自 eval_d064.py，无需重跑 SciERC 部分。**

### 3. eval_d064.py vs violation_checker CF 计算差异

| | eval_d064.py | violation_checker.py |
|---|---|---|
| **CF 来源** | 仅从 **relation 的 head_type/tail_type** 收集 entity→type 映射 | 从 **entities 列表 + relation head_type/tail_type** 两处合并 |
| **计数粒度** | per-unique-entity（同一 mention 算 1 次冲突） | per-unique-mention（同上，但来源更多所以冲突更多） |
| **分母** | `total_entities_pred` | `total_pred_entities`（相同） |
| **beam1 con 结果** | **9 violations, CF=0.5%** | **24 violations, CF=1.34%** |

**根因**：violation_checker 将 entity list 的类型标注与 relation 的 head/tail 类型合并，因此捕获了 entity list 标注 "Task" 但 relation 中标注 "Generic" 这类**跨字段不一致**。eval_d064.py 仅看 relation 内部的类型标注，所以少了 entity list 与 relation 之间的冲突。

**DR/ET/RV 对比**：两者逻辑基本一致（eval_d064.py 用简单 alias 归一化，violation_checker 多了 fuzzy match + Levenshtein），数字相同或极接近。差异仅在 CF。

### 4. 所有 d066 JSONL 文件清单

**westd-21461:**

| 文件 | 行数 | 完整? | 有 eval? | 管道 |
|------|------|-------|---------|------|
| qwen_scierc_beam1_full_s1.jsonl | 551 | ✅ | ✅ eval_beam1_con.json | eval_d064 |
| qwen_scierc_beam1_unconstrained.jsonl | 551 | ✅ | ✅ eval_beam1_unc.json | eval_d064 |
| qwen_scierc_beam2_full_s1.jsonl | 551 | ✅ | ✅ eval_beam2_con.json | eval_d064 |
| qwen_scierc_beam2_unconstrained.jsonl | 551 | ✅ | ✅ eval_beam2_unc.json | eval_d064 |
| qwen_scierc_beam4_full_s1.jsonl | 551 | ✅ | ✅ eval_beam4_con.json | eval_d064 |
| qwen_scierc_beam4_unconstrained.jsonl | 551 | ✅ | ✅ eval_beam4_unc.json | eval_d064 |
| qwen_scierc_beam8_full_s1.jsonl | 551 | ✅ | ✅ eval_beam8_con.json | eval_d064 |
| qwen_scierc_beam8_unconstrained.jsonl | 551 | ✅ | ✅ eval_beam8_unc.json | eval_d064 |
| llama_docred_200_beam1_full_s1.jsonl | 140 | ❌ | ❌ | — |
| llama_docred_200_beam1_unconstrained.jsonl | 200 | ✅ | ❌ | — |
| llama_scierc_beam1_unconstrained.jsonl | 275 | ❌ | ❌ | — |

**westd-16980:**

| 文件 | 行数 | 完整? | 有 eval? | 管道 |
|------|------|-------|---------|------|
| qwen_docred_200_greedy_s1.jsonl | 200 | ✅ | ❌ | — |
| qwen_docred_200_greedy_unc.jsonl | 200 | ✅ | ❌ | — |
| qwen_docred_200_beam2_full_s1.jsonl | 200 | ✅ | ❌ | — |
| qwen_docred_200_beam2_unconstrained.jsonl | 200 | ✅ | ❌ | — |
| qwen_docred_200_beam8_full_s1.jsonl | 200 | ✅ | ❌ | — |
| qwen_docred_200_beam8_unconstrained.jsonl | 200 | ✅ | ❌ | — |
| llama_docred_200_beam2_full_s1.jsonl | 200 | ✅ | ❌ | — |
| llama_docred_200_beam2_unconstrained.jsonl | 200 | ✅ | ❌ | — |
| llama_docred_200_beam8_full_s1.jsonl | 200 | ✅ | ❌ | — |
| llama_docred_200_beam8_unconstrained.jsonl | 200 | ✅ | ❌ | — |
| llama_docred_200_beam4_unconstrained.jsonl | 110 | ❌ | ❌ | — |

### 5. 结论

- **SciERC beam sweep 表（tab:beam-sweep）数据来自 eval_d064.py，无需重跑。**
- **westd-16980 上 10 个完整的 DocRED JSONL 文件** 如需入表，需要用 eval_d064.py 跑 eval（当前完全没有 eval 结果）。
- 3 个未完成文件（llama_docred beam1 s1 = 140行, llama_scierc beam1 unc = 275行, llama_docred beam4 unc = 110行）需先完成推理再 eval。
- violation_checker 的 violations/ 目录输出**仅供调试参考，不应用于论文数字**。

---
