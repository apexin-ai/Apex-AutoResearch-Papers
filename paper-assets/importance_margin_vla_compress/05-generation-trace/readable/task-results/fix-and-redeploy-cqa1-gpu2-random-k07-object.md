# fix and redeploy cqa1 gpu2 random k07 object

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix-and-redeploy-cqa1-gpu2-random-k07-object_20260523T225403_result.json`
- **Structured JSON:** [`3c575c1af08f5f1f3f17.json`](../../sessions/3c/3c575c1af08f5f1f3f17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功通过所有加载阶段，正在启动评估：

- Tokenizer 加载：通过（`TRANSFORMERS_OFFLINE=1` 生效，使用缓存）
- 模型加载：通过（4143.4M params）
- GPU 2 显存：9507 MiB
- Pruning 配置：random, keep 179/256 tokens (k=0.7)
- Suite：libero_object, 10 tasks, 已开始运行

**根因**：v2 失败因为没有设置 `TRANSFORMERS_OFFLINE=1` 和 `HF_HOME=/root/autodl-tmp/.hf_cache`，导致尝试从网络下载 paligemma tokenizer 时报 `httpx.ConnectError`。v3 已修复，实验 `eval_pi05_random_k07_object_seed42_v3` 在 cqa1-33015 GPU 2 上正常运行，registry 状态已更新为 DEPLOYED。

---
