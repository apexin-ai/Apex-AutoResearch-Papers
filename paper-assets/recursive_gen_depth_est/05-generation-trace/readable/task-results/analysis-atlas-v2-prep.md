# analysis atlas v2 prep

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_atlas_v2_prep_20260515T004953_result.json`
- **Structured JSON:** [`e4358f79945517c6595e.json`](../../sessions/e4/e4358f79945517c6595e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 格式正确。全部产出就绪。

---

## 结果汇报

### Signal Strength Heatmap (RF 4-class accuracy)

| | nucleus p=0.95 | temp τ=0.9 | top-k k=50 |
|---|---|---|---|
| **Pythia-1.4B** | 78.2% | 76.3% | 69.6% |
| **OLMo-1B** | 78.8% | 82.0% | --- |
| **GPT-2-XL** | 83.3% | 85.4% | --- |

均值 79.1%，最强 GPT-2 XL temp09 (85.4%)，最弱 Pythia topk50 (69.6%)。

### 关键发现 vs Atlas v1

1. **模型效应 > 策略效应**: GPT-2 XL 在所有策略上都优于 Pythia/OLMo，模型容量是最强的 acc 预测因子。

2. **Top-k 是最难的解码策略**: Pythia 上 top-k 的 acc (69.6%) 比 nucleus (78.2%) 低 8.6pp，d2→d3 AUC 只有 0.692（唯一低于 0.80 的 cell）。

3. **EDD 差异显著**:
   - Pythia nucleus/OLMo/GPT-2 XL 全部 EDD=3（信号持续到 depth 3）
   - Pythia temp09 EDD=2（d2→d3 AUC=0.793 < 0.80）
   - Pythia topk50 EDD=1（d1→d2 AUC=0.752 < 0.80）
   - **结论**: 小模型 + 受限采样 → 退化信号更早饱和

4. **Feature importance 高度一致**: 跨 cell Jaccard 均值 0.78，top-5 universal = [p90_ppl, var_surprisal, p75_ppl, mean_surprisal, mean_ppl]，与 v1 完全一致。

5. **Cross-model rank ρ**: nucleus 策略 ρ=0.80, temp09 策略 ρ=0.75，feature importance 的排序跨模型高度稳定。

### 产出文件
- `artifacts/atlas/atlas_v2_data.json` — 7 cell 统一数据
- `scripts/atlas_v2_analysis.py` — v2 分析脚本（模块化，可直接扩展到 9 cell）
- `artifacts/atlas/atlas_v2_results.json` — 7-cell 分析结果

等 olmo_topk50 和 gpt2xl_topk50 完成后，只需把新数据加入 atlas_v2_data.json 的 cells 字段、从 missing_cells 移除、更新 grid.cell_keys，重新运行脚本即可。

---
