# train non nlp baseline

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_non-nlp-baseline_20260514T155423_result.json`
- **Structured JSON:** [`5781d83676292652b8e5.json`](../../sessions/57/5781d83676292652b8e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验完成

### 结果

| Method | Macro-F1 | Accuracy | F1(stag) | F1(prog) |
|--------|----------|----------|----------|----------|
| GRU Probe (ref) | 0.9055 | — | — | — |
| MeanPool+LR (ref) | 0.8435 | — | — | — |
| **Struct + LR** | **0.9874** | 0.9901 | 0.9815 | 0.9933 |
| **Struct + RF** | **0.9951** | 0.9962 | 0.9928 | 0.9974 |
| **Struct + GB** | **0.9951** | 0.9962 | 0.9928 | 0.9974 |

### 假设被否定

纯结构特征（30维）macro_f1=0.9951，远超 NL embedding probe 的 0.9055。原因是 labeling functions 本身就是结构启发式规则（edit 命令计数、命令重复检测、轨迹结果回溯），结构特征本质上在逆向工程这些 LF。

最强预测特征：`max_consecutive_similar` (LR coef=-5.53), `avg_adjacent_cmd_sim` (-3.13), `num_search_cmds` (-2.32)——这些直接对应 LF2 (command_repetition) 的判定逻辑。

### 产出
- 脚本：`non_nlp_baseline.py` (服务器)
- 结果：`data/non_nlp_baseline_results.json`
- Registry: `non-nlp-baseline` (DONE, conclusion=negative)
- Artifact: `non-nlp-baseline-results` (report)

---
