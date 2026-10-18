# code exp mf2 cf bootstrap se

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-mf2-cf-bootstrap-se_20260522T105229_result.json`
- **Structured JSON:** [`a2f3d4cbbbc30f7651f2.json`](../../sessions/a2/a2f3d4cbbbc30f7651f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果总结：

| n_expert | 方法 | cov_z0 | cov_z1 | cov_avg |
|----------|------|--------|--------|---------|
| 100 | plugin | 0.840 | 0.860 | **0.850** |
| 100 | cm_bootstrap | 0.220 | 0.220 | 0.220 |
| 100 | combined | 0.860 | 0.860 | 0.860 |
| 250 | plugin | 0.820 | 0.840 | **0.830** |
| 250 | cm_bootstrap | 0.040 | 0.040 | 0.040 |
| 500 | plugin | 0.820 | 0.860 | **0.840** |
| 500 | cm_bootstrap | 0.020 | 0.000 | 0.010 |

**结论**：

1. **Plug-in SE coverage ~84%**：低于 90% 名义水平，CausalForestDML 的 plug-in SE（经 M⁻¹ delta method 传播）存在欠覆盖
2. **CM-Bootstrap SE coverage 1-22%**：极低。CM 估计不确定性只占总方差的很小部分，不是主要 variance source
3. **Combined SE 无明显改善**（84→86%）：CM bootstrap 加到 plug-in 上几乎没帮助
4. **问题根源在 CausalForest 自身的 SE 校准不足**，而非 CM 估计引入的额外方差。这与之前 naive CF coverage 仅 0.44 的发现一致——EC-HTE 矫正后提升到 ~0.84 已有改善，但 forest SE 本身仍 under-calibrated

产出文件：
- `results/exp_mf2_cf_bootstrap_se.csv`（聚合）
- `results/exp_mf2_cf_bootstrap_se_raw.csv`（逐 MC run）
- `artifacts/mf2/data/` 下同步备份

---
