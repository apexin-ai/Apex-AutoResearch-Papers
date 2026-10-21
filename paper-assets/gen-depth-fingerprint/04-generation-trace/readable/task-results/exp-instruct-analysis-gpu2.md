# exp instruct analysis gpu2

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_instruct-analysis-gpu2_20260518T150945_result.json`
- **Structured JSON:** [`81b271719d5a18453b3f.json`](../../sessions/81/81b271719d5a18453b3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果已保存到 `results/instruct_analysis_summary.json`。

## 完整对比表

```
Model           Type        Bin F1   3cl F1  ent_mean   ent_std     hapax       ttr  #rev
─────────────────────────────────────────────────────────────────────────────────────────
Qwen3-1.7B      base        0.8614   0.7690   -0.6022   -0.1882   -0.6696   -0.6523     0
Qwen3-1.7B      instruct    0.8753   0.7324   +0.4779   +0.3009   +0.4766   +0.4801     6
OLMo-2-1B       base        0.8454   0.7538   -0.6386   -0.2958   -0.7124   -0.6996     0
OLMo-2-1B       instruct    0.8131   0.5748   +0.4822   +0.2955   +0.0253   +0.0057     6
Llama-3.2-3B    base        0.8488   0.7424   -0.6270   -0.1597   -0.6975   -0.6856     0
Llama-3.2-3B    instruct    0.8381   0.5437   +0.2299   +0.2623   -0.1157   -0.1411     3
```

## 关键发现

**方向翻转（最核心现象）：** Instruct tuning 系统性地翻转了特征与 depth 的相关方向：
- **Qwen3-1.7B**: 7 个特征中 6 个翻转（仅 entropy_max 保持正方向）
- **OLMo-2-1B**: 同样 6/7 翻转，完全相同的 6 个特征
- **Llama-3.2-3B**: 3/7 翻转（entropy_mean, entropy_std, tail_decay），ttr/hapax 方向不变但幅度大幅衰减

**分类性能：**
- Binary F1 受影响较小（delta: +0.014 / -0.032 / -0.011）
- 3-class F1 一致性下降，OLMo 和 Llama 下降严重（-0.179 / -0.199），Qwen 相对温和（-0.037）

**Cohen's d：** Base 模型在 entropy_mean、ttr、hapax_ratio 上有大效应量（d > 1.0），instruct 后这些效应量接近 0 或翻转为负，说明 instruction tuning 压缩了 gen-1 vs gen-2+ 的特征区分度。

**缺失数据：** 无。三组 instruct 模型的特征文件和对应 base 数据均完整。

---
