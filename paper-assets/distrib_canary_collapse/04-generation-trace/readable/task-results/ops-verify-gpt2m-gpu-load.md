# ops verify gpt2m gpu load

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-gpt2m-gpu-load_20260515T120226_result.json`
- **Structured JSON:** [`f54074f219d33863ffd1.json`](../../sessions/f5/f54074f219d33863ffd1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**根因确认：**

`/root/autodl-tmp/models/gpt2-medium/` 下所有文件都是**断裂的符号链接**——指向 `/root/autodl-tmp/.hf_cache/models--gpt2-medium/snapshots/6dcaa7a...`，但该目录不存在。HF cache 实际结构在 `.hf_cache/hub/` 下，不是直接在 `.hf_cache/` 下。

下载时用了 `huggingface-hub` 的 `snapshot_download(local_dir=...)` 创建了符号链接，但 `HF_HOME=/root/autodl-tmp/.hf_cache` 导致 blob 存储路径为 `.hf_cache/hub/models--gpt2-medium/...`，而符号链接指向的是 `.hf_cache/models--gpt2-medium/...`（少了 `hub/` 层级）。

**修复方案**：重新下载模型，这次不用符号链接，直接用 `local_dir` + `local_dir_use_symlinks=False`：

```python
from huggingface_hub import snapshot_download
snapshot_download("gpt2-medium", local_dir="/root/autodl-tmp/models/gpt2-medium", local_dir_use_symlinks=False)
```

或者直接删掉当前目录，让 `AutoTokenizer.from_pretrained` 指向 HF cache 中的正确路径：`/root/autodl-tmp/.hf_cache/hub/models--gpt2-medium/snapshots/...`。

需要我执行修复吗？

---
