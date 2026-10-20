# code scp llama model and launch v3

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_scp_llama_model_and_launch_v3_20260518T072523_result.json`
- **Structured JSON:** [`54a3a8ced48e5b7c9762.json`](../../sessions/54/54a3a8ced48e5b7c9762.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成，汇总：

| Step | 结果 |
|------|------|
| **Step 1** | westd-21461 旧模型已清理 |
| **Step 2** | westd-16980 模型 15G，4 个 safetensors 分片完整 |
| **Step 3** | 方案 A 失败（16980→21461 不通），方案 B 变体成功：从 21461 拉取 16980（21461 有 16980 的 SSH config），速度 ~500MB/s |
| **Step 4** | westd-21461 模型 15G，文件字节数完全一致；Python 验证通过：**Model loaded OK, params: 8,030,261,248** |
| **Step 5** | `type_mask_processor.py` = 938 行 ✓；**PID=9486**（实际 python 进程 PID=9491） |
| **Step 6** | GPU 1 占用 **18,268 MiB**，利用率 88%；输出文件已生成（30KB，正在写入）；日志显示模型加载完成，已开始 constrained generation |

---
