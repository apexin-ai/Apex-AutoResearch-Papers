# fix c3 llama cli flags

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_c3_llama_cli_flags_20260514T145214_result.json`
- **Structured JSON:** [`a16a9d49da4f1aec51ca.json`](../../sessions/a1/a16a9d49da4f1aec51ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：**

- `run_profiling.py` 默认值 `max_new_tokens=2048`（L564）、`min_phase_length=10`（L572），与 bf16 实验完全一致
- `run_c3_llama_full.sh` 不显式传参时使用的就是这些默认值，**无需修复，数据可比**
- pdflatex 124224 已退出，无需处理
- registry 已更新验证记录

---
