# CLS 8B seed123 ckpt-3000 val eval — 待提交

## 状态
- **日期**: 2026-05-14
- **原因**: 所有 4 个 GPU 都在使用中，无法提交

## 正确 Checkpoint 路径
```
/root/autodl-tmp/checkpoints_backup_cls_8b_seed123/checkpoint-3000
```
- base_model: Qwen3-8B (已验证 adapter_config.json)
- 注意: `checkpoints_repo_cls_seed123/checkpoint-3000` 是 4B 的，不要用

## 提交命令
```bash
# submit_training_job 参数:
# server: seetacloud-westd-4x5090
# gpu_ids: ["cuda:1"]  (或任何空闲 GPU)
# exp_id: cls8b-seed123-ckpt3000-val-eval
# account: root

bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_backup_cls_8b_seed123/checkpoint-3000 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --split val --max_seq_length 8192 --batch_size 1 --device cuda:0 --output /root/autodl-tmp/results/cls8b_seed123_ckpt3000_val/summary.json --pred_output /root/autodl-tmp/results/cls8b_seed123_ckpt3000_val/predictions.jsonl"
```

## GPU 占用情况 (截至查询时)
| GPU | 进程 | 预估空闲时间 |
|-----|------|-------------|
| cuda:0 | eval cls 8B ckpt-600 val (PID 285772, ~10min) | 较快空闲(预计30-60min) |
| cuda:1 | eval cls v5 ckpt-400 val (PID 281646, ~29min) | 最快空闲(预计10-30min) |
| cuda:2 | train CWM 8B seed42 (PID 266816, 3h+) | 长期占用 |
| cuda:3 | train CLS 8B seed123 续训 (PID 266449, 3h+) | 长期占用 |

## 提交时注意
- `--device` 参数改为实际空闲的 GPU
- 确保结果目录 `/root/autodl-tmp/results/cls8b_seed123_ckpt3000_val/` 存在（脚本可能自动创建）
- eval 需要 ~13-20GB 显存（8B 模型推理）
