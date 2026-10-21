# diagnose ced kl001 resubmit

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_ced_kl001_resubmit_20260514T152717_result.json`
- **Structured JSON:** [`4682d69e0b718d858403.json`](../../sessions/46/4682d69e0b718d858403.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现状明确了。sft_eval_r3 在 GPU 1 上才完成 31%（19/62 batches），约需再 75 分钟。**所有 4 个 GPU 均被占用，无法立即提交。**

诊断结果汇总：

**三次失败根因确认：**
1. `--lr` → argparse 定义的是 `--learning_rate`
2. 缺少 `bash -c` + conda 激活
3. 缺少 `--data_dir`（默认值为 None）

**正确命令已构建**（基于 GPU 0 上 ced_r5 的实际运行命令，仅改 kl_coef + output_dir + save_total_limit + wandb_run_name）：

```json
{
  "submitted": false,
  "exp_id": "mvp2_grpo_ced_kl001_r4",
  "reason": "所有4个GPU被占用: cuda:0=ced_r5(stage3,~3h), cuda:1=sft_eval_r3(31%,~75min剩余), cuda:2=extract_r3(stage1,~3h), cuda:3=flatnli_r4(stage2,刚启动). 最早可用GPU: cuda:1 约75分钟后",
  "command": "bash -c \"source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_DISABLE_XET=1 REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES={GPU_ID} python -m freige.training.grpo_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_dir /root/autodl-tmp/data/docred --stage 3 --tau_start 0.3 --tau_end 0.5 --output_dir /root/autodl-tmp/grpo_ced_kl001 --num_generations 4 --reward_device cpu --per_device_batch_size 1 --gradient_accumulation_steps 16 --num_epochs 1 --learning_rate 5e-5 --seed 42 --kl_coef 0.01 --save_steps 20 --save_total_limit 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --num_iterations 1 --wandb_run_name grpo-s3-ced-kl001-r4\"",
  "verified": false,
  "note": "无D020新增参数需要添加，argparse中无F1 gating相关新参数"
}
```

与 ced_r5 的差异仅 3 处：`kl_coef=0.01`(was 0.0)、`save_total_limit=20`(was default 5)、output_dir/wandb_run_name。命令将 `{GPU_ID}` 替换为实际可用 GPU 编号后即可提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "submitted": false,
    "exp_id": "mvp2_grpo_ced_kl001_r4",
    "reason": "所有4个GPU被占用: cuda:0=ced_r5(stage3,~3h), cuda:1=sft_eval_r3(31%,~75min剩余), cuda:2=extract_r3(stage1,~3h), cuda:3=flatnli_r4(stage2,刚启动). 最早可用GPU: cuda:1 约75分钟后",
    "command": "bash -c \"source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_DISABLE_XET=1 REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES={GPU_ID} python -m freige.training.grpo_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_dir /root/autodl-tmp/data/docred --stage 3 --tau_start 0.3 --tau_end 0.5 --output_dir /root/autodl-tmp/grpo_ced_kl001 --num_generations 4 --reward_device cpu --per_device_batch_size 1 --gradient_accumulation_steps 16 --num_epochs 1 --learning_rate 5e-5 --seed 42 --kl_coef 0.01 --save_steps 20 --save_total_limit 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --num_iterations 1 --wandb_run_name grpo-s3-ced-kl001-r4\"",
    "verified": false,
    "note": "无D020新增参数需要添加，argparse中无F1 gating相关新参数"
  }
}
```

</details>

---
