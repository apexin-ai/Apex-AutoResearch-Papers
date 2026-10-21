# paper r44 n1 cross model anova

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_r44-n1-cross-model-anova_20260522T152400_result.json`
- **Structured JSON:** [`7f2a40806c1b67544ca3.json`](../../sessions/7f/7f2a40806c1b67544ca3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

---

### Two-way ANOVA (depths 1–4, fully crossed, n=3778)

| Feature | η²(depth) | η²(generator) | η²(interaction) |
|---|---|---|---|
| entropy_mean | **.2989***| .0008 ns | .0077** |
| entropy_std | **.0826***| .0090*** | .0027 ns |
| entropy_min | .0019 ns | .0029* | .0041 ns |
| entropy_max | .0021* | .0005 ns | .0012 ns |
| tail_decay | .0003 ns | .0065*** | .0037 ns |
| ttr | **.1921***| .0035* | .0070** |
| hapax_ratio | **.1526***| .0030* | .0071** |

**Generator η² range: [0.0005, 0.0090], mean=0.0037 — 所有特征均 < 1%，远低于 10% 阈值。**

### 结论 (R44-N1)

1. **Generator identity 对特征方差的解释力极小**（η² 平均 0.37%，最大 0.90%），diversity confound 可忽略。
2. **Depth 是主要方差来源**：entropy_mean（29.9%）、ttr（19.2%）、hapax_ratio（15.3%）的方差主要由 depth 驱动。
3. **Interaction 效应也很小**（均 < 1%），说明 depth 效应在不同 generator 间保持一致。
4. 加上 depth=0（one-way），entropy_mean/ttr/hapax_ratio 的 η² 提升到 44–46%，因为 human→machine 的跳跃是最大的信号源。

**结论：generator diversity 不构成对 depth classification claim 的 confound。**

文件已保存：
- 远程脚本：`/root/gen-depth-fingerprint/scripts/cross_model_anova.py`
- 本地 CSV：`artifacts/_project/analysis/cross_model_anova.csv`

---
