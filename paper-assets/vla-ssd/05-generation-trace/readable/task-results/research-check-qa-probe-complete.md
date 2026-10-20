# research check qa probe complete

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_check_qa_probe_complete_20260516T230242_result.json`
- **Structured JSON:** [`8fb31beedaf5ca22115e.json`](../../sessions/8f/8fb31beedaf5ca22115e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

| 项目 | 状态 |
|------|------|
| **tmux session** | `STILL_RUNNING` |
| **Python 进程** | PID 744978, CPU 3689%, 已运行 2240 分钟 (~37 小时), 占用 ~2.1GB RAM |
| **GPU** | 无 GPU 显存占用（纯 CPU sklearn 任务） |
| **结果文件** | 1548 bytes, 最后修改 May 17 06:01 |
| **已完成层** | 2/18 (L0 trained + L0 untrained) |
| **当前状态** | 仍在跑，log 充满 sklearn ConvergenceWarning（lbfgs 1000 iter 未收敛） |

**结果数据** (目前只有 L0):

```
=== PROGRESS 4-CLASS ===
dino_cls:   acc=0.9545, f1=0.9544
projector:  acc=0.9474, f1=0.9476
trained L0: acc=0.9474, f1=0.9476
untrained L0: acc=0.9474, f1=0.9476

=== SUBTASK BINARY ===
dino_cls:   acc=0.9836, f1=0.9836
projector:  acc=0.9829, f1=0.9829
trained L0: acc=0.9829, f1=0.9829
untrained L0: acc=0.9829, f1=0.9829
```

**问题**: 进程跑了 37 小时但只完成了 L0。大量 ConvergenceWarning 表明后续层的 LogisticRegression 在 1000 iter 内不收敛，导致每个 cross-validation fold 耗时极长。可能卡在 L1 或之后的某层上。

---
