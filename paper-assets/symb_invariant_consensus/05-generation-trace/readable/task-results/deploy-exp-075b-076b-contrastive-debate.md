# deploy exp 075b 076b contrastive debate

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_exp-075b-076b-contrastive-debate_20260519T174515_result.json`
- **Structured JSON:** [`0f72dc00a1353bc36185.json`](../../sessions/0f/0f72dc00a1353bc36185.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp-075 和 exp-076 正在服务器上活跃运行：**

- **exp-075 (Contrastive)**: 进度 [17/204]，ETA ~170 分钟，输出到 `results/exp075_contrastive_mistral_folio/`，vLLM 在 port 8002 (GPU 2)
- **exp-076 (Debate)**: 正在处理中，输出到 `results/exp076_debate_mistral_folio/`，vLLM 在 port 8003 (GPU 3)
- **exp-074**: 也在运行，port 8000 (GPU 0)

这些 sessions 是今天 01:29-01:39 创建的，看起来已经被重启过了。

GPU 2 和 3 当前被这些实验占用。要部署 exp-075b/076b，需要先 kill 当前运行的 exp-075/076。要继续吗？还是等当前实验跑完？

---
