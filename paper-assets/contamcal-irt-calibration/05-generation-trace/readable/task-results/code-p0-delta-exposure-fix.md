# code p0 delta exposure fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_p0_delta_exposure_fix_20260514T192535_result.json`
- **Structured JSON:** [`3b61ba29bfec8b5b4d32.json`](../../sessions/3b/3b61ba29bfec8b5b4d32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D024 Delta Exposure Fix — 完整结果

### 修改内容
`run_exp006.py` line 195-201：在 `load_exp002_signals()` 后、`build_exposure_matrix()` 前，减去 d000 baseline signal（0.6131）并 clip 负值为 0。

### Per-benchmark IRT (4PL+gamma) 修复前后对比

| 指标 | 修复前 | 修复后 (D024) |
|------|--------|--------------|
| **Rhat** | 1.53 | **1.0096** ✅ |
| **ESS** | 7 | **522.2** ✅ |
| **Divergences** | — | **0 (0%)** ✅ |
| **gamma mean** | — | **0.508** (正方向) ✅ |
| **gamma 95%CI** | — | [-0.64, 1.84] |
| Signal scores | [0.61, 0.63, 0.68, 0.81] | **[0.0, 0.016, 0.065, 0.197]** |

### Joint-fit（仍然收敛）

| 指标 | 值 |
|------|-----|
| Rhat | **1.0081** ✅ |
| ESS | **956.4** ✅ |
| Divergences | **0** ✅ |
| gamma mean | **0.346** |
| gamma 95%CI | [-0.65, 1.40] |

### 判断
**修复成功。** D024 delta fix 完全解决了 per-benchmark NUTS 不收敛的问题。根因确认：raw signal scores 的 d000 baseline（≈0.613）导致所有模型看起来都有高 exposure，Stan 无法区分 contaminated vs clean models。减去 baseline 后 d000 exposure ≈ 0，与 joint-fit 的 oracle dosage 语义对齐。

结果已保存到 `/root/autodl-tmp/exp006/results_05B_gsm8k_delta/`，不需要单独提交正式运行——这次运行本身就是完整的 GSM8K pipeline 结果（含 IRT + 7 baselines + evaluation + joint-fit）。

---
