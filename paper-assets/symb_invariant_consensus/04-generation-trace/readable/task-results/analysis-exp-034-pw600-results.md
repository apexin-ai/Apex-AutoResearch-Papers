# analysis exp 034 pw600 results

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-034-pw600-results_20260518T193030_result.json`
- **Structured JSON:** [`7bdf5a8a14a674161b5b.json`](../../sessions/7b/7bdf5a8a14a674161b5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the complete analysis:

---

## exp-034 分析报告：Qwen2.5-14B PW-600 (Partial)

### 实验状态：INCOMPLETE — 93/600 完成后崩溃

崩溃原因：conda 环境丢失 (`python: command not found`)，tmux 日志记录 `EXIT_CODE=0`。

### 核心指标 (n=93, 全部 OWA-D5)

| Metric | SICA | SC | Delta |
|--------|------|----|-------|
| Accuracy | **77.42%** (72/93) | 74.19% (69/93) | **+3.23pp** |
| Correct | 72 | 69 | +3 |

- **McNemar p = 0.5078** — 不显著
- Discordant pairs: SICA-only=6, SC-only=3 (仅 9 对，样本太小)
- C0 (non-unanimous): 58.1%
- Avg majority fraction: 0.8324
- Extraction rate: 99.19%
- Avg unique constraints: 35.6/problem
- GT 分布均匀: True=32, False=28, Unknown=33

### Delta 收敛趋势

| 时间点 | n | SICA | SC | Delta |
|--------|---|------|----|-------|
| 中间结果 | 65 | 76.92% | 70.77% | **+6.15pp** |
| 最终(partial) | 93 | 77.42% | 74.19% | **+3.23pp** |

Delta 从 +6.15pp 缩减到 +3.23pp。SC 准确率上升更快（70.77%→74.19%），说明早期子集可能采样偏向 SICA 友好的题目。

### 9 个 Disagreement 问题的模式

**SICA 赢的 6 题**：全部是 SC 票数近似对半分的情况
- 典型: votes 5-5, 5-7, 6-6, 5-6, 4-8 — SC majority vote 在高 uncertainty 下选错
- SICA 的 MaxSAT 加权正确地解析了这些 ambiguous votes

**SC 赢的 3 题**：SICA 错误地被约束权重拉偏
- 2/3 是 GT=Unknown 但 SICA 选了 False（约束过度自信）
- 1/3 是 GT=True 但 SICA 选了 Unknown

### 与其他实验对比

| 实验 | 模型 | 数据集 | n | Delta | p |
|------|------|--------|---|-------|---|
| exp-026 | 14B | FOLIO-204 | 204 | **-0.49pp** | 1.0 |
| exp-035 | 7B | FOLIO-204 | 203 | **-0.49pp** | 1.0 |
| exp-033 | Mistral-7B | FOLIO-204 | 204 | **+4.90pp** | 0.013 |
| **exp-034** | **14B** | **PW-93** | **93** | **+3.23pp** | **0.51** |

### 对 regime-dependent framing 的意义

1. **方向性正面**：这是 Qwen-14B 首次在任何数据集上 SICA 方向性超越 SC (+3.23pp)，之前 FOLIO 上是 -0.49pp
2. **但不能下结论**：p=0.51 远不显著，且只完成 15.5% 的数据
3. **PW vs FOLIO 差异假说**：PW-D5 是纯规则推理（closed-world rules + chaining），约束提取更 structured → SICA 的约束质量可能更高。FOLIO 是自然语言逻辑，formalization 噪音更大
4. **C0=58.1%** 介于 14B-FOLIO (低) 和 Mistral-7B-FOLIO (81%) 之间 — 适度 diversity 下 SICA 有轻微优势
5. **关键限制**：93/600 太少，discordant pairs 仅 9 个，任何结论都 premature

### 下一步

**实验需要 resume 重跑剩余 507 题**。如果 discordant rate 保持 ~9.7%，完整 600 题应有 ~58 个 discordant pairs，McNemar 检验将有足够 power。按当前 2:1 (SICA:SC) 比率外推，完整结果可能达到 p<0.05。

---
