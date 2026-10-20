# Dedup Sensitivity Analysis (R1-N2 fix)

## 方法

**数据集结构**：测试集包含 119 个 unique problems（来自 HumanEval 和 MBPP），每个 problem 恰好 10 条样本（不同 solutions 对应 pass/fail）。训练集 472 个 problems，80/20 按 problem-level 划分。

**去重策略**：
1. **Problem-level accuracy (macro)**：对每个 problem 分别计算 accuracy，再取均值（等权重对待每个 problem，消除 per-problem 样本数不均的影响）
2. **Train-test overlap 检查**：检查 problem_id 和 exact input 是否存在 train/test 重叠

因为每个 problem 恰好 10 条样本（完全均衡），sample-level（micro）和 problem-level（macro）accuracy 数学上等价。

## 结果

### Problem-level vs Sample-level Accuracy（19 experiments, 4 models）

| Model | Condition | n_samp | n_prob | SampleAcc | ProblemAcc | Delta | 95% CI |
|-------|-----------|--------|--------|-----------|------------|-------|--------|
| Qwen-7B | exception_only | 1190 | 119 | 99.8% | 99.8% | +0.0pp | [99.5%, 100.0%] |
| Qwen-7B | no_trace | 1190 | 119 | 75.1% | 75.1% | +0.0pp | [68.0%, 81.7%] |
| Qwen-7B | full_trace | 1190 | 119 | 81.8% | 81.8% | +0.0pp | [75.7%, 87.3%] |
| Qwen-7B | vota | 1190 | 119 | 99.4% | 99.4% | +0.0pp | [98.3%, 100.0%] |
| Qwen-7B | ae_only | 1190 | 119 | 99.9% | 99.9% | +0.0pp | [99.7%, 100.0%] |
| Qwen-7B | loop_only | 1190 | 119 | 85.6% | 85.6% | +0.0pp | [80.2%, 90.6%] |
| Qwen-7B | vota_no_ae | 1190 | 119 | 99.4% | 99.4% | +0.0pp | [98.3%, 100.0%] |
| Qwen-7B | full_trace_label_only | 1190 | 119 | 86.2% | 86.2% | -0.0pp | [80.4%, 91.5%] |
| DeepSeek | exception_only | 1190 | 119 | 99.3% | 99.3% | -0.0pp | [98.2%, 100.0%] |
| DeepSeek | no_trace | 1190 | 119 | 73.4% | 73.4% | -0.0pp | [66.3%, 80.3%] |
| DeepSeek | full_trace | 1190 | 119 | 10.6% | 10.6% | +0.0pp | [6.5%, 15.1%] |
| DeepSeek | vota | 1190 | 119 | 84.5% | 84.5% | +0.0pp | [78.5%, 90.0%] |
| CodeLlama-13B | exception_only | 1190 | 119 | 99.8% | 99.8% | +0.0pp | [99.5%, 100.0%] |
| CodeLlama-13B | no_trace | 1190 | 119 | 76.5% | 76.5% | +0.0pp | [69.8%, 82.9%] |
| CodeLlama-13B | vota | 1190 | 119 | 98.6% | 98.6% | -0.0pp | [96.4%, 100.0%] |
| Qwen-1.5B | exception_only | 1190 | 119 | 99.8% | 99.8% | +0.0pp | [99.5%, 100.0%] |
| Qwen-1.5B | no_trace | 1190 | 119 | 67.3% | 67.3% | -0.0pp | [59.9%, 74.7%] |
| Qwen-1.5B | full_trace | 1190 | 119 | 77.1% | 77.1% | +0.0pp | [70.5%, 83.5%] |
| Qwen-1.5B | vota | 1190 | 119 | 99.6% | 99.6% | +0.0pp | [98.9%, 100.0%] |

### Train-Test Overlap

| Condition | Train samples | Train problems | Test samples | Test problems | Problem overlap | Input overlap |
|-----------|--------------|----------------|-------------|---------------|-----------------|---------------|
| exception_only | 4720 | 472 | 1190 | 119 | **0** | **0** |
| no_trace | 4720 | 472 | 1190 | 119 | **0** | **0** |
| full_trace | 4720 | 472 | 1190 | 119 | **0** | **0** |
| vota | 4720 | 472 | 1190 | 119 | **0** | **0** |

## 结论

1. **Problem-level 和 sample-level accuracy 完全一致**（delta = 0.00pp across all 19 experiments）。因为数据集按 problem 均匀采样（每个 problem 10 条），micro/macro averaging 数学等价，不存在 per-problem 样本不均导致的 aggregation bias。

2. **训练集和测试集零重叠**：按 problem_id 划分（80/20 split），无任何 problem-level 或 exact-input-level 的 train-test leakage。

3. **结论 robust**：去重不影响任何实验结果。数据划分干净，无数据泄漏风险。
