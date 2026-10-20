# code d049 awq download

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d049_awq_download_20260518T102640_result.json`
- **Structured JSON:** [`41f82b15a8af78278937.json`](../../sessions/41/41f82b15a8af78278937.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

| 项目 | 状态 |
|------|------|
| FP16 下载 | 已 kill 并清理 |
| autoawq | v0.2.9 安装成功，导入 OK（有 deprecation warning，不影响使用） |
| AWQ-INT4 下载 | **已启动**，repo: `LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4`（ModelScope） |
| 模型大小 | 19 文件，9 个 safetensors（每个 ~4.5GB），总计 ~40GB |
| 预计下载时间 | ~40-60 分钟（8 个 shard 并行下载，每个 ~1-2MB/s） |
| transformers | v5.8.1，远超 4.35，**支持 AWQ 自动加载**，可直接用 `AutoModelForCausalLM.from_pretrained(path, device_map='auto')` |
| 磁盘空间 | 202GB 可用，充足 |

注：HuggingFace 在该服务器上不可达，最终从 ModelScope 镜像 `LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4` 下载。

---
