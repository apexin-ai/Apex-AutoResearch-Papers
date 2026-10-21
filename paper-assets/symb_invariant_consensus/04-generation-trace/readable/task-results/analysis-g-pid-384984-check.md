# analysis g pid 384984 check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_g-pid-384984-check_20260520T111709_result.json`
- **Structured JSON:** [`f7454971d4ba9ce2fe1d.json`](../../sessions/f7/f7454971d4ba9ce2fe1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 回答

### 1. PID 384984 状态: **DEAD**

`ps -p 384984` 返回空，进程不存在。

### 2. 当前活跃的 direction_g 进程

| PID | 启动时间 | 运行时长 | 命令 |
|-----|---------|---------|------|
| **307169** | 18:15 | ~1h02m | `python -u direction_g_decoupling.py` |

这是唯一活跃的 direction_g 进程。PID 384984 已死，307169 是后续重新启动的实例。

### 3. 进度

日志显示当前在 **conservative 策略**，已完成 **60/204** 题。

- 当前 accuracy: 0.633 (38/60)
- 速率: ~0.02 prob/s
- ETA: ~8655s (~2.4h)
- `results.json` 里只有 3 题的 dry-run 结果（旧文件），尚未被当前运行覆盖

还有 3 个策略要跑（conservative → standard → aggressive），总时间预计 **~7-8h**。

### 4. 其他相关进程

同一服务器上还有：
- **PID 314822** — `direction_q_premise_mutation.py`（19:15 启动，端口 8020）
- 4 个 vLLM 实例分别占 GPU 0-3（端口 8012/8013/8020/8021）
- direction_g 使用的是 port 8012 或 8013（共享 vLLM）

---
