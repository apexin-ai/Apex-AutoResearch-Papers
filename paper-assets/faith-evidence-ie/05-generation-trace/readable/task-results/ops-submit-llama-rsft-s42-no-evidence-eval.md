# ops submit llama rsft s42 no evidence eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submit_llama_rsft_s42_no_evidence_eval_20260519T223825_result.json`
- **Structured JSON:** [`5fca086e851e2d46d2aa.json`](../../sessions/5f/5fca086e851e2d46d2aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

提交完成。

**汇总：**
- **exp_id**: `eval_llama_rsft_s42_no_evidence`
- **PID**: 731088
- **GPU**: cuda:3（提交前确认 0 MiB 占用）
- **tmux session**: `eval_llama_rsft_s42_no_evidence`
- **日志**: `~/runs/faith-evidence-ie/eval_llama_rsft_s42_no_evidence.log`
- **完整命令**: `CUDA_VISIBLE_DEVICES=3 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_llama_3_1_8b_k1 --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --no_evidence --output_dir /root/autodl-tmp/eval_results/eval_llama_rsft_s42_no_evidence`
- **parent**: `d102_llama_rsft_k1_s42`
- **Registry 状态**: RUNNING
- **关键参数**: `--no_evidence` 已添加（C005 约束）

---
