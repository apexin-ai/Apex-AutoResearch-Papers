# code v2 lambda and config fix

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v2_lambda_and_config_fix_20260518T114552_result.json`
- **Structured JSON:** [`8b42826119504d6e36c9.json`](../../sessions/8b/8b42826119504d6e36c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总结果：

## Part 1: config.py 一致性修复

| 参数 | 旧值 | 新值 |
|------|------|------|
| GAR_EPSILON | 0.002 | 0.001 |
| GAR_LAMBDA | 1.0 | 2.0 |
| MAX_SEQ_LEN | 4096 | 2048 |
| INIT_BIAS | (缺失) | 2.0 |
| GAR_LOSS_MODE | (缺失) | "cumulative" |

train_phase2.py 的 argparse 默认值全部改为引用 config 常量，新增 `--batch-size` 参数。

## Part 2: λ=2.0 Dry-run 结果

| Step | L_NTP | L_GAR | Total Loss | Gate mean | VRAM |
|------|-------|-------|------------|-----------|------|
| 0 | 1.9796 | 0.1266 | 2.2328 | 0.8743 | 42.3GB |
| 1 | 1.3270 | 0.1266 | 1.5802 | 0.8744 | 42.3GB |
| 2 | 1.5083 | 0.0849 | 1.6781 | 0.8747 | 46.7GB |
| 3 | 1.6247 | 0.0924 | 1.8094 | 0.8760 | 46.7GB |
| 4 | 1.8396 | 0.0541 | 1.9478 | 0.8765 | 46.7GB |

**λ × L_GAR vs L_NTP 比例分析：**
- Step 0: 2.0 × 0.1266 = 0.253, ratio = 0.253 / 1.980 = **0.13x** (< 0.3x)
- Step 2: 2.0 × 0.0849 = 0.170, ratio = 0.170 / 1.508 = **0.11x**
- Step 4: 2.0 × 0.0541 = 0.108, ratio = 0.108 / 1.840 = **0.06x**

**比例持续 < 0.3x**，且 L_GAR 在 5 步内从 0.127 快速下降到 0.054，GAR loss 贡献相对于 NTP loss 偏小。Gate gradient 已确认收到。

## Part 3: 临时目录已清理

## 本地同步: 已完成

---
