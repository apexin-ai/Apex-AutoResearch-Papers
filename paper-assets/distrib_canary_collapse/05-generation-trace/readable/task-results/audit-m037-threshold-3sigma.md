# audit m037 threshold 3sigma

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_m037_threshold_3sigma_20260520T041508_result.json`
- **Structured JSON:** [`57f97acbd550873ec7e1.json`](../../sessions/57/57f97acbd550873ec7e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## M037 审计完成

### 结果汇总

| 实验 | K≥3(3σ+D111) | 旧 threshold |
|---|---|---|
| Pythia-410M s42 | **6/8** | 3x_sigma_drift |
| GPT-2m s43 | **6/8** | 3x_sigma_drift |
| OPT-1.3B s42 | **6/8** | 3x_sigma_drift |
| OPT-1.3B s43 | **6/8** | D105 3σ (已正确) |
| C4 Pythia-1B s43 | **6/8** | 3x_sigma_drift |
| Padding-410M s42 | **3/8** | unknown |
| Pythia-410M s43 | **6/8** | unknown† |
| Pythia-1.4B s42 | **1/8** | 3x_sigma_drift |
| Pythia-1.4B s43 | **3/8** | 3x_sigma_drift |

### 关键发现

1. **6/9 实验用的是 `3x_sigma_drift`**（简单幅值检查），不是 D105 要求的 true 3σ。切换后 threshold_onset 显著率普遍降至 0-2/8。

2. **D111 direction check 的影响**：大多数实验不受影响（naive peak_lag 已 < 0）。例外是 **Pythia-1.4B s43**（K≥3 从 6/8 降至 3/8，所有 naive peak_lag > 0）。

3. **opt13b_s43 旧 registry 有误**：旧 note 声称 K≥3=0/8（基于错误的 `peak_lag ≤ 0 = not forward`），M037 修正为 6/8（所有 naive peak_lag 严格 < 0，M035 判定为 forward）。

4. 产出文件: `artifacts/m037_audit/audit_report.md`，已 `register_artifact`。9 个实验的 registry 已更新 `threshold_onset_3sigma_m037` 和 `K3_3sigma_m037` 字段。

---
