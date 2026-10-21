# research preference leakage eval

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_preference_leakage_eval_20260522T004420_result.json`
- **Structured JSON:** [`bf3778bd7b8a2b8ec552.json`](../../sessions/bf/bf3778bd7b8a2b8ec552.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息已全部收集完毕。以下是可行性报告。

---

## Preference Leakage Baseline 可行性报告

### 1. 仓库状态

| 项目 | 状态 |
|------|------|
| 仓库 | [David-Li0406/Preference-Leakage](https://github.com/David-Li0406/Preference-Leakage) |
| Stars/Forks | 55 / 3 |
| License | **无 license** |
| 语言分布 | Jupyter Notebook 82.2%, Python 17.0% |
| 最新版本 | arXiv v3 (2026-03-04) |
| Venue | **ICLR 2026** (已接收) |

**代码结构：**
```
├── analysis/          # 核心分析脚本（~15个.py + .sh）
│   ├── correlation.py         # Spearman 排名相关性
│   ├── self_recognition_pairwise.py  # judge 能否识别 student
│   ├── bert_recognition.py    # BERT 分类器识别 student output
│   ├── alpacaEval.py          # 生成 student model 的 AlpacaEval outputs
│   └── ...
├── config/            # LLaMA Factory 训练配置（SFT/DPO/mix等）
├── evaluation/
│   ├── Alpaca_Eval2/  # 完整 fork 的 AlpacaEval 2.0 评估框架
│   └── Arena_Hard/    # 完整 fork 的 Arena-Hard 评估框架
├── resource/          # 绘图脚本 + PDF 图表
├── training/          # 6个训练 shell 脚本（调用 LLaMA Factory）
└── utils.py           # API 调用封装（OpenAI/Gemini/Together/vLLM）
```

### 2. 方法核心

**论文**：*Preference Leakage: A Contamination Problem in LLM-as-a-judge* (Dawei Li et al., ICLR 2026, arXiv 2502.01534)

**核心发现**：当 judge LLM 与训练数据的 generator LLM 有关联时（同模型/继承/同家族），judge 会系统性偏高评分——即使 judge 无法显式识别 student outputs（识别准确率 ≈ 50%）。

**三类关联性：**
1. **Same Model**: M_G ≡ M_J（如 GPT-4o 生成数据 + GPT-4o 评分）
2. **Inheritance**: M_S 在 M_G 数据上 fine-tuned，M_J 是 M_G（风格继承）
3. **Same Family**: M_G 和 M_J 同系列（如都是 LLaMA-3.x）

**核心指标 — Preference Leakage Score (PLS)：**
```
PLS(i,j) = [(WR(i,i) − AVG(i,j)) / AVG(i,j) + (WR(j,j) − AVG(j,i)) / AVG(j,i)] / 2
```
其中 WR(i,i) 是 judge_i 给自己 student 的 win-rate。**仅聚合级别**，无 per-item 分数。

**效应量：**
- Same model: PLS ≈ 23.6%
- Inheritance: PLS ≈ 22.3%
- Same family (same series): PLS ≈ 8.9%
- Same family (diff series): PLS ≈ 2.8%

**5种 mitigation 方法（论文测试）：**
- Prompting / CoT / Paraphrasing / Auto-calibration / Contextual Calibration
- 最优：Contextual Calibration，Error Bias 从 17.8 → 7.3

### 3. 与 G-MFRM Pipeline 兼容性分析

**关键矛盾点：**

| G-MFRM 需要 | Preference Leakage 提供 | 匹配度 |
|-------------|------------------------|--------|
| Per-item contamination signal (e_i) | 仅 aggregate PLS | **不匹配** |
| 通用 benchmark contamination 检测 | 特定于 LLM-as-judge 偏好泄漏 | 部分相关 |
| 任意 model pair 的 item-level 校正 | Model pair 级别 win-rate 偏差 | **不匹配** |
| 无需训练 student model | 需训练 student 才能测量 leakage | **不匹配** |

**核心问题**：Preference Leakage 测量的是 "judge 偏向其 student" 这一特定 bias，而非 benchmark item 层面的 contamination signal。PLS 是一个 aggregate 统计量（两个模型在整个 benchmark 上的 win-rate 差异），无法分解到单个 item。

### 4. 代码可用性评估

**82% Notebooks 的实际影响**：实际核心代码主要在 `analysis/` 目录的 `.py` 文件中，notebooks 主要在 `evaluation/` 下 fork 的 AlpacaEval/Arena-Hard 框架里。核心逻辑（PLS 计算、recognition 实验、correlation 分析）已经是独立 Python 脚本。

**可提取的核心算法：**
- PLS 计算：~20 行公式，trivial 重实现
- Spearman 相关分析：`correlation.py`，标准统计
- Self-recognition：`self_recognition_pairwise.py`，prompt + API 调用
- BERT recognition：`bert_recognition.py`，标准 HF Trainer pipeline

**无 license 影响**：
- ICLR 2026 paper → 学术复现 fair use 无问题
- PLS 公式是论文公开的数学定义，重实现不涉及版权
- 不能直接复制代码 redistribute，但无需——核心算法 trivial

### 5. 使用方案与推荐

**方案 A：直接用仓库代码** → ❌ 不推荐
- PLS 是 aggregate metric，无法提供 G-MFRM 需要的 per-item signal
- 即使跑通全流程，输出格式与 G-MFRM pipeline 不兼容

**方案 B：提取核心代码适配** → ❌ 意义不大
- 核心就是 win-rate 差异公式，无复杂算法值得提取
- 无法通过适配获得 per-item granularity（这是方法论限制，非工程问题）

**方案 C：作为 aggregate-level baseline 重实现** → ✅ 推荐
- 重实现 PLS 计算：~1小时，20-30 行代码
- 作为 exp-004 的 baseline #8，定位为 "aggregate-level detection only" 的对照
- 论文中的 Contextual Calibration 可以作为校正方法的 aggregate-level 对照
- 实验中只需计算 G-MFRM 已有 judge outputs 的 PLS，无需额外训练

**工作量估算：**
- PLS 公式重实现 + 数据适配：**0.5 天**
- 在 G-MFRM 已有 judge data 上跑 PLS baseline：**0.5 天**
- 论文中引用 + baseline 对比描述：**0.5 天**
- 总计：**~1.5 天**

**在论文中的定位**：Preference Leakage 检测的是 judge-generator relatedness bias（宏观 win-rate 偏差），而 G-MFRM 提供 per-item contamination signal，这是粒度维度上的本质差异，构成有力的 motivation——"现有方法只能检测 aggregate bias，无法定位具体哪些 items 受污染"。

Sources:
- [arXiv: Preference Leakage](https://arxiv.org/abs/2502.01534)
- [GitHub: David-Li0406/Preference-Leakage](https://github.com/David-Li0406/Preference-Leakage)
- [HuggingFace Paper Page](https://huggingface.co/papers/2502.01534)

---
