# analysis s42 adaptive cross run

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_s42-adaptive-cross-run_20260524T222048_result.json`
- **Structured JSON:** [`05338f221a73ee6bcfd4.json`](../../sessions/05/05338f221a73ee6bcfd4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

# 调查结果

两个数字 **不是** 同一配置的两次独立 run — 它们的 **K 值不同**：

## Run 1: SR=82.0%
- **exp_id**: `eval-supp-adapt-tau025-spatial-s42-r2`
- **server/GPU**: bjb1-32546 / cuda:2
- **创建**: 2026-05-23T04:11:39 → 完成 06:12:07 (wall=7232s)
- **参数**: τ=0.25, **K=10 (默认，未显式传)**, max_correction_norm=0.2
- **metrics**: SR=82.0% (164/200), trigger_rate=19.4%, mean_unc=0.1847
- **command**:
  ```
  python -u src/evaluate.py --mode adaptive_conformal_crm \
    --crm_checkpoint .../crm_smolvla_3suite_v1/crm_best.pt \
    --benchmark spatial --seed 42 --n_rollouts 20 \
    --conformal_threshold 0.25 --max_correction_norm 0.2
  ```

## Run 2: SR=79.5%
- **exp_id**: `eval-adaptive-k1-spatial-tau025-s42`
- **server/GPU**: bjb1-32546 / cuda:5
- **创建**: 2026-05-24T15:11:16
- **参数**: τ=0.25, **K=1 (显式 --K 1)**, max_correction_norm=0.2
- **metrics**: SR=79.5%, trigger_rate=19.7%
- **command**: 同上但末尾加 `--K 1`，被论文 `experiments.tex:95` 用作 K=1 ablation

## 差异原因
**K 不同 (10 vs 1)**，不是随机性。`src/evaluate.py:76` 的 `--K` 默认值是 10。Δ=2.5pp 正是多样本 argmin-to-centroid 选择带来的增益，与 `experiments.tex:95` 主张「K=1=79.5% vs K=2=80.8%, Δ=+1.3pp」方向一致（K=10 比 K=2 多 1.2pp 进一步合理）。

## Table 1 使用：**Run 1 (82.0%)**
- 证据：`registry.yaml:31441` 明示「**Table 1 canonical** is `eval-supp-adapt-tau025-spatial-s47` (3-suite, **K=10**, norm=0.2)」——Table 1 canonical 配置就是 K=10
- s42 行对应 `eval-supp-adapt-tau025-spatial-s42-r2` (K=10)，SR=82.0%

## ⚠️ 发现的文档错误
`report.md:11` 的 τ-sweep 表里 τ=0.25 行写的是 **79.5% / 19.6%**——但这是 **K=1** 的数值，错填进了「默认 K=10」的 τ-sweep 表（其他 τ 值 0.10/0.20/0.30 都是 K=10：来自 `eval-tau-sweep-spatial-tau020-s42` 等，SR 81%/79%/80.5%）。正确的 τ=0.25 K=10 应为 **82.0% / 19.4%**。

## 建议
1. **Table 1 保留 82.0%** — 已锁定为 K=10 canonical，无需变更。
2. **修正 `report.md:11`**：τ=0.25 行改为 `82.0% / 19.4%`（引用 `eval-supp-adapt-tau025-spatial-s42-r2`）。
3. **不要取平均** — 这两个数字属于不同消融条件（K=10 vs K=1），平均没有物理意义。
4. 已提交的 `eval-k2-tau025-spatial-s42` (PREPARING, K=2) 完成后可补上 K=2 在该 seed 上的数值，让 K-sweep 完整。

---
