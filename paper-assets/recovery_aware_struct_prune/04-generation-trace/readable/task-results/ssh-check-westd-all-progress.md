# ssh check westd all progress

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_westd_all_progress_20260520T224134_result.json`
- **Structured JSON:** [`d934c661a2bd505ed5d4.json`](../../sessions/d9/d934c661a2bd505ed5d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-29022 状态汇总

### GRPO 训练（GPU 2 & 3）— 全部失败

| 任务 | 状态 | 错误 |
|------|------|------|
| grpo_standard_15_seed123_v3 | **FAILED** (EXIT_CODE=1) | `RuntimeError: unexpected pos 111488 vs 111382` — optimizer state写入损坏 |
| grpo_standard_15_seed456_v3 | **FAILED** (EXIT_CODE=1) | `No space left on device (os error 28)` — tokenizer保存时磁盘满 |

- 两个任务均未成功保存 checkpoint（目录不存在）
- GPU 2/3 当前空闲（0% utilization, 0 MiB memory）

### 根因：根分区 100% 满

```
overlay   30G   30G   2.1M  100%  /
```

根分区只剩 2.1M，seed456 直接报 `No space left on device`，seed123 的 optimizer state 写入损坏大概率也是磁盘满导致。数据盘正常（88G 可用）。

### CKA-only Eval（GPU 0 & 1）— 进行中

| 任务 | 进度 | 当前 Accuracy | ETA |
|------|------|--------------|-----|
| eval_gsm8k_grpo_cka_only_15_seed123 | **57%** (755/1319) | 73.20% @ 750 samples | ~45 min |
| eval_gsm8k_grpo_cka_only_15_seed456 | **47%** (614/1319) | 73.50% @ 600 samples | ~55 min |

两个 eval 仍在正常运行，GPU 0/1 利用率 91-92%。

### 需要处理

GRPO 训练重跑前必须先清理根分区。需要排查什么占满了根分区（wandb logs、临时文件、HF cache 等可能写到了 `/root/` 而非 `/root/autodl-tmp/`）。

---
