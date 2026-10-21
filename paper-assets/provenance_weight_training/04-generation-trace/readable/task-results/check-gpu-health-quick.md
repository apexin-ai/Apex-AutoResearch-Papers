# check gpu health quick

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu_health_quick_20260521T204656_result.json`
- **Structured JSON:** [`f2276123467c9fcdc5a1.json`](../../sessions/f2/f2276123467c9fcdc5a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个训练全部健康，进程存活且 step 在推进：

| GPU | PID | 实验 | 进度 | 运行时间 | GPU利用率 | 显存 |
|-----|--------|------|------|---------|----------|------|
| cuda:0 | 645294 | bs16_adaptive_tau07_seed123 | **2701/6103 (44%)** | 1h51m | 100% | 90199/97887 MiB |
| cuda:1 | 643185 | bs16_uniform_seed123 | **3408/6103 (56%)** | 2h18m | 100% | 90199/97887 MiB |
| cuda:2 | 646037 | detect_remove_q05_v2_seed123 | **9983/24414 (41%)** | 1h44m | 100% | 28697/97887 MiB |
| cuda:3 | 653354 | random_reweight_seed123 | **455/6103 (7%)** | 19m | 97% | 28697/97887 MiB |

注意：detect_remove 的总 step 是 24414（不是 6103），batch size 更小所以 step 更多，但单步更快（1.62 it/s vs ~0.4 it/s）。

预估剩余时间：
- bs16_adaptive: ~2h20m
- bs16_uniform: ~1h50m
- detect_remove_v2: ~2h29m
- random_reweight: ~4h02m

---
