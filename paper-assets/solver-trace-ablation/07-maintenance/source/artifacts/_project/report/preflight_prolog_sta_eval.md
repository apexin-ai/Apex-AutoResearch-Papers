# Prolog STA s43/s44 Eval 预检报告

**日期**: 2026-05-14  
**结论**: **Yes — eval 管线就绪**

## 检查结果

| 检查项 | 状态 | 备注 |
|--------|------|------|
| eval_sta.py | OK | 11KB, 支持 `--logic_type prolog` |
| swipl | OK | `/usr/bin/swipl` 可用 |
| eval 数据 | OK | `data/proofwriter_fol_100.jsonl` 存在 |
| s43 训练 | 进行中 | checkpoint-250, checkpoint-300 已存在 (16GB) |
| s44 训练 | 进行中 | checkpoint-150 已存在 (15GB) |
| 磁盘 | 注意 | 41GB 剩余 / 250GB, eval 后必须立即清理 checkpoint |

## s42 eval 参考 (registry)

- eval_data: proofwriter_fol_100.jsonl
- eval_prove_rate: 0.50, eval_mean_isr: 0.50
- eval_h7_rate: 1.00 (100% H7, 极端 Goodhart)
- eval_n_clauses_mean: 1

## Eval 命令

训练完成后, 最终 checkpoint 预计为 checkpoint-500 (save_steps=50, 共 500 步, save_total_limit=1 仅保留最新)。

### s43

```bash
export CUDA_VISIBLE_DEVICES=0  # 根据 GPU 可用情况调整
cd /root/solver-trace-ablation
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

python3 scripts/eval_sta.py \
  --model_path /root/autodl-tmp/outputs/plan006_prolog_sta_s43/checkpoint-500 \
  --data_path data/proofwriter_fol_100.jsonl \
  --logic_type prolog \
  --output_path /root/autodl-tmp/outputs/plan006_prolog_sta_s43/eval_results.json
```

### s44

```bash
export CUDA_VISIBLE_DEVICES=1  # 根据 GPU 可用情况调整
cd /root/solver-trace-ablation
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

python3 scripts/eval_sta.py \
  --model_path /root/autodl-tmp/outputs/plan006_prolog_sta_s44/checkpoint-500 \
  --data_path data/proofwriter_fol_100.jsonl \
  --logic_type prolog \
  --output_path /root/autodl-tmp/outputs/plan006_prolog_sta_s44/eval_results.json
```

## 注意事项

1. **Checkpoint 路径**: 最终 checkpoint 可能不是 checkpoint-500（如训练提前停止）。执行前先 `ls` 确认实际目录名。
2. **磁盘紧张** (41GB/250GB): eval 完成后立即删除 checkpoint 目录释放空间。每个 checkpoint ~8GB。
3. **C005**: eval 前必须 `export CUDA_VISIBLE_DEVICES=N`，禁止裸跑。
4. **C004**: 跨 seed 对比必须使用 eval_sta.py 结果，禁止引用训练日志 ISR。
5. **s43 当前有两个 checkpoint** (250 + 300)，save_total_limit=1 应该只保留最新，但实际有两个。训练结束后确认只剩最终 checkpoint，否则手动清理旧的。
6. **Eval 耗时参考**: prolog-exec 实验 eval 约 10-15 分钟/个。
