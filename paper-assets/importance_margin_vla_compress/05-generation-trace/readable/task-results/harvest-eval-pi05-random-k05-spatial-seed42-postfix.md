# harvest eval pi05 random k05 spatial seed42 postfix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_eval_pi05_random_k05_spatial_seed42_postfix_20260524T005615_result.json`
- **Structured JSON:** [`7d6963ac58ae0ab6007c.json`](../../sessions/7d/7d6963ac58ae0ab6007c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 不存在（可能已在之前的 session 中删除）。

## 结果

**eval_pi05_random_k05_spatial_seed42_postfix — 失败（未产出数据）**

- **原因**：启动命令缺少 `TRANSFORMERS_OFFLINE=1` 和 `HF_HUB_OFFLINE=1`，脚本尝试从网络下载 `google/paligemma-3b-pt-224` tokenizer 时报 `Network is unreachable`，在模型加载阶段就崩溃了
- **SR**：无（未执行任何 episode）
- **与 pre-fix 71.6% 对比**：无法对比

**需要重跑**，正确的命令应包含离线环境变量（参考同服务器上 k=0.85 postfix 的成功启动命令）：
```bash
export TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=1
```

**westd-41074 GPU 状态**：全部 4 卡空闲（0 MiB / 98 GB）。

---
