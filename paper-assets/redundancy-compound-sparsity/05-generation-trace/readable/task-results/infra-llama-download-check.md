# infra llama download check

**When Does KV Redundancy Predict MLP Sparsity? Architecture Dependence of Cross-Axis Signals in Reasoning Inference** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_llama-download-check_20260512T004124_result.json`
- **Structured JSON:** [`375584c78a5dd26cd85d.json`](../../sessions/37/375584c78a5dd26cd85d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

排查完成，结果如下：

---

### 网络排查结果

| 渠道 | 状态 | 说明 |
|------|------|------|
| **HuggingFace** | **不可用** | API 返回 503 Service Unavailable，curl 超时 |
| **ModelScope** | **可用** | API 响应 0.16s，模型 `LLM-Research/Meta-Llama-3.1-8B-Instruct` 存在 |

### 模型文件详情

仓库总大小 29.93 GB，但包含重复格式：
- `consolidated.00.pth`: 14.96 GB（PyTorch 原始格式，可跳过）
- `model-*.safetensors` (4个文件): **14.96 GB**（safetensors 格式，推荐）

只下载 safetensors 格式即可，实际需下载 **~15 GB**。

### 磁盘空间

`/root/autodl-tmp/` 剩余 **221 GB**，充足。

### 推荐下载方式

通过 ModelScope 下载，跳过 `.pth` 文件：

```python
from modelscope import snapshot_download
snapshot_download(
    'LLM-Research/Meta-Llama-3.1-8B-Instruct',
    cache_dir='/root/autodl-tmp/.ms_cache',
    ignore_file_pattern=['*.pth']
)
```

ModelScope CDN 在 AutoDL 上通常 10-50 MB/s，预计 **5-25 分钟**完成。建议用 nohup 后台执行防止 SSH 超时。

---
