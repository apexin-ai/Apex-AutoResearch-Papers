# prep codellama 13b shard2 fix

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_codellama-13b-shard2-fix_20260516T084702_result.json`
- **Structured JSON:** [`5db51c1b68e4cc2fae44.json`](../../sessions/5d/5db51c1b68e4cc2fae44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成报告

| 项目 | 结果 |
|------|------|
| Shard 1 | 9.3GB ✓ |
| Shard 2 | 9.3GB ✓（已修复，ModelScope 下载） |
| Shard 3 | 5.8GB ✓ |
| 3 shard 合计 | 24.4GB ✓ |
| Dry-run | DRY_RUN_OK — Vocab=32016, LlamaForCausalLM, Hidden=5120, Layers=40 |

Shard 2 修复成功。HuggingFace 因 xethub 超时失败，ModelScope 国内 CDN（不走 network_turbo 代理）约 20 分钟下载完成。

---
