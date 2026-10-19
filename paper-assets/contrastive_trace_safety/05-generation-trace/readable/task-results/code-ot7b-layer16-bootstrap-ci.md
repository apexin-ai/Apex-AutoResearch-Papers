# code ot7b layer16 bootstrap ci

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ot7b_layer16_bootstrap_ci_20260517T093734_result.json`
- **Structured JSON:** [`ff04fab19610ea759176.json`](../../sessions/ff/ff04fab19610ea759176.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

## Layer 16 vs Layer 0 对比

### Probe 性能（Layer 16 全面优于 Layer 0）
| 指标 | Layer 0 | Layer 16 | 变化 |
|------|---------|----------|------|
| bal_acc | 0.672 | **0.762** | +9.0pp |
| precision | 0.357 | **0.565** | +20.8pp |
| pre_cp_fpr | 0.188 | **0.100** | -8.7pp |

### Bootstrap（1000 resamples, Bonferroni α=0.017）
| 指标 | L16 delta | 95% CI | p-value | 显著 |
|------|-----------|--------|---------|------|
| bal_acc | +0.1067 | [0.049, 0.163] | **0.000** | YES |
| precision | +0.2189 | [0.140, 0.296] | **0.000** | YES |
| pre_cp_fpr | -0.1705 | [-0.222, -0.122] | **0.000** | YES |

关键改进：precision 在 Layer 0 时 p=0.056（未过 Bonferroni），Layer 16 上 p=0.000，**三个指标全部通过 Bonferroni 校正**。

### Selectivity
- Layer 16: 18.3pp (real=0.688, random=0.505) — PASS
- Layer 0: 18.5pp — 基本持平

产出：
1. 脚本: `src/experiments/exp_ot7b_layer16_bootstrap_full.py`
2. 结果 JSON: `artifacts/ot7b_layer16_bootstrap/results.json`
3. 报告已注册: `art_20260517_04c053`

---
