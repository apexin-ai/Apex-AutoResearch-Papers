# infra llama en activations

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_llama_en_activations_20260521T160439_result.json`
- **Structured JSON:** [`0c7228b1c89c93e3f566.json`](../../sessions/0c/0c7228b1c89c93e3f566.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务正常运行中：

- **PID**: 16398
- **tmux session**: `llama31_en_activations`
- **GPU**: cuda:2
- **状态**: 数据已加载（1096 train + 272 test），模型权重加载中（291 shards）
- **日志**: `logs/collect_en_activations_llama.log`
- **预估耗时**: 模型加载 ~1 分钟，1368 条样本激活收集约 10-20 分钟（取决于 batch size 和序列长度），总计约 15-25 分钟
- **产出**: `data/llama31/en_activations.pt`

---
