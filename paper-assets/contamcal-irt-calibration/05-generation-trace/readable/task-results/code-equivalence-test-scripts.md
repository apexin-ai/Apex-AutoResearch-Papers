# code equivalence test scripts

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_equivalence-test-scripts_20260518T155723_result.json`
- **Structured JSON:** [`bfc8761ddd9e78d1376d.json`](../../sessions/bf/bfc8761ddd9e78d1376d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部通过。汇总：

**脚本路径（westd-29999）**
- `/root/contamcal-irt-calibration/exp006/tost_equivalence.py`
- `/root/contamcal-irt-calibration/exp006/power_analysis.py`

**TOST demo 输出**
- mean_diff = -0.0022, 90% CI = [-0.0054, 0.0011], p_tost = 2.16e-06, **equivalent = true**
- 16 个模拟模型，bound ±0.015，差异远在 equivalence region 内

**Power analysis demo 输出**
- N=16, σ=0.008, bound=±0.015: power@δ=0 = 100%, MDES@80% = 0.0100
- required_n@80% power = 3（σ=0.008 相对 bound=0.015 很小，power 充裕）
- power 在 δ=0.010 时降至 80%，δ=0.012 时降至 44%

**验证项全部通过**: 语法检查 OK，`--help` OK，`--demo` JSON 输出 OK，`--plot` PNG 生成 OK。

---
