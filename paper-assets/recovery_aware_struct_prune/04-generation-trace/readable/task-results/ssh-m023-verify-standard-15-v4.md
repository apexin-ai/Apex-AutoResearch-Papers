# ssh m023 verify standard 15 v4

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_m023_verify_standard_15_v4_20260520T225004_result.json`
- **Structured JSON:** [`c3c7d7fc0cd5cb68ee9e.json`](../../sessions/c3/c3c7d7fc0cd5cb68ee9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## M023 验证结果：v4 双双失败

### 原因
两个 seed 完全相同的错误：

```
ConnectionError: Couldn't reach 'openai/gsm8k' on the Hub (OfflineModeIsEnabled)
```

`train_grpo_v5.py:164` 调用 `load_dataset("openai/gsm8k", ...)` 时触发离线模式限制。

### 验证清单

| 项目 | 状态 |
|------|------|
| GPU 2/3 显存 > 10GB | ❌ 0 MiB / 0 MiB（进程已退出） |
| 无 "No space left" | ✅ 磁盘正常（根 17%, 数据盘 90%) |
| 绝对路径加载模型 | ✅ `Loading pruned model from /root/autodl-tmp/...` |
| output_dir 数据盘创建 | ⚠️ 目录创建了但为空（训练未开始就崩了） |
| 无 RuntimeError | ❌ ConnectionError: OfflineModeIsEnabled |

### 根因

启动命令大概率包含了 `HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1`（与同服务器上的 eval 任务一样），或者这些变量在环境中全局设置了。GSM8K 数据集需要从 Hub 下载但被离线模式阻断。

### 修复方向

1. 去掉启动命令中的 `HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1`
2. 或者先缓存 GSM8K 数据集再启动离线训练
3. 或者让 `train_grpo_v5.py` 支持从本地路径加载已缓存的 GSM8K

---
