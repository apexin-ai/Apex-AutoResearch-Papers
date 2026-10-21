# check home cwm8b eval feasibility

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_home-cwm8b-eval-feasibility_20260515T141430_result.json`
- **Structured JSON:** [`8ef916922b2e8f61abb2.json`](../../sessions/8e/8ef916922b2e8f61abb2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 评估结论：home-1x5090 当前不可达

SSH 连接全部超时（5 次尝试，每次 10s timeout），服务器可能：
- 关机/休眠
- 网络配置变更（IP/端口变了）
- SSH 服务未启动

**无法完成评估。** 需要你先确认 home-1x5090 是否在线，检查 SSH 连接信息是否最新。

---

**替代方案建议**（不依赖 home 服务器）：

1. **westd 多 GPU 并行**：当前 eval 只用 cuda:3，检查 cuda:0/1/2 是否空闲，在 westd 上直接 shard 到多卡并行跑
2. **优化单卡速度**：增大 batch size（如果显存允许）、用 vLLM 替代 HF generate 加速推理
3. **home 恢复后再评估**：服务器上线后我可以重新跑这套检查

要我先检查 westd 的其他 GPU 是否空闲？

---
