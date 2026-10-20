# research 4b rsft s42 canonical deep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_4b_rsft_s42_canonical_deep_20260519T134413_result.json`
- **Structured JSON:** [`dff9cf9440edbe1e72a6.json`](../../sessions/df/dff9cf9440edbe1e72a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

搜索完成。结论：

## 4B CED RSFT s42 Checkpoint — 已被删除

**原始路径**: `/root/autodl-tmp/rsft_output/`（checkpoint-510 为 reeval 使用的版本）

**确认依据**:
- `eval_results/rsft_r1/metrics.json` → `model_path: /root/autodl-tmp/rsft_output`, seed=42
- `eval_results/rsft_ced_s42_reeval/metrics.json` → `model_path: /root/autodl-tmp/rsft_output/checkpoint-510`, seed=42
- 两者都是 base=Qwen3-4B, sft_adapter=sft_output

**删除原因推测**: 这是最早的 RSFT 实验，使用了无后缀的泛化名称 `rsft_output/`。后续实验改用明确命名（`rsft_output_ced_s43`, `rsft_output_random_k1` 等），原始目录在某次磁盘清理中被删除。

**历史性能** (rsft_r1 eval):
- F1=0.4449, Ign-F1=0.4449, Evi-F1=0.8187, EDCR=0.6565

**可重训**: CED-scored 训练数据仍存在：
| 数据文件 | 行数 | 含 ced_score |
|----------|------|-------------|
| `/root/autodl-tmp/rsft_filtered/rsft_train.jsonl` | 2,718 | Yes |
| `/root/autodl-tmp/rsft_filtered_topk3_ced_filtered/rsft_train.jsonl` | 7,942 | Yes |

如需重训，两个数据文件内容一致（首条记录相同），`rsft_filtered/` 更可能是原始训练用的版本（行数较少，对应原始 CED top-1 筛选）。

---
