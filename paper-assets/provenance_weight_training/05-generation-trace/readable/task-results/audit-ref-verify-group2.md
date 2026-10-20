# audit ref verify group2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_ref-verify-group2_20260526T101557_result.json`
- **Structured JSON:** [`0833e26b8205d19c4c83.json`](../../sessions/08/0833e26b8205d19c4c83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

The arXiv page confirms author order for ye2025mixing as "Yunhua Zhou, Jun Zhan" — matching the bib. The agent was wrong on that one. Now I have all the data. Here's the full report:

---

## 引用验证结果（Group 2: Entry 20–37）

```
[20] xie2023doremi — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (NeurIPS 2023)
  arXiv: N/A (2305.10429 可选添加)
  引用上下文: OK — related_work.tex L10 引用 domain-level importance sampling，正确

[21] xie2023dsir — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (NeurIPS 2023)
  arXiv: N/A (2302.03169 可选添加)
  引用上下文: OK — related_work.tex L10 引用 domain-level importance sampling，正确

[22] chen2025aioli — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (ICLR 2025)
  arXiv: N/A (2411.05735 可选添加)
  引用上下文: 未在正文中引用（orphaned bib entry）

[23] kimura2024iw — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (TMLR 2024)
  arXiv: N/A (2403.10175 可选添加)
  引用上下文: 未在正文中引用（orphaned bib entry）

[24] mitchell2023detectgpt — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (ICML 2023)
  arXiv: N/A (2301.11305 可选添加)
  引用上下文: OK — related_work.tex L9 引用 probability curvature detector，正确

[25] shi2024minkprob — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (ICLR 2024)
  arXiv: N/A (2310.16789 可选添加)
  引用上下文: OK — related_work.tex L9 引用 low-probability token statistics，正确

[26] alemohammad2024mad — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (ICLR 2024)
  arXiv: N/A (2307.01850 可选添加)
  引用上下文: OK — related_work.tex L3 引用 Model Autophagy Disorder，正确

[27] cheng2025contamination — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (arXiv:2502.14425)
  arXiv: OK (2502.14425)
  引用上下文: OK — introduction.tex L1, related_work.tex L5, method.tex L8 引用 synthetic 20-60% 估计，正确

[28] ye2025mixing — ✅
  标题: OK
  作者: OK（arXiv 确认顺序为 Zhou, Yunhua → Zhan, Jun，与 bib 一致）
  年份: OK
  Venue: OK (ICLR 2025)
  arXiv: N/A (2403.16952 可选添加)
  引用上下文: OK — related_work.tex L10/L20, discussion.tex L31 引用 data mixing laws 和 PPL-to-accuracy transfer，正确

[29] yang2026mixing — ⚠️
  标题: OK
  作者: OK
  年份: OK
  Venue: ⚠️ ACL 2026 尚未召开（当前 2026-05-26），venue 无法独立确认
  arXiv: N/A (2507.15640 可选添加)
  引用上下文: 未在正文中引用（orphaned bib entry）

[30] penedo2024fineweb — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (NeurIPS Datasets and Benchmarks 2024)
  arXiv: N/A (2406.17557 可选添加)
  引用上下文: OK — experiments.tex L2 引用 FineWeb 作为 real-data source，正确

[31] yang2025qwen3 — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (arXiv:2505.09388)
  arXiv: OK (2505.09388)
  引用上下文: OK — experiments.tex L3 引用 Qwen3-0.6B 作为 generator，正确

[32] kuo2024weighting — ❌
  标题: OK
  作者: ❌ 除首作者外全部错误。Bib: "Tan, Pei-Yu; Peng, Chao-Wei; Chen, Yun-Nung"
        实际: Kuo, Hsun-Yu; Liao, Yin-Hsiang; Chao, Yu-Chieh; Ma, Wei-Yun; Cheng, Pu-Jen
  年份: OK
  Venue: OK (arXiv:2410.21526)
  arXiv: OK (2410.21526)
  引用上下文: 未在正文中引用（orphaned bib entry）

[33] bengio2009curriculum — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (ICML 2009)
  arXiv: N/A
  引用上下文: OK — related_work.tex L10 引用 instance-level curriculum learning，正确

[34] radford2019language — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (OpenAI Blog 2019)
  arXiv: N/A
  引用上下文: 未在正文中引用（orphaned bib entry）

[35] brown2020language — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (NeurIPS 2020)
  arXiv: N/A (2005.14165 可选添加)
  引用上下文: 未在正文中引用（orphaned bib entry）

[36] longpre2024pretrainers — ❌
  标题: OK
  作者: ❌ 第二作者起全部错误。Bib: "Mahari, Robert; Lee, Naana Obeng-Marnu; others"
        实际: Longpre, Shane; Yauney, Gregory; Reif, Emily; Lee, Katherine; Roberts, Adam;
              Zoph, Barret; Zhou, Denny; Wei, Jason; Robinson, Kevin; Mimno, David; Ippolito, Daphne
  年份: OK
  Venue: ⚠️ 应为 NAACL 2024（已发表于 ACL Anthology 2024.naacl-long.179），非仅 arXiv preprint
  arXiv: OK (2305.13169)
  引用上下文: 未在正文中引用（orphaned bib entry）

[37] lee2022dedup — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (ACL 2022)
  arXiv: N/A (2107.06499 可选添加)
  引用上下文: 未在正文中引用（orphaned bib entry）
```

---

## 汇总

| | 数量 |
|---|---|
| 总数 | 18 |
| ✅ OK | 15 |
| ❌ 有问题 | 2 |
| ⚠️ 待确认 | 1 |

### 必须修复

| # | Key | 问题 | 修复方案 |
|---|-----|------|---------|
| 32 | `kuo2024weighting` | **作者列表伪造**（仅首作者正确） | 改为: `Kuo, Hsun-Yu and Liao, Yin-Hsiang and Chao, Yu-Chieh and Ma, Wei-Yun and Cheng, Pu-Jen` |
| 36 | `longpre2024pretrainers` | **作者列表伪造**（仅首作者正确）+ venue 应升级 | 作者改为: `Longpre, Shane and Yauney, Gregory and Reif, Emily and Lee, Katherine and Roberts, Adam and Zoph, Barret and Zhou, Denny and Wei, Jason and Robinson, Kevin and Mimno, David and Ippolito, Daphne`；venue 改为 `NAACL 2024`，类型改为 `@inproceedings` |

### 待确认

| # | Key | 问题 |
|---|-----|------|
| 29 | `yang2026mixing` | ACL 2026 尚未召开，venue 无法独立验证。论文本身存在（arXiv:2507.15640）。建议确认接收通知后再标注 venue |

### 额外发现：8 条 orphaned entries

以下 entry 存在于 `references.bib` 但正文中未引用：`chen2025aioli`, `kimura2024iw`, `yang2026mixing`, `kuo2024weighting`, `radford2019language`, `brown2020language`, `longpre2024pretrainers`, `lee2022dedup`。如果最终不引用，应在提交前删除以免 LaTeX warning。

---
