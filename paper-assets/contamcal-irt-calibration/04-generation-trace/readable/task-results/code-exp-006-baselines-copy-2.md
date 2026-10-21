# code exp 006 baselines

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-006-baselines_20260514T091334_result.json`
- **Structured JSON:** [`4cb99f0eb545db47f87b.json`](../../sessions/4c/4cb99f0eb545db47f87b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成总结

exp-006 代码**已基本完成**，dry-run 全部通过。

### 代码状态

| 组件 | 状态 | 说明 |
|------|------|------|
| `run_irt_calibration.py` | ✅ | ContamCal 4PL+γ via CmdStanPy NUTS |
| `baselines.py` (7 baselines) | ✅ | B0-B6 全部实现，统一矩阵接口 |
| `evaluate_calibration.py` | ✅ **已补全** | +ECE, MCE, Brier Score, reliability diagram |
| `run_exp006.py` | ✅ | 端到端 pipeline |
| `run_all_baselines.py` | ✅ **已修复** | 旧接口导致 NaN，已重写 |
| Stan models (3) | ✅ | 4PL+γ simple, 2PL+γ, vanilla 4PL |

### 本次修改

1. **`evaluate_calibration.py`**: 新增 `metric_ece()`, `metric_mce()`, `metric_brier()`, `reliability_diagram_data()`。更新 `evaluate_method` 输出 8 个 metrics + reliability diagram data。更新 LaTeX/text 表格格式含 ECE/Brier 列。

2. **`run_all_baselines.py`**: 重写为使用 `baselines.py` 的矩阵级 API（原代码使用废弃的 per-model 函数接口导致全部 NaN）。

### Dry-run 验证

- 合成数据 6×20（6 models, 20 items, dosages=[0,0,25,50,75,100]）
- ContamCal + 7 baselines 全部运行成功
- 8 个评估 metrics + reliability diagram 全部计算正确
- Stan 采样正常（CmdStanPy 1.3.0 + CmdStan 2.38.0）

### 等待真实数据

Pipeline 已就绪，等 exp-002 signals → exp-003 RRF 完成后即可用真实数据运行 `run_exp006.py`。

---
