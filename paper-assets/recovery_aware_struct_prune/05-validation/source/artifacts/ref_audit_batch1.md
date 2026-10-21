# 引用核对清单 — Batch 1

| # | bib key | 存在? | 标题正确? | 作者正确? | 年份正确? | Venue正确? | arXiv ID正确? | 问题 |
|---|---------|-------|----------|----------|----------|-----------|-------------|------|
| 1 | austin2021mbpp | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 无 |
| 2 | deepseek2025r1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 无 |
| 3 | qwen2.5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 无 |
| 4 | cobbe2021gsm8k | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 无 |
| 5 | shao2024grpo | ✅ | ✅ | ⚠️ | ✅ | ✅ | ✅ | 作者列表不完整，缺少 Xiao Bi 和 Haowei Zhang |
| 6 | llmpruner2023 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 无 |
| 7 | graspprune2026 | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | 已被 ACL 2026 Main 接收，bib 中仅标注为 arXiv preprint，建议更新 venue |
| 8 | resp2025 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 无 |
| 9 | selfhealing2025 | ✅ | ✅ | ✅ | ✅ | ⚠️ | N/A | 可能已被 COLM 2026 接收（出现在 COLM 2026 accepted papers 列表），bib 中仍为 "OpenReview preprint"，建议确认并更新 venue |
| 10 | bonsai2025 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | bib key 含 "2025" 但 year 字段正确为 2024，key 名无实际影响 |
| 11 | paser2025 | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | bib 标题写 "Large Language Model"，arXiv 原文标题也是 "Large Language Model"——实际一致，无问题 |
| 12 | rlsqueezes2026 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | bib key 含 "2026" 但 year 字段正确为 2025（arXiv 提交于 2025-09），key 名无实际影响 |
| 13 | kornblith2019cka | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 无 |

## 详细问题

### #5 shao2024grpo — 作者列表不完整
bib 中作者列表为：Shao, Zhihong and Wang, Peiyi and Zhu, Qihao and Xu, Runxin and Song, Junxiao and Zhang, Mingchuan and Li, Y.K. and Wu, Y. and Guo, Daya

arXiv 原文完整作者列表为：Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, **Xiao Bi**, **Haowei Zhang**, Mingchuan Zhang, Y.K. Li, Y. Wu, Daya Guo

缺少 Xiao Bi 和 Haowei Zhang 两位作者。建议补全。

### #7 graspprune2026 — Venue 可更新
GitHub 官方仓库 (https://github.com/ZiY-Wang/GRASPrune) 标注 "ACL 2026 Main"。当前 bib 仅标注为 `arXiv preprint`。建议更新为 `@inproceedings` 并标注 ACL 2026。

### #9 selfhealing2025 — Venue 可能需要更新
搜索结果显示该论文出现在 COLM 2026 accepted papers 列表中。当前 bib 标注为 "OpenReview preprint"。建议确认是否已正式接收，若是则更新 venue 为 COLM 2026。

### #11 paser2025 — 标题核实
经二次核实，bib 标题 "PASER: Post-Training Data Selection for Efficient Pruned Large Language Model Recovery" 与 arXiv 原文标题一致（均为 "Large Language Model" 而非缩写 "LLM"）。无问题。

## 总结

- **13 条引用全部真实存在**，无 hallucinated paper
- **0 条标题错误**
- **1 条作者不完整**（#5 shao2024grpo，缺 2 位共同作者）
- **0 条年份错误**
- **2 条 venue 可更新**（#7 graspprune2026 → ACL 2026 Main；#9 selfhealing2025 → 可能 COLM 2026）
- **0 条 arXiv ID 错误**
