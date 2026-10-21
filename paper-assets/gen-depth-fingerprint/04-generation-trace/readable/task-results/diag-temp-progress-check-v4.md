# diag temp progress check v4

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_temp-progress-check-v4_20260518T165440_result.json`
- **Structured JSON:** [`c089f99f2ea8e9e5b206.json`](../../sessions/c0/c089f99f2ea8e9e5b206.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 温度实验状态汇报

| 组 | Seeds | 总量 | 进度 | 状态 | 预计剩余 |
|---|---|---|---|---|---|
| **olmo-2-1b-t05** | 868 | 995 | 87% | 生成中 (GPU 0, 46%) | ~18 min |
| **qwen3-0.6b-t05** | 582 | 996 | 58% | 生成中 (GPU 1, 32%) | ~81 min |
| **olmo-2-1b-t09** | 0 | — | — | 未启动，数据文件不存在 | — |
| **qwen3-0.6b-t09** | 0 | — | — | 未启动，数据文件不存在 | — |

**关键发现：**

- **t=0.9 两组未启动**。当前只有 t=0.5 的两个生成进程在跑（temp_olmo 和 temp_qwen06 各一个 session），GPU 2-3 空闲。t=0.9 的生成进程完全没有被启动。
- **Pipeline 未触发**。当前 feature CSV 都是 5 月 15-16 日基线实验的，不是温度实验产出。Monitor 在正常轮询（每 120s），但因为 t05 尚未完成、t09 未启动，所以没有触发 feature extraction。Monitor 日志无报错。
- **OLMo t=0.5 约 18 分钟后完成**（8.6s/seed，剩余 127 seeds）。Qwen3 t=0.5 约 81 分钟后完成（11.74s/seed，剩余 414 seeds）。

**需要决策**：t=0.9 两组是打算 t=0.5 跑完后复用同 GPU 顺序跑，还是现在就在空闲的 GPU 2-3 上并行启动？

---
