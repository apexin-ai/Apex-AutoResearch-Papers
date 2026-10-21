# analysis m4 contamination

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_m4_contamination_20260522T091212_result.json`
- **Structured JSON:** [`d99e2342d79981ff8cd8.json`](../../sessions/d9/d99e2342d79981ff8cd8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

**结论：Contamination risk = LOW**

核心证据：
1. **Per-type accuracy 高方差** (std=0.147)：15/80 types 低于 70%（最低 16.7%），与记忆模式不符
2. **跨模型一致性**：4 个模型家族（Qwen3/LLaMA/Gemini）的 count-degradation 斜率几乎相同（-30.1pp vs -30.7pp）
3. **BCS 因果机制成立**：IntraSub 错误随 BCS 单调递增（ρ=0.954），100% 类型混淆都是 intra-batch，这个模式无法被记忆解释
4. **跨数据集复现**：DocRED（r=-0.760）和 Few-NERD 上都观察到相同效应
5. **Wikipedia 文本 vs 任务格式**：原始文本可能在预训练中，但 schema-conditioned extraction 的任务格式不在

报告已保存并注册，包含论文中 address 此问题的建议措辞。

---
