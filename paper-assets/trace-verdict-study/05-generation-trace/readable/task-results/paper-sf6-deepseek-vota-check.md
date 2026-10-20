# paper sf6 deepseek vota check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_sf6_deepseek_vota_check_20260521T084417_result.json`
- **Structured JSON:** [`a347d6720a4cbde64fc3.json`](../../sessions/a3/a347d6720a4cbde64fc3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是分析结果：

---

## DeepSeek VOTA outlier 处理现状

### Table 2（experiments.tex，主表）
- DeepSeek VOTA 报告为 **99.25‡**（2-seed mean），不是 3-seed mean
- 脚注 `‡` 明确说明：`DeepSeek VOTA 3 seeds: 84.45/99.16/99.33; seed 42 (84.45%, fail recall=45.4%) is a training failure due to tokenizer-driven truncation (Appendix §tokenizer_analysis), reported as 2-seed mean.`

### experiments.tex 正文（§VOTA cross-family variation, L59-61）
- 明确说 "Excluding outlier seeds, VOTA achieves ≥98.57%"
- 单独一句详细说明：seed 42 是 training failure，原因是 tokenizer-induced truncation（91.7% samples affected），seeds 123/456 match cross-model performance

### appendix.tex
- **Full results table** (tab:full_deepseek, L242-244)：三个 seed 逐行列出，seed 42 标注 "training failure; fail recall = 45.4%"
- **Tokenizer analysis section** (L256-262)：详细解释 seed 42 failure 机制——DeepSeek tokenizer 平均 2626 tokens/sample vs Qwen 1929，91.7% 训练样本超出 2048 context window；seeds 123/456 避开了 truncation-sensitive initialization basin
- **Per-class metrics table** caption (L8)：也标注了 seed 42 是 training failure

### discussion.tex
- 无直接提及 seed42/outlier 关键词，但有 tokenizer instability 的讨论（L31, L42）

---

## 结论：处理正确，无需修改

论文已经全面、正确地处理了 seed42 outlier：
1. **主表**用 2-seed mean (99.25%) 而非 3-seed mean (94.31%)，避免 outlier 拉低数值
2. **脚注**透明披露全部 3 个 seed 的原始数值和排除理由
3. **正文**单独段落解释 outlier 成因（tokenizer truncation）
4. **Appendix** 提供完整 seed-level breakdown 和详细 tokenizer analysis
5. 标记符号 `‡` 贯穿一致，读者可追溯

D111 SF-6 的要求已满足。

---
