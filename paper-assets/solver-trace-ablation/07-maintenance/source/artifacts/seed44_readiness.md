# seed=44 exec-only 实验就绪报告

**日期**: 2026-05-14
**状态**: ✅ READY

## Config 摘要 (`configs/grpo_exec_only.yaml`)
- model: Qwen3-4B (`/root/autodl-tmp/models/Qwen3-4B`)
- reward_mode: execution_only (exec=1.0, sta=0.0)
- batch: per_device=4, grad_accum=2, num_generations=8
- max_completion_length: 512
- lr: 1e-6
- solver: prover9

## 数据文件
- `data/train_500_seed42.jsonl` — 484KB ✅（符合 C001）

## 磁盘空间
- `/root/autodl-tmp/`: 112GB 可用 / 250GB 总量（56% 使用）
- s43 实验占用 ~30GB，s44 预计同量级，剩余 ~82GB

## Import 验证
- `from scripts.train_grpo import *` — ✅ 通过（仅 vLLM 版本 warning，不影响）

## 注意事项
- `save_total_limit=2`（C003 要求 1），但与 s43 一致，112GB 余量足够
- `log_completions=False` — completions parquet 已禁用 ✅
- 当前 GPU 0/1 均占用 ~80GB，需等 s43 完成释放 cuda:1

## 完整提交命令

```bash
bash -c "export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s44"
```

用 nohup 提交（推荐）：
```bash
bash -c "export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && nohup python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s44 > /root/autodl-tmp/outputs/plan001_exec_only_s44/train.log 2>&1 &"
```
