# ssh d046 cwm eval immediate check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d046-cwm-eval-immediate-check_20260513T075818_result.json`
- **Structured JSON:** [`9fca90286724f589192c.json`](../../sessions/9f/9fca90286724f589192c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## CWM v10 Eval 状态汇报

### PID 123610: **已结束**（进程不存在）

### 评估已完成，结果文件：

| 文件 | 大小 | 时间 |
|------|------|------|
| `eval_repo_cwm.json` | 997B | May 13 15:54 |
| `eval_repo_cwm_predictions.jsonl` | 3.8MB / 9784 行 | May 13 15:54 |
| `eval_repo_cwm_summary.json` | **不存在**（结果在 `eval_repo_cwm.json` 里） |

### 核心指标（`eval_repo_cwm.json`）：

| 指标 | 值 |
|------|-----|
| **Accuracy** | **69.91%** |
| Majority baseline | 72.96% |
| **Gap vs majority** | **-3.05 pp** ❌ |
| F1 (fail) | 11.54 |
| F1 (pass) | 81.87 |
| F1 (macro) | 46.71 |
| Precision fail / pass | 28.15 / 73.04 |
| Recall fail / pass | 7.26 / 93.14 |
| **Unparseable** | **9102 / 9784 (93%)** |
| Truncated | 478 (4.89%), 其中 accuracy 仅 21.76% |

### 混淆矩阵：
```
              Pred Fail  Pred Pass
Actual Fail      192       2454
Actual Pass      490       6648
```
Support: fail=2646, pass=7138

### 关键问题：
1. **93% unparseable** — 模型输出几乎全部无法解析为结构化结果，解析逻辑或 prompt 格式可能有严重问题
2. **低于 majority baseline 3pp** — 模型表现不如简单多数投票
3. **Fail 类召回率仅 7.26%** — 几乎无法识别 fail 样本，模型倾向于全部预测为 pass
4. Checkpoint 路径显示用的是 `checkpoints_repo_cwm_v9/checkpoint-400`，而非 v10

### GPU 状态：
4x RTX 5090 全部空闲（0% utilization, 0 MiB used）

### 配置：
- 模型: Qwen3-4B, max_seq_length=2048, max_new_tokens=64, batch_size=8

---
