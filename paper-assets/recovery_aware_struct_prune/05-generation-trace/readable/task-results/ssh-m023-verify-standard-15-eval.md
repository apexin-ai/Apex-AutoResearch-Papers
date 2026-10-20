# ssh m023 verify standard 15 eval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_m023_verify_standard_15_eval_20260520T224714_result.json`
- **Structured JSON:** [`315135ab55452a17e939.json`](../../sessions/31/315135ab55452a17e939.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### Standard 15% eval — 两个都失败了

两个 seed 启动后立即报错退出，GPU 2/3 显存 0 MiB，进程已不在。错误相同：

```
OSError: Repo id must be in the form 'repo_name' or 'namespace/repo_name': 
'/root/recovery_aware_struct_prune/grpo_standard_15_seed{123,456}_v3/checkpoint-100'
```

checkpoint 路径在根分区 `/root/recovery_aware_struct_prune/`，transformers 无法将其识别为本地路径。可能原因：
1. checkpoint 不存在于该路径（应在 `/root/autodl-tmp/...`）
2. `from_pretrained()` 调用方式有问题

需要确认 checkpoint 实际位置。

### CKA-only 15% eval — 正常运行中

| Eval | GPU | 进度 | 当前 acc | ETA |
|------|-----|------|---------|-----|
| seed123 | cuda:0 | 760/1319 (58%) | 73.20% (@750) | ~32min |
| seed456 | cuda:1 | 672/1319 (51%) | 72.46% (@650) | ~29min |

两个 CKA-only eval 预计约 30 分钟内完成，结果文件尚未生成。

---

要不要我查一下 standard checkpoint 的实际路径，定位问题？

---
