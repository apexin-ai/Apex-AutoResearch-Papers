# fix transformers compat 30476

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_transformers_compat_30476_20260517T111833_result.json`
- **Structured JSON:** [`ea08ab9646ffcc7bce46.json`](../../sessions/ea/ea08ab9646ffcc7bce46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器均验证通过。

## 修复报告

| 项目 | 详情 |
|---|---|
| **transformers 版本** | westd-30476: **5.8.1**, westd-41312: **4.57.6** |
| **根因** | transformers 5.x 移除了 `Trainer.__init__()` 的 `tokenizer` 参数（4.46 起已 deprecated，重命名为 `processing_class`） |
| **修改文件** | `training/pretrain_weighted.py` 第 415 行 |
| **修改内容** | `tokenizer=tokenizer,` → `processing_class=tokenizer,` |
| **影响范围** | 全项目仅此一处传 `tokenizer=` 给 Trainer |
| **兼容性** | `processing_class` 自 4.46 起可用，两台服务器均兼容 |
| **验证** | 两台服务器 `import WeightedTrainer` 均成功 |

---
