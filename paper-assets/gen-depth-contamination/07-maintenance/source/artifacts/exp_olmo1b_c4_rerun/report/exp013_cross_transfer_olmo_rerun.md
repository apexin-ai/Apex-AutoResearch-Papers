# exp013 Cross-Transfer Rerun (OLMo K*=1 Data)

## 背景

原始 exp013 使用旧 OLMo 数据 (`data_exp002_olmo`, K\*=2)。OLMo 标准化重跑后 K\*=1 (`data/exp_olmo1b_c4_rerun/features.csv`, AUC\_1v2=0.508)。本次用 rerun 数据重跑所有涉及 OLMo 的 transfer pair。

## 数据源

| Model  | Data Path                           | Samples | Self K\* |
|--------|-------------------------------------|---------|---------|
| OLMo   | `data/exp_olmo1b_c4_rerun/`        | 30,000  | 1       |
| Pythia | `data/exp_pythia14b_c4_rerun/`     | 30,000  | 2       |
| Qwen   | `data_exp016_qwen_base/`           | 30,000  | 2       |

## K\* Transfer Matrix (train=row, test=col)

|  Train \ Test | OLMo | Pythia | Qwen |
|---------------|------|--------|------|
| **OLMo**      | 1    | 1 ✗    | 1 ✗  |
| **Pythia**    | 1 ✓  | 2      | 1 ✗  |
| **Qwen**      | 1 ✓  | 2 ✓    | 2    |

✓ = correctly predicts test model's self K\*; ✗ = mismatch

**Aggregate accuracy:** 6/9 = 66.7% (theta=0.60)

## AUC(0v1) Transfer Matrix

|  Train \ Test | OLMo   | Pythia | Qwen   |
|---------------|--------|--------|--------|
| **OLMo**      | 0.9860 | 0.9505 | 0.8477 |
| **Pythia**    | 0.6870 | 0.9979 | 0.8383 |
| **Qwen**      | 0.9494 | 0.9926 | 0.9875 |

## 完整 Pairwise AUC

| Pair              | 0v1    | 1v2    | 2v3    | 3v4    | 4v5    | K\*  |
|-------------------|--------|--------|--------|--------|--------|------|
| OLMo → OLMo      | 0.9860 | 0.5080 | 0.4973 | 0.5024 | 0.4942 | 1    |
| OLMo → Pythia     | 0.9505 | 0.5533 | 0.4980 | 0.4947 | 0.4989 | 1    |
| OLMo → Qwen       | 0.8477 | 0.5275 | 0.4813 | 0.5052 | 0.4995 | 1    |
| Pythia → OLMo     | 0.6870 | 0.4934 | 0.4984 | 0.4948 | 0.5027 | 1    |
| Pythia → Pythia   | 0.9979 | 0.8786 | 0.5399 | 0.5062 | 0.5025 | 2    |
| Pythia → Qwen     | 0.8383 | 0.4882 | 0.5230 | 0.5163 | 0.4959 | 1    |
| Qwen → OLMo      | 0.9494 | 0.5122 | 0.4988 | 0.5019 | 0.5022 | 1    |
| Qwen → Pythia    | 0.9926 | 0.6132 | 0.5158 | 0.5125 | 0.4982 | 2    |
| Qwen → Qwen      | 0.9875 | 0.6289 | 0.5548 | 0.5270 | 0.5198 | 2    |

## 分析

### 3 个 K\* 不匹配的 pair

1. **OLMo → Pythia**: predicted K\*=1, true=2. OLMo 训练集只有 0v1 可区分 (AUC=0.986)，depth≥1 已饱和，因此分类器学不到 1v2 的信号来迁移到 Pythia。
2. **OLMo → Qwen**: 同理，OLMo 训练数据 depth≥1 无信号。
3. **Pythia → Qwen**: predicted K\*=1, true=2. Pythia 自身 AUC(1v2)=0.8786 很强，但 transfer 到 Qwen 后 AUC(1v2)=0.4882 (随机水平)。Pythia 的 depth-1→2 特征模式与 Qwen 不同，不可迁移。

### 关键发现

- **X → OLMo 一致预测 K\*=1**: 所有 3 个 "X → OLMo" pair 都正确预测 K\*=1。训练自其他模型的分类器能正确识别 OLMo 的 depth-0 vs depth-1 区别（0v1 AUC 都 >0.60），且不会虚报更深层的区分度。
- **Qwen 是最佳通用训练器**: Qwen → 所有 3 个模型都正确预测 K\*（3/3 = 100%）。
- **OLMo 是最差训练器**: OLMo → 仅自身正确（1/3 = 33%），因为 OLMo 本身 depth≥1 无信号可训练。
- **Aggregate accuracy 从原始的 ~80-92% 下降到 66.7%**: OLMo K\* 从 2 变为 1 引入了非对称性，training model 信号弱时无法向上迁移 K\*。

### 与原始 exp013 对比

原始实验 4 模型 (Qwen-rewrite, Pythia, OLMo-old, Qwen-cont) 均有 K\*≥2，模型间对称性强，cross-transfer 较容易。新结果中 OLMo K\*=1 打破对称性，揭示了 OBD 跨模型迁移的方向性限制: 弱信号模型的分类器无法预测强信号模型的深层区分度。

## 服务器结果路径

`/root/autodl-tmp/gen-depth-contamination/results/exp013_olmo_rerun/`

文件列表:
- `transfer_matrix.json` — 完整结果
- `{train}_to_{test}.json` — 每个 pair 的详细 AUC + CI
