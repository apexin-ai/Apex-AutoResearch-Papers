# verify pdf patches

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_pdf-patches_20260523T174403_result.json`
- **Structured JSON:** [`aebe4c2bd88ab2118714.json`](../../sessions/ae/aebe4c2bd88ab2118714.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

服务器没有 pdflatex，PDF 已在本地编译完成。汇总结果：

---

## Patch 验证

**Patch 1: PIQA routing** ✅ 已到位
- `experiments.tex:41` — 明确报告 PIQA routing 为负结果：`"on PIQA, it is significantly negative ($-0.49$\,pp, $p = .006$)"`
- `conclusion.tex:5` — 同样确认：`"routing is counterproductive on low-$\alpha$ tasks ($-0.49$\,pp on PIQA)"`

**Patch 2: Appendix P.2 Shapiro-Wilk** ✅ 已到位
- `appendix.tex:541` — 包含 W 统计量（`all $W < 0.98$, $p < 10^{-6}$`）和 `"approximately log-normal distribution"` 描述，含 skewness 数据

**Patch 3: Appendix Y AI disclosure** ✅ 已到位
- `appendix.tex:777-789` — 完整声明：`\section{Use of AI Assistants}`，列出 Claude (Anthropic) 用于 Code/Writing/Literature 三方面

**Patch 4: R15-R17 五处微调** ✅ 全部到位
- **"nearly disjoint" 替换**: ✅ 主论文 tex 中无此短语（仅出现在 author_response_r7.tex 中），主文使用 `"${\sim}90\%$ non-overlap"` 等 calibrated 表述
- **GDN confound inline**: ✅ `experiments.tex:110` (§4.4 Robustness) 详细讨论 GDN 16-head confound，引用 Appendix E
- **5-arch 验证 (10 pairs)**: ✅ `experiments.tex:110` — `"Five-architecture validation at 340M (GLA, DeltaNet added) confirms $J \leq 0.14$ across all ten pairs and four benchmarks (all $p < .01$)"`
- **DeltaNet Table 30**: ✅ `appendix.tex:740-770` — 含 GLA-DeltaNet 等全部 10 对数据
- **Abstract 5-arch 句法**: ✅ `main.tex:26` — `"validation across five architectures and ten pairwise comparisons confirms this on all four benchmarks (all $p < .01$)"`

---

## 编译结果

| 项目 | 结果 |
|------|------|
| 编译状态 | ✅ 成功（本地编译，服务器无 pdflatex） |
| Warnings | 1（`caption` 包 hypcap 选项，无害） |
| Undefined references | 0 |
| Undefined citations | 0 |
| 总页数 | 22 页 |
| Abstract 字数 | ~160 words（≤ 200 ✅） |

## ⚠️ 需注意

**主文超 8 页**：§5 Conclusion 从第 9 页开始，主文（§1-§5）约 9 页，超过 EMNLP 2026 的 8 页限制。Limitations/References/Appendix 不计入，但 Conclusion 属于主文。需要压缩约 1 页。

PDF 路径：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.pdf`

---
