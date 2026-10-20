# ops check 05B d025 checkpoint

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_05B_d025_checkpoint_20260514T215758_result.json`
- **Structured JSON:** [`dc3727c755e664e2fc65.json`](../../sessions/dc/dc3727c755e664e2fc65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

trainer_state.json 确认 `global_step: 3384`, `epoch: 1.0`，训练完整跑完。

**汇报：**

| 项目 | 结果 |
|------|------|
| **Checkpoint 路径** | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42/lora_adapter/` |
| **Adapter 权重** | `adapter_model.safetensors` (34M)，完整 |
| **训练完成度** | 3384/3384 steps, epoch=1.0，完整完成 |
| **训练配置** | LoRA r=16 α=32, lr=2e-4, 54133 samples, seed=42 |
| **已有 eval** | `Qwen2.5-0.5B_d025_s42_aligned/` (eval_results.json 2.0M, correctness_matrix.json 112K, item_responses.json 2.3M) |
| **Para aligned eval** | `Qwen2.5-0.5B_d025_s42_para_aligned/` 也已存在 |

**结论：** Checkpoint 有效且完整。Aligned eval 和 para_aligned eval **均已跑完**，无需补跑。d025 数据点已可直接用于 dose-response 曲线。

---
