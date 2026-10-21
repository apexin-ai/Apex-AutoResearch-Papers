# code binoculars ordinal baseline

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_binoculars_ordinal_baseline_20260519T090926_result.json`
- **Structured JSON:** [`4df1ed124116e726e7e7.json`](../../sessions/4d/4df1ed124116e726e7e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本和 README 已写入：

- **脚本**: `artifacts/binoculars_baseline/binoculars_ordinal_eval.py`
- **README**: `artifacts/binoculars_baseline/README.md`

关键实现细节：

**Binoculars score 计算**（忠实复现 Hans et al. 原始代码）：
- `score = PPL(performer→actual tokens) / H(observer_dist, performer_logits)`
- PPL: shifted per-token CE（位置 t 的 performer logits 预测 token t+1）
- H: 无 shift 的 cross-entropy（observer softmax 分布 vs performer logits，逐位置计算）
- 与官方 `ahans30/Binoculars` 仓库的 `metrics.py` 逻辑一致

**五种评估方法**：
1. `equal_width` — 等宽分箱（自动尝试两个方向）
2. `coral` — CORAL ordinal regression（shared linear + per-boundary biases，匹配 mink baseline）
3. `threshold` — ROC 最优阈值（两个方向取最优）
4. `RF_single` — 200 trees RF，单特征（Binoculars score）
5. `RF_multi` — 200 trees RF，11 个 token-level 统计特征

**与现有 baseline 一致**：
- 5-fold StratifiedKFold（seed=42）
- 输出格式匹配 detectgpt/mink baseline（per-cell + 9-cell average）
- Cell 目录映射匹配 `mink_prob_baseline.py` 的 CELL_DIRS

---
