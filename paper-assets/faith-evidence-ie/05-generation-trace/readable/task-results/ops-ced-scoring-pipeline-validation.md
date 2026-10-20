# ops ced scoring pipeline validation

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_ced_scoring_pipeline_validation_20260516T163031_result.json`
- **Structured JSON:** [`a8a364c72c4e0dbc9797.json`](../../sessions/a8/a8a364c72c4e0dbc9797.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成，汇总结果：

## CED Scoring Pipeline 验证结果

### 1. 脚本与模型
| 检查项 | 状态 |
|--------|------|
| `rsft_score_filter.py` 存在 | OK (24KB, May 15) |
| `from freige.training.rsft_score_filter import main` | OK |
| NLI 模型加载 (nli-deberta-v3-base) | OK, vocab_size=128000 |

### 2. Dry-run 结果 (5 条记录)
- 输入 5 条，选出 1 条 (top 25% → 20% selection rate)
- 输出文件齐全：`rsft_scores.jsonl` (20KB), `rsft_train.jsonl` (3.7KB), `rsft_report.json` (4.6KB)
- 分数分布合理：format_reward=1.0, f1_reward mean=0.759, ced_reward mean=0.574, combined mean=0.733
- 选出样本 combined_score=0.806，符合 top 25% 逻辑
- **Pipeline 完全可用，零问题。**

### 3. RSFT Gen 当前进度
| 模型 | 行数 | 预计总量 (每 doc 8 gen, ~500 docs = ~4000) | 状态 |
|------|------|-------------------------------------------|------|
| 1.7B | 6024 | ~4000+ | 已完成（超预期，可能含多轮） |
| 8B | 4824 | ~4000+ | 已完成或接近完成 |
| LLaMA-3.1-8B | 1616 | ~4000 | 进行中 (~40%) |

### 4. GPU 状态
| GPU | 已用/总量 | 空闲 |
|-----|-----------|------|
| 0 | 13.5/32.6 GB | 18.6 GB |
| 1 | 10.3/32.6 GB | 21.8 GB |
| 2 | 24.0/32.6 GB | 8.1 GB |
| 3 | 28.1/32.6 GB | 4.0 GB |

### 5. LLaMA CED Scoring 命令模板确认
```bash
CUDA_VISIBLE_DEVICES=X python -m freige.training.rsft_score_filter \
    --input_dir /root/autodl-tmp/rsft_candidates_llama_3_1_8b \
    --output_path /root/autodl-tmp/rsft_scored_llama_3_1_8b \
    --nli_model_path /root/autodl-tmp/.hf_cache/models--cross-encoder--nli-deberta-v3-base/snapshots/6c749ce3425cd33b46d187e45b92bbf96ee12ec7 \
    --nli_device cuda:0 \
    --scoring_mode ced \
    --selection_strategy top_pct --top_pct 25
```
命令模板正确，参数与 1.7B/8B 一致，仅 input_dir/output_path 路径不同。

### 6. 风险/注意事项
- **1.7B 和 8B 的 gen 看起来已完成**（行数超过预期 4000），可以立即启动 scoring，无需等到 May 17。
- LLaMA gen 还在跑（1616/~4000），预计还需数小时。
- NLI 模型仅 ~400MB，任何一张有 2GB+ 空闲的 GPU 都能跑 scoring，不与训练冲突。
- Dry-run 耗时仅 ~10s（含模型加载），全量 scoring 预计几分钟内完成。

---
