# eval test eval 8b rsft s42

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_test_eval_8b_rsft_s42_20260521T114555_result.json`
- **Structured JSON:** [`0d2a38a8eaa5cd965209.json`](../../sessions/0d/0d2a38a8eaa5cd965209.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

1.7B eval (PID 102820) 仍在运行，已 8.5 分钟。1.7B 模型处理 500 docs 可能还需 20-40 分钟。

**当前状态汇总：**
- 所有路径已验证 OK
- Registry 条目 `test_eval_8b_rsft_s42` 已创建（PREPARING）
- Base model: `/root/autodl-tmp/models/Qwen/Qwen3-8B`
- **阻塞**：cuda:3 被 1.7B test eval 占用（6062 MiB），C001 约束要求 < 2GB 才能提交

命令已准备好，等 cuda:3 空闲即可提交：
```
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && CUDA_VISIBLE_DEVICES=3 python -m freige.eval.test_inference --model_path /root/autodl-tmp/rsft_output_qwen3_8b_k1 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 --data_path /root/autodl-tmp/data/re-docred-repo/data --split test_revised --max_new_tokens 2048 --no-quantize --seed 42 --output_dir /root/autodl-tmp/eval_results/test_eval_8b_rsft_s42"
```

要我设置轮询等 1.7B 完成后自动提交，还是你手动告诉我什么时候提交？

---
