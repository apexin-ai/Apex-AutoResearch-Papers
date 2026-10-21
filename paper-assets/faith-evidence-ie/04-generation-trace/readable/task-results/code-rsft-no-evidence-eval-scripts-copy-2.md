# code rsft no evidence eval scripts

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_rsft_no_evidence_eval_scripts_20260519T122513_result.json`
- **Structured JSON:** [`470fb91398a168d8752b.json`](../../sessions/47/470fb91398a168d8752b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已创建，语法检查通过，所有路径已验证存在。

| 脚本 | 路径 |
|---|---|
| 4B | `scripts/seed_expansion/eval_4b_rsft_no_evidence.sh` |
| 8B | `scripts/seed_expansion/eval_8b_rsft_no_evidence.sh` |

**注意**：4B RSFT s42 checkpoint 不存在，使用了 s44 (`rsft_output_4b_sft_s44`)。8B RSFT s42 (`rsft_output_qwen3_8b_k1`) 正常。两个脚本均遵循 1.7B 模板格式，包含 `--no_evidence` 和 `--no-quantize`，未实际执行。

---
