# plan002-additive-b01-s42 训练准备报告

## 实验配置
- reward: r = r_exec * (1 + 0.1 * ISR)
- β: 0.1 (plan002-b03 用 0.3, PR=18% negative)
- steps: 500, K: 8, seed: 42
- model: Qwen3-4B
- data: data/train_500_seed42.jsonl (500 lines)
- GPU: cuda:0
- save_total_limit: 1 (hardcoded in script L418)
- log_completions: False (hardcoded in script L423)

## 完整训练命令

```bash
bash -c "export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s42"
```

## 验证清单
- [x] 数据文件存在: 500 lines ✓
- [x] Config 存在: configs/grpo_additive_bonus.yaml ✓
- [x] Output dir 干净: 不存在 ✓
- [x] save_total_limit=1: 脚本硬编码 ✓
- [x] log_completions=False: 脚本硬编码 ✓
- [x] CUDA_VISIBLE_DEVICES=0: export 方式设置 ✓
- [x] Registry 已注册: PENDING ✓

## 与 plan002-b03 唯一区别
- --beta 0.3 → --beta 0.1
- output_dir: plan002_additive_beta03_s42 → plan002_additive_b01_s42
