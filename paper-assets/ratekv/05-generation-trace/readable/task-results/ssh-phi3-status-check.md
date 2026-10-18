# ssh phi3 status check

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_phi3_status_check_20260515T194308_result.json`
- **Structured JSON:** [`0698c3a795d90a9ea885.json`](../../sessions/06/0698c3a795d90a9ea885.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

### phi3 进程：已死
- 无 phi3 相关进程在运行
- 当前 GPU 0 上跑的是 `run_codellama_hires_profiling.py`（PID 362950）

### 失败原因：模型下载中断
- `phi3_profiling.log` 显示实验卡在模型下载阶段，监控下载 PID 347659
- 从 May 16 00:00 轮询到 00:19 后日志停止，下载监控进程被杀或 SSH 超时断连
- 下载进程（347659）已不存在

### Phi-3 模型文件：不完整
- 需要 6 个 safetensors shards（model-00001 到 model-00006）
- **仅有 shard 5**（`model-00005-of-00006.safetensors`，4.77GB）
- 缺失 shards 1, 2, 3, 4, 6 — 模型不可用，需要重新下载

### GPU 占用
| GPU | 型号 | 显存占用 | 利用率 | 进程 |
|-----|------|---------|--------|------|
| 0 | RTX PRO 6000 Blackwell (98GB) | 17.0/97.9 GB | 100% | CodeLlama profiling |
| 1 | RTX PRO 6000 Blackwell (98GB) | 0/97.9 GB | 0% | 空闲 |

**结论**：phi3_medium_hires_profiling 实验已挂，registry 应更新为 FAILED。重跑前需先完成 Phi-3-medium 模型下载（缺 5/6 shards）。GPU 1 当前空闲可用。

---
