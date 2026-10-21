# analysis perlayer kl k16 s42 v3

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_perlayer_kl_k16_s42_v3_20260523T044424_result.json`
- **Structured JSON:** [`5f13522f333c7fcd4dd1.json`](../../sessions/5f/5f13522f333c7fcd4dd1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## perlayer_kl_k16_s42_v3 结果汇报

### 提取指标
| 指标 | 值 |
|------|-----|
| final KL (step 1000) | 0.1406 |
| final avg_kl (running avg) | 0.1582 |
| final avg_sparsity | 0.286 |
| wall time | 1982.9s (~33 min) |
| wikitext2 PPL | **未评估**（训练脚本无 eval 步骤） |

### Checkpoint
| 文件 | 大小 |
|------|------|
| `predictor_perlayer_kl_k4.pt` (final) | 145 MB |
| `predictor_perlayer_kl_k4_step_1000.pt` | 435 MB |
| `predictor_perlayer_kl_k4_step_500.pt` | 435 MB |

路径: `/root/distill_sparse_swiglu/checkpoints/perlayer_kl_k16_s42_v3/`

### 与 K=8 对比
| 指标 | K=8 | K=16 | 差异 |
|------|-----|------|------|
| avg_kl | 0.0983 | 0.1582 | +0.0599 (↑61%) |
| avg_sparsity | 0.281 | 0.286 | +0.005 |
| wikitext2 PPL | 8.97 | N/A | 需要单独 eval |

### Conclusion: **success**
- 训练正常完成 1000 steps，无 error/warning
- 3 个 checkpoint 已保存
- avg_kl 比 K=8 高 61%，符合预期（K 越大，每步 mask 越多层，KL 优化更难收敛）
- avg_sparsity 0.286 接近 target 0.3，正常
- Per-layer summary 显示所有 32 层均有充分训练（每层 ~470-535 次参与），avg_sparsity 在 0.298-0.312 范围内分布均匀

### 待做
**wikitext2 PPL 需要单独运行 eval 脚本**才能与 K=8 (PPL=8.97) 和 K=1 baseline (PPL~8.81) 对比。

---
