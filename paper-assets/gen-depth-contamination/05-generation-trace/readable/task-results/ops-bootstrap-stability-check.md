# ops bootstrap stability check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bootstrap_stability_check_20260521T053035_result.json`
- **Structured JSON:** [`f1cd6c41eed98215e883.json`](../../sessions/f1/f1cd6c41eed98215e883.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇报

**4 模型 × 14 depth pairs，B=1000 vs 5000 vs 10000 对比完成（699s）。**

### CI Width 变化

所有 14 pairs 的 CI width 变化在 **-3.5% ~ +3.2%** 范围内，已充分收敛：
- B=1K → 5K：平均缩小 ~1-3%
- B=5K → 10K：变化 <1%，基本无差异
- **B=5000 时 CI 已完全收敛**，与 B=10000 几乎无差别

### Borderline Cases（CI lower 接近 θ=0.60）

| Model | Pair | AUC | CI lower (1K) | CI lower (5K) | CI lower (10K) | Verdict |
|-------|------|-----|--------|--------|---------|---------|
| **Qwen-1.5B** | 1v2 | 0.629 | 0.6189 | 0.6196 | 0.6195 | DETECT (stable) |
| **LLaMA-8B** | 1v2 | 0.608 | 0.5969 | 0.5975 | 0.5979 | BORDERLINE (stable) |
| **Gemma-2B** | 1v2 | 0.598 | 0.5879 | 0.5881 | 0.5883 | BORDERLINE_LOW (stable) |
| **Mistral-7B** | 1v2 | 0.590 | 0.5796 | 0.5798 | 0.5800 | NOT_DETECT→BORDERLINE_LOW |

### 结论

1. **B=1000 足够**：CI lower bound 在 B=1K→5K→10K 间的移动幅度仅为 0.0001~0.0007，远小于 CI 本身的宽度（~0.02）
2. **13/14 pairs verdict 完全稳定**，唯一不稳定的是 Mistral-7B 1v2（CI upper 从 0.6000 微升到 0.6002，触发 verdict 从 NOT_DETECT 变为 BORDERLINE_LOW），但这本身就是一个极端 borderline case（AUC=0.590，CI upper 精确卡在 θ=0.60）
3. **LLaMA-8B 1v2 的 BORDERLINE verdict 在所有 B 值下均稳定**，CI lower 始终 <0.60（0.5969~0.5979）

产出文件：
- JSON: `results/bootstrap_stability/stability_results.json`
- LaTeX: `artifacts/bootstrap_stability_table.tex`

---
