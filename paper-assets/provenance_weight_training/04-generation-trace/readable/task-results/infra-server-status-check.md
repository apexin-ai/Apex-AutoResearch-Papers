# infra server status check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_server-status-check_20260514T135859_result.json`
- **Structured JSON:** [`2c81c50900d4325cd9aa.json`](../../sessions/2c/2c81c50900d4325cd9aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. 训练进度

| GPU | 实验 | 进度 | 剩余时间 | 备注 |
|-----|------|------|----------|------|
| cuda:0 | grid_b_seed42_batch (b=2.0) | **4777/6103 (78%)** | ~47min | 之后还剩 b=3.0, b=5.0 两轮，每轮~3.6h，**总剩余~7.7h** |
| cuda:1 | grid_b2_0_seed123 | **5721/6103 (94%)** | **~13min** | 即将完成 |
| cuda:2 | grid_b3_0_seed123 | **5426/6103 (89%)** | ~24min | 正常 |
| cuda:3 | grid_b5_0_seed123 | **552/6103 (9%)** | **~6.9h** | ⚠️ 速度从2.11s/it骤降到4.48s/it（step 547附近），ETA从3:15h飙到6:55h |

**注意**: cuda:3 的 grid_b5_0_seed123 在 step ~547 处速度减半（2.11→4.48s/it），可能是 eval/save 触发或被其他进程抢占 GPU 资源。值得关注是否持续。

### 2. auto_eval_watcher
- 旧 PID 74145: **已死**
- 新 PID **99508**: **存活**（20:37 启动），正常运行

### 3. adaptive_fix D012
**已部署确认。** `pretrain_weighted.py` 第279-280行:
```python
if args.n_min is None:
    args.n_min = max(2, args.batch_size // 2)
```

### 4. 磁盘

| 分区 | 容量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| / (根) | 30G | 23G | 7.7G | **75%** |
| /root/autodl-tmp | 250G | 70G | 181G | 28% |
| output/ 目录 | — | 56G | — | — |

根分区 75% 偏高，output/ 占 56G 是大头。如果后续实验继续产出 checkpoint，可能需要清理旧的。

---
