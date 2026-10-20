# code mvp seed0 replication

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp_seed0_replication_20260514T003407_result.json`
- **Structured JSON:** [`343226c366ba2cff215d.json`](../../sessions/34/343226c366ba2cff215d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**磁盘空间不足，实验无法启动。**

当前状态：
- `/root/autodl-tmp` 总共 250GB，仅剩 7GB
- `output_v7/`: 92GB（每个 G 有 5 个训练 checkpoint × 5.7GB = ~28.5GB/G）
- `.hf_cache/`: 67GB

seed0 实验需要类似的 ~90GB 空间。

**建议：删除 v7 的中间训练 checkpoints**（checkpoint-76/152/228/304），保留 checkpoint-305 和 final_model。每代省 ~23GB，3 代共省 ~69GB。加上现有 7GB → ~76GB 可用。

如果还不够，可以进一步删除 checkpoint-305（因为 final_model 已是最终权重的独立副本），3 代再省 17GB → ~93GB。

要删哪些？还是你有其他方案？

---
