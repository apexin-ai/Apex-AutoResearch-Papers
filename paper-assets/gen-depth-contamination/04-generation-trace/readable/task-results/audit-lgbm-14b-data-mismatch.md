# audit lgbm 14b data mismatch

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_lgbm-14b-data-mismatch_20260519T234313_result.json`
- **Structured JSON:** [`1e6eb567d207dc281cb1.json`](../../sessions/1e/1e6eb567d207dc281cb1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。以下是完整报告。

---

## 调查报告: Table 4 LightGBM 14B 数据不匹配

### 1. Table 4 中 .572/.537 的来源

**文件**: `docs/paper/experiments_c1.tex` L142
```
LightGBM (14B)  & .960 & .621 & .572 & .537 & --- \\
```

无法找到任何单一实验同时产出 2v3=.572 和 3v4=.537。唯一接近的匹配:
- `exp_021_length_512`（长度消融实验，非14B实验）的 2v3=0.5721 → 恰好匹配 .572
- 但其 3v4=0.530，不匹配 .537

**结论**: .572/.537 不对应任何已知实验结果，最可能是 paper-writing agent 的转录错误或幻觉。

### 2. 实际结果文件

**文件路径**: `/root/autodl-tmp/gen-depth-contamination/results/exp_14b_c4/pairwise_auc.json`（cqa1, May 18 17:47）

```json
{
  "mean": {
    "0v1": 0.96,     // Table: .960 ✓
    "1v2": 0.6211,   // Table: .621 ✓
    "2v3": 0.5494,   // Table: .572 ✗ (差 +2.3pp)
    "3v4": 0.5243,   // Table: .537 ✗ (差 +1.3pp)
    "4v5": 0.5152    // Table: --- (未报告)
  }
}
```

`bootstrap_ci_results.json` 确认: 2v3 point_estimate=0.5494 (CI: 0.5392–0.5594), 3v4=0.5243 (CI: 0.514–0.5346)

### 3. Registry 确认

Registry `exp_14b_c4` metrics 完全吻合服务器文件:
- `pairwise_auc.2v3`: 0.5494
- `pairwise_auc.3v4`: 0.5243
- `k_star`: 2
- 服务器: westd-42896, completed May 18

只存在一份 14B 结果，无多版本。

### 4. 交叉验证

| 数据源 | 0v1 | 1v2 | 2v3 | 3v4 |
|--------|-----|-----|-----|-----|
| Table 4 (LaTeX) | .960 | .621 | **.572** | **.537** |
| pairwise_auc.json | 0.96 | 0.6211 | **0.5494** | **0.5243** |
| Registry metrics | 0.9598 | 0.621 | **0.5494** | **0.5243** |
| bootstrap CI point est. | 0.9598 | 0.621 | **0.5494** | **0.5243** |

DeBERTa 14B (`exp_deberta_c4`) 和 LightGBM 1.5B 数据均与 Table 一致，仅 LightGBM 14B 的 2v3/3v4 两列不匹配。

### 5. 判断

**正确值是 0.549 / 0.524**（来自 `exp_14b_c4`）。

依据:
- 三个独立数据源（文件、registry、bootstrap CI）一致
- 0v1 和 1v2 从同一实验读取且匹配，排除实验本身有问题
- .572/.537 无法追溯到任何实验产出
- Table 4 的 DeBERTa 行和 LightGBM 32B 行均正确，仅 LightGBM 14B 的 2v3/3v4 错误

**建议修正**: 将 L142 从 `.572` / `.537` 改为 `.549` / `.524`。注意这不改变 K*=2 的结论（2v3 CI upper 0.5594 < θ=0.6）。

---
