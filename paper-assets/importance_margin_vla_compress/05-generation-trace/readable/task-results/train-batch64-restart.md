# train batch64 restart

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_batch64_restart_20260517T065140_result.json`
- **Structured JSON:** [`afc65c7dcc528861f390.json`](../../sessions/af/afc65c7dcc528861f390.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**`libero_fullft_batch64_v2` 已在 cqa1-33015 GPU 1 上启动。**

- Config: `save_every` 改为 5000（原 10000）
- 环境修复：设了 `HF_HOME=/root/autodl-tmp/.hf_cache`、`HF_HUB_OFFLINE=1`（服务器无法访问 huggingface.co）、`WANDB_MODE=offline`，并创建了 lerobot 数据集的符号链接以支持离线加载
- 训练状态：step 50 已达，loss 1.5052→1.3758，sps≈0.27，GPU 显存 2727 MiB
- 预计 ~4.3 天完成 100K steps
- 首个 checkpoint 将在 step 5000 保存（约 5 小时后）
- Registry 已注册为 RUNNING

---
