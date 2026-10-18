# diagnose eval pi05 random k07 long seed42 strict

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_random_k07_long_seed42_strict_20260527T083921_result.json`
- **Structured JSON:** [`4711dd364ae927ea77b0.json`](../../sessions/47/4711dd364ae927ea77b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 失败根因

`httpx.ConnectError: [Errno 99] Cannot assign requested address`

tokenizer 初始化时 (`AutoTokenizer.from_pretrained("google/paligemma-3b-pt-224")`)，`transformers` 内部调用了 `huggingface_hub.model_info()` 去 HF Hub 查询模型元信息（判断是否为 Mistral base model 的逻辑），网络连接失败。可能是端口耗尽或网络限制导致无法建立出站连接。

### v2 重试状态

正常运行中。PID 109152 已运行 19 分钟，v2 命令加了 `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1`，完全跳过了 HF Hub 网络调用，不会触发同样的问题。

当前进度：Task 0 已完成 30/50 episodes，成功率 100%，正在正常推进。

---
