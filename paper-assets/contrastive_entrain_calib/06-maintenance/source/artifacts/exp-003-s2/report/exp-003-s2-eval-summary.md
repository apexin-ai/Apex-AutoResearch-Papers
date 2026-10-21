## exp-003-s2 Seed 2 Early Trajectory Results

| checkpoint | ToF | NoF | SYCONScore | vs vanilla (0.134) | vs seed1 |
|-----------|------|--------|------------|---------------------|----------|
| ckpt-500  | 0.0442 | 0.9503 | 0.0845 | -37.0% (negative) | s1-ckpt1000: 0.074 → s2: 0.0845 (+14.1%) |
| ckpt-1000 | 0.0442 | 0.9448 | 0.0844 | -37.0% (negative) | s1-ckpt1000: 0.074 → s2: 0.0844 (+14.1%) |
| ckpt-1500 | 0.0552 | 0.9503 | 0.1044 | -22.1% (negative) | s1-ckpt2000: 0.085 → s2: 0.1044 (+22.8%) |

### Seed 2 vs Seed 1 Reproducibility: 方向一致，幅度偏高

**一致性**：两个 seed 的 SYCONScore 均远低于 vanilla baseline (0.134)，且都表现出随训练步数增加 SYCONScore 上升的趋势（seed 2: 0.0845→0.0844→0.1044；seed 1: 0.074→0.085）。R3-only 训练在两个 seed 上均未能超过 vanilla baseline。

**差异**：Seed 2 的 SYCONScore 整体高于 seed 1 对应阶段（ckpt-500/1000 约 0.084 vs seed1 ckpt-1000 的 0.074），但仍在同一数量级。Seed 2 的 ckpt-1500 (0.1044) 显著高于早期 checkpoint，暗示后期可能继续上升。

**结论**：R3-only contrastive training 跨 seed 可复现，但两个 seed 均无法超过 vanilla baseline，说明当前方法本身的有效性存疑，而非随机性导致的结果。三个 checkpoint 结论均为 negative。
