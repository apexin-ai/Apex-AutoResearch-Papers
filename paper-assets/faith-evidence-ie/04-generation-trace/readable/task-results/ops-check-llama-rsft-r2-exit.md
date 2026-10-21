# ops check llama rsft r2 exit

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_llama_rsft_r2_exit_20260516T145541_result.json`
- **Structured JSON:** [`1633ac9002fffc01e682.json`](../../sessions/16/1633ac9002fffc01e682.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：plan_016_llama_rsft_candidates_r2 失败。**

- 进程在 cuda:1 上运行约 23 分钟后被外部终止（无 Python traceback/error）
- 仅完成 64/3027 docs（2.1%），生成 512 行
- 大概率 OOM：8B 模型加载时日志已提示 "We will use 90% of the memory on device 0"，但实际设置的是 CUDA_VISIBLE_DEVICES=1，显存紧张
- Registry 已更新为 DONE/failed，cron 已删除

---
