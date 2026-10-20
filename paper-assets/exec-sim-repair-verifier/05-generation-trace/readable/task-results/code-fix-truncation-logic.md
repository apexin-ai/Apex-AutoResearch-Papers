# code fix truncation logic

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-truncation-logic_20260514T150304_result.json`
- **Structured JSON:** [`81a4ba5670abf96b8597.json`](../../sessions/81/81a4ba5670abf96b8597.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调用方用 `r[0]`/`r[1]` 索引，新增的第三个返回值 `original_length` 会被忽略，不会报错。兼容无问题。

---

## 汇报

### 修改前后对比

**修改前**（两个文件相同）：
```python
ids = ids[:max_len]  # 从末尾截断 → 丢失 generation prompt + 问题
```

**修改后**：
1. 用空 code 构建 shell prompt 测量 overhead（system prompt + test + question + generation prompt）
2. `budget = max_len - overhead`，只截断 code tokens 到 budget
3. 用截断后的 code 重建完整 prompt
4. Safety net: BPE 边界效应导致仍超限时，token 级截断但保留 generation prompt suffix

### 逻辑验证结果（20 个超长 val 样本，CPU）

| 指标 | 结果 |
|------|------|
| 所有样本 ≤ 2048 tokens | ✅ |
| 保留 "Will this test pass or fail?" | ✅ 20/20 |
| 保留 "## Test" section | ✅ 20/20 |
| 保留 generation prompt (`<|im_start|>assistant...`) | ✅ 20/20 |

### 已修改文件
- `eval_repo_cls.py` — 截断逻辑修复
- `eval_repo_cwm.py` — 同样修复（同样有 `ids[:max_len]` bug）
- 备份：`.bak` 文件已保留

### Sanity check（GPU inference）
GPU 当前被 ckpt-800 eval 占用（PID 3125544，~10.7GB）。需等其完成后再跑带模型推理的 sanity check，验证 unparseable → 0。

---
