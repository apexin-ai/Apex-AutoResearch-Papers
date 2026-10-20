# ops check running experiments

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-running-experiments_20260516T051830_result.json`
- **Structured JSON:** [`2770704b14eacc14e0b9.json`](../../sessions/27/2770704b14eacc14e0b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

| # | 实验 | 服务器 | 状态 | 结果 |
|---|------|--------|------|------|
| 1 | eval_grpo_rasp_v9_step10 | westb-23072 | **RUNNING** | 249/1319 (19%), 当前 acc≈68%, ~2.3s/it |
| 2 | eval_grpo_unpruned_v2_step100 | westd-11672 | **FINISHED** | **acc=81.27%** (1072/1319) |
| 3 | eval_grpo_unpruned_v2_step90 | westd-11672 | **FINISHED** | **acc=80.59%** (1063/1319) |

### 详细结果

**实验 2 — Unpruned GRPO step-100:**
- Accuracy: 81.27% (1072/1319), stderr=1.07%
- EOS rate: 99.70%, avg response length: 209
- 路径: `/root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_unpruned_v2_step100.json`

**实验 3 — Unpruned GRPO step-90:**
- Accuracy: 80.59% (1063/1319), stderr=1.09%
- EOS rate: 99.62%, avg response length: 213
- 路径: `/root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_unpruned_v2_step90.json`

**实验 1 — RASP v9 step-10 (进行中):**
- 进度: 249/1319 (19%), 已运行 ~15 分钟
- 中间 acc: 200 样本时 68.0%
- 预计剩余: ~40 分钟 (按 ~2.3s/it)

### GPU 使用情况

| 服务器 | GPU 0 | GPU 1 |
|--------|-------|-------|
| westb-23072 | 28.7G/95.6G, **100%** (实验1占用) | **空闲** |
| westd-11672 | **空闲** | **空闲** |

### 可接新任务的卡
- **westb-23072 cuda:1** — 空闲
- **westd-11672 cuda:0** — 空闲
- **westd-11672 cuda:1** — 空闲

---
