# prep random rsft baseline

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_random_rsft_baseline_20260518T130620_result.json`
- **Structured JSON:** [`aaf02aebd43a72498d66.json`](../../sessions/aa/aaf02aebd43a72498d66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出汇报

### Random Selection 数据
- **路径**: `/root/autodl-tmp/rsft_random_k1/rsft_train.jsonl`
- **样本数**: 2716（CED k=1 为 2718，差 2 个因候选源 doc_id 数轻微差异）
- **选择方式**: 每个 doc 从其 ~8 个候选中 `random.choice`，seed=42
- **格式**: 与 CED 数据完全一致（input, output, ced_score, doc_id, generation_idx 等 8 个字段）
- **所有 doc_id 唯一**: 2716 unique docs / 2716 samples = 严格 1 per doc

### 训练脚本
- **路径**: `/root/autodl-tmp/freige/scripts/d102_next_batch/random_rsft.sh`
- **超参**: lr=2e-5, epochs=3, batch=1, grad_accum=8, warmup=100, lora_rank=64, lora_alpha=128, lora_dropout=0.05, max_length=2048, bf16
- **GPU**: 通过 `CUDA_VISIBLE_DEVICES=${GPU:-0}` 指定，启动时 `GPU=X bash random_rsft.sh`
- **输出**: `/root/autodl-tmp/rsft_output_random_k1`
- **bash 语法检查和 module import 均通过**

### 与 CED 数据对比
| | CED k=1 | Random k=1 |
|---|---|---|
| 候选源 | `rsft_generations/generations.jsonl` (21968) | 同 |
| 选择策略 | 按 combined_score 取 top-1 per doc | random.choice per doc |
| 样本数 | 2718 | 2716 |
| 唯一 doc | 2718 | 2716 |

### Dry-run 说明
GPU 全部被占用（GPU 0: 22GB, GPU 1: 28GB, GPU 2: 17GB, GPU 3: 18GB），未能完成模型加载级别的 dry-run。数据验证和脚本语法检查已通过。实际训练时需等 GPU 空闲后执行。

---
