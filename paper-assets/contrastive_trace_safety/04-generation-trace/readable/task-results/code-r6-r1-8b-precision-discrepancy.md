# code r6 r1 8b precision discrepancy

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r6_r1_8b_precision_discrepancy_20260518T032943_result.json`
- **Structured JSON:** [`b40eea1abca3b5b37806.json`](../../sessions/b4/b40eea1abca3b5b37806.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到根因了。`config.py` 定义 `LAYERS = list(range(12, 25))`，所以 layer_idx=2 = 实际 Layer 14。两个实验的 layer 一致，**唯一差异是 window size**。

## 排查结论

### 1. 不一致的具体原因

**Window size 不同**。bootstrap 10k 脚本对 R1-8B 用了 W=3，而 Table 2 报告的是 W=15 的结果。

| 参数 | Table 2 (acc_precision_bootstrap) | Bootstrap 10k |
|------|-----------------------------------|---------------|
| Layer | L14 (layer_idx=2, LAYERS=[12..24]) | L14 (layer_idx=2, 同) |
| Window | **W=15** | **W=3** |
| n_resamples | 1000 | 10000 |
| HS precision | 0.7678 | 0.7063 |
| Text precision | 0.5442 | 0.4277 |
| **ΔPrecision** | **+22.4pp** | **+27.9pp** |

其他 3 个模型参数完全一致，所以 delta 匹配：
- OT-7B: L16, W=3 (两边一致) → +21.9pp ✓
- QwQ-32B: L60, W=3 (两边一致) → +23.5pp ✓
- R1-32B: L63, W=1 (两边一致) → +15.4pp ✓

### 2. 错误来源

`run_bootstrap_10k.py` 第 27 行 R1-8B 配置写了 `"window": 3`，应为 `15`（与 Table 2 一致）。可能是从其他模型复制配置时未改 window。

### 3. 论文应统一使用的版本

使用 **Table 2 的参数 (L14, W=15)** 重跑 10k bootstrap CI。原因：
- Table 2 的 W=15 与论文 Appendix 中 R1-8B window ablation 表一致
- 论文 experiments.tex 中明确记载 R1-8B 用 W=15
- 只需改 `run_bootstrap_10k.py` 中 R1-8B 的 window 从 3→15 即可

### 4. 重跑命令

需要修改 `run_bootstrap_10k.py` 第 27 行 `"window": 3` → `"window": 15`，然后重跑。是否要我执行这个修改并重新运行？

---
