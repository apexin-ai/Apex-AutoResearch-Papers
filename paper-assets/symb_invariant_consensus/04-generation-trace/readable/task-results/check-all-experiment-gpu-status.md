# check all experiment gpu status

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_all-experiment-gpu-status_20260523T172210_result.json`
- **Structured JSON:** [`1489dc2bbbf2373842cd.json`](../../sessions/14/1489dc2bbbf2373842cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 活跃实验（westd-30973 GPU 2，共享 vLLM）

| 实验 | 进度 | 状态 |
|------|------|------|
| llama8b_pw_seed456_v2 | **496/600** (82.7%) | 🟢 运行中 |
| llama8b_pw_seed789_v2 | **330/600** (55.0%) | 🟢 运行中（01:18 恢复） |

### 需要关注

1. **qwen25_pw_seed789_v3** 在 339/600 处被 SIGTERM 杀掉（May 23 12:40 UTC），无运行进程。原始版本（westd-16639）已有 600/600 完整结果。
2. **westd-16639 上 3 个 vLLM 服务器空转**（GPU 0/2/3），占 ~260 GB VRAM，无实验在用。
3. 两个活跃实验共享一个 GPU，吞吐减半。

### 空闲 GPU：5 张

- westd-16639: GPU 1 完全空闲；GPU 0/2/3 可杀 vLLM 回收
- westd-30973: GPU 0/1 完全空闲

报告已写入 `experiment_status_20260524.md` 并注册。

---
