# code c3 coupling oracle prep

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_c3_coupling_oracle_prep_20260517T110528_result.json`
- **Structured JSON:** [`5c251cfdeee730aba891.json`](../../sessions/5c/5c251cfdeee730aba891.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 完全成功。5 steps 正常运行，训练循环无报错。

**结果总结：**

脚本 `/root/distill_sparse_swiglu/scripts/c3_coupling_oracle.py` 已就绪。

**关键参数：**
| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--num_steps` | 1000 | 与 KL 训练一致 |
| `--batch_size` | 4 | 与 KL 训练一致 |
| `--lr` | 1e-3 | 与 KL 训练一致 |
| `--bottleneck_dim` | 128 | d_b=128，与 KL/BCE 一致 |
| `--sparsity_target` | 0.5 | 50% sparsity |
| `--sparsity_reg_weight` | 0.1 | 与 BCE 训练一致 |
| `--kl_checkpoint` | `checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt` | 冻结 KL oracle |
| `--dataset` | wikitext-103 | 与 KL 训练一致 |

**预估训练资源：**
- GPU: 1× RTX PRO 6000 (`cuda:0`)，无需梯度回传基础模型
- 时间: ~0.3s/step × 1000 steps ≈ **~5 分钟**（远快于 KL 的 ~45min，因为无需 gradient checkpointing/模型反向传播）
- 显存: ~16GB（仅基础模型 fp16 推理 + predictor fp32 训练）

**正式训练命令：**
```bash
cd /root/distill_sparse_swiglu && WANDB_MODE=disabled nohup /root/miniconda3/bin/python scripts/c3_coupling_oracle.py --gpu 0 --dataset wikitext-103 > logs/c3_coupling_oracle.log 2>&1 &
```

**实验逻辑：**
- 每个 batch：基础模型 forward（no grad）→ 用冻结 KL predictor 生成 sigmoid(logits) 作为 soft target → 新 predictor 以 BCE loss 拟合这些 soft target
- 去掉了 gradient coupling（梯度不流经基础模型），保留了 KL oracle 的"什么该 prune"的信息
- 训完后对比 PPL，即可判断 hypothesis A vs B

---
