# ops spatial pipeline v2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_spatial-pipeline-v2_20260521T182916_result.json`
- **Structured JSON:** [`5b694fc2bdb76b8b6e02.json`](../../sessions/5b/5b694fc2bdb76b8b6e02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Phase 1 状态**：
- 6 个 shard (s0-s5) 仍在运行，shard6 **从未启动**（服务器只有 6 GPU）
- 进度：shard0 已到 7400/8608 (~86%)，速度 2.27s/sample，ETA ~46 分钟
- 这与历史 object cache 同样配置（6/7 shards），预计 merge 后 n_samples ≈ 51,648
- ⚠️ **51,648 / 60,250 = 85.7%**，**低于 90% 阈值 (54,225)**

已设置 5 分钟后轮询。如果合并后样本数确实低于 90%，会停止并报告。

---
