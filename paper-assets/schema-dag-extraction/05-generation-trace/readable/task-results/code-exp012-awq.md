# code exp012 awq

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp012_awq_20260515T160358_result.json`
- **Structured JSON:** [`c5b4f76cf0dca2d6bf51.json`](../../sessions/c5/c5b4f76cf0dca2d6bf51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已下载 7/9 分片 (27.85GB/37GB)。剩余 2 个分片总共约 9.2GB，下载速度约 40-70MB/min。

当前状态汇总：

**已完成的准备工作：**
- 脚本已创建：`/root/schema-dag-extraction/scripts/run_exp012_llama_awq.sh`
- Registry 已注册：`exp012_llama_awq` (status=PREPARING)
- 自动化监控脚本已后台运行 (PID 292859)：等待下载完成后自动启动实验

**下载进度：**
- 模型：`hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4`
- 完成：model-00002, 004, 005, 006, 007, 008, 009 (7/9)
- 进行中：model-00001 (~2.74/4.89GB), model-00003 (~3.03/4.89GB)
- 下载进程：PID 284997 (`huggingface-cli download`)
- 预计完成时间：约 30-60 分钟

**自动化流程：**
下载完成 → 验证 9 个分片 → 自动执行 `run_exp012_llama_awq.sh` → 日志输出到 `/tmp/exp012_awq.log`

**验证命令：**
```bash
# 查看下载进度
tail -5 /tmp/exp012_awq.log

# 查看实验是否已启动
ps aux | grep run_experiment
```

需要注意：`submit_training_job` 工具在当前 MCP 工具集中不可用，因此用 nohup 后台执行作为替代。如果需要等下载完成后手动提交，可以在模型就绪后再操作。

---
