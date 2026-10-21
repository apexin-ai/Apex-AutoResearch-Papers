# ops westb cleanup verify eval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb_cleanup_verify_eval_20260520T103030_result.json`
- **Structured JSON:** [`f4ea6ff3744e449a711d.json`](../../sessions/f4/f4ea6ff3744e449a711d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个进程均在运行。

## 总结

| 项目 | 结果 |
|------|------|
| **optimizer.pt 清理** | 文件已不存在（之前已清理），无额外释放 |
| **磁盘剩余** | /root/autodl-tmp/ 9.8G 可用 (97%) |
| **Standard checkpoint-935** | 完好，339 tensors，12.3GB |
| **CKA-only checkpoint-935** | 完好，339 tensors，12.3GB |
| **eval 提交 - CKA-only** | `eval_gsm8k_sft_qwen_cka_only_20`，westb:0，PID 14636 |
| **eval 提交 - Standard** | `eval_gsm8k_sft_qwen_standard_20`，westb:1，PID 14714 |
| **Standard v2 registry** | 已标记 DONE/failed |

---
