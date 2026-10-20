# paper discussion draft

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_discussion_draft_20260514T003756_result.json`
- **Structured JSON:** [`a4b981eef8c8b1e0ff08.json`](../../sessions/a4/a4b981eef8c8b1e0ff08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译通过，输出 16 页 PDF，无错误。

完成内容：
- **§5.1** 新增 exp-005 feature degradation 段落：surprisal variance 特征跨模型一致退化（ρ≥0.85），解释为什么两步即耗尽可区分信号
- **§5.2** 将 transfer retention 数据量化为"70-85% text-intrinsic + 15-30% model self-familiarity"分解，强调 Pythia↔OLMo 91-92% 跨架构迁移
- **§5.5** 新增 θ-sensitivity limitation：θ=0.55→K\*=3, θ∈[0.60,0.65]→K\*=2, θ=0.70→K\*=1（限制数从6增至7）
- **§5.6 Broader Impact** 全新章节：synthetic data curation（三级分类法 + one-wash laundering）、model collapse 关联（prompt-chain vs retrain-chain）、depth-aware detection 优于 binary detection
- C3 占位符 `% TODO: exp-006 graduated filtering 结果填充` 保留

---
