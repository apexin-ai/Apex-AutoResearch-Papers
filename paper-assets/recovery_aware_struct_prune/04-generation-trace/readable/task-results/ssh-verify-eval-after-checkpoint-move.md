# ssh verify eval after checkpoint move

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_eval_after_checkpoint_move_20260520T224800_result.json`
- **Structured JSON:** [`46ec960a71e8fbf5c354.json`](../../sessions/46/46ec960a71e8fbf5c354.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. 旧路径：完全不存在
两个旧路径已被移除，无文件无 symlink：
- `/root/recovery_aware_struct_prune/grpo_standard_15_seed123_v3/` → **不存在**
- `/root/recovery_aware_struct_prune/grpo_standard_15_seed456_v3/` → **不存在**

### 2. Eval 状态：两个都已失败（EXIT_CODE=1）
两个 standard_15 eval 都因路径不存在而崩溃，错误相同：
```
OSError: Repo id must be in the form 'repo_name' or 'namespace/repo_name': 
'/root/recovery_aware_struct_prune/grpo_standard_15_seed123_v3/checkpoint-100'
```
因为设了 `HF_HUB_OFFLINE=1`，本地路径不存在后 transformers 把它当 HF repo id 解析，直接报错。

### 3. 新路径（数据盘）：存在，但 seed456 有问题
- **seed123** `/root/autodl-tmp/.../grpo_standard_15_seed123_v3/checkpoint-100/` — 完整（model.safetensors 13GB, tokenizer.json 11MB, optimizer.pt 318MB）
- **seed456** `/root/autodl-tmp/.../grpo_standard_15_seed456_v3/checkpoint-100/` — **tokenizer.json 为 0 字节**，且缺少 optimizer.pt 和 training_args.bin（移动可能被中断）

### 4. GPU 占用
| GPU | 利用率 | 显存 | 任务 |
|-----|--------|------|------|
| 0 | 97% | 29.8/95.6 GB | `grpo_cka_only_15_seed123` eval（运行中） |
| 1 | 99% | 30.3/95.6 GB | `grpo_cka_only_15_seed456` eval（运行中） |
| 2 | 0% | 空闲 | — |
| 3 | 0% | 空闲 | — |

### 需要处理
1. **seed456 checkpoint 数据损坏**：tokenizer.json 0字节，需要从备份恢复或重新复制
2. **重新提交两个 eval**：路径改为 `/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_15_seed{123,456}_v3/checkpoint-100`，可用 GPU 2/3
3. 当前 GPU 0/1 正在跑 cka_only eval，不受影响

---
