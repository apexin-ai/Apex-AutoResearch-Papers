# exp perlayer kl k8 s42

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_perlayer_kl_k8_s42_20260523T020035_result.json`
- **Structured JSON:** [`8e82c2f300dfb5978e7a.json`](../../sessions/8e/8e82c2f300dfb5978e7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已提交，registry 已更新。

**总结：**
- **PID**: 98975
- **GPU**: westd-34887 cuda:1
- **脚本**: `src/train_perlayer_kl_k4.py --num_masked_layers 8`
- **参数**: seed=42, 1000 steps, sparsity=0.3, gradient_checkpointing, save_every=500
- **日志**: `logs/perlayer_kl_k8_s42.log`
- **Checkpoint**: `checkpoints/perlayer_kl_k8_s42/predictor_perlayer_kl_k4.pt`
- **Registry**: `perlayer_kl_k8_s42` → RUNNING

基于 K=4 s42 的训练速度（~1.86s/step），预计 1000 steps 约 31 分钟完成。Cron 会自动检测完成并触发 eval。

---
