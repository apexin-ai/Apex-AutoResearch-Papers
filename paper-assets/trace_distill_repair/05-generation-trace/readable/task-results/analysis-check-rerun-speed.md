# analysis check rerun speed

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_check_rerun_speed_20260514T202340_result.json`
- **Structured JSON:** [`eddb5dd224a08cfbd9b8.json`](../../sessions/ed/eddb5dd224a08cfbd9b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

---

### 1. 并发数：**max_concurrent = 10**（默认值）

启动命令未传 `--max-concurrent` 参数。代码默认值是 10（`run_phase2_scoring.py:112` 和 `:232`）。

Director 要求 10-15，**当前 10 在范围下限，符合要求。**

### 2. 实际速率

进程已运行 **1 分 40 秒**，处理模式为**逐 instance 串行**，instance 内 segments 并发。

| Instance | Segments | 耗时（墙钟） | 秒/segment |
|----------|----------|-------------|------------|
| black_14 (第1个) | 9 | ~52s（含启动开销） | ~5.8 |
| black_1 | 11 | ~15s | ~1.4 |
| black_2 | 10 | ~12s | ~1.2 |

- **稳态速率**：~13-15s/instance（~10 segments），约 **1.3s/segment**
- 第一个 instance 52s 是启动开销（冷启动），后续稳定在 12-15s

### 3. 进度与 ETA

- 总量：**38 instances**（排除了 fastapi_5, fastapi_3）
- 已完成：**3/38**，第 4 个（black_5, 9 segments）进行中
- 剩余 ~34 instances × ~14s ≈ **~8 分钟**
- **预计总耗时 ~10 分钟**，大约在 04:33 左右完成

### 4. 错误计数

| 类型 | 计数 |
|------|------|
| NoneType | 0 |
| API_FAILURE | 0 |
| fallback | 0 |
| ERROR | 0 |
| error | 0 |

**零错误，API 全部 200 OK，运行完全正常。**

---
