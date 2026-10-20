# check gamma sweep status

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gamma_sweep_status_20260512T173128_result.json`
- **Structured JSON:** [`e0accdc8fee1abb87cd3.json`](../../sessions/e0/e0accdc8fee1abb87cd3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## gamma_sweep 状态

**仍在运行** — PID 40063，已运行 58 分钟，当前正在处理 **gamma=0.3**（prefill 阶段 85%，44/52 batches）。

### 已完成的结果（JSON 增量写入中）

| Strategy | Gamma | PPL | vs Random | vs Full |
|----------|-------|-----|-----------|---------|
| **full** (无淘汰) | - | **7.1822** | - | baseline |
| **random** | - | **7.6353** | baseline | +6.31% |
| **recency** | - | **7.1758** | +6.02% better | -0.09% (比 full 还好) |
| **ema_0.1** | 0.1 | **8.1707** | **-7.01% (比 random 差)** | +13.76% |

目前只完成了 1/8 个 gamma 值。gamma=0.1 表现比 random 还差，当前 JSON 结论标记为 `"ema_method_flawed"`。

### 进度估算

每个 gamma 约 22 分钟（gamma=0.1 耗时 1304s）。gamma=0.3 prefill 还剩 ~2 min + eval ~8 min，之后还有 6 个 gamma。预计还需 **~2.5 小时**完成全部 8 个 gamma。

### GPU 状态

| GPU | Utilization | Memory |
|-----|------------|--------|
| GPU 0 | 27% | 32.4 / 97.9 GB |
| GPU 1 | 0% (idle) | 28.7 / 97.9 GB |

### 值得注意

recency baseline PPL (7.1758) 竟然略优于 full KV cache (7.1822)，这可能意味着淘汰旧 token 反而有微弱正则化效果。但 EMA gamma=0.1 严重劣于 random，需要等更高 gamma 值的结果才能下结论。

---
