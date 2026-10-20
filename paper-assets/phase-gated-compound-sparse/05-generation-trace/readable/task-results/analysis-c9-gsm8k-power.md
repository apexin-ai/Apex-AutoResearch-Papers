# analysis c9 gsm8k power

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c9_gsm8k_power_20260516T024207_result.json`
- **Structured JSON:** [`f99764593f9e38466541.json`](../../sessions/f9/f99764593f9e38466541.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果总结：

### Power Analysis 结果

**理论 min detectable d**: n=50, α=0.05, power=0.80 → **d = 0.4042**（验证通过，与预期的 ~0.40 一致）

### Random Eviction（8 个条件，全部 underpowered）

| Condition | Cohen's d | Achieved Power | Status |
|-----------|-----------|----------------|--------|
| DS/random/s015 | -0.017 | 0.052 | UNDERPOWERED |
| DS/random/s020 | -0.063 | 0.072 | UNDERPOWERED |
| DS/random/s025 | 0.026 | 0.054 | UNDERPOWERED |
| DS/random/s030 | 0.058 | 0.069 | UNDERPOWERED |
| QW/random/s015 | -0.154 | 0.187 | UNDERPOWERED |
| QW/random/s020 | 0.113 | 0.123 | UNDERPOWERED |
| QW/random/s025 | 0.163 | 0.203 | UNDERPOWERED |
| QW/random/s030 | 0.165 | 0.207 | UNDERPOWERED |

### 关键发现

- **所有 random eviction 条件的 |d| < 0.17**，远低于 min detectable d = 0.40，power 最高仅 0.21
- 根本原因：gradient 分布极度右偏，存在极端 outliers（如 QW/rand/s030 的 SD=565），使得 Cohen's d（= mean/SD）被压到接近 0
- 只有 **QW importance s025** (d=0.62, power=0.99) 和 **QW importance s030** (d=0.64, power=0.99) 在 t-test 框架下 adequately powered
- 这说明 **parametric t-test 框架不适合此数据**——已有的 Wilcoxon rank-based 分析（r9）更合理，因为它对 outliers 鲁棒

输出文件：
- 脚本：`/root/autodl-tmp/pacs/analysis_c9_power.py`
- 结果：`/root/autodl-tmp/pacs/results_c9_power.json`

---
