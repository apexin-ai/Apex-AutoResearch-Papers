# research paper figure prep

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper-figure-prep_20260515T043852_result.json`
- **Structured JSON:** [`3f66a68d4561aac80bf6.json`](../../sessions/3f/3f66a68d4561aac80bf6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出目录 `artifacts/paper_figures/`，6 个 figure 脚本 + 1 个共享样式模块 + 1 个 LaTeX 表格 + README：

| 文件 | 内容 | 论文 Section |
|------|------|-------------|
| `fig1_nve_diagnostic.py` | Normalized v/e ratio 诊断图，1.5× 红区，6 条实验线 | Results (C2) |
| `fig2_eval_curves.py` | 全配置 eval return 学习曲线对比 | Results (C1/C3/C6) |
| `fig3_causal_chain.py` | 因果链示意图：dt_emb → RSSM gap → nve>1.5× → collapse | Discussion |
| `fig4_multiseed.py` | 2×2 grid: trained/no dt_emb × eval/nve，跨 seed 对比 | Results (C2) |
| `fig5_rssm_fidelity.py` | RSSM fidelity 柱状图 + `tab_rssm_fidelity.tex` | Discussion |
| `fig6_mitigation.py` | C6 mitigation 双面板（eval + nve），008e_v3 vs 006 vs baseline | Results (C6) |

所有脚本已验证无 warning 运行，输出 PDF+PNG。数据从 registry 硬编码，结构到位，后续替换为 W&B 实时拉取即可。008e_v3 s2 完成后需更新 fig6。

---
