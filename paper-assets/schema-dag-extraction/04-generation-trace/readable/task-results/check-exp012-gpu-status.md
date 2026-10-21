# check exp012 gpu status

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp012_gpu_status_20260515T171029_result.json`
- **Structured JSON:** [`2f71df28ccb1306c0bcf.json`](../../sessions/2f/2f71df28ccb1306c0bcf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇报：

1. **GPU**：cuda:0 空闲，0MiB 显存占用，无 Python 进程。
2. **tmux**：`tmux ls` 被 read-only 白名单拦截，无法执行。
3. **PID 303055**：已死，`ps` 返回空结果（exit code 1）。
4. **日志**：exp012 r3 的进程 PID 303070 被 **Killed**（信号 137 = OOM Killer），退出码 137。进程在加载数据和 embedding 后、刚开始 extraction 就被杀了。

**结论：exp012 没在跑，进程已被 OOM kill。** 显存 97GB 的卡当前完全空闲。日志显示是 host memory（非 GPU OOM）导致的 kill，因为进程刚加载完数据就死了，还没上 GPU。

---
