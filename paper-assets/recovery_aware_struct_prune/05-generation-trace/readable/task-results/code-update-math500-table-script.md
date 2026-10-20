# code update math500 table script

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_update_math500_table_script_20260523T204459_result.json`
- **Structured JSON:** [`fc0080a10806e2604839.json`](../../sessions/fc/fc0080a10806e2604839.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建并注册。

**用法**：
- `python artifacts/update_math500_table.py --source registry` — 从 registry.yaml 读指标，生成表格
- `python artifacts/update_math500_table.py --source json --json-dir &lt;path>` — 从本地 JSON 文件读
- 加 `--cross-validate --json-dir &lt;path>` 可交叉核验 registry vs JSON

**当前状态**：20 个实验中 4 个有结果（dense_unpruned, grpo_unpruned, sft_cka_only_20_fixed_v2, sft_rasp_alpha1p0_20_fixed），其余 16 个还在 RUNNING/PREPARING 或未注册。

---
