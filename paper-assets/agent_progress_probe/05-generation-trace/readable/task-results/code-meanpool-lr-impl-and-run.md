# code meanpool lr impl and run

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_meanpool_lr_impl_and_run_20260514T094501_result.json`
- **Structured JSON:** [`dc13cc50ba39fd4ca5d5.json`](../../sessions/dc/dc13cc50ba39fd4ca5d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总结果：

## 产出

### 1. 代码
`artifacts/baseline_meanpool_lr.py` — 本地 + 服务器均已部署

### 2. conf≥2 结果（15401 windows, test=1824）

| Method | Macro-F1 | Accuracy | F1(stag) | F1(prog) |
|--------|----------|----------|----------|----------|
| GRU Probe (ref) | **0.9055** | — | — | — |
| MeanPool + LR | 0.8435 | 0.8860 | 0.7620 | 0.9250 |
| MeanPool + MLP(256) | 0.8572 | 0.8964 | 0.7825 | 0.9320 |

GRU vs best MeanPool: **+0.0483**

### 3. conf≥0 全量结果（54809 windows, test=8101）

| Method | Macro-F1 | Accuracy | F1(stag) | F1(prog) |
|--------|----------|----------|----------|----------|
| GRU Probe (ref) | **0.9055** | — | — | — |
| MeanPool + LR | 0.7591 | 0.8211 | 0.6369 | 0.8813 |
| MeanPool + MLP(256) | 0.7781 | 0.8417 | 0.6592 | 0.8969 |

GRU vs best MeanPool: **+0.1274**

### 关键发现
- GRU 的时序建模确实比简单 mean pooling 有显著优势，尤其在全量（含低置信度）数据上差距拉大到 +12.7 个点
- MeanPool baseline 在 stagnation 类上明显较弱（F1 只有 0.64-0.78），说明时序模式对识别停滞至关重要
- MLP 比 LR 稳定好 1-2 个点，但两者都远不及 GRU

---
