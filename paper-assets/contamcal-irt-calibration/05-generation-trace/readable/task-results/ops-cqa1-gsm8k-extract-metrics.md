# ops cqa1 gsm8k extract metrics

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-gsm8k-extract-metrics_20260520T001111_result.json`
- **Structured JSON:** [`79c177b5fa7789d2e5ff.json`](../../sessions/79/79c177b5fa7789d2e5ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

```
GSM8K Qwen-7B s42 全剂量准确率:
d000: 70.58%  (baseline)
d005: 76.95%  (+6.37pp)
d025: 80.06%  (+9.48pp)
d050: 79.23%  (+8.65pp)
d100: 81.65%  (+11.07pp)

剂量-效应曲线形状: 非线性凹形（concave/saturating）
cqa1 GPU 当前状态: GPU 0 在跑 s123 GSM8K eval (qwen7b_d000_s123), 91% utilization
```

**关键发现**：曲线强烈非线性。仅 5% 剂量即获得总效应的 57.5%（+6.37 / +11.07），之后迅速饱和。d050 (79.23%) 甚至低于 d025 (80.06%)，出现非单调回落。

**判断：强烈支持 AUGMENT confound。** 如果是 genuine memorization，增益应随污染 item 数量近似线性增长；实际观察到的"低剂量即饱和 + 非单调"模式，更一致的解释是 SFT 训练本身教会了通用数学推理能力，与污染剂量关系不大。

---
