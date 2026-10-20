# fix delete 35pct models

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_delete_35pct_models_20260514T161302_result.json`
- **Structured JSON:** [`6cb8816be0ff884134b9.json`](../../sessions/6c/6cb8816be0ff884134b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

35% 模型目录已不存在，无需删除。但数据盘 250G 用了 247G（剩 3.8G），大头如下：

| 目录 | 大小 |
|------|------|
| `/root/autodl-tmp/output/` | 150G |
| `/root/autodl-tmp/schema-conform-ie-training/` | 19G |
| `/root/autodl-tmp/models/` | 19G |
| `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B/` | 15G |
| `/root/autodl-tmp/pruned_standard_20/` | 12G |
| `/root/autodl-tmp/pruned_rasp_20/` | 12G |
| `/root/autodl-tmp/pruned_standard_25/` | 11G |
| `/root/autodl-tmp/pruned_rasp_25/` | 11G |

**汇报：**
- 任务中列出的 8 个 35% 相关目录均已不存在（之前已被清理过）
- 无 recovered_*/sft_* 残留，无 35% symlink
- 数据盘仍然 99% 满，`output/` 目录占 150G 是最大头。如需进一步释放空间，需要清理 `output/` 或其他目录

---
