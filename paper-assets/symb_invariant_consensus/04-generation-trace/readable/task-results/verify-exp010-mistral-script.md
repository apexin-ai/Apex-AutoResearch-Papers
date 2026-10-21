# verify exp010 mistral script

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_exp010-mistral-script_20260517T052103_result.json`
- **Structured JSON:** [`c8c06a5bcf5b38cf9a3a.json`](../../sessions/c8/c8c06a5bcf5b38cf9a3a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部确认完毕：

**脚本参数** — 已正确修复，无需再改：
- `--max-model-len 8192` ✓
- `--max-tokens 4096` ✓
- 模型路径 `/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3` ✓
- port 8000 ✓
- K=12, T=0.7, 60 problems (30 FOLIO + 30 ProofWriter), seed=42 ✓

**语法检查** — `bash -n` 通过

**模型文件** — 完整（config.json, 3 个 safetensors 分片 + consolidated.safetensors, tokenizer 均在）

状态：**无需修改，可直接启动实验。**

---
