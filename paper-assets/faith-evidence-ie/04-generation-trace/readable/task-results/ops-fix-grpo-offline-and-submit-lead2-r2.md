# ops fix grpo offline and submit lead2 r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_grpo_offline_and_submit_lead2_r2_20260517T060713_result.json`
- **Structured JSON:** [`1ac27d78436f2b84963a.json`](../../sessions/1a/1ac27d78436f2b84963a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

eval 正在推理 (0/247 batches)，模型和数据加载成功。

总结完成情况：

**Priority 1 ✅**: 修复了 `docred_processor.py`
- 添加了 `import os`
- 在 `load_split()` 的 HF fallback 前加了离线模式检查，`HF_HUB_OFFLINE=1` 或 `TRANSFORMERS_OFFLINE=1` 时要求必须传 `data_dir`

**Priority 2 ✅**: 1.7B RSFT eval 已提交
- Job: `plan006_1_7b_rsft_eval`, PID 420013, cuda:1
- 985 documents, 247 batches, 预计 ~15-20min

**Priority 3 就绪**: Lead 2 GRPO 命令已准备好，等 eval 完成释放 cuda:1 后提交。关键修正：
- 参数名应为 `--data_dir`（不是 `--data_path`）
- 完整命令：
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python3 -m freige.training.grpo_trainer --model_name /root/autodl-tmp/merged_sft_rsft_ced_s43 --data_dir /root/autodl-tmp/data/docred --stage 3 --max_steps 50 --learning_rate 1e-6 --num_generations 8 --kl_coef 0.01 --no-quantize --ced_reward_weight 1.0 --f1_reward_weight 0.0 --format_reward_weight 0.5 --output_dir /root/autodl-tmp/grpo_from_rsft_lead2_r2 --wandb_run_name lead2_rsft_grpo_ced_r2 --save_steps 10 --seed 42"
```

---
