# diagnosis ext val final check and melt

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_ext-val-final-check-and-melt_20260519T231621_result.json`
- **Structured JSON:** [`44e1865a386efc835bd3.json`](../../sessions/44/44e1865a386efc835bd3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**状态总结：**

| Task | 完成 | Int DR | Det DR | ΔDR | D/I/N |
|------|------|--------|--------|-----|-------|
| boil | 20/20 | 55% | 25% | +30% | 6/0/14 |
| use-thermometer | 20/20 | 50% | 20% | +30% | 7/1/12 |
| find-living-thing | 20/20 | 55% | 15% | +40% | 10/0/10 |
| power-component | 20/20 | 50% | 15% | +35% | 7/0/13 |
| melt | **0/20** | — | — | — | — |

**关键发现**：4 个 excluded task 全部复现了 internal routing 的高死亡率（平均 ΔDR=+33.75%），80 个 episode 中仅 1 个 internal-preferred（use-thermometer ep3）。模式与训练集 task 一致。

**melt 重跑**：已在 tmux `ext-val-melt` 中启动（GPU 0，vLLM 正在加载模型），预计 60-90 分钟完成。

---
