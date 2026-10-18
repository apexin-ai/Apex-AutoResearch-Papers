# ssh exp008 analysis prep

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp008-analysis-prep_20260515T111102_result.json`
- **Structured JSON:** [`61fb7e11e39252b5ca99.json`](../../sessions/61/61fb7e11e39252b5ca99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行成功，per_type 结果也已出（F1=0.2915）。两个脚本都已创建完成。

**分析结果摘要：**

| Mode | F1 | Precision | Recall | #Batches | Time(s) | Δ vs single_pass |
|------|-----|-----------|--------|----------|---------|------------------|
| single_pass | 0.4451 | 0.5631 | 0.3679 | 1 | 77.3 | baseline |
| sdgd_zero | 0.2514 | 0.2096 | 0.3141 | 8 | 408.7 | -0.1937 |
| random_batch | 0.3197 | 0.2491 | 0.4462 | 8 | 476.1 | -0.1253 |
| per_type | 0.2915 | 0.1940 | 0.5856 | 66 | 2532.2 | -0.1536 |

关键发现：所有分解模式 F1 都低于 single_pass baseline。分解提升了 recall（per_type 0.59 vs single_pass 0.37）但 precision 大幅下降。sdgd_zero 甚至不如 random_batch。

**已创建的文件：**
- `src/analyze_exp008_results.py` — 分析脚本，已在服务器 dry-run 验证通过，summary 已保存到 `artifacts/exp008/analysis_summary.json`
- `scripts/compute_fewrel_qwen3_embeddings.sh` — FewRel embedding 脚本，使用 `configs/fewrel_relation_types.json`（80 relations）+ Qwen3-32B-FP8，输出 embeddings 和 sim_matrix 两个 .pt 文件。未执行，等 GPU 空闲时运行。

---
