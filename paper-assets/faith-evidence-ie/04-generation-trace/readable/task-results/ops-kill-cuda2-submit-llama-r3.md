# ops kill cuda2 submit llama r3

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_cuda2_submit_llama_r3_20260517T032731_result.json`
- **Structured JSON:** [`e8dbc04b6208c07f93f4.json`](../../sessions/e8/e8dbc04b6208c07f93f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**总结：**
- 死进程 405397 已清理（实际已不存在）
- 第一次提交因 `rsft_data_path` 指向目录而非文件失败，残留进程 408764 占满 cuda:2 导致第二次 OOM
- 已 kill 残留进程，第三次提交成功
- **PID 409565** 在 cuda:2 上运行，占用 17883MiB，训练已开始（0/3312 steps）
- 配置：bf16 + gradient_checkpointing（代码内硬编码） + batch_size=1 × grad_accum=8 = effective_batch=8
- Registry 已更新为 RUNNING

---
