# ssh m023 verify standard 15 v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_m023_verify_standard_15_v2_20260520T215600_result.json`
- **Structured JSON:** [`5b26aadf0a814a6bc9aa.json`](../../sessions/5b/5b26aadf0a814a6bc9aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**两个训练均已卡死，未真正运行。**

### 状态

| 实验 | PID | GPU | 显存 | 状态 |
|------|-----|-----|------|------|
| grpo_standard_15_seed123_v2 | 287258 (python: 287263) | cuda:2 | **3 MiB** | 卡在模型加载 |
| grpo_standard_15_seed456_v2 | 287400 (python: 287405) | cuda:3 | **3 MiB** | 卡在模型加载 |

### 原因

两个进程都在尝试从 HuggingFace 下载 `sft_standard_15`，但网络不通：

```
Loading pruned model from sft_standard_15
'[Errno 101] Network is unreachable' thrown while requesting HEAD https://huggingface.co/sft_standard_15/resolve/main/config.json
Retrying in 1s [Retry 1/5].
```

`--model_path sft_standard_15` 被当成 HuggingFace model ID 而非本地路径。需要改为完整本地路径（如 `/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_15`），或者设置 `HF_HUB_OFFLINE=1` 强制离线加载。

两个进程会在 5 次重试后失败，需要 kill 后用正确路径重新提交。

---
