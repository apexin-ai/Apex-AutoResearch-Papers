# PSN-IRT 4PL Item Parameters 数据调查报告

**日期**: 2026-05-20

---

## 1. 数据可用性：已找到公开 4PL 参数

PSN-IRT 的完整 4PL item parameters **已公开发布**，包含全部 41,871 items 的 (a, b, c, d) 参数。

## 2. 数据位置

### 主数据源：PSN-IRT（4PL）

| 资源 | URL |
|------|-----|
| GitHub Repo | https://github.com/Joe-Hall-Lee/PSN-IRT |
| Item Parameters | `results/item_parameters.csv` (41,871 rows) |
| Response Matrix | `data/combine.csv` (12 models × 41,871 items) |
| Model Abilities | `results/student_abilities.csv` (12 models) |
| Benchmark Aggregates | `results/dataset_analysis.csv` (11 benchmarks) |
| 论文 | https://arxiv.org/abs/2505.15055 (AAAI 2026 Oral) |

### 替代数据源：ATLAS（3PL，含 TruthfulQA）

| 资源 | URL |
|------|-----|
| GitHub Repo | https://github.com/Peiyu-Georgia-Li/ATLAS |
| 论文 | https://arxiv.org/abs/2511.04689 |
| 参数文件 | 每个 benchmark 目录下 `irt_item_parameters_combined.csv` |

## 3. 数据格式

### PSN-IRT `item_parameters.csv`

- **格式**: CSV，无 header 列名分别为 `difficulty, discrimination, guessing, feasibility`
- **参数映射**: difficulty=b, discrimination=a, guessing=c, feasibility=d
- **Item 排列**: 按 benchmark 名称字母序连续排列（已验证）
- **无 benchmark 标签**: 原始 CSV 不含 benchmark 或 item ID 列

### Benchmark-to-Row 映射（已验证）

| Benchmark | Start Index | End Index | Item Count |
|-----------|------------|-----------|------------|
| ARC-C | 0 | 295 | 295 |
| BBH | 295 | 6,806 | 6,511 |
| Chinese SimpleQA | 6,806 | 9,806 | 3,000 |
| GPQA Diamond | 9,806 | 10,004 | 198 |
| GSM8K | 10,004 | 11,323 | 1,319 |
| HellaSwag | 11,323 | 21,365 | 10,042 |
| HumanEval | 21,365 | 21,529 | 164 |
| MATH | 21,529 | 26,529 | 5,000 |
| MBPP | 26,529 | 27,029 | 500 |
| MMLU | 27,029 | 41,071 | 14,042 |
| TheoremQA | 41,071 | 41,871 | 800 |

验证方法：按字母序假设的每段均值与 `dataset_analysis.csv` 的 benchmark 均值精确匹配（误差 < 0.001）。

### ATLAS `irt_item_parameters_combined.csv`

- **格式**: CSV
- **参数**: a1 (discrimination), d (easiness, 非 difficulty), g (guessing), u (upper asymptote)
- **注意**: ATLAS 用的是 slope-intercept 参数化（d = easiness），需转换: b = -d/a1

## 4. 参数范围统计

### PSN-IRT 全局统计（41,871 items）

| Parameter | Min | Max | Mean | Median |
|-----------|-----|-----|------|--------|
| a (discrimination) | -0.0356 | 2.6567 | 1.3223 | 1.3519 |
| b (difficulty) | -2.6834 | 1.7275 | -0.6591 | -0.7058 |
| c (guessing) | 0.0033 | 0.7666 | 0.1879 | 0.1221 |
| d (feasibility) | 0.1563 | 0.9972 | 0.8696 | 0.9494 |

### 目标 Benchmark 详细统计

#### MMLU (14,042 items)
| Param | Min | Max | Mean | Median | Std |
|-------|-----|-----|------|--------|-----|
| a | 0.0063 | 2.6567 | 1.1968 | 1.1618 | 0.5415 |
| b | -2.6834 | 1.6925 | -0.8383 | -0.8947 | 0.7905 |
| c | 0.0050 | 0.7647 | 0.2381 | 0.1798 | 0.1905 |
| d | 0.1869 | 0.9968 | 0.8921 | 0.9555 | 0.1499 |

#### GSM8K (1,319 items)
| Param | Min | Max | Mean | Median | Std |
|-------|-----|-----|------|--------|-----|
| a | 0.1345 | 2.4958 | 1.5255 | 1.6134 | 0.4845 |
| b | -2.4478 | 1.6224 | -0.7898 | -0.8103 | 0.6885 |
| c | 0.0065 | 0.7208 | 0.1491 | 0.0914 | 0.1447 |
| d | 0.1858 | 0.9957 | 0.9167 | 0.9631 | 0.1297 |

#### HumanEval (164 items)
| Param | Min | Max | Mean | Median | Std |
|-------|-----|-----|------|--------|-----|
| a | 0.4934 | 2.3604 | 1.4459 | 1.4398 | 0.4706 |
| b | -2.4412 | 1.4219 | -0.6351 | -0.6316 | 0.7493 |
| c | 0.0050 | 0.7171 | 0.1565 | 0.0789 | 0.1721 |
| d | 0.2648 | 0.9950 | 0.8957 | 0.9475 | 0.1397 |

