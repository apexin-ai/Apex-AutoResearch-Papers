# ops fix gpu allocation 17855

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-gpu-allocation-17855_20260522T100543_result.json`
- **Structured JSON:** [`a8148dc5be4a49982ff6.json`](../../sessions/a8/a8148dc5be4a49982ff6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。17855 GPU 分配最终状态：

| GPU | Memory | Util | 实验 | PID |
|-----|--------|------|------|-----|
| cuda:0 | 10.3 GB | 90% | **t15_a060 1.4B v2** (新启动, gen_2起) | 664582 |
| cuda:1 | 11.2 GB | 90% | t15_a050 1.4B v3 (gen_2起) | 662119 |
| cuda:2 | 29.3 GB | 89% | t10_a075 1.4B v2 | 655764 |
| cuda:3 | 29.3 GB | 89% | t10_a060 1.4B v2 | 655841 |
| cuda:4 | 14.2 GB | 95% | t20_a075 410M s43 | 603938 |
| cuda:5 | 14.5 GB | 67% | t25_a045 410M s43 | 577241 |

- PID 661775 (重复 t10_a050) 已 kill，cuda:0 释放并成功分配给 t15_a060
- t15_a050 (cuda:1) 运行正常
- Registry 已更新：`scale_14b_t15_a060_s42_fp32_v2` → RUNNING

---
