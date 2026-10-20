# research related work survey

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_related_work_survey_20260514T012010_result.json`
- **Structured JSON:** [`45bbbac9d64686772196.json`](../../sessions/45/45bbbac9d64686772196.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文献调研已完成，保存到 `artifacts/related_work_survey.md`。

覆盖了 26 篇论文（2023-2025），分三个方向整理。核心发现：

**Direction 1**：没有工作成功用 spectral effective rank 检测 iterative model collapse。Spectral Flattening 论文发现 eff_rank 上升 = collapse，与我们的 negative result 一致。多个独立工作验证 entropy-based 指标更有效。

**Direction 2**：Accumulate > Replace 是共识。Strong Model Collapse（ICLR 2025）证明 0.1% synthetic 即可 collapse，说明主动调节必要。"Model Collapse Does Not Mean What You Think" 指出 8 种矛盾定义需要注意。

**Direction 3**：所有现有 adaptive mixing（DoReMi/Aioli/RegMix/Chameleon）都基于 loss 信号做 domain-level mixing。**没有方法用 collapse detection 信号驱动 real/synthetic ratio 调节，也没有控制论视角的工作**。这是我们最清晰的 novelty 空间。

---
