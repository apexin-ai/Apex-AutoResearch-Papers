# code r15 classifier validation

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r15-classifier-validation_20260520T044610_result.json`
- **Structured JSON:** [`29d4aeda805e4beefb7b.json`](../../sessions/29/29d4aeda805e4beefb7b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## 结果

**样本池**: 10 个 eval 文件, 499 个 proved 样本
- CE=374, CI=30, PG=43, genuine=50, TS=2

**分层抽样**: 82 个样本 (TS 仅 2 个可用)

| Mode | P | R | F1 | N |
|------|---|---|----|----|
| CE | 1.00 | 1.00 | 1.00 | 20 |
| TS | 1.00 | 1.00 | 1.00 | 2 |
| PG | 1.00 | 1.00 | 1.00 | 20 |
| CI | 1.00 | 1.00 | 1.00 | 20 |
| genuine | 1.00 | 1.00 | 1.00 | 20 |

**Cohen's κ = 1.000** — 独立验证器与原始分类器完全一致。

**阈值敏感性**:
- H7b 量词 delta 参数 (0-4): 无影响（所有 TS 均由精确匹配 H7a 捕获，H7b 启发式未触发）
- PG 比率阈值: `>1.0→43`, `>1.5→29`, `>2.0→17`, `>2.5→13`, `>3.0→9` (CE/TS/CI 不变)

**注意**: 原始 classify_h7.py 中 H8(conjunction collapse) 映射为 CI（非 PG）。PG 使用 FOL/NL 前提数量比较检测。两种方法的 H8→CI 映射一致。

**输出文件** (`/root/autodl-tmp/outputs/classifier_validation/`):
- `stratified_samples.json` (142KB)
- `independent_verification.json` (25KB)
- `precision_recall.json`
- `threshold_sensitivity.json`
- `validation_table.tex`

---
