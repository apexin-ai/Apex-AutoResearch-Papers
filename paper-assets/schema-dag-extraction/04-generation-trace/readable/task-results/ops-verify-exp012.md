# ops verify exp012

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_exp012_20260515T140828_result.json`
- **Structured JSON:** [`17d4506e8990d9d6a272.json`](../../sessions/17/17d4506e8990d9d6a272.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

| 检查项 | 状态 |
|--------|------|
| **tmux** | `tmux` 不在 read_only 白名单，无法查 |
| **PID 273161** | **已死**（exit code 1，无输出） |
| **GPU** | NVIDIA RTX PRO 6000 Blackwell (98GB)，显存 0 MiB / 利用率 0% — 空闲 |
| **日志尾部** | **exp-012 崩溃退出**，exit code 1 |

**崩溃原因**：vLLM engine core 初始化失败 — `RuntimeError: Engine core initialization failed` ，traceback 指向 `vllm/v1/engine/utils.py:1178` 的 `wait_for_engine_startup`。日志显示 `Failed core proc(s): {}`，说明 engine core 子进程启动后立即挂掉，未返回具体错误。

需要查看日志中更早的部分（root cause 在 traceback 上方）来定位具体原因。是否继续排查？

---
