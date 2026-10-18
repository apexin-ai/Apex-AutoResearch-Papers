# deploy westd41074 pi05 attn strict k09 k085

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd41074_pi05_attn_strict_k09_k085_20260527T034113_result.json`
- **Structured JSON:** [`41a0bbc3975343aeceb6.json`](../../sessions/41/41a0bbc3975343aeceb6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

1. **Random k=0.85 strict v2 (PID 86688+86689)** — 已 kill，registry 标记 `killed`
2. **Attn k=0.9 Long strict** — GPU 2, PID 94308, RUNNING，tmux session `eval_pi05_attn_k09_strict`
3. **Attn k=0.85 Long strict** — GPU 3, PID 94384, RUNNING，tmux session `eval_pi05_attn_k085_strict`

两个进程正在加载 π0.5 模型（~35GB CPU 内存），模型加载完成后会上 GPU 开始 eval。日志路径：
- `logs/eval_pi05_attn_k09_long_seed42_strict.log`
- `logs/eval_pi05_attn_k085_long_seed42_strict.log`

---
