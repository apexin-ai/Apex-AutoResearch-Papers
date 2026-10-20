# code verify ced pipeline

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify-ced-pipeline_20260515T022425_result.json`
- **Structured JSON:** [`f2353a9898eeabfa9f4a.json`](../../sessions/f2/f2353a9898eeabfa9f4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

---

## 验证报告

### 要求满足情况

| # | 要求 | 状态 |
|---|------|------|
| 1 | 加载 merge_shards 产物 | ✅ `load_generations()` 支持 root + shard 目录，按 `(doc_id, generation_idx)` 去重 |
| 2 | 计算 CED score | ✅ 三维打分（format/f1/ced）+ weighted combined_score |
| 3 | top-1/top-k 参数化筛选 | ✅ `--selection_strategy top_k --top_k 1` 正常工作，每 doc 选 best candidate |
| 4 | 输出格式兼容 rsft_trainer | ✅ `{input, output, ced_score, ...}` 与 `load_rsft_data()` 完全匹配 |
| 5 | Summary 统计 | ✅ 已补充 p5/p10/p90/p95 + histogram bins |

### 修改内容
- `generate_report()` 中 `{name}_stats` 新增 p5/p10/p90/p95 percentiles 和 10-bin histogram
- `selected_stats` 新增 median/p25/p75

### Dry-run 结果
- 3 docs / 24 records → top_k=1 筛选后 3 条（每 doc 1 条，selection_rate=12.5%）
- 输出字段正确：`input`（从 prompt 提取的 user content）、`output`、`ced_score`
- report 包含完整统计 + histogram

### 生成完成后的确切运行命令

```bash
cd /root/autodl-tmp && \
HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
python -m freige.training.rsft_score_filter \
    --input_dir /root/autodl-tmp/rsft_generations \
    --output_path /root/autodl-tmp/rsft_filtered \
    --selection_strategy top_k --top_k 1 \
    --nli_device cuda:0
```

---
