# paper post llama consistency check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_post_llama_consistency_check_20260516T224223_result.json`
- **Structured JSON:** [`6d76979efae35f13d601.json`](../../sessions/6d/6d76979efae35f13d601.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 一致性检查结果

### Tex 文件内部一致性

**总体：tex 文件之间高度一致。** LLaMA 数据（n=250, d_z=0.81-1.15, imp/rand ratio 2.0-2.6×）和"architecture-dependent"表述在 abstract/introduction/results/conclusion/appendix 中完全统一。

发现以下问题：

#### 问题 1: appendix_moved.tex 内部矛盾（"2.7-20×"）
- **Line 88**: "but $2.7$--$20{\times}$ weaker than importance-based"
- **Line 100** (同文件): "the random phase gradient is $2.7$--$3.5{\times}$ weaker"（带具体数字验证：0.39 vs 1.07, 0.91 vs 3.16）
- Line 100 正确。Line 88 的"20×"无法从数据验证（Qwen s025=2.7×, s030=3.5×）。

#### 问题 2: conclusion.tex "n=500" vs results.tex "n=496"
- conclusion.tex line 4: "DeepSeek, $n{=}500$"
- results.tex table 1 caption: "$n{=}496$"
- 实验入组 500，排除 4 得到 n_eff=496。Conclusion 用 500 指实验规模是可接受的，但与 results 不一致，审稿人可能注意到。

#### 问题 3: discussion.tex GSM8K "~3×" 的来源
- discussion.tex line 8: "MATH-500 ($15$--$17{\times}$) $>$ GSM8K (${\sim}3{\times}$)"
- 但 results.tex GSM8K 部分说 random 在 GSM8K 上全部 NS（CIs spanning zero）
- 若 random NS 则无法计算有意义的 imp/rand ratio。"~3×"来源不明确（可能从原始 Δ 值计算但统计无效）。

---

### paper_framing.md 与 tex 文件的不一致（需更新）

#### 问题 4（主要）: LLaMA 数据仍为旧 c3_llama n=50

paper_framing.md Core Insight:
> "imp_vs_rand d_z 0.19→0.34, 仅 s030 显著"

Tex 文件（n=250 data）:
- Random d_z = 0.41-0.46, ALL conditions p < 10^{-12}
- Imp/rand Δ ratio = 2.0-2.6×

paper_framing.md 的 "d_z 0.19→0.34, 仅 s030 显著" 是旧 n=50 数据，完全过时。

#### 问题 5: paper_framing.md "random d_z 0.35→0.44" vs tex d_z 0.41-0.46
- paper_framing.md: "random 在 LLaMA 上也显示显著 phase gradient（d_z 0.35→0.44）"
- Tex table: d_z = 0.436, 0.459, 0.424, 0.410 → range 0.41-0.46
- "0.35→0.44"不准确。

#### 问题 6: paper_framing.md "15-36×" vs tex "15-17×"
- paper_framing.md C1: "MATH-500: importance gradient 15-36× random"
- paper_framing.md RC1: "strategy ratio $15$--$36{\times}$"
- Tex 文件一致使用: "$15$--$17{\times}$"（DeepSeek），"$2.7$--$17{\times}$"（跨模型）
- 计算验证: DS s025=15.3×, DS s030=16.6× → 15-17× ✓
- **"36×"无来源**，可能是旧版计算残留。

#### 问题 7: paper_framing.md header "imp/rand 2.7-15×"
- 更新记录写 "imp/rand 2.7-15×"
- 实际: DeepSeek s030 = 16.6× ≈ 17×
- 应为 "2.7-17×"

#### 问题 8: paper_framing.md RC1 "n=50 限制功效"
- RC1: "(c) LLaMA 跨架构验证 n=50 限制功效"
- 已完成 n=250 验证（c8_llama_n250_fixed），此限制大幅缓解。

---

### 无问题确认

- "architecture-dependent" 在所有 6 个更新文件中一致使用 ✓
- DS median_diff (0.39/1.21/3.99/8.48) 全文一致 ✓
- QW median_diff (0.07/0.31/1.07/3.16) 全文一致 ✓
- LLaMA d_z=0.81-1.15 在 abstract/intro/results/conclusion/appendix 一致 ✓
- LLaMA imp/rand 2.0-2.6× 在所有位置一致 ✓
- 无遗留的旧 "pilot n=50" 数据出现在主文 tex 文件中（profiling subset n=50 有正确标注） ✓
- Cohen's d 数字 (DS 0.94, QW 0.92) 一致 ✓

---

### paper_framing.md 草拟更新

需要更新的部分：

**Core Insight 段落中的 LLaMA 部分，替换为：**

> LLaMA 跨架构验证（D060, c8_llama_n250_fixed）qualitative direction consistent（within-importance d_z=0.81-1.15, all p<10^-29），且 random 在 LLaMA 上所有条件均显著（d_z=0.41-0.46, all p<10^-12），imp/rand Δ ratio 仅 2.0-2.6×（vs DeepSeek 15-17×），strategy×phase 交互强度 architecture-dependent。

**C1 claim，"15-36×" 改为 "15-17×"：**

> MATH-500: importance gradient 15-17× random（DeepSeek s025-s030）

**Header 更新记录，"imp/rand 2.7-15×" 改为 "2.7-17×"**

**RC1 更新：**
- "(c) LLaMA 跨架构验证 n=50 限制功效" → "(c) LLaMA n=250 验证 strategy specificity 弱于 Qwen2 架构（2.0-2.6× vs 15-17×）"

**C8 部分，替换旧 n=50 数据描述：**

> D060 + c8_llama_n250_fixed: within-importance phase gradient 强(d_z=0.81-1.15, all p<10^-29) ✓。Random 所有条件显著(d_z=0.41-0.46, all p<10^-12)，与 DeepSeek/Qwen random 低 sparsity NS 模式定性不同。Imp/rand Δ ratio 2.0-2.6×（远低于 DS 15-17×）。n=250 功效充分。

---

### 建议修复优先级

1. **High**: paper_framing.md 的 LLaMA 数据全面更新（问题 4-8）
2. **Medium**: appendix_moved.tex line 88 的 "2.7-20×" → "2.7-3.5×"
3. **Low**: conclusion.tex "n=500" → "n=496"（或保持不变，加脚注说明）
4. **Low**: discussion.tex "~3×" GSM8K ratio 加限定语（raw magnitude comparison, random NS）

需要我执行这些修复吗？

---
