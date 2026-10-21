# analysis s43 1000 ncomponents3 investigation

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_s43-1000-ncomponents3-investigation_20260515T165157_result.json`
- **Structured JSON:** [`973db99f880fbe2b917f.json`](../../sessions/97/973db99f880fbe2b917f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Report written and registered. Here's the summary:

---

## 调查结论

**n_components=3 不是 parsing artifact。**

### 核心发现

1. **Explanation 文本完全未影响 parsing**：0/90 proved 样本有 Explanation 文本泄漏到 premises 中。`_parse_formalization()` 正确忽略了 `Conclusion:` 之后的所有内容。

2. **n_components=3 的来源**：89/90 proved 样本的结构完全一致——单一 premise（等于 conclusion 的拷贝）+ conclusion 的 ∃x 量词分解：
   ```
   (premise, conclusion_quantifier, conclusion_whole)
   ```
   全部是 H7 hack（premise == conclusion）。

3. **ISR 分布**（90 proved 样本中 89 个 nc=3）：
   - ISR=0.333（n_necessary=1）：26 个
   - ISR=0.667（n_necessary=2）：58 个
   - ISR=1.000（n_necessary=3）：5 个

4. **量词分解实际上是在拉低 ISR**：如果合并 conclusion 为一个 component，corrected ISR = 0.856（比原始 0.590 更高）。高 ISR 的根因是**单 premise H7 hack**——唯一的 premise 必然是 necessary 的。

5. **跨 seed 对比**：

   | Seed | H7 率 | nc 中位数 | ISR |
   |------|-------|----------|-----|
   | s42 (350-step) | 0/93 | 7 | 0.132 |
   | s43-1000-r2 | 90/90 | 3 | 0.531 |
   | s44-1000-r2 | 0/100 | 13 | 0.002 |

   s44 使用 7-24 个冗余 premise（删任一个不影响结果→ISR≈0），s43 使用 1 个 premise（删了必挂→ISR≥0.33）。

6. **对论文的影响**：ISR=0.531 计算本身没有 bug。异常值来自 hacking 策略差异（单 premise vs 多 premise 冗余），符合 C006 约束的语义。

报告已保存至 `artifacts/s43_1000_n_components_investigation.md`。

---
