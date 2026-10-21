# ssh full gpu audit director order

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_full-gpu-audit-director-order_20260520T051752_result.json`
- **Structured JSON:** [`c794cf0d77e9937282f1.json`](../../sessions/c7/c794cf0d77e9937282f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集。以下是完整审计报告。

---

# 全集群 GPU 审计报告 (2026-05-20)

**结论：17 张卡中 9 张活跃，8 张空闲。系统健康数据 ~8 空闲是正确的。**

---

## bjb2-28827 (6×4090)

| GPU | VRAM Used | Util% | PID | 实验内容 | 状态 |
|-----|-----------|-------|-----|----------|------|
| 0 | 5508/24564 | 17% | 197016 | evaluate.py --mode vla_only --benchmark goal --seed 50 --K 1 | RUNNING |
| 1 | 1/24564 | 0% | — | tmux session `eval-adaptive-k-p75-seed42` 残留但无 python 进程 | **空闲** (刚完成) |
| 2 | 1869/24564 | 18% | 154335 | evaluate.py --mode vla_only --benchmark long --seed 51 | RUNNING |
| 3 | 5508/24564 | 19% | 197289 | evaluate.py --mode vla_only --benchmark goal --seed 51 --K 1 | RUNNING |
| 4 | 1/24564 | 0% | — | — | **空闲** |
| 5 | 1/24564 | 0% | — | — | **空闲** |

**最近完成 (60min 内):**
- `eval_goal_obs_only_norm02_seed48.json`
- `eval_spatial_obs_only_norm02_seed49.json`
- `eval_long_vla_only_seed49.json`
- `eval_long_vla_only_seed50.json`
- `crm_magnitude_calibration.json` ← **Calibration 结果在此服务器**

---

## bjb1-18228 (4×4090)

| GPU | VRAM Used | Util% | PID | 实验内容 | 状态 |
|-----|-----------|-------|-----|----------|------|
| 0 | 1961/24564 | 25% | 239026 | evaluate.py --mode adaptive_k --threshold 0.054959 --benchmark object --seed 44 (P25) | RUNNING |
| 1 | 1/24564 | 0% | — | — | **空闲** |
| 2 | 1/24564 | 0% | — | — | **空闲** |
| 3 | 1/24564 | 0% | — | tmux session `eval-adaptive-k-p50-seed43` 残留但无 python 进程 | **空闲** (刚完成) |

**最近完成 (60min 内):**
- `eval_spatial_obs_only_norm02_seed51.json`
- `eval_goal_vla_only_seed49.json`
- `eval_long_vla_only_seed52.json`

---

## bjb1-32546 (6×4090)

| GPU | VRAM Used | Util% | PID | 实验内容 | 状态 |
|-----|-----------|-------|-----|----------|------|
| 0 | 2/24564 | 0% | — | — | **空闲** |
| 1 | 6383/24564 | 36% | 254517 | evaluate.py --mode crm_obs_only --benchmark long --seed 51 --K 10 --max_correction_norm 0.2 | RUNNING |
| 2 | 6283/24564 | 21% | 254789 | evaluate.py --mode vla_only --benchmark long --seed 53 --K 1 | RUNNING |
| 3 | 2/24564 | 0% | — | — | **空闲** |
| 4 | 6283/24564 | 25% | 255073 | evaluate.py --mode vla_only --benchmark long --seed 54 --K 1 | RUNNING |
| 5 | 5509/24564 | 18% | 255608 | evaluate.py --mode vla_only --benchmark goal --seed 52 --K 1 | RUNNING |

**最近完成 (60min 内):**
- `eval_object_vla_only_seed51.json`
- `eval_long_obs_only_norm02_seed49.json`
- `eval_long_obs_only_norm02_seed48.json`
- `eval_spatial_vla_only_seed51.json`
- `eval_long_obs_only_norm02_seed50.json`

---

## bjb2-40593 (1×4090)

| GPU | VRAM Used | Util% | PID | 实验内容 | 状态 |
|-----|-----------|-------|-----|----------|------|
| 0 | 3135/24564 | 21% | 660279 | **calibrate_crm_signal.py** (SCREEN session `calibrate`) | RUNNING |

**最近完成 (60min 内):**
- `eval_adaptive_k_p25_seed44.json`

---

## 汇总

| 服务器 | 总卡数 | 活跃 | 空闲 |
|--------|--------|------|------|
| bjb2-28827 | 6 | 3 | **3** |
| bjb1-18228 | 4 | 1 | **3** |
| bjb1-32546 | 6 | 4 | **2** |
| bjb2-40593 | 1 | 1 | 0 |
| **合计** | **17** | **9** | **8** |

---

## Calibration 结果 (crm_magnitude_calibration.json)

**文件位于 bjb2-28827**，完整内容：

```json
{
  "go_nogo": "NO-GO",
  "total_steps": 27626,
  "config": {
    "benchmark": "object",
    "n_episodes": 10,
    "seed": 42,
    "crm_checkpoint": "crm_v3_norm/obs_only/crm_best.pt",
    "max_correction_norm": 0.2
  },
  "correlations": {
    "k1_corr_mag_vs_k10_var":  { "rho": 0.1523, "p_value": 6.37e-143 },
    "k2_corr_mag_vs_k10_var":  { "rho": 0.1340, "p_value": 8.66e-111 },
    "k1_corr_mag_vs_k2_l2":   { "rho": 0.1319, "p_value": 1.76e-107 }
  },
  "distributions": {
    "k1_correction_magnitude": { "mean": 0.12078, "std": 0.01046, "P25-P90": ~0.12052 (几乎无变化) },
    "k2_correction_magnitude": { "mean": 0.12074, "std": 0.01052, "P25-P90": ~0.12052 (几乎无变化) },
    "k10_variance":            { "mean": 0.00048, "std": 0.00043, "P50": 0.00037 },
    "k2_l2_distance":          { "mean": 0.15019, "std": 0.08004, "P50": 0.13426 }
  }
}
```

**关键发现：** correction magnitude 的 P25-P90 百分位几乎完全一样 (~0.12052)，说明 CRM 输出基本是常数——信号没有随输入变化。相关性虽统计显著 (p≈0) 但 rho 仅 ~0.13-0.15，实际预测力极弱。结论 **NO-GO**。

**注意：** bjb2-40593 上 `calibrate_crm_signal.py` 仍在运行中（PID 660279），可能是新一轮 calibration。该服务器上尚未生成 calibration JSON。

---
