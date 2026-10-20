# code verify ced recall penalty

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify-ced-recall-penalty_20260514T195228_result.json`
- **Structured JSON:** [`9e8b2ed5591d607d9426.json`](../../sessions/9e/9e8b2ed5591d607d9426.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

### 结果

**1. 参数格式**：`--ced_recall_penalty` 是 boolean flag（`store_true`），无需传值，加上即启用。

**行为**：在 CED reward 计算中，`mean_ced *= recall`，即将 CED 得分乘以 recall（`matched_gold_keys / total_gold`），惩罚漏提取。

**2. 完整提交命令**：

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.training.grpo_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_dir /root/autodl-tmp/data/docred --stage 3 --tau_start 0.3 --tau_end 0.5 --output_dir /root/autodl-tmp/grpo_ced_lr5e6_rp --num_generations 8 --reward_device cuda --per_device_batch_size 1 --gradient_accumulation_steps 16 --num_epochs 1 --learning_rate 5e-6 --seed 42 --kl_coef 0.01 --save_steps 20 --save_total_limit 20 --max_steps 200 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --num_iterations 1 --ced_recall_penalty --wandb_run_name grpo-s3-ced-lr5e6-rp-r1"
```

**3. 无异常**。参数解析正常，import 正常，命令可直接用于 `submit_training_job`。

---
