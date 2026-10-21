# analyze ablation random occ s0

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_ablation_random_occ_s0_20260522T012745_result.json`
- **Structured JSON:** [`44c185765fe67bcd9d30.json`](../../sessions/44/44c185765fe67bcd9d30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

**训练**: 已正常完成 50005 步，EXIT_CODE=0，耗时 ~14.5h。50000 checkpoint 完整（4 model shards + action_head + occ_head + lora_adapter）。

**Loss metrics**: 不可用。wandb 未配置（entity/project 为占位符），log 仅有进度条输出。

**Eval**: 已启动运行中。
- PID: 615697
- GPU: cuda:1，NVIDIA RTX PRO 6000 (98GB)
- 配置: libero_spatial, 10 tasks × 50 rollouts
- 输出: `/root/autodl-tmp/checkpoints/ablation_random_occ_s0/eval_results.json`
- Log: `~/runs/occsafe_vla/ablation_random_occ_s0_eval.log`
- ETA: ~35 min（当前 ~4s/episode，共 500 episodes）

**待 eval 完成后对比**: 若 CAR ≈ 78%（vanilla），则 Claim 4 成立——occ 空间内容（非任意辅助 loss）才是 CAR 提升的关键。

---
