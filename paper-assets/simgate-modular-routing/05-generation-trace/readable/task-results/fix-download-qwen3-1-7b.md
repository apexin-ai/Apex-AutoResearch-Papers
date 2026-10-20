# fix download qwen3 1 7b

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_download-qwen3-1_7b_20260514T054327_result.json`
- **Structured JSON:** [`562c59dbe6e7fb6c0d21.json`](../../sessions/56/562c59dbe6e7fb6c0d21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型已就绪，汇总如下：

**模型已存在，无需重新下载。**

| 项目 | 结果 |
|------|------|
| **本地路径** | `/root/autodl-tmp/models/Qwen/Qwen3-1.7B` (符号链接 → `Qwen3-1___7B/`) |
| **大小** | 3.8 GB，含 2 个 safetensors 分片，文件完整 |
| **Tokenizer 验证** | 加载成功，`vocab_size=151643` |
| **训练脚本参数** | `--model_name`（第 53 行），默认值 `"Qwen/Qwen3-1.7B"`（HF hub ID） |

训练脚本调用时需要把 `--model_name` 改为本地路径：
```bash
--model_name /root/autodl-tmp/models/Qwen/Qwen3-1.7B
```

---
