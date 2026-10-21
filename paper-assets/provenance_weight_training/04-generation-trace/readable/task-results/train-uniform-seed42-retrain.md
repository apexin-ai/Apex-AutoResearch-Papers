# train uniform seed42 retrain

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_uniform_seed42_retrain_20260517T145620_result.json`
- **Structured JSON:** [`dbb02af750c7ba01430b.json`](../../sessions/db/dbb02af750c7ba01430b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已正常启动并稳定运行。

**总结：**
- 实验 ID: `qwen06b_uniform_seed42`
- 服务器: westd-41312, GPU: cuda:0
- 配置: Qwen3-0.6B, uniform weighting, seed=42, 6103 steps, save_steps=200
- 输出: `/root/autodl-tmp/provenance_weight_training/output/models/uniform_seed42`
- 速度: ~2.15s/step，预计总训练时间 ~3.6 小时
- 日志: `~/runs/provenance_weight_training/qwen06b_uniform_seed42.log`

注：wandb 在此服务器未配置 API key，已设为 disabled。eval_steps 从 500 调整为 200 以匹配 save_steps（HuggingFace Trainer 要求 save_steps 是 eval_steps 的整数倍）。

---
