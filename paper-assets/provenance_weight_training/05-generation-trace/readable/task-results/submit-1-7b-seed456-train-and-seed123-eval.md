# submit 1 7b seed456 train and seed123 eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_1_7b_seed456_train_and_seed123_eval_20260520T155636_result.json`
- **Structured JSON:** [`6d02e141fb86efe9935c.json`](../../sessions/6d/6d02e141fb86efe9935c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 job 全部确认在跑。

## 汇总

### Part A: seed123 checkpoint
- **uniform_1_7b_seed123**: 存在，`model.safetensors` 3.4GB，May 19 12:03
- **adaptive_1_7b_seed123**: 存在，`model.safetensors` 3.4GB，May 19 09:04

### Part B: seed456 训练
| 实验 | GPU | PID | 状态 |
|------|-----|-----|------|
| uniform_1_7b_seed456 | cuda:2 | 494625 | RUNNING, ~step 21/6103 |
| adaptive_1_7b_seed456 | cuda:3 | 494706 | RUNNING, ~step 20/6103 |

ETA ~5h（2.9s/step × 6103 steps）。Registry 已更新为 RUNNING。

### Part C: seed123 eval
| 实验 | GPU | PID | 流程 |
|------|-----|-----|------|
| eval_uniform_1_7b_seed123 | cuda:0 | 495407 | OWT PPL → Wiki PPL → lm_eval downstream |
| eval_adaptive_1_7b_seed123 | cuda:1 | 495970 | OWT PPL → Wiki PPL → lm_eval downstream |

模型已加载完成，正在跑 OpenWebText PPL。三阶段串行：OOD PPL × 2 + downstream 5 tasks。

### 磁盘
`/root/autodl-tmp`: 90GB 可用，2 个新训练需 ~30GB，余量充足。

### 待办
eval 完成后需要读取结果文件并更新 seed123 registry metrics（eval_ppl_openwebtext, eval_ppl_wikipedia, downstream_*）。

---
