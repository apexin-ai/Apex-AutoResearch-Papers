# code 32b power analysis

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_32b_power_analysis_20260517T104240_result.json`
- **Structured JSON:** [`f847fdc8643e10fb8da4.json`](../../sessions/f8/f847fdc8643e10fb8da4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

### R1-32B (n=20, current power ~40%)

| Metric | Delta | σ_boot | α=0.05 需要 n | α=0.017 (Bonf) 需要 n |
|--------|-------|--------|---------------|----------------------|
| bal_acc | +0.084 | 0.050 | **55** | **74** |
| precision | +0.094 | 0.052 | **49** | **65** |
| pre_cp_fpr | -0.084 | 0.049 | **54** | **72** |

R1-32B 效果中等，当前 n=20 power 约 40%，**增加到 ~55-75 条 traces 即可达到 80% power**。

### QwQ-32B (n=19, current power 6-17%)

| Metric | Delta | σ_boot | α=0.05 需要 n | α=0.017 (Bonf) 需要 n |
|--------|-------|--------|---------------|----------------------|
| bal_acc | +0.009 | 0.035 | **2365** | **3155** |
| precision | +0.057 | 0.058 | **142** | **190** |
| pre_cp_fpr | -0.030 | 0.038 | **243** | **324** |

QwQ-32B 的 effect size 极小（尤其 bal_acc delta 仅 0.009），precision 需要 ~142-190 条，而 bal_acc 需要 ~2400+ 条才能达到 80% power，基本说明 HS 对 QwQ 没有实质性优势。

- 脚本: `src/experiments/exp_power_analysis.py`
- 结果: `artifacts/power_analysis/results.json`

---
