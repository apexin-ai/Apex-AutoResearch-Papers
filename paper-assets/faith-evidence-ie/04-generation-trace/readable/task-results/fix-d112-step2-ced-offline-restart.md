# fix d112 step2 ced offline restart

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_d112_step2_ced_offline_restart_20260519T031916_result.json`
- **Structured JSON:** [`59d8e0bc2e31d9ceb02a.json`](../../sessions/59/59d8e0bc2e31d9ceb02a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇报：

- **旧进程 PID 603844**：已 kill 确认终止
- **新进程 PID 604576**：运行在 GPU 0，占用 1399MiB
- **NLI 模型加载成功**：`cross-encoder/nli-deberta-v3-base` 从本地缓存加载，无网络错误
- **数据**：24216 条记录（3027 unique docs）从 4 个 shard 加载完成
- **修复内容**：脚本中加入 `HF_HUB_OFFLINE=1` + `TRANSFORMERS_OFFLINE=1`，确保离线加载
- **日志**：`/root/autodl-tmp/logs/d112_ced_score.log`

---
