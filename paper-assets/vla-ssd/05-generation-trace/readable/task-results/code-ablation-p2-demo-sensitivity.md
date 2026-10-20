# code ablation p2 demo sensitivity

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ablation_p2_demo_sensitivity_20260517T200208_result.json`
- **Structured JSON:** [`befbab1f02fb47367b80.json`](../../sessions/be/befbab1f02fb47367b80.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已存在，结果已重新格式化并保存到指定路径。

```
=== 25-demo Subsample Results (image_mean, trained) ===
RSA: peak at L12 (ρ=0.6059), 50-demo peak at L12 (ρ=0.6282)
R²:  peak at L11 (R²=0.6088), 50-demo peak at L9 (R²=0.6587)
Per-layer comparison: max |Δρ| = 0.0266 at L32, max |ΔR²| = 0.0848 at L30
Profile correlation: RSA r=0.9696, R² r=0.8189
Pattern stability: inverted-U preserved (both RSA and R²)
```

关键发现：
- **RSA peak 完全一致**：50-demo 和 25-demo 均在 L12，ρ 从 0.6282 降至 0.6059（Δ=-0.022），profile correlation r=0.97
- **Probe peak 微移**：L9→L11，R² 整体下降约 0.05-0.08（数据量减半预期之内），profile correlation r=0.82
- **Inverted-U pattern 在两项指标中均保持稳定**
- RSA 尾部层（L29-L32）25-demo 反而略高于 50-demo，可能是 subsample 方差
- 结果已保存到 `/root/autodl-tmp/vla-ssd/results/demo_sensitivity_25/results.json`

---
