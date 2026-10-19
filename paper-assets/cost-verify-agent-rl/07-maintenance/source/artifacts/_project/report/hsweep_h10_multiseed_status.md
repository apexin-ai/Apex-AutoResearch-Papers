# h-sweep h=10 Multi-Seed Experiment Status

## 配置文件
- **路径**: `/root/cost-verify-agent-rl/RAGEN/config/_alfworld_hsweep_h10_1gpu.yaml`
- **关键参数变更**（相比原始 h10 双卡配置）:
  - `n_gpus_per_node: 1`（原 2）
  - `CUDA_VISIBLE_DEVICES: "0"`（原 "0,1"）
  - `total_training_steps: 5`（原 15）
  - `ppo_mini_batch_size: 8`（原 16，保持 per-GPU batch 不变）
  - `optimizer_offload: True`（不变）
  - `val_before_train: True`（不变，step 0 和 step 5 有 eval）
  - `test_freq: 5`, `save_freq: 5`（不变）
  - `step_independent_history_length: 10`（不变）

## Seed2 (train_seed=20000)
- **状态**: ✅ 已启动，正在加载数据
- **PID**: 42499（shell）→ TaskRunner pid=44542, WorkerDict pid=44710
- **GPU**: cuda:0, 14.8GB 占用
- **Log**: `/root/autodl-tmp/hsweep_h10_seed2.log`
- **W&B experiment_name**: `hsweep-h10-seed2-1gpu`
- **启动时间**: 2026-05-23

## Seed3 启动命令（待 seed2 完成后执行）
```bash
cd /root/cost-verify-agent-rl/RAGEN
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

CUDA_VISIBLE_DEVICES=0 nohup python train.py \
    --config-name _alfworld_hsweep_h10_1gpu \
    seed.train=30000 \
    trainer.experiment_name="hsweep-h10-seed3-1gpu" \
    > /root/autodl-tmp/hsweep_h10_seed3.log 2>&1 &

echo "PID: $!"
```

## Seed4 启动命令（备用）
```bash
CUDA_VISIBLE_DEVICES=0 nohup python train.py \
    --config-name _alfworld_hsweep_h10_1gpu \
    seed.train=40000 \
    trainer.experiment_name="hsweep-h10-seed4-1gpu" \
    > /root/autodl-tmp/hsweep_h10_seed4.log 2>&1 &
```
