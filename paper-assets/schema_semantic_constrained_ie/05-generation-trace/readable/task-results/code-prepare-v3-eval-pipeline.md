# code prepare v3 eval pipeline

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare_v3_eval_pipeline_20260518T080405_result.json`
- **Structured JSON:** [`c6b9a57997adf17919dc.json`](../../sessions/c6/c6b9a57997adf17919dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 脚本文件和参数

| 项目 | 值 |
|---|---|
| violation checker | `violation_checker_wikievents.py` |
| 参数 | `--input_path &lt;file> --constraints_path data/wikievents/ontology_constraints_wikievents.json` |
| eval 脚本 | `eval_event_extraction.py` |
| 参数 | `--input_path &lt;file>` |

### run_v3_eval.sh

已部署到两台服务器 `/root/schema_semantic_constrained_ie/run_v3_eval.sh`，内容已确认正确。

### v3 当前进度 (目标 246 lines)

**westd-16980:**

| 实验 | 行数 | 进度 |
|---|---|---|
| qwen v3 constrained full | 98/246 | 39.8% |
| mistral v3 constrained full | 6/246 | 2.4% |
| mistral grammar_only v3 | 68/246 | 27.6% |

**westd-21461:**

| 实验 | 行数 | 进度 |
|---|---|---|
| llama v3 constrained full | 51/246 | 20.7% |
| mistral v3 constrained full | 66/246 | 26.8% |
| qwen v3 constrained full | 6/246 | 2.4% |

注意：mistral v3 constrained full 在两台机器上都有输出（16980: 6 行, 21461: 66 行），可能存在重复运行或分配问题，需要确认哪台是主跑。

---
