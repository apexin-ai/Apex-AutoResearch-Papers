# code oh full finetune

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_oh-full-finetune_20260514T150345_result.json`
- **Structured JSON:** [`161551f3af560d5d8486.json`](../../sessions/16/161551f3af560d5d8486.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## oh-full-finetune 完成

### 核心结果

| 数据比例 | Macro-F1 | F1(stag) | F1(prog) |
|---------|----------|----------|----------|
| 0% (zero-shot) | 0.532 | 0.200 | 0.864 |
| 5% | 0.570 | — | — |
| 10% | 0.574 | — | — |
| 20% | 0.611 | — | — |
| 50% | 0.688 | — | — |
| **100%** | **0.751** | **0.544** | **0.959** |
| SWE-Agent in-domain | 0.906 | — | — |

### 关键发现

1. **100% > 50%，曲线未饱和**：100% OH macro_f1=0.751 比 50% 的 0.688 提升 +0.063，说明 50% 时并非数据量饱和，更多数据仍能持续提升性能。

2. **但距离 in-domain 仍有大差距**：0.751 vs SWE-Agent in-domain 0.906，差距 0.155。这个 gap 可归因于 LF 噪声标签的可靠性上限——即使用全部数据，噪声标签的质量限制了模型能学到的信号。

3. **严重的灾难性遗忘**：OH 微调后在 SWE-Agent 测试集上 macro_f1 从 0.789 降到 0.600（Δ=-0.189），需要 EWC/replay 等正则化手段。

### 对 reviewer 的回应

50%→100% 的持续提升说明 LF 可靠性天花板高于 0.688 但低于 0.906。Few-shot 曲线的增长趋势（log-linear）表明瓶颈同时来自数据量和 LF 噪声，非单一因素。Best epoch=20（达到上限），模型在当前训练配置下可能仍未完全收敛。

---
