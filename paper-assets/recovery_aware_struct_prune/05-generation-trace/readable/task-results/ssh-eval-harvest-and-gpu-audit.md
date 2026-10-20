# ssh eval harvest and gpu audit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_eval_harvest_and_gpu_audit_20260521T053523_result.json`
- **Structured JSON:** [`ff6a3555ba0d684e63a2.json`](../../sessions/ff/ff6a3555ba0d684e63a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Eval 状态总结

### westd-29022（4 GPU）

| Eval | 进度 | 状态 | 关键数据 |
|------|------|------|---------|
| **cka_only_25 v4** | 2/1319 (0%) | **死了** — 无对应进程 | log 停在加载数据集后 |
| **cka_only_25 v3** | 282/1319 (21%) | **运行中** PID 322443, GPU 0 | **acc=0.6000** @250, ~2.5s/it |
| **random_20 v3** | 448/1319 (34%) | log 有近期输出至 13:33，但 ps 中无匹配进程 → 可能是旧 run 残留 log | **acc=0.4875** @400 |
| **random_20 v2** | log 仅显示 5/1319 | **运行中** PID 322611, GPU 1 | log 输出未 flush，实际进度应远超 5（进程已跑 47min） |

### westb-23072（2 GPU）

| 任务 | 进度 | 状态 |
|------|------|------|
| **eval_math500 sft_standard_25** | 158/500 (32%) | **运行中** PID 62714, GPU 0, ~70-80s/sample |
| **grpo_standard_25_westb** | 81/100 steps (81%) | **运行中** PID 64194, GPU 1, ~117s/step |

---

## 6-GPU 对账表

| 服务器 | GPU | 显存占用 | 进程 | PID | 状态 |
|--------|-----|---------|------|-----|------|
| westd-29022 | cuda:0 | 28933 MiB (99%) | eval_gsm8k cka_only_25 v3 | 322443 | 运行中 21% |
| westd-29022 | cuda:1 | 26219 MiB (91%) | eval_gsm8k random_20 v2 | 322611 | 运行中 (log 未 flush) |
| westd-29022 | cuda:2 | 0 MiB (0%) | — | — | **空闲** |
| westd-29022 | cuda:3 | 0 MiB (0%) | — | — | **空闲** |
| westb-23072 | cuda:0 | 16867 MiB (99%) | eval_math500 sft_standard_25 | 62714 | 运行中 32% |
| westb-23072 | cuda:1 | 55535 MiB (100%) | grpo_standard_25_westb | 64194 | 运行中 81/100 steps |

**注意**: v4 (cka) 已死，westd GPU 2/3 空闲可用。grpo_standard_25 预计还需 ~37 分钟完成剩余 19 步。

---
