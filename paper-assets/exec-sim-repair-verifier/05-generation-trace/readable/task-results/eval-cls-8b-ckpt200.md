# eval cls 8b ckpt200

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cls-8b-ckpt200_20260513T213258_result.json`
- **Structured JSON:** [`c98a0df425b04fc76fd8.json`](../../sessions/c9/c98a0df425b04fc76fd8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## CLS 8B (Qwen3-8B, checkpoint-200, seed=42) 评估结果

| 指标 | CLS 8B ckpt-200 | CLS v5 baseline | 差值 |
|------|-----------------|-----------------|------|
| **Accuracy** | 71.37% | 76.92% | **-5.55pp** |
| **F1 macro** | 69.05% | — | — |
| **fail_f1** | 60.57% | 65.01% | **-4.44pp** |
| **pass_f1** | 77.53% | 82.78% | **-5.25pp** |
| **fail_precision** | 48.26% | — | — |
| **fail_recall** | 81.29% | — | — |
| **pass_precision** | 90.71% | — | — |
| **pass_recall** | 67.69% | — | — |

**Confusion Matrix:**
```
              Predicted
              fail    pass
Actual fail   2151     495
Actual pass   2306    4832
```

**Unparseable:** 136 / 9784 = 1.39%

**关键发现：**

1. **Accuracy 低于 majority baseline**（71.37% vs 73.0%），gap = -1.6pp，模型表现甚至不如直接预测多数类
2. **全面低于 CLS v5 baseline**，accuracy -5.55pp，fail_f1 -4.44pp，pass_f1 -5.25pp
3. **fail 类严重过预测**：recall 81.3% 但 precision 仅 48.3%，模型把大量 pass 误判为 fail（FN=2306）
4. **136 条 unparseable**（1.39%），用 majority fallback 处理
5. 运行环境：westd (SeetaCloud)，transformers 5.8.0，batch_size=8，max_seq_length=2048

checkpoint-200 的 8B 模型明显欠拟合或训练策略有问题，建议检查后续 checkpoint 或训练超参。

---
