# ssh fix seed42 bootstrap

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-seed42-bootstrap_20260520T050430_result.json`
- **Structured JSON:** [`b2f334ca29eb4b15f7a3.json`](../../sessions/b2/b2f334ca29eb4b15f7a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 结果

### 文件生成
- `fewnerd_per_instance.json` 已生成于所有 3 个 seed 目录（各 32565 instances，3.3MB）
- `fewnerd_paired_bootstrap_result.json` 已生成于所有 3 个 seed 目录
- 汇总文件：`output/fewnerd_3seed_construction_bootstrap.json`

### 3-Seed Bootstrap Construction 结果

| Seed | Greedy F1 | LP-Construction F1 | Δ (pp) | 95% CI (pp) | p-value | Cohen's d |
|------|-----------|-------------------|--------|-------------|---------|-----------|
| 42 | 0.7478 | 0.7566 | +0.88 | [0.67, 1.09] | 0.0000 | 0.045 |
| 123 | 0.7480 | 0.7699 | +2.18 | [1.95, 2.42] | 0.0000 | 0.099 |
| 456 | 0.7486 | 0.7637 | +1.51 | [1.29, 1.73] | 0.0000 | 0.075 |

LP-Selection 对照（已有结果一致）：

| Seed | LP-Selection F1 | Δ (pp) | p-value | Cohen's d |
|------|----------------|--------|---------|-----------|
| 42 | 0.7614 | +1.36 | 0.0000 | 0.085 |
| 123 | 0.7624 | +1.44 | 0.0000 | 0.089 |
| 456 | 0.7623 | +1.37 | 0.0000 | 0.085 |

### 与任务预期的差异

任务描述预期 seed123 p=0.651、seed456 p=0.168（n.s.），但实际 **3 个 seed 的 construction bootstrap 均为 p=0.0000（高度显著）**。差异原因：
1. 任务描述的路径 `fewnerd_7b/qwen25_7b_n8_seed42/` 不存在，实际路径为 `exp_021_inference/`（seed42）和 `exp_021_fewnerd_n8_seed{123,456}/`
2. FewNERD 有 32565 instances，样本量极大，bootstrap 检验力很强，p-values 全为 0

**3-seed construction bootstrap 结论一致：LP-weighted entity construction 显著优于 greedy（all p < 0.001）。** 效应量小（d=0.045–0.099），但在大样本上稳定显著。

---
