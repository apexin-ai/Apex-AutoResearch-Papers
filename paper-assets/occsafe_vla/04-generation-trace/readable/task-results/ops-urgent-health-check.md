# ops urgent health check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_health_check_20260524T093840_result.json`
- **Structured JSON:** [`c9219d8300a6fd169076.json`](../../sessions/c9/c9219d8300a6fd169076.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
[10894 状态]
- PID 746616 (ablation_occ_detach_s0_retrain): alive, GPU 0, 99% util, step ~1571/50005 (3%)
- PID 742741 (full_occ_ln_s0): alive, GPU 1, 64% util, step ~1927/50005 (4%)
- PID 742888 (full_occ_ln_s1): alive, GPU 2, 89% util, step ~1931/50005 (4%)
- PID 743106 (full_occ_ln_s2): alive, GPU 3, 99% util, step ~1919/50005 (4%)

[34685 状态]
- cutoff_15k_s0 (PID 443639): alive, step 47660/50005 (95%), ETA ~45min
- cutoff_45k_s0 (PID 456023): alive, step 46826/50005 (94%), ETA ~55min
- cutoff_25k_s1: step 33841/50005 (68%)
- reverse_cutoff_s1: step 33886/50005 (68%)

⚠️ 34685 GPU util 全部 0%（内存已占满 62-63GB/98GB），但进程存活且日志在推进，应为瞬时采样到 data loading 间隙，正常。

[行动]
- 已启动 eval: 无（尚无完成的实验）
- 需要重启: 无
- 最快完成: cutoff_15k_s0 约 45 分钟后完成，cutoff_45k_s0 约 55 分钟后
```

---
