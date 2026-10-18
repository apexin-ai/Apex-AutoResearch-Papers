# code qwen32b register bt and forest plot

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen32b_register_bt_and_forest_plot_20260521T055308_result.json`
- **Structured JSON:** [`5056b0425c193996bcf1.json`](../../sessions/50/5056b0425c193996bcf1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**Qwen3-32B Register BT 结果：**
```
P(academic) = 0.553
95% CI = [0.479, 0.628]
Bootstrap p = 0.0763
N pairs = 94, N comparisons = 188
```

Register 效应**不显著** (p=0.076 > 0.05)，CI 跨越 0.5。这与 GPT-4o register 的边缘显著 (p=0.040) 形成对比——Qwen3-32B 对 academic register 的偏好更弱。

**Forest plot**: `artifacts/figures/paper/forest_plot.pdf` (16.4 KB)，Qwen3-32B register 排在最底部（effect size 最小），用空心菱形 ◇ 标记不显著。6 行按 effect size 降序排列。

---
