# analyze eval pi05 attn k095 long seed42 strict w41

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_attn_k095_long_seed42_strict_w41_20260527T120433_result.json`
- **Structured JSON:** [`b3fa80a8e92c5662520d.json`](../../sessions/b3/b3fa80a8e92c5662520d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**实验失败** — 启动后立即崩溃，未产生任何 eval 数据。

**原因**: 启动命令缺少 `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1` 环境变量（C004 违规）。`make_pre_post_processors()` (line 464) 调用 `AutoTokenizer.from_pretrained('google/paligemma-3b-pt-224')` 尝试联网，westd-41074 无外网访问，报 `[Errno 101] Network is unreachable`。

**需要重跑**: 启动命令需加上 `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl`。k=0.95 三方法 strict 对比仍缺 Attn 数据点。

---
