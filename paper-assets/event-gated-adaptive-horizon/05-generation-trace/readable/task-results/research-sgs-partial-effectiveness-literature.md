# research sgs partial effectiveness literature

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_sgs-partial-effectiveness-literature_20260517T225544_result.json`
- **Structured JSON:** [`8c06e0a527698e49ca9e.json`](../../sessions/8c/8c06e0a527698e49ca9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**文献搜索结果** — Full-SGS 环境依赖效果有充分文献支持：

| 论文 | 核心发现 |
|------|----------|
| Ma et al. (ICML 2024) | World model 的 policy gradient 随 horizon 指数衰减；gradient path 质量是环境依赖的 |
| Heess et al. (NeurIPS 2015, SVG) | SVG(0)（无 model gradient）仅简单任务有效；复杂任务需 SVG(1+) |
| Amos et al. (L4DC 2021) | 完全无 dynamics gradient 比有噪声的 dynamics gradient 更差 |
| Nauman et al. (ICML 2024) | 60+ agents / 14 tasks：regularization effectiveness fundamentally task-dependent |

**机制解释**：DreamerV3 连续控制 actor 依赖 dynamics backprop 作为主要梯度来源。Full-SGS 完全阻断此通路。Walker（2关节/浅层 credit assignment）能靠残余信号存活；Cheetah（6关节/深层协调）被梯度饥饿（actor_grad_norm=0.0-0.1），但因 DreamerV3 的 categorical value + normalization 隐式正则化最终自恢复。

**论文 framing**：这不是 SGS 的失败，而是论证 event-gated selective intervention 优于 blanket SGS 的证据。

已更新：literature_map.yaml（+4 papers, survey_tag: sgs-partial-effectiveness）、memory.md（新增段落）。

---
