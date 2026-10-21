# ssh fewrel 80rel status check

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fewrel-80rel-status-check_20260515T125957_result.json`
- **Structured JSON:** [`9bbc3ce27fe24181a056.json`](../../sessions/9b/9bbc3ce27fe24181a056.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**实验状态：正在运行**

| 项目 | 状态 |
|------|------|
| PID 267149 | 存活，tmux session `exp_fewrel_formal_80rel` 正常 |
| 阶段 | exp1 的 extract 阶段（vLLM 推理中） |
| 进度 | 41/110 batches 完成（~37%），当前在 `count_1_random_33` |
| GPU | GPU 0: 94217/97887 MiB 占用，利用率 14%（vLLM 推理为主，burst 模式正常） |
| 启动时间 | 2026-05-15 20:57（运行约 3 分钟） |
| 输出目录 | `artifacts/fewrel_formal_full/`（已有 preprocess_exp1.json、batch_config_exp1.json、relation_sim_matrix.pt） |

**实验计划**：exp1 完成后会自动继续 exp2（同一 tmux session 串行执行）。总推理量约 13,200 samples（110 batches × 12 samples/batch × 各 count 级别）。

---
