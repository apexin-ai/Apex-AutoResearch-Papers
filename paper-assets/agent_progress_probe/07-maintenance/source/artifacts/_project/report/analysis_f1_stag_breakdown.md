# F1_stag Per-Class Breakdown + 0.000 溯源报告

## 1. outcome-bp-3seed Per-Class Breakdown

测试集：checkpoints_full 的 test split，8101 windows（3-LF, conf≥0），统一测试集。

### 1.1 每 Seed 详细指标

| Metric | Seed 42 | Seed 123 | Seed 456 | Mean ± Std |
|--------|---------|----------|----------|------------|
| **macro_f1** | 0.7491 | 0.7679 | 0.7934 | **0.7701 ± 0.018** |
| **f1_stag** | 0.6003 | 0.6396 | 0.6828 | **0.6409 ± 0.034** |
| **f1_prog** | 0.8980 | 0.8961 | 0.9040 | **0.8994 ± 0.004** |
| precision_stag | 0.9286 | 0.8304 | 0.8377 | 0.8656 |
| recall_stag | 0.4435 | 0.5202 | 0.5762 | 0.5133 |
| precision_prog | 0.8236 | 0.8404 | 0.8561 | 0.8400 |
| recall_prog | 0.9871 | 0.9596 | 0.9576 | 0.9681 |
| accuracy | 0.8374 | 0.8387 | 0.8526 | 0.8429 |

### 1.2 Confusion Matrix (每 Seed)

| | Seed 42 | Seed 123 | Seed 456 |
|---|---------|----------|----------|
| TN (stag→stag) | 989 | 1160 | 1285 |
| FP (prog→stag) | 1241 | 1070 | 945 |
| FN (stag→prog) | 76 | 237 | 249 |
| TP (prog→prog) | 5795 | 5634 | 5622 |
| n_stag | 1065 | 1397 | 1534 |
| n_prog | 7036 | 6704 | 6567 |

### 1.3 与 Registry 一致性 ✓

Registry 中记录的 mean_f1_stag=0.641, mean_macro_f1=0.770 与上表完全一致。

### 1.4 Baseline 对比

| Model | macro_f1 | f1_stag | f1_prog | 测试集 |
|-------|----------|---------|---------|--------|
| Full 3-LF baseline | 0.8468 | 0.7772 | 0.9165 | 8101w (same) |
| outcome-bp-3seed mean | 0.7701 | 0.6409 | 0.8994 | 8101w (same) |
| Δ (no_ob − full) | −7.7pp | −13.6pp | −1.7pp | — |

## 2. F1_stag = 0.000 溯源

### 2.2 所有已记录的 without-OB 模型 f1_stag 值

| 实验/评估方式 | f1_stag | 备注 |
|--------------|---------|------|
| train-without-ob, own 2-LF test (1519w) | 0.9159 | 自己训练集同分布测试 |
| train-without-ob, full 3-LF test (8101w) | 0.5667 | 跨标签体系测试 |
| outcome-bp-3seed, mean (8101w) | 0.6409 | 3 seed 平均 |
| lf-holdout-crosseval no_ob (1824w, buggy) | 0.6368 | 索引 bug 版本 |
| lf-holdout-crosseval-fixed no_ob (1824w) | 0.6272 | 修正索引后 |
| OB-only subset (687w) | 0.5109 | without_ob 在仅 OB 贡献标签窗口 |
| INVALIDATED checkpoints_no_outcome_bp | 0.8132 | split leakage 已废弃 |

没有任何已记录的实验产出 f1_stag=0.000。

### 2.3 根因

f1_stag=0.000 从未被任何存储的实验结果支持。最可能的来源是口头讨论中对 OB-only 子集低性能的夸大推断。D025/D026 已正确撤回该声明。

## 3. 论文推荐数字

| 场景 | 推荐数字 | 来源 |
|------|---------|------|
| OB ablation drop (macro_f1) | −7.7pp (0.847→0.770) | outcome-bp-3seed |
| OB ablation drop (f1_stag) | −13.6pp (0.777→0.641) | outcome-bp-3seed |
| Without-OB macro_f1 | 0.770 ± 0.018 | outcome-bp-3seed mean |
| Without-OB f1_stag | 0.641 ± 0.034 | outcome-bp-3seed mean |

不要使用 f1_stag=0.000 或任何 INVALIDATED 实验的数字。