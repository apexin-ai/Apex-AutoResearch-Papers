# analysis ff residual regression

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ff_residual_regression_20260522T153308_result.json`
- **Structured JSON:** [`efbcd13efe8e41f482d9.json`](../../sessions/ef/efbcd13efe8e41f482d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结果：

**FF Benchmarks（自由格式）— 残差高度系统化**
| Benchmark | Overall Residual % | R² (full) | R² (difficulty only) | Significant Features |
|-----------|-------------------|-----------|---------------------|---------------------|
| GSM8K | 51.9% | 0.468 | 0.449 | difficulty, difficulty², question_length |
| MATH | 56.3% | 0.856 | 0.845 | difficulty, difficulty², 4个subject类别 |

**MC Benchmarks（选择题）— 残差较低且不太系统**
| Benchmark | Overall Residual % | R² (full) | R² (difficulty only) | Significant Features |
|-----------|-------------------|-----------|---------------------|---------------------|
| MMLU | 37.0% | 0.377 | 0.347 | difficulty, difficulty², n_choices, subject_unknown |
| ARC | 28.1% | 0.221 | 0.204 | difficulty, difficulty², question_length |
| HellaSwag | 22.3% | 0.156 | 0.140 | difficulty, difficulty² |

**关键发现：**
- **FF 残差更系统化**：FF 基准的 mean R² = 0.662，MC 基准的 mean R² = 0.252。FF 残差中有更大比例可被 item 特征（尤其是 difficulty 的二次效应）预测
- **Difficulty 的非线性效应是主导因素**：所有 5 个 benchmark 中 difficulty 和 difficulty² 都是最显著的预测因子（p < 1e-5）。正系数 + 负二次系数 = 倒 U 形：中等难度 items 有最大残差，极易/极难 items 残差小
- **MATH R² = 0.856 极高**：说明 MATH 的残差几乎完全由 item difficulty 驱动，属于系统性方差而非随机噪声
- **n_steps 和 answer_length 对 GSM8K 不显著**（p > 0.38），残差主要由 difficulty 的 quadratic 效应解释

**输出文件位置：**
- 本地：`artifacts/exp004/ff_residual_analysis/ff_residual_regression.json`
- 服务器：`/root/nlp_variance_gtheory/results/exp004_ff_residual/`（包含全部 JSON + 5 个 scatter plot PDF/PNG）

---
