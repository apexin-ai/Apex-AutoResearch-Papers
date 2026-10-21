# ssh diagnose latency profile n1000

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose-latency-profile-n1000_20260520T083933_result.json`
- **Structured JSON:** [`2b759ed9391dacbbaaf7.json`](../../sessions/2b/2b759ed9391dacbbaaf7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 全部更新完成。诊断结果汇总：

## 诊断结果

**状态**: 实验成功完成（之前被 cron 误判为 failed，因脚本无 sentinel 文件）

### 进程状态
- PID 252933 已退出
- JSON 输出文件完整（5589 bytes, 2026-05-20 16:08）
- 日志文件完整（4015 bytes）

### 关键延迟数据（mean_ms, N=1000, RTX 4090）

| 组件 | mean (ms) | p95 (ms) | min (ms) |
|------|-----------|----------|----------|
| vla_encode_prefix | 43.4 | 71.2 | 32.5 |
| vla_sample K=1 | 213.8 | 220.9 | 205.1 |
| vla_sample K=10 | 211.2 | 215.9 | 204.4 |
| vla_e2e K=1 | 256.5 | 281.0 | 239.6 |
| vla_e2e K=10 | 253.2 | 273.4 | 237.1 |
| cgs_compute_features | 5.75 | 6.29 | 5.57 |
| crm_forward | 0.28 | 0.31 | 0.27 |
| argmin_l2 K=10 | 0.060 | 0.063 | 0.057 |
| full_pipeline K=10 | 249.0 | 270.6 | 224.8 |
| adaptive_fast_path | 252.9 | 279.1 | 236.6 |
| adaptive_full_path | 459.6 | 491.4 | 438.9 |

### 关键发现
- **CRM overhead vs VLA K=10**: -4.2 ms (-1.66%) — CRM 几乎零开销
- **Adaptive speedup (fast vs full)**: 252.9 vs 459.6 ms (**1.82x**)
- **K=1→K=10 采样延迟几乎不变**（213.8 → 211.2 ms），多候选采样无额外成本
- GPU 内存占用仅 903 MB

### 日志末尾 20 行
```
vla_sample_K5             217.999    8.228  228.490  208.717  310.502
vla_sample_K10            211.154    6.629  215.881  204.355  339.466
vla_e2e_K1                256.466   19.644  281.017  239.629  435.471
vla_e2e_K2                258.713   15.846  278.892  245.234  504.025
vla_e2e_K5                257.087   17.892  274.796  244.654  504.724
vla_e2e_K10               253.192   13.157  273.364  237.144  437.553
argmin_l2_K2                0.060    0.004    0.072    0.056    0.087
argmin_l2_K5                0.065    0.007    0.074    0.057    0.092
argmin_l2_K10               0.060    0.002    0.063    0.057    0.075
cgs_compute_features        5.749    0.269    6.288    5.570    8.164
crm_forward                 0.280    0.015    0.306    0.269    0.624
full_pipeline_K10         248.978   17.817  270.642  224.849  446.413
adaptive_fast_path        252.867   18.649  279.057  236.550  425.973
adaptive_full_path        459.615   23.821  491.429  438.930  692.367

[derived] CRM overhead over VLA K=10: -4.214 ms (-1.66%)
[derived] Adaptive K speedup (fast vs full): 252.87 vs 459.61 ms (1.82x)

[profile] Results saved to logs/latency_profile_n1000.json
```

---
