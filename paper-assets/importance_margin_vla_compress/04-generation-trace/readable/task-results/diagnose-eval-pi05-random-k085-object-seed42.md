# diagnose eval pi05 random k085 object seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_random_k085_object_seed42_20260521T201334_result.json`
- **Structured JSON:** [`3e80ad60559758232227.json`](../../sessions/3e/3e80ad60559758232227.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因**：网络不可达（`[Errno 101] Network is unreachable`）。`AutoTokenizer.from_pretrained('google/paligemma-3b-pt-224')` 在模型加载后尝试连接 HuggingFace Hub 失败。与同服务器 k095 实验完全相同的问题。

GPU、磁盘均正常。可以直接重跑，但启动前需 `source /etc/network_turbo` 或设置 `TRANSFORMERS_OFFLINE=1`（需 tokenizer 已缓存）。

报告已写入 `artifacts/diagnose_eval_pi05_random_k085.md`。

---
