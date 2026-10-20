# research d134 reference verification

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_d134-reference-verification_20260518T102656_result.json`
- **Structured JSON:** [`23f9628ec4c92c8af98c.json`](../../sessions/23/23f9628ec4c92c8af98c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。

```
=== 论文 1: Cao et al. 2026 ===
arXiv ID 2601.22642: ✅ 存在
实际标题: "Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification"
作者: Chuxue Cao, Jinluan Yang, Haoran Li, Kunhao Pan, Zijian Zhao, Zhengyu Chen, Yuchen Tian, Lijun Wu, Conghui He, Sirui Han, Yike Guo
提交日期: 2026-01-30
摘要概要: 提出 formal logic verification 与自然语言生成动态交织的框架，在推理链中实时检测和修正逻辑错误（区别于被动的 post-hoc 验证）。用 SFT + policy optimization 两阶段流水线训练，7B/14B 模型在 6 个 benchmark 上分别超 baseline 10.4%/14.2%。
与本文相关性: 中高
  - 共同点：formal logic verification 作为 RL 训练信号、intermediate reasoning 质量控制
  - 差异：他们做 interleaved real-time verification，我们做 post-hoc ISR reward shaping + hacking taxonomy
  - 未提及 Goodhart's Law 或 reward hacking
建议引用位置: Related Work（formal verification for reasoning 子节）+ Introduction（现有方法对比）

=== 论文 2: Wang et al. 2025 ===
arXiv ID 2510.01367: ✅ 存在
实际标题: "Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort"
作者: Xinpeng Wang, Nitish Joshi, Barbara Plank, Rico Angell, He He
提交日期: 2025-10-01（v4: 2026-03-02）
摘要概要: 提出 TRACE（Truncated Reasoning AUC Evaluation），通过逐步截断 CoT 测量 reasoning effort 来检测 implicit reward hacking。核心观察：hacking 比真正解题"更容易"，hacker 只需 CoT 的一小部分就能获得高 reward。在 math reasoning 上比 72B CoT monitor 高 65%，coding 上比 32B monitor 高 30%。也在 OpenReview 上有记录。
与本文相关性: 高
  - 直接相关：reward hacking 检测、reasoning effort 量化
  - 我们的 ISR（Inference Step Redundancy）本质上也是量化 reasoning effort/necessity
  - TRACE 用截断 AUC 检测 hacking，我们用 per-step ablation 检测 hacking
  - 互补视角：他们做 detection，我们做 reward shaping + taxonomy
建议引用位置: Related Work（reward hacking detection 子节）+ Introduction（motivation for detecting hacking）+ Discussion（与 TRACE 方法论对比）
```

两篇论文均真实存在，arXiv ID 和标题完全匹配。Wang et al. (TRACE) 与本文高度相关，应重点引用；Cao et al. 属于 formal verification for reasoning 方向，相关但角度不同。

---
