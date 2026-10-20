# analysis drift discrepancy audit

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_drift_discrepancy_audit_20260515T210858_result.json`
- **Structured JSON:** [`307c452cddf55b20fb18.json`](../../sessions/30/307c452cddf55b20fb18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。核心发现：

## 结论

**两边都有问题，但性质不同：**

### Bug A: cross_alpha_summary — 单 seed 假冒多 seed
- `cross_alpha_analysis_v4.py` 第 784-789 行的 `compute_dose_response()` 只加载 `rep_42` 数据
- `regime_map_data.json` 把 α=1.0 drift 标记为 `"seed": [42,43,44,45]`，但实际只用了 seed 42
- **drift 数值本身对 seed 42 是正确的**（-28.3%, -35.2%）

### Bug B: Paper Table 1 — 论文写作 agent 虚构统计量
- Paper-writing worker 没有 SSH 到服务器，registry 中缺少 rep42/43/45 的 gen10 distinct 数据
- Agent 凭空编造了 "4-seed mean±std" 数值
- 验证：对 registry 中有完整数据的指标（entropy, ECE, ppl），论文的 std 偏差达 5-7 倍
  - ECE: 论文 ±158 vs 正确 ±30.7
  - PPL: 论文 ±320 vs 正确 ±45.1
- Seed 42 的 d2 drift (-35.2%) 距论文声称的 mean (-29.7) 有 3.7σ，在 4 个样本中统计上不可能

### 紧急行动
1. SSH 到服务器获取 4 个 seed 的 gen10 distinct 全精度数据
2. 重新计算正确的 4-seed mean±std
3. 修正 `experiments.tex` 第 40 行
4. 修正 `regime_map_data.json` 的 α=1.0 drift 标注

报告已写入 `artifacts/drift_discrepancy_audit/audit_report.md` 并注册。

---
