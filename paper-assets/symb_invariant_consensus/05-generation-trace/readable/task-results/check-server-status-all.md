# check server status all

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_server-status-all_20260523T201122_result.json`
- **Structured JSON:** [`25b299c02d63c98bcad9.json`](../../sessions/25/25b299c02d63c98bcad9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇总

### westd-30973 (3× RTX PRO 6000 Blackwell)

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 0 / 98 GB | 0% |
| 1 | 0 / 98 GB | 0% |
| 2 | 88 / 98 GB | 97% |

| 实验 | 状态 | 进度 | 备注 |
|------|------|------|------|
| LLaMA seed456-v2 | **running** | **597/600** | cuda:2, 即将完成（几分钟内） |
| LLaMA seed789-v2 | **killed** | 378/600 | exit code 129, 05-23 18:23 被杀，从 326 推进到 378 后停止。vLLM 已关闭，**需要恢复** |
| Qwen2.5 seed789-v3 | **killed** | 339/600 | 如预期，无需恢复 |

---

### westd-16639 (4× RTX PRO 6000 Blackwell)

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 88 / 98 GB | 100% |
| 1 | 0 / 98 GB | 0% |
| 2 | 88 / 98 GB | 100% |
| 3 | 88 / 98 GB | 100% |

| 实验 | 状态 | 进度 | 备注 |
|------|------|------|------|
| Qwen3-14B seed123 | **running** | 71/600 | cuda:0, port 8020 |
| Qwen3-14B seed456 | **running** | 71/600 | cuda:2, port 8021 |
| Qwen3-14B seed789 | **running** | 72/600 | cuda:3, port 8022 |

Qwen3 三个种子 02:07 启动，2h 完成 ~71 个，速率 ~35/h，预计还需 **~15h**，约今天 **19:00** 完成。

---

**需要关注的问题：**
1. **LLaMA seed789-v2 被意外杀死**，停在 378/600，cuda:1 和 vLLM 都已空闲。需要重新启动 vLLM + resume 才能继续。
2. **LLaMA seed456-v2 即将完成**（597/600），完成后 cuda:2 上的 vLLM 可以复用给 seed789-v2。

---
