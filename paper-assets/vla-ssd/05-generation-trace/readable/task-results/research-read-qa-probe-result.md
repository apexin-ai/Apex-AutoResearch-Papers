# research read qa probe result

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_read_qa_probe_result_20260516T223757_result.json`
- **Structured JSON:** [`d325226189c6cc6857fd.json`](../../sessions/d3/d325226189c6cc6857fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果如下。文件已写入，但进程仍在运行（可能在跑更多层，当前只有 L0）。

---

## QA Probe Classification Results

**Method**: Classification probe (LogisticRegression)

### Progress 4-class

| Condition | Acc | F1 |
|-----------|------|------|
| **trained L0** | 0.9474 | 0.9476 |
| **untrained L0** | 0.9474 | 0.9476 |
| **dino_cls** | 0.9545 | 0.9544 |
| **projector** | 0.9474 | 0.9476 |

### Subtask Binary

| Condition | Acc | F1 |
|-----------|------|------|
| **trained L0** | 0.9829 | 0.9829 |
| **untrained L0** | 0.9829 | 0.9829 |
| **dino_cls** | 0.9836 | 0.9836 |
| **projector** | 0.9829 | 0.9829 |

---

**状态**: 进程仍在运行（tmux session `qa_probe_classification` 活跃，python 进程占 CPU 3877%）。当前结果只有 L0 层，后续层正在计算中。Log 显示大量 LogisticRegression convergence warnings（lbfgs 达到 max_iter=1000 上限）。

**初步观察**（仅 L0，不下结论）：trained 与 untrained 在 L0 上数值完全相同，dino_cls 略高。需等全部层跑完再看趋势。

---
