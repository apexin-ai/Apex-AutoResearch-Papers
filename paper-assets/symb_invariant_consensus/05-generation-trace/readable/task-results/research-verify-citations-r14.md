# research verify citations r14

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_verify-citations-r14_20260522T134400_result.json`
- **Structured JSON:** [`3b6c3dd11df4af57be5c.json`](../../sessions/3b/3b6c3dd11df4af57be5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三篇全部验证完毕，结果如下：

---

### 论文 1: SETS

```
标题: SETS: Leveraging Self-Verification and Self-Correction for Improved Test-Time Scaling
作者: Jiefeng Chen, Jie Ren, Xinyun Chen, Chengrun Yang, Ruoxi Sun, Jinsung Yoon, Sercan Ö. Arık
发表: arXiv:2501.19306 (2025年1月)
摘要要点: 提出 Self-Enhanced Test-Time Scaling (SETS)，策略性结合 parallel sampling 和 sequential self-correction，利用 LLM 内在的 self-verification 和 self-correction 能力提升 test-time scaling 效率。解决了 parallel 方法快速饱和、sequential 方法几轮后停滞的问题。
与我们的关系: 直接相关——self-verification 在 test-time scaling 中的正面效果
arXiv ID 是否正确: 是
```

### 论文 2: MAV

```
标题: Multi-Agent Verification: Scaling Test-Time Compute with Multiple Verifiers
作者: Shalev Lifshitz, Sheila A. McIlraith, Yilun Du
发表: arXiv:2502.20379 (2025年2月)
摘要要点: 提出 Multi-Agent Verification (MAV) 范式，引入"扩展 verifier 数量"作为 test-time compute 的新维度。使用 Aspect Verifiers（不同 LLM 验证输出的不同方面）无需额外训练，BoN-MAV 算法展现出比 self-consistency 和 reward model verification 更强的 scaling 模式，且能实现 weak-to-strong generalization。
与我们的关系: 直接相关——multi-agent verification 扩展 test-time compute
arXiv ID 是否正确: 是
```

### 论文 3: Reflexion

```
标题: Reflexion: Language Agents with Verbal Reinforcement Learning
作者: Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao
发表: arXiv:2303.11366 / NeurIPS 2023
摘要要点: 提出通过语言反馈（而非权重更新）强化 language agents 的框架。Agent 对 task feedback 进行 verbal self-reflection，将反思文本存入 episodic memory 以改进后续决策。在 HumanEval 上达到 91% pass@1（超过 GPT-4 的 80%）。
与我们的关系: 直接相关——self-correction via natural language feedback 的开创性工作
arXiv ID 是否正确: 是（2303.11366，非用户提供的 ID——用户未给出具体 ID，确认正确 ID 为 2303.11366）
```

---

三篇论文全部真实存在，arXiv ID 均正确，内容与据称描述一致。

Sources:
- [SETS - arXiv](https://arxiv.org/abs/2501.19306)
- [SETS - HuggingFace Papers](https://huggingface.co/papers/2501.19306)
- [MAV - arXiv](https://arxiv.org/abs/2502.20379)
- [MAV - OpenReview](https://openreview.net/pdf?id=LriQ3NY9uL)
- [Reflexion - arXiv](https://arxiv.org/abs/2303.11366)
- [Reflexion - NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/file/1b44b878bb782e6954cd888628510e90-Paper-Conference.pdf)
- [Reflexion - GitHub](https://github.com/noahshinn/reflexion)

---
