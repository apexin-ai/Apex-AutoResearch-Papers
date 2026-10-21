# ops gpt2m dryrun and cleanup

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpt2m-dryrun-and-cleanup_20260515T120520_result.json`
- **Structured JSON:** [`aa81a2f668ed77730ac2.json`](../../sessions/aa/aa81a2f668ed77730ac2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**PASS**。结果汇总：

- 断裂 symlink `/root/autodl-tmp/models/gpt2-medium/` 已清理
- HF cache 完整（snapshot `6dcaa7a`, 1.5G）
- dry-run 通过：tokenizer vocab=50257, params=354,823,168
- 可以用 `--model_name gpt2-medium` + `HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1` 提交训练

---
