#!/bin/bash
# exp025_verl_agent_baseline: verl-agent ALFWorld GRPO with Qwen3-1.7B
# Server: bjb1-17606, GPUs: cuda:0,1 (2x RTX 4090 or equivalent)
# Goal: Reproduce ~72.7% ALFWorld success rate using verl-agent GRPO
#
# Key fixes from dry-run iterations (v6-v9):
#   - FLASH_ATTN backend (xformers 0.0.32 incompatible with flash-attn 2.8.3)
#   - ray_init.num_cpus=24 + num_gpus=2 (AutoDL 1040-CPU container + PID limit 20480)
#   - resources_per_worker.num_cpus=1.0 (prevent CPU starvation for FSDP placement group)
#   - TORCHINDUCTOR_DISABLE=1 (avoid Triton JIT PassManager crash)
#   - Must ray stop --force before launch to clear stale sessions

set -x
ENGINE=${1:-vllm}
export VLLM_ATTENTION_BACKEND=FLASH_ATTN
export ALFWORLD_DATA=/root/autodl-tmp/alfworld
export CUDA_VISIBLE_DEVICES=0,1
export TORCHINDUCTOR_DISABLE=1

num_cpus_per_env_worker=1.0
train_data_size=16
val_data_size=128
group_size=8

MODEL_PATH=/root/autodl-tmp/models/Qwen/Qwen3-1___7B

# Activate conda environment
source /root/miniconda3/etc/profile.d/conda.sh
conda activate /root/autodl-tmp/conda-envs/verl-agent

# Clean stale Ray sessions
ray stop --force 2>/dev/null; sleep 2

cd /root/autodl-tmp/verl-agent

# Prepare data (parquet files for verl-agent)
python3 -m examples.data_preprocess.prepare \
    --mode 'text' \
    --train_data_size $train_data_size \
    --val_data_size $val_data_size

python3 -m verl.trainer.main_ppo \
    algorithm.adv_estimator=grpo \
    data.train_files=$HOME/data/verl-agent/text/train.parquet \
    data.val_files=$HOME/data/verl-agent/text/test.parquet \
    data.train_batch_size=$train_data_size \
    data.val_batch_size=$val_data_size \
    data.max_prompt_length=2048 \
    data.max_response_length=512 \
    data.filter_overlong_prompts=True \
    data.truncation='error' \
    data.return_raw_chat=True \
    actor_rollout_ref.model.path=$MODEL_PATH \
    actor_rollout_ref.actor.optim.lr=1e-6 \
    actor_rollout_ref.model.use_remove_padding=True \
    actor_rollout_ref.actor.ppo_mini_batch_size=256 \
    actor_rollout_ref.actor.ppo_micro_batch_size_per_gpu=32 \
    actor_rollout_ref.actor.use_kl_loss=True \
    actor_rollout_ref.actor.kl_loss_coef=0.01 \
    actor_rollout_ref.actor.kl_loss_type=low_var_kl \
    actor_rollout_ref.model.enable_gradient_checkpointing=True \
    actor_rollout_ref.actor.fsdp_config.param_offload=False \
    actor_rollout_ref.actor.fsdp_config.optimizer_offload=False \
    actor_rollout_ref.rollout.log_prob_micro_batch_size_per_gpu=32 \
    actor_rollout_ref.rollout.tensor_model_parallel_size=2 \
    actor_rollout_ref.rollout.name=$ENGINE \
    actor_rollout_ref.rollout.gpu_memory_utilization=0.6 \
    actor_rollout_ref.rollout.enable_chunked_prefill=False \
    actor_rollout_ref.rollout.enforce_eager=False \
    actor_rollout_ref.rollout.free_cache_engine=False \
    actor_rollout_ref.rollout.val_kwargs.temperature=0.4 \
    actor_rollout_ref.rollout.val_kwargs.do_sample=True \
    actor_rollout_ref.ref.log_prob_micro_batch_size_per_gpu=32 \
    actor_rollout_ref.ref.fsdp_config.param_offload=True \
    actor_rollout_ref.actor.use_invalid_action_penalty=True \
    actor_rollout_ref.actor.invalid_action_penalty_coef=0.1 \
    algorithm.use_kl_in_reward=False \
    env.env_name=alfworld/AlfredTWEnv \
    env.seed=0 \
    env.max_steps=50 \
    env.rollout.n=$group_size \
    env.resources_per_worker.num_cpus=$num_cpus_per_env_worker \
    trainer.critic_warmup=0 \
    trainer.logger=['console','wandb'] \
    trainer.project_name='verl_agent_alfworld' \
    trainer.experiment_name='exp025_grpo_qwen3_1.7b' \
    trainer.n_gpus_per_node=2 \
    trainer.nnodes=1 \
    trainer.save_freq=-1 \
    trainer.test_freq=5 \
    trainer.total_epochs=150 \
    trainer.val_before_train=True \
    ray_init.num_cpus=24 \
    +ray_init.num_gpus=2 $@
