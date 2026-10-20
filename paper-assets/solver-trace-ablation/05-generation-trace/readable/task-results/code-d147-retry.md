# code d147 retry

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d147-retry_20260519T143154_result.json`
- **Structured JSON:** [`6321e992b444db12e20f.json`](../../sessions/63/6321e992b444db12e20f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D146 pipeline 正在运行，step 1 已完成。

---

## 报告

| 项目 | 结果 |
|------|------|
| **1. LLaMA completion 样本** | 无。d144 训练在 5 步后因 `wandb.errors.UsageError: No API key configured` 崩溃，reward_log 5 步全零（reward=0, prove_rate=0, parse_rate=1.0），无 completion 文本字段 |
| **2. Kill + 清理** | d144 tmux 已 kill，checkpoint 已删，额外清理了一个 7.2GB 僵尸 LLaMA CPU 推理进程（PID 400818）和重复 dry-run 进程 |
| **3. ProofFOL configs** | `configs/grpo_prooffol_exec_only.yaml` + `configs/grpo_prooffol_isr_b01.yaml` 已创建（data_path → `data/prooffol_train_500.jsonl`） |
| **4. Dry-run parse_rate** | **1.000** (step 1, 15.54s/step) |
| **5. Pipeline** | tmux session `d146-pf-pipeline`，6 runs 串行（exec s42/s43/s44 → isr s42/s43/s44），GPU:0 占用 91GB，util 88%，step 1 已完成（16.33s/it → 预估 exec-s42 约 2.3h，全 pipeline 约 14h） |
| **6. 磁盘** | 199G 可用 / 250G（21% used） |

---
