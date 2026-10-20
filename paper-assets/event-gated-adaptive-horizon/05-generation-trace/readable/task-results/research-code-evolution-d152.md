# research code evolution d152

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_code_evolution_d152_20260525T155900_result.json`
- **Structured JSON:** [`cfe24260393eea5326af.json`](../../sessions/cf/cfe24260393eea5326af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/d152_code_evolution_report.md`。

## 调查结论

**主因：`subsample_variable_dt` 参数路由 bug (BF1)**

旧代码 `models.py:172` 将 `gate_max_dt=8` 传给 `subsample_variable_dt`，完全忽略了 `gate_subsample_max_dt=2`。旧 `tools.py` 的函数签名也不接受 `effective_max_dt` 参数。结果：

- **旧代码实际行为**：dt 从 {1,2,3,4,5,6,7,8} log-uniform 采样 → 训练时 70%+ 数据用 dt≠1，想象时永远 dt=1 → 巨大的 train/imagination 分布 gap → 触发 CIVO
- **新代码正确行为**：dt 仅从 {1,2} 采样 → 分布 gap 极小 → CIVO 不触发

**次因：replay sampling seed bug (BF2)** — 旧代码 `sample_episodes(seed=0)` 硬编码，所有 seed 共享相同 replay 采样顺序。

**结论：旧 008e_v3 数据 (2/5 collapse) 无效**——它运行的实际上是一个不同的实验（dt 范围 1-8 而非 1-2）。论文应仅引用当前代码数据 (0/4 CIVO)。

---
