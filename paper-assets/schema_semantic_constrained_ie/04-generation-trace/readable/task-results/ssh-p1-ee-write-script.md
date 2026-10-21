# ssh p1 ee write script

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p1_ee_write_script_20260518T202112_result.json`
- **Structured JSON:** [`b6f6093030b34bcbe010.json`](../../sessions/b6/b6f6093030b34bcbe010.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果汇总：**

- 所有 4 个脚本均存在：`train_lora_wikievents.py`、`run_constrained_extraction.py`、`eval_event_extraction.py`、`violation_checker_wikievents.py`
- 测试数据：`data/wikievents/test.jsonl`
- Constraints：`data/wikievents/ontology_constraints_wikievents.json`
- 模型 Qwen/Qwen3-8B 已缓存在 HF hub
- 环境验证通过：Python 3.12.3, torch 2.8.0+cu128, CUDA OK, 2 GPUs

**脚本已写入** `/root/schema_semantic_constrained_ie/scripts/run_p1_ee_ft.sh`，包含 5 步：Training → Unconstrained Inference → Constrained Inference (full_s1) → Eval → Violation Check。无缺失文件，所有步骤均可执行。

**产出报告** 已写入 `artifacts/p1_ee_script_setup.md`。

---
