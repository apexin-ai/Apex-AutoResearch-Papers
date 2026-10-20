## 统一 Instance 集 N-scaling 重算结果

### 方法
- Instance 集: 所有 N 的文件包含相同 instances (SciERC 551/529 gold-nonempty, CoNLL 3453/2756)
- Greedy 不一致: SciERC 52/529, CoNLL 24/2756 instances 的 greedy 在不同 N runs 中不同
- 解决: 统一使用 N=8 的 greedy 作为固定 baseline

### SciERC Finetuned (seed=42, 529 instances)

| N | Greedy F1 | MV strict F1 | MV Δ(pp) | Degen% | Oracle F1 |
|---|-----------|-------------|----------|--------|-----------|
| 8 | 0.6683 | 0.6558 | -1.24 | 13.4% | 0.7840 |
| 16 | 0.6683 | 0.6622 | -0.61 | 7.6% | 0.8179 |
| 32 | 0.6683 | 0.6706 | +0.24 | 3.6% | 0.8399 |
| 64 | 0.6683 | 0.6735 | +0.53 | 2.1% | 0.8626 |

### CoNLL Finetuned (seed=42, 2756 instances)

| N | Greedy F1 | MV strict F1 | MV Δ(pp) | Degen% | Oracle F1 |
|---|-----------|-------------|----------|--------|-----------|
| 8 | 0.9123 | 0.9142 | +0.20 | 56.7% | 0.9543 |
| 16 | 0.9123 | 0.9155 | +0.32 | 46.5% | 0.9636 |
| 32 | 0.9123 | 0.9166 | +0.44 | 40.5% | 0.9690 |
| 64 | 0.9123 | 0.9184 | +0.61 | 30.6% | 0.9751 |

### 关键发现
- 统一 baseline 后 MV Δ 完美单调递增
- 之前 SciERC N=64 的非单调 (+0.78→+0.63) 是 greedy 漂移假象
- SciERC 需 N≥32 MV 才超越 greedy; CoNLL 在所有 N 都正向但极小
- N=64 时 gain 仍不到 1pp，64× cost 换 <1pp = cost-ineffective