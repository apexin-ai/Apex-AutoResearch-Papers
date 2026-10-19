# ops watcher and m1 check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_watcher-and-m1-check_20260516T023236_result.json`
- **Structured JSON:** [`185c1b10c334399ca72d.json`](../../sessions/18/185c1b10c334399ca72d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. Watcher PID 966920: **ALIVE**
- 运行时间：1天11小时
- 脚本：`/root/structfuse/watch_and_chain_qwen_s42.sh`
- 逻辑：监视 Qwen s43+ 队列（PID 337267），完成后自动触发 `run_m2_s42_supplement.sh --encoder qwen --gpu cuda:0`
- tmux session：`qwen_s42_watcher`
- 另外还有一个 StarCoder s42 watcher（PID 20226，`watch_and_chain_starcoder_s42.sh`）也在运行

### 2. m1_reextract_v2: **82/82 repos，moto 250/536 (46.6%)**
- 进度从上次的 200/536 → 现在 250/536（07:02 记录）
- 速率：~50 instances / 4小时
- 剩余 286 instances，**ETA ≈ May 17 ~10:00**
- ⚠️ CodeQL call_graph.ql 对 moto 大量实例报 exit status 33（每5分钟一次），但这是 WARNING 不影响整体推进——批处理仍在继续处理其他实例
- all.jsonl: 44,173 行（稳定）
- skip_log: 582 条

### 3. BM25 watcher: **不存在**
- 无 BM25 相关 tmux session 或进程
- 当前 tmux sessions：`m1_reextract_v2`、`m2_full_starcoder`、`m2_qwen_s43`、`qwen_s42_watcher`

---
