# submit baseline meanpool lr

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_baseline-meanpool-lr_20260514T095131_result.json`
- **Structured JSON:** [`77f3e614b7851b850a4c.json`](../../sessions/77/77f3e614b7851b850a4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**baseline-meanpool-lr 实验结果**

| 指标 | MeanPool+LR | GRU Probe | 差值 |
|------|------------|-----------|------|
| test_macro_f1 | 0.8435 | 0.9055 | +6.2pp |
| test_accuracy | 0.8860 | 0.9282 | |
| test_f1_stagnation | 0.7620 | 0.8593 | |
| test_f1_progress | 0.9250 | 0.9518 | |

- 修复了脚本的数据路径 bug（`data/data/embeddings.pt` → `data/embeddings.pt`）
- 移除了不需要的 MLP baseline，只保留 LR
- 最佳正则化参数 C=0.01，验证集 Macro-F1=0.861
- GRU Probe 在所有指标上均优于 MeanPool+LR，尤其在 stagnation 类别（+9.7pp），确认了时序建模的增量价值

---
