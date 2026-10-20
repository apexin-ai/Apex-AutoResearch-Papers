# experiment d073 cycle detector baseline

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_d073-cycle-detector-baseline_20260516T034410_result.json`
- **Structured JSON:** [`757c597bc6932d578bf9.json`](../../sessions/75/757c597bc6932d578bf9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

| Method | Silver F1 | Gold F1 | 类型 |
|---|---|---|---|
| Structural GB | 0.9951 | 0.839 | Ours |
| MV baseline | — | 0.798 | Silver label |
| GRU Probe | 0.906 | 0.789 | Ours |
| **Cycle (3-gram)** | **0.7207** | **0.8410** | External baseline |
| **Cycle (2-gram)** | **0.6607** | **0.8397** | External baseline |

要点：
- 3-gram 优于 2-gram（silver 0.72 vs 0.66），最佳阈值 t=0.70
- Silver 上远低于 GB（0.72 vs 0.99），符合预期——简单 n-gram 无法捕捉结构特征的丰富信号
- Gold 上意外接近 GB（0.841 vs 0.839），说明 action-type 重复率在 gold 分布下是个不错的 heuristic
- Silver-Gold gap 极大（0.72→0.84），暗示 cycle detector 在 silver label noise 下退化严重，而 structural GB 对 noise 更鲁棒

脚本在服务器 `/root/autodl-tmp/agent_progress_probe/cycle_detector_baseline.py`，结果 JSON 在同目录 `results_cycle_detector.json`，已注册 registry `d073-cycle-detector`。

---
