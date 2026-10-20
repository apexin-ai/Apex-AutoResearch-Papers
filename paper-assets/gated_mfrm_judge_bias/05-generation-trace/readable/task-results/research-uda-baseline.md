# research uda baseline

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_uda_baseline_20260522T025936_result.json`
- **Structured JSON:** [`8a34ff7bf48745c1d526.json`](../../sessions/8a/8a34ff7bf48745c1d526.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## UDA Baseline 代码评估报告

### 1. 代码可用性：❌ 不可用

- Anonymous repo 仍返回 **403 Forbidden**
- 7 位作者（Yang Zhang/ZhipuAI, Cunxiang Wang/Westlake, Guangsheng Bao/Westlake 等）GitHub 均无 UDA repo
- PapersWithCode 无条目

### 2. 重实现可行性：✅ 可行，但有不确定性

**已知（足够实现核心）：**
- Differentiable Elo 更新公式完整：`R_i ← R_i + K_ij·(s_i - σ(R_i - R_j))`
- MLP 输入 `φ ∈ ℝ^(6D+9)`（6 个 embedding 差异向量 + 9 个标量特征），输出 3 维 `(K_ij, s_i, s_j)`
- Loss 三项结构：trajectory alignment + consensus MSE + Pearson correlation
- 训练：AdamW, 4090 单卡 8h

**缺失（需猜测/调参）：**

| 风险 | 缺失细节 |
|------|---------|
| 🔴 高 | Loss 权重 α, σ, β（直接影响收敛） |
| 🔴 高 | MLP 隐层大小（仅说 "compact, 3 layers"） |
| 🟡 中 | K-factor 输出范围约束 |
| 🟡 中 | Feature 中 "normalized products" 精确定义 |
| 🟡 中 | Judge embedding 获取方式 |
| 🟢 低 | LR / epochs / batch（可标准调参） |

### 3. 替代实现：❌ 无直接可用

无现成 differentiable Elo PyTorch 实现。标准 Elo 库（sublee/elo 等）非 differentiable。Elo 公式本身简单，从头写比改造现有库更快。

### 4. 预估工时

~400-500 行 Python，**3-4 天**（含调参）。

### 5. 建议

1. **邮件联系作者要代码**（Cunxiang Wang @ Westlake 最可能响应）
2. **同时启动重实现**——differentiable Elo core 半天可完成，主要时间花在 feature engineering 和 loss 权重调参
3. 论文中标注为 "our reproduction"

Sources:
- [UDA arXiv](https://arxiv.org/abs/2508.09724)
- [UDA AAAI Proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/40788)
- [UDA Full Paper HTML](https://arxiv.org/html/2508.09724)
- [Cunxiang Wang Homepage](https://wangcunxiang.github.io/)
- [Guangsheng Bao GitHub](https://github.com/baoguangsheng)

---
