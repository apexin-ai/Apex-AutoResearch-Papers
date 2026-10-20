# ssh deepseek cwm eval results

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_deepseek-cwm-eval-results_20260520T011720_result.json`
- **Structured JSON:** [`2a5ac8071ceb227dbd46.json`](../../sessions/2a/2a5ac8071ceb227dbd46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## DeepSeek CWM s42 e3 seq4096 Eval 结果

| 指标 | 值 |
|------|-----|
| **N** | 83 |
| **Accuracy** | 54/83 = **65.06%** |
| **Unparseable rate** | 52/83 = **62.65%** |
| **Truncated** | 0/83 = 0% |
| **Parseable-only acc** | 12/31 = **38.71%** |

### Confusion Matrix

|  | Pred=1 | Pred=0 |
|--|--------|--------|
| **Label=1** | TP=52 | FN=15 |
| **Label=0** | FP=14 | TN=2 |

- **Precision**: 0.7879
- **Recall**: 0.7761
- **F1**: 0.7820
- Label分布: pos=67, neg=16 (极度不均衡)
- Pred分布: pos=66, neg=17

### Unparseable 分析

52条 unparseable 样本**全部被默认判为 pred=1**（pass），其中42条 label=1 → 正确率 80.77%。这意味着高 accuracy 主要来自 unparseable 默认 pass + 正样本占比高（67/83=80.7%），而非模型真正的判别能力。

### 可解析样本的真实表现

31条可解析样本 accuracy 仅 **38.71%**，比随机猜还差。模型在能解析的情况下判别能力极弱。

### Gen Length

mean=1706 chars, median=1727, min=1241, max=2624, stdev=277

### GPU 状态

| GPU | Util | Memory |
|-----|------|--------|
| 0 | 99% | 21253/32607 MiB (占用中) |
| **1** | 100% | **0 MiB** (已释放，util=100%可能是瞬时读数) |
| **2** | 0% | **0 MiB** (已释放) |
| 3 | 95% | 31259/32607 MiB (占用中) |

**结论**: 这个 checkpoint 效果很差。unparseable rate 62.65% 说明模型大量生成无法解析的输出；可解析部分 accuracy 38.71% 低于 baseline。高整体 accuracy 是 unparseable→默认pass + 正样本占比 80.7% 的假象。

---
