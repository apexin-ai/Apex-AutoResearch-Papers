# ablation_random_occ_s0 训练分析报告

## 训练状态
- **完成**: 50005/50005 步，EXIT_CODE=0
- **时间**: 2026-05-21 18:56 → 2026-05-22 09:24（约14.5小时）
- **速度**: ~1.08 it/s

## Checkpoint 状态
路径: `/root/autodl-tmp/checkpoints/ablation_random_occ_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt`

文件完整:
- model-00001~00004-of-00004.safetensors (4 shards)
- action_head--50000_checkpoint.pt
- occ_head--50000_checkpoint.pt
- proprio_projector--50000_checkpoint.pt
- lora_adapter/ (adapter_model.safetensors + adapter_config.json)
- dataset_statistics.json
- config.json, tokenizer 等

## Loss Metrics
**不可用** — wandb 未正确配置（entity/project 为占位符），log 文件仅含进度条输出，无显式 loss 值记录。

## 模型参数
- trainable params in proprio_projector: 16,818,176
- trainable params in action_head: 151,117,831
- trainable params in occ_head: 1,213,313
- total trainable params: 279,977,608 (1.45% of 7.65B)

## Eval 启动
- **PID**: 615697
- **GPU**: cuda:1 (NVIDIA RTX PRO 6000 Blackwell, 98GB)
- **配置**: libero_spatial, 10 tasks × 50 rollouts = 500 episodes
- **Log**: ~/runs/occsafe_vla/ablation_random_occ_s0_eval.log
- **输出**: /root/autodl-tmp/checkpoints/ablation_random_occ_s0/eval_results.json
- **预计完成**: ~35 min（约 4s/episode）

## 预期对比
| Model | TSR | CAR |
|-------|-----|-----|
| Vanilla baseline | ~90.7% | ~78.0% |
| Full occ (mvp_occ s0) | - | 83.2% |
| Random occ (本实验) | 待 eval | 待 eval |

若 random_occ CAR ≈ vanilla(78%)，则证明 occ 空间内容是关键（Claim 4 成立）。
若 random_occ CAR ≈ full occ(83%)，则说明任意辅助 loss 都能提升 CAR。
