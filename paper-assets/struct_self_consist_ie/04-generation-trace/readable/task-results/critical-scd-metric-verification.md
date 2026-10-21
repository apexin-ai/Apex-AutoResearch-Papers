# critical scd metric verification

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_critical_scd_metric_verification_20260520T195556_result.json`
- **Structured JSON:** [`5423d55afbe3f6c6e20d.json`](../../sessions/54/5423d55afbe3f6c6e20d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 集一致（均为 37648 行 `data/fewnerd/test.json`）。

## 结论

**+3.84pp 是 metric artifact，SCD 在统一口径下并没有明显正向效果。**

### 根因

`eval_scd.py` 中 `load_pre_metrics()` 从 `full_signal_report.json` 读取 baseline，该 report 的 `baselines.greedy.mean = 0.7482` 是 **instance-average F1（gold-filtered, n=32565）**。而被拿来对比的 post-SCD 数字 0.7866 是 `eval_scd_greedy_fewnerd.py` 输出的 **micro-F1（full, n=37648）**。

**双重不可比**：
1. **Metric 类型不同**：instance-average F1 vs micro-F1
2. **Eval 集不同**：32565 (去除 gold-empty) vs 37648 (全集)

### 统一口径后的真实数字

#### Micro-F1（全集 n=37648）

| 模型 | Micro-F1 | P | R | Δ vs Pre-SCD |
|------|----------|------|------|-------------|
| **Pre-SCD baseline** | **0.7886** | 0.7866 | 0.7906 | — |
| Post-SCD standard | 0.7813 | 0.7583 | 0.8057 | **-0.73pp** |
| Post-SCD fallback (curriculum_q) | 0.7866 | 0.7663 | 0.8080 | **-0.20pp** |

#### Instance-avg F1（全集 n=37648）

| 模型 | Instance-avg F1 | Δ vs Pre-SCD |
|------|----------------|-------------|
| **Pre-SCD baseline** | **0.7719** | — |
| Post-SCD standard | 0.7703 | **-0.16pp** |
| Post-SCD fallback (curriculum_q) | 0.7809 | **+0.90pp** |

### 结论

- **Micro-F1 口径**：两个 SCD 变体都**变差了**（standard -0.73pp, fallback -0.20pp）
- **Instance-avg 口径**：standard 持平略负，fallback 有 +0.90pp 小幅提升——远非 +3.84pp
- SCD 训练改变了 P/R trade-off（precision 下降，recall 上升），但净效果接近零或略负
- **SCD 不构成有效论文贡献**，+3.84pp 完全是比较了不同 metric 类型和不同 eval 子集的 artifact

---
