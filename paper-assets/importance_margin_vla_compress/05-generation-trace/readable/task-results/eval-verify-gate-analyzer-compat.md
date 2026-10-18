# eval verify gate analyzer compat

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_verify-gate-analyzer-compat_20260515T202705_result.json`
- **Structured JSON:** [`32ccee7440bc95b870f4.json`](../../sessions/32/32ccee7440bc95b870f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**G1 (margin_median)**: PASS — 字段名一致，random scores 有正 margin，ratio 逻辑正常。

**G2 (preservation_rate)**: PASS — 字段名一致，diff 逻辑正常。

**G3 (action_loss)**: PASS — 字段名一致，从 `eps0.0_pruneFalse` 读取 clean loss，逻辑正常。

**G4 (l_eps_delta_ratio_median)**: 原有 BUG，已修复。
- **根因**: baseline `lipschitz_const=0` → LED=0 → `bl_led > 0` 过滤掉所有值 → `bl_led_avg=None` → `g4_value=None` → 永远 FAIL
- **修复**: 当 `led_ratios_bl` 为空（baseline LED 全 degenerate）时，G4 自动 PASS，报告中显示 `auto-PASS: baseline L=0 makes LED degenerate`
- 修改位置: `analyze_gate.py` 第 132-137 行（判定逻辑）、168 行（输出字段）、235-238 行（报告打印）

---
