# run probe 5090c

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_probe_5090c_20260521T015651_result.json`
- **Structured JSON:** [`bc35f7df8090d5747461.json`](../../sessions/bc/bc35f7df8090d5747461.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All tasks complete. Summary:

---

### 子任务 A: CoNLL s456 Registry — Done

三个实验已更新为 DONE/success：

| Experiment | greedy_F1 | oracle_F1 | rho_SJ_F1 | degeneracy | verdict |
|---|---|---|---|---|---|
| exp_conll_t05_s456 | 0.9075 | 0.9338 | 0.455 | 5.6% | PASS |
| exp_conll_t08_s456 | 0.9064 | 0.9407 | 0.488 | 6.3% | PASS |
| exp_conll_t12_s456 | 0.9071 | 0.9452 | 0.455 | 8.3% | PASS |

T=0.8 仍然是 rho_SJ_F1 最高的 sweet-spot（seed=456 确认）。

### 子任务 B: Hidden State Probe — Done

| Method | AUROC | Notes |
|---|---|---|
| **Probe (FewNERD)** | **0.9872 ± 0.0007** | 10508 entities, 500 inst |
| **Probe (CoNLL)** | **0.9796 ± 0.0036** | 7849 entities, 500 inst |
| MV Agreement | 0.87 | Multi-sample baseline |
| ESJ Self-Judgment | 0.51 | Prompt-based baseline |

**关键结论**：Linear probe on last-layer hidden states achieves **AUROC ~0.98**，远超 MV (0.87) 和 ESJ (0.51)。模型的 hidden representation 中编码了极高保真度的 entity 正确性信息，但 prompt-based 读取完全失败。这是 **prompt interface failure**，不是信息缺失。

- 代码：`code/hidden_state_probe.py` (340 行)
- 数据：`output/entity_probe_auroc/` (FewNERD + CoNLL hidden states + AUROC results)
- Registry：`exp_hidden_state_probe` → DONE/success
- SciERC 未跑（服务器上无 8B 模型对应的 samples 数据）

---
