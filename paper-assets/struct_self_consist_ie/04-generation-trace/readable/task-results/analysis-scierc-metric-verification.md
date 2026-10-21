# analysis scierc metric verification

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_scierc-metric-verification_20260524T083725_result.json`
- **Structured JSON:** [`11a121dd7bb7d26db1bf.json`](../../sessions/11/11a121dd7bb7d26db1bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。核心结论：

1. **greedy 字段存在且正确使用** — samples.jsonl 里 551/551 个实例都有 `greedy` 字段（T=0 decode），old script 的 `inst.get("greedy", inst["samples"][0])` 正确取到了它

2. **64.67% vs 66.3% 的差距完全来自 metric 类型** — micro-F1（论文用的）vs instance-averaged F1（construction 脚本用的），差距约 1.8-2.1pp，与观察到的 ~1.6pp 完全吻合

3. **用论文一致的 micro-F1 重算后，LP construction Δ = -0.20pp（p=0.78）**，5个seed中只有1个正向。+1.11pp 的增益完全是 metric 不一致的产物

**对论文 patch 的影响**：SciERC 上的 construction 增益在 micro-F1 下不成立。需要决定：
- 整篇论文改用 instance-averaged F1（需要修改所有 baseline 数字）
- 或接受 construction 在 SciERC micro-F1 下无效，调整 claim

---
