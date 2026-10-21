# deploy westd41074 gpu1 pi05 attn k05

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd41074_gpu1_pi05_attn_k05_20260527T121035_result.json`
- **Structured JSON:** [`1f18db87edba46914f8c.json`](../../sessions/1f/1f18db87edba46914f8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

π0.5 模型加载需要几分钟（~15GB 权重）。进程已启动，tmux session `pi05_attn_k05` 运行中。

部署完成：

| 项目 | 值 |
|------|-----|
| Registry | `eval_pi05_attn_k05_long_seed42_strict_w41` → RUNNING |
| 服务器 | westd-41074 GPU1 (`CUDA_VISIBLE_DEVICES=1`) |
| tmux session | `pi05_attn_k05` |
| 日志 | `eval_pi05_attn_k05_long_seed42_strict_w41.log` |
| 参数 | `--prune_mode attention --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 42` |
| offline flags | HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME + MUJOCO_GL=egl ✓ |

模型正在加载中，预计几分钟后 GPU1 显存会上升并开始评估。

---
