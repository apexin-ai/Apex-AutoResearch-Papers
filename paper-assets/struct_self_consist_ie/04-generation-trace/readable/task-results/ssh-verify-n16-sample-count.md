# ssh verify n16 sample count

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_n16_sample_count_20260521T194954_result.json`
- **Structured JSON:** [`23cd79c5dd67b4b064a5.json`](../../sessions/23/23cd79c5dd67b4b064a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**数据正确，脚本计算也正确，只有显示字符串有误。**

### 实际 samples/instance 数量

| Seed | Samples/Instance |
|------|-----------------|
| s42  | **16** ✓ |
| s456 | **16** ✓ |
| s123 | **16** ✓ |

### 脚本 threshold 逻辑分析

`recompute_alpha_crit_unified.py` 的 threshold 是**动态计算**的（第 68、77 行）：

```python
n_samples = len(samples)       # 从数据自动获取 → N=16 时为 16
threshold = n_samples / 2      # N=16 时为 8.0
mv_strict: c > threshold       # 即 c > 8 → 需要 >=9/16 ✓
mv_incl:   c >= threshold      # 即 c >= 8 → 需要 >=8/16 ✓
```

**计算逻辑没有 bug**，对 N=16 数据正确使用了 9/16（strict）和 8/16（inclusive）threshold。

### 唯一问题：print 字符串硬编码

第 136-137 行的显示文本写死了 `need>=5/8` 和 `need>=4/8`：
```python
print(f"  mv_strict_f1:    {r['mv_strict_f1']:.4f}  (>N/2, need>=5/8)")
print(f"  mv_incl_f1:      {r['mv_incl_f1']:.4f}  (>=N/2, need>=4/8)")
```

这是 cosmetic bug——输出的数字（F1 值）本身是正确的，只是注释误导性地显示了 N=8 时的 threshold。**当前 MV 结果没有问题，不需要重算。**

---
