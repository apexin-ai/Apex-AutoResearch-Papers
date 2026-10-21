# infra download qwen3 1 7b

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_download-qwen3-1_7b_20260514T055647_result.json`
- **Structured JSON:** [`b3b1d2ca29b02c005ba4.json`](../../sessions/b3/b3b1d2ca29b02c005ba4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。

## 结果

**模型下载路径**: `/root/autodl-tmp/models/Qwen/Qwen3-1.7B` (symlink → `Qwen3-1___7B`，ModelScope 下载的完整副本)

**验证结果**: 通过
- Tokenizer: vocab_size=151643
- Model: 1720.6M params, 2 shards 均正常加载

**另一个路径 `/root/autodl-tmp/models/Qwen3-1.7B-hf/` 不完整**（有 `.aria2` 残留，缺少第 2 个 shard），不要使用。

**训练脚本参数** (`router_sft_train.py:53`):
- 参数名: `--model_name`
- 默认值: `Qwen/Qwen3-1.7B`（HF hub ID，会触发网络请求）
- 需要改为本地路径

**plan-002-formal-v3 建议命令**:
```bash
python src/router_sft_train.py \
  --model_name /root/autodl-tmp/models/Qwen/Qwen3-1.7B \
  ... # 其他参数
```

关键点：`--model_name` 传本地绝对路径即可避免 HF Hub 网络请求。

---
