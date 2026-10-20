# infra download diagnose

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_download-diagnose_20260515T093832_result.json`
- **Structured JSON:** [`2b9bd032f5ac7d4be7b6.json`](../../sessions/2b/2b9bd032f5ac7d4be7b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

vLLM is up and serving QwQ-32B!

**汇报：**

1. **下载诊断**：ModelScope 并行下载 6 个分片，速度 17-26 MB/s（稳定增长），无阻塞问题。下载走的是 ModelScope cache 结构（`Qwen/QwQ-32B/` 嵌套路径），不是平坦目录。

2. **采取的措施**：
   - 持续监控下载进度直到完成（从 ~46GB 到 ~62GB，约 20 分钟）
   - 清理了 `._____temp/` 和 `.lock/` 目录
   - 另一个 Worker 在我的首次 vLLM 启动失败后（engine core 初始化错误），成功以 `max_model_len=16384` 启动了 vLLM

3. **最终状态**：
   - 14/14 shards 全部下载完成，模型路径 `/root/autodl-tmp/models/QwQ-32B/Qwen/QwQ-32B/`
   - vLLM 0.20.2 已启动，bfloat16，61.04 GiB 显存占用
   - 服务端点：`http://localhost:8000/v1/models`
   - GPU：RTX PRO 6000 Blackwell (98GB)，充足空间
   - `max_model_len=16384`，最大并发 5.31x

---
