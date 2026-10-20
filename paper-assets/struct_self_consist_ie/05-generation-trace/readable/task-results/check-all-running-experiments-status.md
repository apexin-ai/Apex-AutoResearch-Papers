# check all running experiments status

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_all_running_experiments_status_20260515T183532_result.json`
- **Structured JSON:** [`112d1634a7e1206069f8.json`](../../sessions/11/112d1634a7e1206069f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### 1. exp_freeform_seed123 — **COMPLETED** → ANALYZING
- 进程 207084 已退出
- 551 instances × 8 samples = 4408 total, 4406 parsed (99.95%)
- 耗时 228s
- 输出: `results/exp_freeform_ablation_seed123/samples.jsonl` (7.16MB, 551行)

### 2. exp_freeform_seed456 — **COMPLETED** → ANALYZING
- 进程 207157 已退出
- 551 instances × 8 samples = 4408 total, 4406 parsed (99.95%)
- 耗时 229s
- 输出: `results/exp_freeform_ablation_seed456/samples.jsonl` (7.16MB, 551行)

### 3. exp_qwen3_4b_conll_finetune — **RUNNING** (不改状态)
- GPU 0: 14902/32607 MiB, 42% utilization
- 进度: step **3070/4390** (69.93%), epoch 3.50
- loss: 0.0201, eval_loss: 0.0293 (step 3000)
- 已运行 1h47m, 预估剩余 ~46min
- 最新 checkpoint: `checkpoint-3000`
- 日志位置: `checkpoints/qwen3-4b-conll2003-lora/trainer_log.jsonl`（注意: `~/runs/` 下无此实验 log）

---
