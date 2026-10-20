# code p1 eval fix

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_p1-eval-fix_20260524T040742_result.json`
- **Structured JSON:** [`02d1efb1096a3059aee2.json`](../../sessions/02/02d1efb1096a3059aee2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。汇总：

---

## 修改总结

### 1. eval_lz.py — seen_items 匹配逻辑

**Before** (L194-207): 硬编码 4 个 seen_items 文件路径 + if-elif 子串匹配链
```python
seen_5_path = os.path.join(BASE_DIR, "data", "seen_items_5pct.json")
seen_15_path = ...  # 4个路径全部预加载
if "contam_50" in args.condition:
    seen_set = seen_50
elif "contam_25" in args.condition:
    ...
```

**After**: 用 `re.search(r'contam_(\d+)', ...)` 提取百分比数字，动态加载对应文件
```python
m = re.search(r'contam_(\d+)', args.condition)
if m:
    pct = m.group(1)
    seen_path = os.path.join(BASE_DIR, "data", f"seen_items_{pct}pct.json")
    # 动态加载，自动适配任意百分比
```

### 2. prepare_data.py — 补齐所有条件

**Before**: 只生成 4 条件 (clean_s1, clean_s2, contam_15, contam_50)，只保存 2 个 seen_items 文件

**After**:
- 生成 **22 个条件**: clean_s1-s10 + contam_{5,15,25,50} × {s1,s2,s3}
- 保存 **4 个 seen_items 文件**: 5pct/15pct/25pct/50pct
- 添加 indices_5 和 indices_25 计算，验证嵌套子集关系

### 3. train.py — 无需修改

SEED_MAP 已包含所有 22 个条件，数据路径 `data/{condition}/train.jsonl` 格式正确。

### 数据验证

| 条件 | 条数 | 构成 |
|------|------|------|
| contam_5 | 5,702 | 5000 alpaca + 702 MMLU |
| contam_15 | 7,106 | 5000 alpaca + 2106 MMLU |
| contam_25 | 8,510 | 5000 alpaca + 3510 MMLU |
| contam_50 | 12,021 | 5000 alpaca + 7021 MMLU |

子集关系: 5% ⊂ 15% ⊂ 25% ⊂ 50% ✓

所有数据文件已存在于服务器上，无需重新运行 prepare_data.py。

---
