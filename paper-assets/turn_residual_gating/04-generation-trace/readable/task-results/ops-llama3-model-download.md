# ops llama3 model download

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama3_model_download_20260519T071642_result.json`
- **Structured JSON:** [`06a27c995879c4d554c0.json`](../../sessions/06/06a27c995879c4d554c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**下载状态报告：**

| 项目 | 状态 |
|------|------|
| **下载进程 PID** | 45803 |
| **下载状态** | 进行中 — 正在下载 4 个 safetensors 分片（model-00003 at 1%, model-00004 刚开始） |
| **已下载文件** | config.json, tokenizer.json, tokenizer_config.json, generation_config.json, model.safetensors.index.json, LICENSE 等元数据文件已就位 |
| **模型分片** | 尚未出现在目标目录（modelscope 先下载到临时目录，完成后移入） |
| **下载速度** | ~6 MB/s |
| **预计剩余时间** | ~40 分钟（总计约 16GB，4 个分片） |
| **GPU 影响** | 无 — GPU 显存 0 MiB，利用率 0%，LoRA 训练不受影响 |

下载已在后台稳定运行（nohup），可通过以下命令随时检查：
- 进度：`tail -5 /root/turn_residual_gating/llama_download.log`
- 进程：`ps -p 45803`
- 完成后验证：`ls -lh /root/.cache/modelscope/hub/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/model*.safetensors`

---
