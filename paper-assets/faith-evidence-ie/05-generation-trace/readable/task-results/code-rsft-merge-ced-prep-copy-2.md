# code rsft merge ced prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_rsft-merge-ced-prep_20260515T014833_result.json`
- **Structured JSON:** [`5325d0717c2bbd4677db.json`](../../sessions/53/5325d0717c2bbd4677db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全流程验证通过：

| 指标 | 值 |
|------|-----|
| 24 条输入 → top_k=2 筛选 → 6 条输出 | 25% selection rate |
| format_reward | mean=1.000 |
| f1_reward | mean=0.719 |
| ced_reward | mean=0.478 |
| combined_score | mean=0.679 |
| SFT 输出格式 | input/output + 元数据字段 |

**总结**：

`rsft_score_filter.py` 已具备完整的 RSFT 后处理 pipeline，唯一修改是 `load_generations()` 支持了多 shard 合并 + 去重。生成完成后，运行命令：

```bash
cd /root/autodl-tmp && \
HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 \
python -m freige.training.rsft_score_filter \
    --input_dir /root/autodl-tmp/rsft_generations \
    --output_path /root/autodl-tmp/rsft_filtered \
    --selection_strategy top_k --top_k 2 \
    --nli_device cuda:0
```

预估 GPU 上打分 ~5-10 min，CPU ~25 min。输出三个文件：`rsft_train.jsonl`（SFT 训练数据）、`rsft_scores.jsonl`（全量评分）、`rsft_report.json`（统计报告）。

---
