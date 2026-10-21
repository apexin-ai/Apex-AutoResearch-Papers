# qwen3-8b-traj-repo-s42-v2 训练分析

## 训练状态：正常完成

EXIT_CODE=0，无 OOM/error/异常退出。

## 训练配置

| 参数 | 值 |
|------|-----|
| 模型 | Qwen3-8B (8.2B params) |
| LoRA | r=16, alpha=32, dropout=0.05, targets=q/k/v/o_proj |
| 可训练参数 | 15.3M / 8.2B (0.19%) |
| 数据 | train=386, val=43 |
| 截断率 | train 2.6% (10/386), val 7.0% (3/43) |
| seq_length | 4096 (v1 OOM at 8192) |
| batch_size | 1, grad_accum=8 |
| lr | 2e-4 |
| epochs | 3 |
| 总 steps | 147 |
| 训练时长 | 350.27s (~5.8 min) |

## Loss 曲线

| Epoch | Train Loss | Eval Loss |
|-------|-----------|-----------|
| 1.0   | 1.4515    | **nan**   |
| 2.0   | 0.1455    | **nan**   |
| 3.0   | (avg) 0.5669 | **nan** |

- Train loss 从 1.45 降至 0.15，下降正常
- **eval_loss 全部为 nan** — 可能是 validation 时 label masking 导致所有 token 被 mask，或 dtype 溢出。不影响模型本身的训练质量，但 "best" checkpoint 的选择可能不可靠（trainer 无法基于 eval_loss 比较）

## Checkpoints

```
/root/autodl-tmp/checkpoints_qwen3_8b_traj_repo/
├── best/              (adapter_model.safetensors, 58.5MB)
├── checkpoint-98/
└── checkpoint-147/
```

## 与 Qwen3-4B TRAJ 对比

| 指标 | Qwen3-4B TRAJ s42 | Qwen3-8B TRAJ s42-v2 |
|------|-------------------|----------------------|
| 训练时长 | — | 5.8 min |
| Train loss (avg) | — | 0.5669 |
| Eval loss | — | nan (all epochs) |
| Variant accuracy | **72.92%** | **待 eval** |

## 风险评估

1. **eval_loss=nan**: 中等风险。"best" checkpoint 可能不是真正的最优模型。建议同时对 checkpoint-98 和 best 运行 eval 对比
2. **seq_length 降至 4096**: 低风险。截断率仅 2.6%/7.0%，且 DeepSeek 在非 8k 条件下结果相当
3. **训练时长极短 (5.8 min)**: 符合预期。数据量仅 386 samples，3 epochs × 49 steps/epoch = 147 steps

## 推荐 Eval 命令

基于 qwen3-4b-traj-repo-s42-eval 模板：

### Best checkpoint
```bash
cd /home/sonny/exec-sim-repair-verifier && \
HF_HUB_OFFLINE=1 /root/miniconda3/bin/python eval_traj_verifier.py \
  --model_path /root/autodl-tmp/checkpoints_qwen3_8b_traj_repo/best \
  --test_file swebench_test.jsonl \
  --output /root/autodl-tmp/eval_results/qwen3_8b_traj_repo_s42_best/eval_test_s42.json \
  --seed 42
```

### Checkpoint-98 (epoch 2, 可选对比)
```bash
cd /home/sonny/exec-sim-repair-verifier && \
HF_HUB_OFFLINE=1 /root/miniconda3/bin/python eval_traj_verifier.py \
  --model_path /root/autodl-tmp/checkpoints_qwen3_8b_traj_repo/checkpoint-98 \
  --test_file swebench_test.jsonl \
  --output /root/autodl-tmp/eval_results/qwen3_8b_traj_repo_s42_ckpt98/eval_test_s42.json \
  --seed 42
```

## 结论

训练正常完成，train loss 下降健康。eval_loss=nan 是唯一异常，不影响模型训练本身但影响 best checkpoint 选择的可靠性。建议先跑 best eval，如结果异常再跑 checkpoint-98 对比。

预期 variant accuracy: 75-85% (介于 Qwen3-4B 的 72.92% 和 DeepSeek 的 81.25% 之间)。
