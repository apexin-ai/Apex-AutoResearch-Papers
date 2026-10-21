# research pi05 server client

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_pi05-server-client_20260522T054649_result.json`
- **Structured JSON:** [`dcca834fc6501c625f4d.json`](../../sessions/dc/dcca834fc6501c625f4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/pi05_server_client_feasibility.md`。

核心结论：

1. **技术上完全可行**，无 showstopper。推荐 **FastAPI Server** 方案，实现复杂度 4-6 小时。

2. **GPU 节省显著**：6 GPU → 1-2 GPU。单张 4090 可同时跑 model server (13GB) + EGL 渲染 (<1GB)。

3. **但吞吐收益有限**：PI05 的 chunk_size=50 意味着每 50 步才推理一次（300 步 rollout 仅 6 次推理），GPU 利用率本来就 <10%。Server 化主要价值是**省卡**，而非提速。

4. **额外优化机会**：K-sample 串行循环可改为 batch 并行（K=10 时推理部分 3-5× 加速），这个优化独立于 server 架构，可单独做。

5. **关键实现细节**：server 应返回完整 50 步 action chunk 让 client 本地 replay，而非每步都调 server。

---
