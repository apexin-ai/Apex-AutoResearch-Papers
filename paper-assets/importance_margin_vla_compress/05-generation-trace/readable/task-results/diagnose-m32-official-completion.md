# diagnose m32 official completion

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_m32_official_completion_20260519T092239_result.json`
- **Structured JSON:** [`594e10f79dce50e3dc2c.json`](../../sessions/59/594e10f79dce50e3dc2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**训练状态**：M=32 official 训练已完成（100K steps，17:20:24 结束）。最终 train loss=0.049, eval loss=0.060。Checkpoint 1.9GB 已从 `/root/checkpoints/` 复制到项目目录。

**已执行操作**：
- Checkpoint 复制到 `/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m32_official/checkpoint.pt`
- Registry `train_smart_compress_m32_official` → ANALYZING
- Cron `train_smart_compress_m32_official` 已删除

**Eval 已启动**：
- `eval_smart_compress_m32_official` 在 cqa1:GPU3 运行（tmux session: `eval_m32_official`）
- LIBERO-Object, 500 episodes (10 tasks x 50), seed=42
- 预计运行 ~1.5h

---
