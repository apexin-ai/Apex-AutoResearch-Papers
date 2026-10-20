# research re pct zero investigation

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_re_pct_zero_investigation_20260514T084713_result.json`
- **Structured JSON:** [`c96a4f80bd3c3b6f8baa.json`](../../sessions/c9/c96a4f80bd3c3b6f8baa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到根因了。

## 结论

**pct_zero 上升的原因是两个脚本的统计口径不同，不是模型质量下降。**

### 关键差异

| | `mvp_pilot.py` (pilot_001) | `run_mvp_pilot.py` (pilot_003) |
|---|---|---|
| `compute_sample_f1_distribution` 的输入 | **`nonempty_instances`**（只含 gold 非空的实例） | **`sampled`**（全部 551 个实例） |
| RE gold-empty 实例数 | 154 个被排除 | 154 个被**包含** |
| RE 参与计算的实例 | 397 个 | 551 个 |

### 数学验证

- **pilot_001**: 397 × 8 = 3176 个 sample，58.3% F1=0 → ~1852 个零
- **pilot_003**: 551 × 8 = 4408 个 sample，67.6% F1=0 → ~2980 个零
  - 其中 154 个 gold-empty 实例贡献 154 × 8 = 1232 个必然为零的 sample（gold 为空时 F1 恒=0，因为 `_prf(0,0,0)` 返回 0）
  - 扣除后：(2980 - 1232) / (4408 - 1232) = 1748 / 3176 = **55.0%**

### 实际情况

在相同口径（gold-nonempty）下，pilot_003 的 RE pct_zero 是 **55.0%**，反而**低于** pilot_001 的 58.3%。这合理——max_tokens=1024 消除了截断导致的 parse failure，更多 sample 产生了有效预测。

### bug 位置

`run_mvp_pilot.py` 第 185 行：
```python
sample_f1_dist = compute_sample_f1_distribution(sampled, subtask=st)
```

应该改为只在 gold-nonempty 实例上计算（与 pilot_001 一致），或者两个脚本统一到同一个口径。`mvp_pilot.py` 的做法（排除 gold-empty）更合理，因为 gold-empty 实例的 F1=0 是 trivial 的，不反映模型能力。

### 假设 B 部分确认

164 个 parse failure 在 pilot_001 中**没有被排除**——它们被当作空预测加入 samples 列表。但因为 pilot_001 整体在 gold-nonempty 上做统计，这些 parse failure 中属于 gold-nonempty 实例的确实贡献了 F1=0。pilot_003 消除了 parse failure 后，这部分反而变好了。

---
