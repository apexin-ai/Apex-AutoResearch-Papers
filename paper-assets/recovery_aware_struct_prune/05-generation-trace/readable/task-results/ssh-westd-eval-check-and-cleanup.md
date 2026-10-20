# ssh westd eval check and cleanup

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd_eval_check_and_cleanup_20260521T034354_result.json`
- **Structured JSON:** [`80204adc5ffbb714629e.json`](../../sessions/80/80204adc5ffbb714629e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GRPO 正在加载模型，运行正常。

---

## 汇报

### 1. eval_gsm8k_grpo_cka_only_25 状态
**已失败。** 没有活跃进程，没有 tmux session，所有 GPU 0MiB。
- Log 内容：`python: can't open file '/root/recovery_aware_struct_prune/eval_gsm8k.py': [Errno 2] No such file or directory` (EXIT_CODE=2)
- 原因：启动命令路径错误，应为 `src/eval_gsm8k.py` 而非 `eval_gsm8k.py`
- 需要用正确路径重新提交

### 2. 磁盘清理
| | Used | Avail | Use% |
|---|---|---|---|
| 清理前 | 610G | 9.5G | 99% |
| 清理后 | 588G | **32G** | 95% |

删除了两个重复的 checkpoint-100 目录（root 级别已有相同 model.safetensors）：
- `grpo_cka_only_20_seed456/checkpoint-100` (~12G)
- `grpo_cka_only_25/checkpoint-100` (~11G)

无 optimizer.pt 文件可清理。

### 3. GRPO Random 20% 已启动
- **exp_id**: grpo_random_20
- **server**: westd-29022, **GPU**: cuda:0
- **PID**: 317332, **tmux session**: grpo_random_20
- **log**: `~/runs/recovery_aware_struct_prune/grpo_random_20.log`
- 状态：模型加载中，检测到 pruned 结构（non-uniform MLP/attention）

---
