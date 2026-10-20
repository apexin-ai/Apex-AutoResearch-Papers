# experiment crossmodel sica recheck

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_crossmodel-sica-recheck_20260521T092448_result.json`
- **Structured JSON:** [`e729c273848218d99700.json`](../../sessions/e7/e729c273848218d99700.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**进程存活** — PID 414515，已运行 44 分钟。

**当前进度: 11/204 (5.4%)**
- checkpoint 记录 11 个已完成样本
- 第 12 个样本正在处理中（已完成 3/4 extraction 阶段）
- 每个样本包含 4 个 extraction 阶段：Mistral same → Mistral→Qwen3 cross → Qwen3 same → Qwen3→Mistral cross
- VLLM 双端口（8000/8001）均正常响应

**速度估算**: ~4 分钟/样本，剩余 193 个样本 ≈ **12.9 小时**，预计 **5月22日 ~06:20** 完成。

**注意**: Qwen3→Mistral cross-extraction 频繁产出 0 constraints（11 个样本中有 6 个为 0），可能影响最终实验结论质量。

---
