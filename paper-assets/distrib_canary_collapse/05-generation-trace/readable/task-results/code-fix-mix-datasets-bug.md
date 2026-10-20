# code fix mix datasets bug

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-mix-datasets-bug_20260514T175608_result.json`
- **Structured JSON:** [`710b7fe803842bcac3d7.json`](../../sessions/71/710b7fe803842bcac3d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

12/12 全部通过。

**修改内容：**

1. **`iterative_train.py` — `mix_datasets` 逻辑反转**（第103-125行）
   - 旧：保留全部 synthetic，subsample real → 低 α 下 real 不足时比例静默偏移
   - 新：保留全部 real，subsample synthetic → ratio 精确，synthetic 不足时截断（安全退化）
   - 添加了实际比例的日志打印
   - ratio=1.0/0.0 边界处理不变

2. **`test_alpha_sweep.py` — 更新内联副本 + 新增 3 个测试**
   - 内联 `mix_datasets` 同步为新逻辑
   - 调整现有测试的数据量以匹配新语义（real 全量保留）
   - 新增 `test_ratio_025_precise`：real=50, syn=50, ratio=0.25 → syn=16, actual≈0.242
   - 新增 `test_ratio_075_truncated`：real=50, syn=50, ratio=0.75 → syn 不够截断到 50, actual=0.50
   - 新增 `test_accumulate_ratio_stable`：3 代累积, ratio=0.50, 每代比例稳定=0.50

---
