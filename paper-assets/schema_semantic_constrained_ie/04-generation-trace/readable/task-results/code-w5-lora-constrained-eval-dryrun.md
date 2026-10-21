# code w5 lora constrained eval dryrun

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_w5_lora_constrained_eval_dryrun_20260515T154837_result.json`
- **Structured JSON:** [`851626cfa897491c8f67.json`](../../sessions/85/851626cfa897491c8f67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Dry-Run 结果

| 项目 | 结果 |
|------|------|
| **状态** | 成功，2/2 samples，0 failures |
| **模型加载** | ~3s（4 shards） |
| **推理时间** | Sample 1: 4.1s（E=4, R=3），Sample 2: 1.3s（E=2, R=1） |
| **Grammar** | XGrammar + TypeConstraintProcessor 正常编译（"Grammar compiled (full schema)"） |
| **GPU 0 显存** | 已释放（0 MiB），进程退出即自动清理 |

**Warnings**（均无影响）：
- Mistral regex pattern warning（Qwen tokenizer 的已知误报）
- `torch_dtype` deprecated 提示
- generation flags `['temperature', 'top_p', 'top_k']` may be ignored

**注意**：实际执行用的 GPU 0（因为 GPU 1 被 DocRED constrained eval PID 276937 占用）。原 unconstrained eval PID 278385 已不存在。

---
