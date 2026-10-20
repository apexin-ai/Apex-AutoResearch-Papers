# code docred batch resume

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_docred_batch_resume_20260513T191555_result.json`
- **Structured JSON:** [`26b8ebfe503f23998f65.json`](../../sessions/26/26b8ebfe503f23998f65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

无残留进程。Dry-run 验证结果汇总：

**验证通过：**
- **Resume**: 正确识别 263 已处理 docs，跳过后处理 2 个新 doc
- **Batch 推理**: 2 docs 在 1 个 batch 中完成，batch 总耗时 34.4s（per-doc 17.2s）
- **输出格式**: JSON parse 2/2 成功，append 模式正确（263→265）
- **文件完整性**: 265 行，265 unique doc_ids，无重复

**速度对比：**
- 旧单条推理: ~18.5s/doc
- 新 batch 推理 (batch=2): 17.2s/doc — 这只是 2 样本的 batch，不是满 batch=4

batch_size=4 的加速主要体现在同时处理 4 个 prompt 时可以共享 prefill 计算。这里只有 2 个样本，效果有限。满 batch=4 预计 per-doc 降到 ~10-12s。

**全量运行命令（供 submit_training_job 使用）：**

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_extraction_docred.py \
    --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B \
    --data_path data/docred/dev.json \
    --output_path outputs/raw_outputs_docred.jsonl \
    --device cuda:1 \
    --constraints_path data/docred/ontology_constraints_docred.json \
    --batch_size 4 \
    --resume
```

**预估时间：**
- 剩余 733 docs (998 - 265)
- 保守估计 per-doc 17s (batch=4 满载会更快): 733 × 17 / 3600 ≈ **3.5 小时**
- 乐观估计 per-doc 12s (batch=4 满载): 733 × 12 / 3600 ≈ **2.4 小时**

---
