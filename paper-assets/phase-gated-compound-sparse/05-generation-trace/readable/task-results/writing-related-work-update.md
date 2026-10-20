# writing related work update

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_related-work-update_20260514T145115_result.json`
- **Structured JSON:** [`668cf186803bddb59135.json`](../../sessions/66/668cf186803bddb59135.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

RC5 和 RC6 已更新，4 篇论文的区分论述已插入：

**RC5** 新增逐篇区分：
- **ThinKV**: 单轴 phase-aware KV 压缩 → 我们是双轴 compound interaction 随 phase 变化，ThinKV 是分析维度的子集
- **Physics of KV Cache Compression**: 机制层面最接近，但维度正交——他们是单轴压缩率 critical threshold，我们是 compound interaction 被 reasoning phase 调制
- **HIES**: score collapse 为我们的 discrimination collapse 提供独立 supporting evidence（单轴对应）
- **R-KV**: task-specific optimization vs 我们的 mechanistic analysis，目标不同

**RC6** 新增整体定位区分：
- Physics of KV 的 "phase" 是 compression-rate phase vs 我们的 reasoning phase，语义不同
- ThinKV/R-KV 都是单轴 phase-aware，无法观察到 compound interaction 的涌现现象
- HIES 的 collapse 佐证我们的机制，但未研究 compound setting 的放大效应
- Related Work §2 定位总结：六篇工作各归其位，我们 = compound × phase × strategy 三维交互

---
