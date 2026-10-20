# ssh p1 qwen ee ft r5 schema fix

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p1_qwen_ee_ft_r5_schema_fix_20260518T232915_result.json`
- **Structured JSON:** [`24b1b129e2e16ea9158a.json`](../../sessions/24/24b1b129e2e16ea9158a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## D060 执行结果

### 代码修改
1. **`compiler/ontology_compiler.py:294`** — `"required": ["entities", "events"]` → `"required": ["events"]`
2. **`run_constrained_extraction.py:808`** — 添加 `--repetition_penalty` CLI 参数，通过 `sampling_kwargs` 传入所有 `model.generate()` 调用

### 结果（WikiEvents 20 docs, Qwen3-8B FT, repetition_penalty=1.2）

| Metric | Unconstrained | Full S1 (Constrained) |
|--------|:---:|:---:|
| Parse Rate | 85% | **95%** |
| Trigger F1 | **32.08** | 26.72 |
| Argument F1 | 7.85 | **8.18** |
| RoV (role violations) | 38.31% | **0%** |
| AC (arg constraint) | 2.68% | **0%** |
| Go/NoGo | 41% | **0%** |

Schema 修复彻底解决了 EE FT parse failure。Constrained decoding 将 RoV+AC violation 从 41% 降至 0%，parse rate 从 ~0%（修复前）提升到 95%。Artifact 已注册，registry 已更新为 DONE/success。

---
