# prep llama dryrun validation

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_llama_dryrun_validation_20260514T104336_result.json`
- **Structured JSON:** [`f7f192bbcb77e34aab7a.json`](../../sessions/f7/f7f192bbcb77e34aab7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

1. **Fallback counter 已确认**：`type_mask_processor.py` L204/387-399，服务器代码已包含
2. **Unconstrained dry-run 通过**：1 sample, E=5 R=1, 4.6s
3. **Full_s1 dry-run 通过**：1 sample, E=5 R=1, 5.4s，触发 2 次 grammar-first fallback
4. **提交命令已写入** `artifacts/llama_submit_commands.md`，含 nohup + log 重定向，方便后续提取 fallback count

注意：fallback count 仅输出到 stderr，不写入 JSONL。正式跑时需用 `> log 2>&1` 保留日志。

---
