# cleanup westd disk urgent

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cleanup_westd_disk_urgent_20260522T141211_result.json`
- **Structured JSON:** [`020f68907b7af918108d.json`](../../sessions/02/020f68907b7af918108d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

**结果：释放 ~77GB，磁盘从 100%（4K 可用）降至 89%（77GB 可用）。**

清理明细：
- optimizer.pt × 6：~78.3GB（5×15G + 1×3.3G）— 主要贡献
- completions parquet：~2MB（很小）
- wandb/：97MB
- training_args.bin + rng_state：微量

α=3.0 eval 和 seed123 eval 现在有足够空间写结果，不会 crash。

---
