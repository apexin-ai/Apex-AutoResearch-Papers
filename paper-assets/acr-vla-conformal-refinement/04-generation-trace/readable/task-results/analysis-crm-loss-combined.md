# analysis crm loss combined

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_crm-loss-combined_20260522T063333_result.json`
- **Structured JSON:** [`ea0ee69de42990991af2.json`](../../sessions/ea/ea0ee69de42990991af2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## crm-loss-combined 训练结果

**核心指标**
- best_val_loss: **0.005302** (epoch 48)
- final_train_loss: 0.004481 (epoch 50)
- initial_val_loss: 0.031324 → 5.9× 收敛
- total_epochs: 50/50, exit_code=0
- DOF weight 范围: [0.0107, 3.7318]
- W&B: 此 run 未启用
- checkpoint: `/root/autodl-tmp/checkpoints/crm_loss_variants/combined/crm_best.pt`

**与其他 loss 变体对比 (best_val_loss)**

| 变体 | val_loss | 相对 combined |
|---|---|---|
| perdof | 0.000124 | **43× 更好** |
| mse_baseline | 0.00208 | 2.5× 更好 |
| **combined (λ=0.1)** | **0.005302** | — |
| conformal | 0.013343 | 2.5× 更差 |

**结论**：combined loss 表现介于 mse_baseline 和 conformal 之间，未达到 perdof 的水平。预期"per-DOF + conformal"的组合优势没有出现——λ_conf=0.1 引入的 conformal 分量似乎拉低了 per-DOF 单独使用时的精度。可能原因：(1) conformal 分量与 per-DOF 加权目标不正交，相互冲突；(2) λ=0.1 权重过大；(3) 训练曲线显示从 epoch 41 起 val_loss 在 0.0053 附近震荡，未进一步下降，提示该 loss 形态已到达瓶颈。建议后续若想保留 conformal 信号，可尝试更小的 λ（0.01）或在 perdof 收敛后再加 conformal 微调。

---
