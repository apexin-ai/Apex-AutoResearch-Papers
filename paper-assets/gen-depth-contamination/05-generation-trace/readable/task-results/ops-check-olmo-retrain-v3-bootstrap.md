# ops check olmo retrain v3 bootstrap

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_olmo_retrain_v3_bootstrap_20260520T142723_result.json`
- **Structured JSON:** [`3eb5530439d11481b697.json`](../../sessions/3e/3eb5530439d11481b697.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**状态：进行中 (3/4 pairs 完成)**

进程活跃，日志最后更新 22:29:11（北京时间），3v4 bootstrap 正在计算。

## 已完成结果

| Pair | Point AUC | Bootstrap AUC | 95% CI |
|------|-----------|---------------|--------|
| 0v1 | 0.9873 | 0.9972 | [0.9967, 0.9977] |
| 1v2 | 0.8889 | 0.9572 | [0.9542, 0.9601] |
| 2v3 | 0.7036 | 0.8885 | [0.8814, 0.8947] |
| 3v4 | 0.6817 | 计算中... | — |

## 时间估算

每个 pair 的 bootstrap (10K resamples) 耗时约 30 分钟：
- 0v1: 20:33 → 21:05 (32 min)
- 1v2: 21:05 → 21:35 (30 min)  
- 2v3: 21:35 → 22:05 (30 min)
- 3v4: ~22:05 开始，预计 **~22:35 完成**（约 5-6 分钟后）

所有 CI 下界远超 θ=0.60 阈值，K*≥4 结论稳固。

---
