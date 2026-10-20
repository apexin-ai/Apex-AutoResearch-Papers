# research baseline code survey

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_baseline_code_survey_20260521T205234_result.json`
- **Structured JSON:** [`4305d05a6345ae598e63.json`](../../sessions/43/4305d05a6345ae598e63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 agent 全部返回，汇总如下：

---

### 1. CyclicJudge
- **公开代码**: 无
- **Repo URL**: N/A
- **License**: N/A
- **代码质量**: N/A
- **适配难度**: N/A
- **重实现复杂度**: **简单** — 核心算法是 round-robin judge 分配，~50-100 行 Python。给 K 个 judge、N 个 scenario，按 `i % K` 分配即可，无需训练或特殊库。
- **备注**: 论文 arXiv [2603.01865](https://arxiv.org/abs/2603.01865)，作者来自 Slingshot AI / Cambridge。作者 GitHub 和机构 org 均无相关 repo，论文中无 code availability 声明。

---

### 2. UDA (Unsupervised Debiasing Alignment)
- **公开代码**: 无（匿名审稿 repo 已 403）
- **Repo URL**: `https://anonymous.4open.science/r/62AB93CD-23B4`（已失效）
- **License**: N/A
- **代码质量**: N/A
- **适配难度**: N/A
- **重实现复杂度**: **中等** — 核心是 3 层 MLP（输入 6D+9 维特征，输出 K-factor + soft labels），配合三项无监督 loss（anchor alignment / rank fidelity / collective consensus）。模型本身简单，主要工作量在数据管线（多 judge pairwise 评测 + embedding 特征提取）和训练流程。估计 2-4 天。
- **备注**: AAAI 2026，作者来自 ZhipuAI / PKU / Tsinghua / Westlake。论文 arXiv [2508.09724](https://arxiv.org/abs/2508.09724)。方法是 post-hoc 的，不修改 judge prompt，只调整 Elo 更新。

---

### 3. DCR (Data Contamination Ratio)
- **公开代码**: 有
- **Repo URL**: [https://github.com/chengxuphd/dcr](https://github.com/chengxuphd/dcr)
- **License**: Apache-2.0
- **代码质量**: **中**（结构清晰、有 README 和示例，但仅 4 commits、1 star，学术发布级别）
- **适配难度**: **中等** — 提供 CLI 和 Python API，模块化设计（core/utils）。需将数据转为其 CSV 格式，阈值 θ₁-θ₄ 需针对新 benchmark 调参。依赖 `skfuzzy` 做模糊推理。
- **重实现复杂度**: 中等（如不用原 repo）— 四级污染检测（语义/信息/数据/标签）+ 模糊推理系统，估计 2-4 天。
- **备注**: EMNLP 2025 Main。arXiv [2507.11405](https://arxiv.org/abs/2507.11405)。方法需要访问训练数据（或代理），对闭源 LLM 适用性受限。

---

### 4. Preference Leakage
- **公开代码**: 有
- **Repo URL**: [https://github.com/David-Li0406/Preference-Leakage](https://github.com/David-Li0406/Preference-Leakage)
- **License**: **未标注**（论文 CC-BY 4.0，repo 无 LICENSE 文件）
- **代码质量**: **中偏差** — 82% Jupyter Notebook，无 docstring，无测试，是实验复现脚本而非可复用库。但包含预计算数据和模型输出（Google Drive），有参考价值。
- **适配难度**: **困难**（集成完整管线）/ **中等**（仅用 leakage score 度量）— 完整管线依赖 LLaMA-Factory + DeepSpeed + vLLM + 多商业 API。度量本身是 win-rate 差值，计算简单。
- **重实现复杂度**: 仅度量部分 **简单**；含训练管线 **中等**。
- **备注**: ICLR 2026 poster。arXiv [2502.01534](https://arxiv.org/abs/2502.01534)，55 stars。作者来自 ASU / UCLA / Notre Dame / UIUC。

---

**总结**:

| Baseline | 有代码 | 可直接用 | 重实现难度 |
|---|---|---|---|
| CyclicJudge | 无 | — | 简单（~100行） |
| UDA | 无（失效） | — | 中等（2-4天） |
| DCR | 有 | 需适配 | 中等 |
| Preference Leakage | 有 | 需大幅重构 | 度量简单/管线中等 |

---
