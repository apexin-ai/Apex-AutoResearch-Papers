# analysis mvp c4 s137

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp_c4_s137_20260518T175832_result.json`
- **Structured JSON:** [`c28b84255742976e6872.json`](../../sessions/c2/c28b84255742976e6872.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

mvp_c4_s137 分析完成，registry 已更新。

**结果摘要：**

| 指标 | s137 | s42 (参考) |
|---|---|---|
| final_train_loss | 0.3114 | 0.308 |
| avg_train_loss | 0.5447 | 0.5461 |
| train_runtime | 10205s (2.84h) | 6040s (1.68h) |
| total_steps | 471 | 471 |
| epochs | 3 | 3 |

**结论：success**
- 训练正常完成（EXIT_CODE=0），checkpoint 5.1G 存在于 `/root/tbab_multi_turn/checkpoints/c4_full_tbab_seed137`
- Loss 与 s42 高度一致，两个 seed 收敛行为稳定
- Runtime 比 s42 长 69%，原因是后半段步速从 ~12s/it 降到 ~27s/it（可能 GPU 热降频或其他进程争抢资源），但不影响训练质量
- W&B 为 offline 模式，run ID: `t0pzdqcv`

---
