# paper discussion ece bidirectionality

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_discussion_ece_bidirectionality_20260517T200348_result.json`
- **Structured JSON:** [`ecc72670f4b4fa1d9fa2.json`](../../sessions/ec/ecc72670f4b4fa1d9fa2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。新段落插入在 line 82，位于 "Token entropy versus perplexity" 和 "NLP-specific constraints on lead-lag analysis" 之间。

**插入位置**: discussion.tex 第 82 行，`\paragraph{ECE bidirectionality in cross-domain transfer.}`

**段落内容**（7 句，~220 words）：
1. C4 域揭示 canary 信号方向性的质性差异（WikiText 中不可见）
2. token_entropy 保持完美单向性（rev=0/4），ECE 双向耦合（rev=3/4，均为 diversity→ECE）
3. 1000 次 permutation bootstrap 一致，排除统计噪声
4. 机制：ECE 对输出分布形状敏感，diversity collapse 重塑 calibration bins 产生反向通道
5. token_entropy 是 held-out 上的标量，不受模型自身输出分布反馈影响
6. 实践建议：token_entropy 为首选 canary，ECE 为辅助（α=0.50 时互补但需谨慎解读）
7. 框架价值：多方法框架独有的诊断能力，单指标系统无法区分干净信号与受反馈污染的信号

---
