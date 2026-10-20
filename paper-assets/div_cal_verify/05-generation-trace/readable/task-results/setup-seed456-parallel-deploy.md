# setup seed456 parallel deploy

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_seed456_parallel_deploy_20260514T072443_result.json`
- **Structured JSON:** [`90bdfde5b517c86384e9.json`](../../sessions/90/90bdfde5b517c86384e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部部署完成，验证通过。

### 产出确认

1. **chain_cuda0_seed456.sh 已修改** — 只保留 uncurated→rgds，random50 已移除
2. **chain_cuda1_seed456.sh 已创建** — cuda:1 跑 random50_seed456
3. **auto_seed456_cuda1 tmux session 已启动** — 正在等待 medium_external_seed456 完成

### 修改后时间线

当 `medium_external_seed456` 完成后：

| GPU | 任务 | 预估时间 |
|-----|------|---------|
| cuda:0 | uncurated_seed456 → rgds_seed456 | ~6-7h（原串行 3 任务约 10h，去掉 random50 后） |
| cuda:1 | random50_seed456 | ~3-3.5h |

两卡并行，总耗时从原来的 ~10h 降至 ~6-7h（取决于 cuda:0 上两个任务的实际时长）。

---
