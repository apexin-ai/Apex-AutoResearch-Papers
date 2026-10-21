# research r17 reference verification

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_r17-reference-verification_20260520T070446_result.json`
- **Structured JSON:** [`cb2b0d11f24ee41b6b4d.json`](../../sessions/cb/cb2b0d11f24ee41b6b4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成，结果如下：

```
引用 1: arXiv:2601.22642
- 真实: YES
- 实际标题: Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification
- 实际作者: Cao et al. (Chuxue Cao, Jinluan Yang, Haoran Li, Kunhao Pan, Zijian Zhao 等)
- 年份: 2026 (January 30)
- 与我们工作相关: YES — 形式逻辑验证引导的 RLVR 训练框架，动态插入符号验证反馈纠正推理错误，直接涉及 verifiable reward + reasoning
- 注意事项: R17 声称 "Xie et al. (2025)" 是错误的。实际第一作者是 Cao，年份是 2026。我们 bib 中 Cao et al. (2026) 的登记是正确的。R17 给出的作者和年份均为 hallucinated。

引用 2: arXiv:2601.11061
- 真实: YES
- 实际标题: Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs
- 实际作者: Yan et al. (Lecheng Yan, Ruizhe Li, Guanhua Chen, Qing Li, Jiahui Geng 等)
- 年份: 2026 (January 16)
- 与我们工作相关: YES — 直接研究 RLVR 中的 spurious reward 导致模型走捷径（memorization shortcut），发现 Perplexity Paradox 和 Anchor-Adapter circuit，与我们的 reward hacking / Goodhart 效应高度相关

引用 3: arXiv:2509.15557
- 真实: YES
- 实际标题: Reward Hacking Mitigation using Verifiable Composite Rewards
- 实际作者: Mirza Farhan Bin Tarek, Rahmatollah Beheshti (University of Delaware)
- 年份: 2025 (September 19)
- 与我们工作相关: YES — 直接研究 RLVR 中的 reward hacking（跳过推理直接给答案、利用格式漏洞），提出 composite reward 缓解策略，与我们的 ISR hacking taxonomy 互补
```

**总结**: 三篇引用全部真实存在且与我们工作高度相关。唯一问题是引用1的作者和年份：R17 声称 Xie et al. (2025)，实际是 Cao et al. (2026)，我们 bib 现有登记正确，无需修改。

Sources:
- [arXiv:2601.22642](https://arxiv.org/abs/2601.22642)
- [arXiv:2601.11061](https://arxiv.org/abs/2601.11061)
- [arXiv:2509.15557](https://arxiv.org/abs/2509.15557)

---
