# code d015 g4 absolute threshold

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d015-g4-absolute-threshold_20260515T203457_result.json`
- **Structured JSON:** [`e51877a4c00014ce072a.json`](../../sessions/e5/e51877a4c00014ce072a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

G4 works correctly — median of `[0.1070, 0.2176, 0.5479]` = `0.2176` < 1.0 → PASS.

### 修改前 vs 修改后对比

| 方面 | D014 (旧) | D015 (新) |
|------|-----------|-----------|
| **G4 指标** | `1 - mean(imm_led)/mean(bl_led)` (relative decrease) | `median(imm_led_ratios)` (absolute value) |
| **G4 阈值** | ≥ 30% decrease | < 1.0 |
| **G4 依赖** | 需要 baseline + IMM 的 LED ratio | 只需 IMM 的 LED ratio |
| **Fallback** | baseline L=0 时 auto-PASS | 无 fallback；IMM 没有 LED 字段则 FAIL |
| **聚合方式** | mean | median |
| **Gate dict key** | `G4_led_ratio_decrease` | `G4_led_ratio_median` |

### 验证结果
- `--help` 参数接口不变（`--baseline`, `--imm`, `--condition`, `--output`）
- dry-run 输出格式正确：`G4 PASS: LED ratio median = 0.2176 < 1.0 (certified bound)`
- G1/G2/G3 逻辑完全未动——从输出可见它们仍独立判定（G1 N/A→FAIL, G2 N/A→FAIL, G3 7.17→FAIL，与旧逻辑一致）

---
