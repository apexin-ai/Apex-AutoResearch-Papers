# code exp 018 llama8b

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_018_llama8b_20260516T045518_result.json`
- **Structured JSON:** [`2f44b66c9eedad05a0ee.json`](../../sessions/2f/2f44b66c9eedad05a0ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认完成：

- **GPU 0**: 16041 MiB / 24564 MiB，利用率 96%，无 OOM 风险
- **pipeline 正常运行**: depth 1 generation 进行中，batch_size=4，~6.4s/batch
- **--scorer_path 修改已生效**: generation 用 LLaMA-3.1-8B，Step 4 feature extraction 将自动切换到 Qwen2.5-1.5B base
- **depth_0.jsonl 复用 exp-016 数据**: 5000 条 C4 seed data（避免 HF tree listing 死循环）

**Registry 已更新**: `exp_018_llama8b_depth` → RUNNING

**预估时间**: depth chain 5 层 ~11h + feature extraction ~1h + analysis ~0.5h ≈ 12-13h 总计。

---
