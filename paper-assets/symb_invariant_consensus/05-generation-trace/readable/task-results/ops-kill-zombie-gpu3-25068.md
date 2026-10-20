# ops kill zombie gpu3 25068

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-zombie-gpu3-25068_20260519T151619_result.json`
- **Structured JSON:** [`e237f93e9a8b01b09c24.json`](../../sessions/e2/e237f93e9a8b01b09c24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果汇报：**

| 项目 | 状态 |
|------|------|
| GPU 3 PID 192666 (`VLLM::EngineCore`) | 已 kill，88106MiB 显存已释放 |
| tmux `exp062_vllm` | 已 kill |
| tmux `exp062_run` | 不存在（已自行退出） |
| GPU 3 最终状态 | **0MiB / 97887MiB，0% util，完全空闲** |

GPU 1 上有另一个 vLLM 进程 (PID 236050, 90232MiB, 96% util) 正在活跃运行，未动。

---