#### ARC-Challenge (295 items)
| Param | Min | Max | Mean | Median | Std |
|-------|-----|-----|------|--------|-----|
| a | 0.1850 | 2.5255 | 1.2822 | 1.1784 | 0.4835 |
| b | -2.5318 | 1.3527 | -1.1637 | -1.2667 | 0.6174 |
| c | 0.0090 | 0.7329 | 0.2621 | 0.2202 | 0.1788 |
| d | 0.2685 | 0.9957 | 0.9481 | 0.9783 | 0.0902 |

#### HellaSwag (10,042 items)
| Param | Min | Max | Mean | Median | Std |
|-------|-----|-----|------|--------|-----|
| a | 0.0043 | 2.5089 | 1.2920 | 1.3442 | 0.5083 |
| b | -2.6821 | 1.6324 | -1.0353 | -1.0868 | 0.7219 |
| c | 0.0082 | 0.7666 | 0.2449 | 0.1906 | 0.1912 |
| d | 0.1912 | 0.9972 | 0.9304 | 0.9677 | 0.1109 |

## 5. 缺失信息

### TruthfulQA：PSN-IRT 未覆盖

PSN-IRT 的 11 个 benchmark 不包含 TruthfulQA。完整列表：ARC-C, BBH, Chinese SimpleQA, GPQA Diamond, GSM8K, HellaSwag, HumanEval, MATH, MBPP, MMLU, TheoremQA。

### 其他限制

- **无 item-level 标识**: `item_parameters.csv` 不含原始 question text 或 item ID，无法直接与 benchmark 原始数据集匹配具体题目
- **Item 内部排序未知**: 每个 benchmark 内部的 item 排列顺序（是否与原始数据集顺序一致）未文档化。推测与 OpenCompass 评测输出顺序一致
- **模型标识缺失**: `student_abilities.csv` 只有 student_id (0-11)，不含模型名称。12 个模型是通过 OpenCompass 评测的 LLMs，具体映射需查论文
- **Response matrix 无 header**: `combine.csv` 无行/列标签

## 6. 替代方案

### 方案 A：ATLAS（推荐用于补充 TruthfulQA）

- **论文**: "Adaptive Testing for LLM Evaluation" (arXiv:2511.04689)
- **GitHub**: https://github.com/Peiyu-Georgia-Li/ATLAS
- **模型**: 3PL IRT（a, b, c），无 d 参数
- **覆盖 benchmark**: ARC (842 items), GSM8K (1,306), HellaSwag (5,608), **TruthfulQA (628)**, WinoGrande (1,046)
- **校准规模**: 3,000-4,680 个 LLMs（远大于 PSN-IRT 的 12 个）
- **优势**: 覆盖 TruthfulQA；校准模型数量多，参数估计更稳定；有模型拟合验证 (RMSEA < 0.05)
- **劣势**: 3PL 而非 4PL（无 feasibility 参数）；不覆盖 MMLU 和 HumanEval；参数化方式不同需转换

### 方案 B：Cross-Difficulty Dataset

- **HuggingFace**: https://huggingface.co/datasets/BatsResearch/Cross-Difficulty
- **模型**: 1PL IRT（仅 difficulty）
- **覆盖 benchmark**: ARC, GSM8K, MMLU-Pro, MATH, BBH, MuSR, IFEval, GPQA-Extended
- **不覆盖**: TruthfulQA, HellaSwag, HumanEval
- **局限**: 仅有 difficulty，无 discrimination/guessing

### 方案 C：Growing Pains（多维 IRT）

- **论文**: arXiv:2604.12843
- **GitHub**: https://github.com/eliyahabba/growing-pains/
- **方法**: 多维 IRT + anchor items + fixed parameter calibration
- **评测规模**: 400+ 模型

### 方案 D：自行校准

用 Open LLM Leaderboard 的 per-item response data + mirt/ltm R 包或 PyTorch 自行拟合 IRT 模型。可覆盖任意 benchmark，但需要大量模型的 item-level responses。

## 7. 本地文件

已提取的数据文件位于 `artifacts/psn_irt_params/`：

| 文件 | 内容 |
|------|------|
| `item_parameters_all.csv` | 全部 41,871 items，含 benchmark 标签列 |
| `arc_c_params.csv` | ARC-Challenge 295 items |
| `gsm8k_params.csv` | GSM8K 1,319 items |
| `hellaswag_params.csv` | HellaSwag 10,042 items |
| `humaneval_params.csv` | HumanEval 164 items |
| `mmlu_params.csv` | MMLU 14,042 items |

Repo 已 clone 到 `/tmp/psn_irt_repo/`。

## 8. 推荐使用策略

对于 6 个目标 benchmark：

| Benchmark | PSN-IRT (4PL) | ATLAS (3PL) | 推荐 |
|-----------|:---:|:---:|------|
| MMLU | 14,042 items | - | PSN-IRT |
| GSM8K | 1,319 items | 1,306 items | PSN-IRT（4PL 更丰富）|
| HumanEval | 164 items | - | PSN-IRT |
| ARC-Challenge | 295 items | 842 items | 两者可用，ATLAS item 数更多 |
| HellaSwag | 10,042 items | 5,608 items | PSN-IRT（item 数更多）|
| TruthfulQA | - | 628 items | **ATLAS（唯一来源）** |
