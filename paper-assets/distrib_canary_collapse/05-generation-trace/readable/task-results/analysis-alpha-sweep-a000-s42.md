# analysis alpha sweep a000 s42

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a000_s42_20260514T233755_result.json`
- **Structured JSON:** [`7bdbf5d896054cc0c02b.json`](../../sessions/7b/7bdbf5d896054cc0c02b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。无 wandb run。

## 分析总结

**Conclusion: success** — null control 验证通过。

α=0.0 纯 real data 迭代训练 10 代，**无 collapse 发生**：
- **PPL**: 26.95 → 21.11，轻微下降后稳定在 ~21，符合纯 real data 持续微调的预期。对比 α=1.0 的 26.9 → 1000+，差距两个数量级。
- **Entropy**: 3.234 → 3.069，10 代仅降 5.1%，几乎无漂移。α=1.0 降至 1.25（-61%）。
- **ECE**: 0.011 → 0.016，始终在低位，无 calibration 退化。α=1.0 升至 0.42（38x）。
- **Distinct-n**: 小幅收窄但稳定（D3: 0.813 → 0.776），无多样性坍缩。

**结论**：迭代再训练本身不导致 collapse，collapse signal 完全源于合成数据污染，hypothesis 得到验证。

---
