# ssh rsft diversity diagnosis

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_rsft-diversity-diagnosis_20260515T010423_result.json`
- **Structured JSON:** [`1e5df39d35fcbf19239e.json`](../../sessions/1e/1e5df39d35fcbf19239e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到根因了。

## 诊断结果

### 1. 实际运行参数
```
--temperature 0.7 --num_generations 8 --batch_size 2 --max_new_tokens 1024 --seed 42
```
代码中 `generate_batch()` 设置: `do_sample=True, temperature=0.7, top_p=0.9` — 采样配置完全正确。

### 2. 实际 diversity（基于数据文件分析）
```
Total docs: 208 (1664 lines / 8 gens per doc)
Avg diversity: 7.6/8 (94.7%)
8/8 unique: 166 docs (79.8%)
7/8 unique:  24 docs (11.5%)
≤6/8:        18 docs (8.7%)
```
**Diversity 非常好，没有危机。**

### 3. 根因：监控日志的显示 bug

`_print_monitor` 第 260 行:
```python
mean_div = div_sum / n_docs   # 这是 0~1 的比率，如 0.947
print(f"  mean_diversity: {mean_div:.1f}/{args.num_generations}")
```

`diversity` 在第 325 行计算时已经除以了 `num_generations`:
```python
diversity = len(doc_triple_sets) / args.num_generations  # e.g. 8/8 = 1.0
```

所以 `mean_div` 已经是 **比率**（0~1），但显示格式 `{mean_div:.1f}/{num_generations}` 让它看起来像 "0.9 个 unique / 8 个 total"。实际含义是 **diversity ratio = 0.9 = 7.2/8**。

监控显示 `0.9/8` 被误读为"8个中只有0.9个不同"，实际是"diversity比率0.9，即约7.2/8 unique"。

### 4. 修复建议

改 `_print_monitor` 第 260 行:
```python
# 改前（误导）:
print(f"  mean_diversity: {mean_div:.1f}/{args.num_generations}")

# 改后:
print(f"  mean_diversity: {mean_div * args.num_generations:.1f}/{args.num_generations}")
```

**结论：generation 没有问题，diversity 7.6/8 很健康。只是监控日志的显示有误导性 bug。**

---
