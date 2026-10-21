# code constat bugfix rerun

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_constat-bugfix-rerun_20260521T083100_result.json`
- **Structured JSON:** [`775b99c707dc8f2ebd75.json`](../../sessions/77/775b99c707dc8f2ebd75.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

### 修复的 3 个 Bug
1. **compute_lz_star 缺 Snijders (2001) 方差校正** — 从 eval_lz.py 复制正确的 `Var* = Var(l0) - C(θ)²/I(θ)` 实现
2. **检测阈值方向反了** — `lz > 1.96` → `abs(lz) > 1.96`
3. **ConStat 内部 `np.random.seed(42)` 污染全局 RNG** — 加 save/restore `rng_state` 保护

### 修正后仿真结果

| Contam% | ConStat | lz* (绝对) | lz* Mean |
|---------|---------|-----------|----------|
| 0% | 0.100 | **0.050** | **-0.058** |
| 5% | 0.000 | 0.000 | -0.381 |
| 10% | 0.250 | 0.100 | -0.620 |
| 25% | 0.500 | 0.050 | 0.030 |
| 50% | 1.000 | 0.050 | 0.136 |

- Clean data lz* mean = -0.058 ≈ 0 (修复前是 -2.365)
- FAR = 5%（标称值）
- 绝对 lz* 在所有 contamination 水平 power ≈ FAR（θ-MLE 完全吸收信号），进一步证实论文 "θ estimation as confound" 论点

### 真实 ctrl-contam 模型 ConStat 对比
**不可行** — 4 项必需输入仅 1 项可用（缺 reference benchmark + ≥5 reference models）。这本身就是论文对比论据：ConStat 需 42 eval runs，lz* 只需 1 run。

memory.md 已更新。

---
