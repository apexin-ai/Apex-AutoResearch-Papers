# ops disk cleanup merge

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-merge_20260516T175215_result.json`
- **Structured JSON:** [`f97e8614000ccdec8c12.json`](../../sessions/f9/f97e8614000ccdec8c12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

### 产出汇报

| 项目 | 结果 |
|------|------|
| (a) 释放空间 | **~43GB**（5.1GB → 49GB，merge 后净余 43GB） |
| (b) d005 merge | **成功** — 2 个 safetensors (4.7G + 1.4G = 6.1G)，含 tokenizer |
| (c) 当前剩余 | **43GB 可用**（≥20GB for d100 ✓） |

清理明细：
- alpha=16 checkpoints (Qwen2.5-3B_d100/d025/d100_s123 + v2_s42/v2_s123): ~3GB
- starcoder2-3b cache: 12GB
- Qwen3-8B: 16GB
- Qwen3-14B-AWQ: 9.4GB
- open_hermes-2.5 dataset: 1.7GB
- 旧日志 + /tmp CSVs + d005 残留 merged/: ~1GB

---
