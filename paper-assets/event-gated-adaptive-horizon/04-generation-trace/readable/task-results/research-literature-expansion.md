# research literature expansion

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-expansion_20260514T093911_result.json`
- **Structured JSON:** [`1e351accc00b3bc8be1e.json`](../../sessions/1e/1e351accc00b3bc8be1e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。`literature_map.yaml` 已创建，包含 28 篇论文（5 篇原有 + 23 篇新增），覆盖全部 10 个审稿人要求的领域。

关键注意事项：
- **Braylan et al. 是 2015 年**，不是任务中写的 2005 年（AAAI Workshop 2015）
- **"Delusional policies" (Delalleau et al. 2019)** 未找到确切匹配——最接近的是 **Lu et al. 2018 "Non-delusional Q-learning" (NeurIPS)**，这是该领域的奠基论文
- **THICK (Gumbsch et al. 2024, ICLR)** 和 **Hieros (Mattes et al. 2024, ICML)** 是最相关的 concurrent work，都通过层级化而非 variable-dt 来实现 temporal abstraction

每篇论文均通过 WebSearch 确认了标题、作者、年份和 venue。新增文献列表已追加到 `memory.md`。

---
