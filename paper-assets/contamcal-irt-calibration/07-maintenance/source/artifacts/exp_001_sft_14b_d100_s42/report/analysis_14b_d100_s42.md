## exp_001_sft_14b_d100_s42 分析结果

conclusion: success
final_train_loss: 0.9682
mean_token_accuracy: 0.7488
entropy: 1.142
total_steps: 4159
num_samples: 66533
training_time: 3h46m (13560s)
checkpoint_exists: yes
checkpoint_path: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d100_s42/lora_adapter
adapter_size: 275 MB (adapter_model.safetensors)
log_path: /root/runs/contamcal-irt-calibration/exp_001_sft_14b_d100_s42.log
wandb_run_id: N/A (no W&B integration in this training run)
lora_config: r=16, alpha=32, lr=5e-5, dropout=0.05, targets=q/k/v/o/gate/up/down_proj
exit_code: 0

## 14B Dosage Sweep Summary (Qwen2.5-14B, seed=42)

| dosage | train_loss | token_acc | entropy | steps | samples | time     | status  |
|--------|-----------|-----------|---------|-------|---------|----------|---------|
| d000   | 0.9089    | 0.7761    | 0.9489  | 3125  | 50000   | 2h43m    | success |
| d005   | 0.9141    | 0.7969    | 0.8794  | 3177  | 50826   | 2h46m    | success |
| d025   | 0.9264    | 0.7677    | 1.001   | 3384  | 54133   | 2h60m    | success |
| d050   | 0.9422    | 0.7627    | 1.054   | 3642  | 58266   | 3h04m    | success |
| d100   | 0.9682    | 0.7488    | 1.142   | 4159  | 66533   | 3h46m    | success |

All 5 dosage points trained with identical hyperparameters: LoRA r=16 alpha=32, lr=5e-5, batch=1 grad_accum=16, max_seq_len=2048, 1 epoch.

## 趋势分析

**Loss vs dosage**: 单调递增 (0.909 → 0.968)。d100 比 d000 高 6.5%，符合预期：contaminated samples（benchmark 原题）的分布与 clean instruction data 不同，混入比例越高 loss 越高。

**Token accuracy vs dosage**: 整体递减趋势 (0.776 → 0.749)，但 d005 异常偏高 (0.797)。d005 的 entropy 也最低 (0.879)，提示极少量 contamination 可能让模型在训练集上的预测更确定。这个异常值得关注，但需要 eval 数据才能判断是否有实际影响。

**Entropy vs dosage**: 单调递增 (0.949 → 1.142)，contamination 数据增加了模型输出的不确定性。

**训练时间**: 与样本数成正比，d100 (66533 samples) 比 d000 (50000 samples) 多 33% 样本，训练时间也多约 39%。

**与 3B 系列对比** (from registry):
- 3B d000 s42 a32: loss=1.132, token_acc=0.733
- 3B d005 s42: loss=1.135, token_acc=0.752
- 14B 全系列 loss 显著低于 3B (~0.91-0.97 vs ~1.13)，token accuracy 也更高 (~0.75-0.80 vs ~0.73-0.75)，符合 scale 预期。

**14B dosage sweep 现在 5 个点全部完成**。下一步需要：
1. 对 5 个 checkpoint 运行 eval (MMLU/GSM8K/ARC/HumanEval para-aligned)
2. 计算 compute_signals 用于 IRT fitting
