# code qwen theta fixed verify

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen-theta-fixed-verify_20260520T234008_result.json`
- **Structured JSON:** [`79eba2b12c6fb5ab6bc0.json`](../../sessions/79/79eba2b12c6fb5ab6bc0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== θ_fixed 分析验证 ===
θ_fixed = -0.0965 (来源: n=3 clean θ_MLE 均值, 不受 ℓz* 校正影响 ✓)

lz* 公式: 旧脚本用 Drasgow 1985 ℓz（无 Var* 校正）
需要重算: 是 — 已用 Snijders 2001 ℓz* 重算完毕

| Condition | θ_free  | lz*_fixed (old Drasgow) | lz*_fixed (new Snijders) | Δlz*_fixed (old) | Δlz*_fixed (new) |
|-----------|---------|-------------------------|--------------------------|-------------------|-------------------|
| clean_s1  | -0.0987 | 7.9501                  | 9.4004                   | +0.6066           | +0.7174            |
| clean_s2  | -0.0842 | 6.2996                  | 7.4485                   | -1.0439           | -1.2345            |
| clean_s3  | -0.1068 | 7.7808                  | 9.2002                   | +0.4373           | +0.5172            |
| contam_15 | +0.1971 | 10.0224                 | 11.8520                  | +2.6790           | +3.1690            |
| contam_50 | +0.3703 | 15.7080                 | 18.5764                  | +8.3646           | +9.8934            |

新 dose-response ratio: |Δcontam_50| / |Δcontam_15| = 3.1219
对比旧 ratio: 3.1223 → 3.1219 (几乎无变化)
```

**结论**: Snijders 校正使所有 lz\*\_fixed 绝对值增大 ~18%（因为 Var\* < Var），但由于校正因子对各 condition 近似等比例缩放，dose-response ratio 基本不变（3.12 → 3.12）。θ\_fixed 值不受影响。

结果已保存至 `/root/autodl-tmp/ctrl_contam_pilot/results/theta_fixed_n3_lzstar.json`。

---
