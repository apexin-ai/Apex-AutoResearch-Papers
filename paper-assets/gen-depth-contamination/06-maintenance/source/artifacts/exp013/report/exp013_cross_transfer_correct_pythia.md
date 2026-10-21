# exp013 Cross-Transfer v2 (Corrected Pythia Data: Nucleus Sampling)

## 背景

上一次 exp013 rerun 错误使用了 greedy Pythia 数据 (`data/exp_pythia14b_c4_rerun/`, AUC\_1v2=0.8786)。Greedy decoding 人为膨胀 AUC，导致 transfer matrix 不可信。本次使用 nucleus sampling Pythia 数据 (`data_exp020_pythia_nuc09/`, AUC\_1v2=0.6756)。

## 数据源

| Model  | Data Path                           | Samples | Self K\* | Self AUC(1v2) |
|--------|-------------------------------------|---------|---------|---------------|
| OLMo   | `data/exp_olmo1b_c4_rerun/`        | 30,000  | 1       | 0.5080        |
| Pythia | `data_exp020_pythia_nuc09/`         | 30,000  | 2       | 0.6756        |
| Qwen   | `data_exp016_qwen_base/`           | 30,000  | 2       | 0.6289        |

Pythia 数据验证：`data_exp020_pythia_nuc09` 是 nucleus p=0.9 采样数据，self AUC(1v2)=0.6756 (远低于 greedy 的 0.8786)，K\*=2 (>theta=0.60)。

## K\* Transfer Matrix (train=row, test=col)

|  Train \ Test | OLMo | Pythia | Qwen |
|---------------|------|--------|------|
| **OLMo**      | 1    | 1 ✗    | 1 ✗  |
| **Pythia**    | 1 ✓  | 2      | 2 ✓  |
| **Qwen**      | 1 ✓  | 2 ✓    | 2    |

✓ = correctly predicts test model's self K\*; ✗ = mismatch

**Aggregate accuracy:** 7/9 = 77.8% (theta=0.60)

## AUC(0v1) Transfer Matrix

|  Train \ Test | OLMo   | Pythia | Qwen   |
|---------------|--------|--------|--------|
| **OLMo**      | 0.9860 | 0.9085 | 0.8477 |
| **Pythia**    | 0.9540 | 0.9948 | 0.9832 |
| **Qwen**      | 0.9494 | 0.9935 | 0.9875 |

## 完整 Pairwise AUC

| Pair              | 0v1    | 1v2    | 2v3    | 3v4    | 4v5    | K\*  |
|-------------------|--------|--------|--------|--------|--------|------|
| OLMo → OLMo      | 0.9860 | 0.5080 | 0.4973 | 0.5024 | 0.4942 | 1    |
| OLMo → Pythia     | 0.9085 | 0.5361 | 0.4887 | 0.4995 | 0.5028 | 1    |
| OLMo → Qwen       | 0.8477 | 0.5275 | 0.4813 | 0.5052 | 0.4995 | 1    |
| Pythia → OLMo     | 0.9540 | 0.5128 | 0.4985 | 0.5065 | 0.4934 | 1    |
| Pythia → Pythia   | 0.9948 | 0.6756 | 0.5595 | 0.5236 | 0.5010 | 2    |
| Pythia → Qwen     | 0.9832 | 0.6328 | 0.5566 | 0.5241 | 0.5124 | 2    |
| Qwen → OLMo      | 0.9494 | 0.5122 | 0.4988 | 0.5019 | 0.5022 | 1    |
| Qwen → Pythia    | 0.9935 | 0.6606 | 0.5526 | 0.5261 | 0.5042 | 2    |
| Qwen → Qwen      | 0.9875 | 0.6289 | 0.5548 | 0.5270 | 0.5198 | 2    |

## 与上一次 (greedy Pythia) 的对比

| 指标 | v1 (greedy Pythia) | v2 (nucleus Pythia) | 变化 |
|------|-------------------|---------------------|------|
| Pythia self AUC(1v2) | 0.8786 | 0.6756 | -0.2030 (去除 greedy 膨胀) |
| Pythia self K\* | 2 | 2 | 不变 |
| **Pythia → Qwen K\*** | **1 ✗** | **2 ✓** | **修正！** |
| Aggregate accuracy | 6/9 = 66.7% | 7/9 = 77.8% | +11.1% |

### 关键变化：Pythia → Qwen 从错误变正确

v1 中 Pythia → Qwen 的 AUC(1v2) = 0.4882（随机水平），因为 greedy Pythia 的 depth-1→2 特征模式是 decoding artifact，不可迁移到 nucleus sampling 的 Qwen。

v2 中 Pythia → Qwen 的 AUC(1v2) = 0.6328（>0.60），nucleus Pythia 的 depth-1→2 信号反映真实的 model collapse 特征，可以成功迁移到 Qwen。

## 分析

### 2 个 K\* 不匹配的 pair

1. **OLMo → Pythia**: predicted K\*=1, true=2. OLMo 训练集只有 0v1 可区分，depth>=1 已饱和，分类器学不到 1v2 信号来迁移。
2. **OLMo → Qwen**: 同理，OLMo 自身无 1v2 信号可训练。

### 关键发现

- **Pythia 和 Qwen 双向迁移成功**: Pythia → Qwen (K\*=2 ✓) 和 Qwen → Pythia (K\*=2 ✓) 都正确。两个 K\*=2 模型的 depth-1→2 信号可互相迁移，说明 nucleus sampling 下的 model collapse 特征具有跨模型一致性。
- **Greedy 数据的危害**: greedy decoding 创造了人工的高区分度 (AUC=0.88)，但这种区分度基于 decoding 策略而非 model collapse，不可跨模型迁移。修正后 accuracy 从 66.7% 提升到 77.8%。
- **OLMo 仍是最差训练器**: OLMo K\*=1 意味着只有 0v1 有信号，无法向上迁移 K\*。这是 OBD 跨模型迁移的方向性限制。
- **Pythia 和 Qwen 是同样好的训练器**: 两者都能正确预测全部 3 个模型的 K\*（3/3 = 100%）。

### 核心结论

使用正确的 nucleus sampling 数据后，OBD cross-transfer 的 aggregate accuracy 从 66.7% 提升到 77.8%。剩余的 2 个错误全部来自 OLMo（K\*=1）作为训练源时无法预测 K\*=2 目标的结构性限制，而非方法论缺陷。

## 服务器结果路径

`/root/autodl-tmp/gen-depth-contamination/results/exp013_olmo_rerun_v2/`

文件列表:
- `transfer_matrix.json` — 完整结果（含数据源路径和版本说明）
- `{train}_to_{test}.json` — 每个 pair 的详细 AUC + 95% CI
