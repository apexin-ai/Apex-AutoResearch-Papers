# exp d158 1 7b rsft s44 ced score

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_d158_1_7b_rsft_s44_ced_score_20260524T181408_result.json`
- **Structured JSON:** [`fb5d5a1432ed9e0f3cfa.json`](../../sessions/fb/fb5d5a1432ed9e0f3cfa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已成功提交并正在运行。

**汇总：**
- **命令**: `CUDA_VISIBLE_DEVICES=0 python -m freige.training.rsft_score_filter --input_dir /root/autodl-tmp/rsft_generations_1_7b_s44 --output_path /root/autodl-tmp/rsft_scored_1_7b_s44 --nli_model_path cross-encoder/nli-deberta-v3-base --nli_device cuda:0 --selection_strategy top_k --top_k 1 --scoring_mode ced`
- **PID**: 325535（tmux session: `d158_ced_score`）
- **GPU**: cuda:0
- **状态**: RUNNING，已加载 24216 records / 3027 unique docs，NLI 模型加载中
- **输出目录**: `/root/autodl-tmp/rsft_scored_1_7b_s44`
- **日志**: `~/runs/faith-evidence-ie/d158_1_7b_rsft_s44_ced_score.log`

3027 unique docs 与 s42 的 3021 接近（差异 0.2%），符合预期。完成后需检查 `rsft_report.json` 中 `selected_records` 的值。

---
