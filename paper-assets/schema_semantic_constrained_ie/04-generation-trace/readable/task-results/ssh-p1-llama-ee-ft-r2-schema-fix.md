# ssh p1 llama ee ft r2 schema fix

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p1_llama_ee_ft_r2_schema_fix_20260518T232932_result.json`
- **Structured JSON:** [`8127d97082d52772137e.json`](../../sessions/81/8127d97082d52772137e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## 执行摘要

### 修改内容
1. **Schema fix** (`compiler/ontology_compiler.py:294`): `required: ["entities", "events"]` → `required: ["events"]`
2. **repetition_penalty** (`run_constrained_extraction.py`): 新增 `--repetition_penalty` CLI 参数 (lines 808, 938-941)
3. **Eval/violation 兼容** (`eval_event_extraction.py`, `violation_checker_wikievents.py`): 处理 unconstrained 模式下 arguments 为 string 的情况
4. **Peft monkey-patch**: 训练脚本已有，推理脚本不 import peft，无需处理

### 结果

| Metric | Unconstrained | Constrained (full_s1) |
|--------|:---:|:---:|
| Parse Rate | 100% | 100% |
| Trigger F1 | 0.2752 | 0.2691 |
| Argument F1 | 0.0998 | 0.0891 |
| RoV | 8.8% | **0.0%** |
| AC | 3.5% | **0.8%** |
| Go/No-go | 12.2% | **0.78%** |

Schema fix 解决了 R1 的 100% parse failure。Constrained decoding 将 Go/No-go 从 12.2% 降至 0.78% (15.6x improvement)。Artifact 已注册，registry 已更新为 DONE/success。

---
