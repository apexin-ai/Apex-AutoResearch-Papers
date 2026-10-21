# ops submit llama ced scoring

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submit_llama_ced_scoring_20260517T013924_result.json`
- **Structured JSON:** [`8e6b5dfef5c3c2fbfde8.json`](../../sessions/8e/8e6b5dfef5c3c2fbfde8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务正常运行中（PID 398949，CPU 129%，已运行 1:36）。CED scoring 是 CPU 密集型的 NLI 推理过程，23704 条记录处理需要一段时间，日志可能在批量打分完成后才输出进度。

**总结**：
- cuda:2 空闲已确认 ✓
- 候选文件 23704 行 ✓
- NLI 模型加载成功（cuda:2, 1425MB）✓
- tmux session `plan_016_llama_ced_scoring` 正在运行
- 参数：`--scoring_mode ced --tau 0.5 --selection_strategy top_k --top_k 3`
- 输出路径：`/root/autodl-tmp/rsft_scored_llama_3_1_8b`
- 日志：`/root/autodl-tmp/plan_016_llama_ced_scoring.log`

---
