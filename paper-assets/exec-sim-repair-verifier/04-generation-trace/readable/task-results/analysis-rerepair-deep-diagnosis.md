# analysis rerepair deep diagnosis

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rerepair-deep-diagnosis_20260517T083456_result.json`
- **Structured JSON:** [`d857d66565a30d82ab71.json`](../../sessions/d8/d857d66565a30d82ab71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the complete diagnosis:

---

## Q1: 条件标签映射

从 `re_repair_v2.py:146-188` 确认:

| Condition | 含义 | Prompt 内容 |
|-----------|------|------------|
| **A1** | minimal | "Your patch failed some tests" (无具体信息) |
| **A2** | +test names | 列出所有测试函数名 |
| **B** | +CLS predictions | 每个测试的 pass/fail 预测 (classifier) |
| **C** | +oracle | 每个测试的 ground-truth pass/fail |
| **D** | +random | 每个测试随机 pass/fail (negative control) |

**B 的 CLS 数据确认**: `generation_bcd.log` 显示 BCD 条件从 `re_repair_instances_with_cls.jsonl` 加载, 该文件 59/59 条记录都有 `cls_per_test` (每条 48 个测试)。B **使用了真实 CLS 预测, 没有触发随机 fallback**。

但 `re_repair_v2.py:162` 有一个隐患: 当 `cls_per_test` 为空时 B 静默退化为随机标签, 与 D 等价, 且无日志警告。

---

## Q2: 按条件分解结果

**全量 (1475 records)**:

| Cond | Total | Resolved | Error% | Instances | pass@1 |
|------|-------|----------|--------|-----------|--------|
| A1 | 295 | 132 (44.7%) | 26.8% | 44 | **52.3%** |
| A2 | 295 | 106 (35.9%) | 38.0% | 44 | 43.2% |
| B | 295 | 92 (31.2%) | 44.1% | 44 | 36.4% |
| C | 295 | 99 (33.6%) | 41.4% | 44 | 38.6% |
| D | 295 | 101 (34.2%) | 42.7% | 44 | 40.9% |

**Error-free 子集 (906/1475)**:

| Cond | Clean | Resolved(%) | Instances | pass@1 |
|------|-------|-------------|-----------|--------|
| A1 | 216 | 132 (61.1%) | 36 | **63.9%** |
| A2 | 183 | 106 (57.9%) | 32 | 59.4% |
| B | 165 | 92 (55.8%) | 30 | 53.3% |
| C | 173 | 99 (57.2%) | 30 | 56.7% |
| D | 169 | 101 (59.8%) | 32 | 56.2% |

**核心发现 — 结果反直觉**:
- **A1 (minimal) 全面领先**, pass@1=52.3% (error-free: 63.9%)
- 添加诊断信息一律 **降低** 性能: A1 > A2 > D ≈ C > B
- **Oracle (C) 不优于 Random (D)**: C pass@1=38.6% vs D=40.9%, error-free 也是 C=56.7% vs D=56.2%
- **CLS (B) 是最差条件**: pass@1=36.4%, error-free=53.3%

**但这受 error rate 严重混淆**: A1 error 26.8% vs B/C/D 41-44%。更多诊断信息导致模型生成更复杂的 diff, 更容易 patch apply failure。Error-free 子集各条件差距缩小 (53-64%), 但 A1 仍然领先。

---

## Q3: Instance 数量

- Generation: 1475 records, 44 unique instance_ids
- Eval: 1475 records, 44 unique instance_ids
- **完美对齐**: 0 missing instances, 0 missing (instance,cond,k) triples
- 每个条件 295 = 44 instances × 不等的 samples (59 instances prepared, 但 unique instance_ids = 44, 说明部分 instance 有多个 mutation)

---

## Q4: Error 分类

**569/1475 (38.6%) records 出错, 100% 都是 "Report not found"**

根因: Docker eval 中 **patch apply failure** (从 `docker_eval.log` 确认), 包括:
- `malformed patch at line X`
- `patch unexpectedly ends in middle of line`
- `unexpected end of file in patch`

**Per-condition error 分布**:

| Cond | Errors | Err Instances | ALL-samples-errored |
|------|--------|---------------|---------------------|
| A1 | 79 | 19 | 8 |
| A2 | 112 | 20 | 12 |
| B | 130 | 24 | 14 |
| C | 122 | 21 | 14 |
| D | 126 | 23 | 12 |

**13 个 instance 在所有 5 个条件下全部失败** (系统性 patch apply failure):
django__django-{11276, 11815, 11964, 14404, 15098, 16136, 16560}, matplotlib__matplotlib-{22865, 25287}, mwaskom__seaborn-3069, pydata__xarray-4075, pytest-dev__pytest-5787, sphinx-doc__sphinx-9461

A1 error 最低 (26.8%) 因为 minimal prompt 下模型更倾向原样返回 patch (mean_similarity=0.937), diff 格式更规范。B/C/D 添加详细诊断后模型做更大幅度修改 (similarity 0.72-0.73), 生成更复杂的 diff, 格式出错概率更高。

---

## Q5: 输出文件清单

| Size | File |
|------|------|
| 9.3MB | `generated_repairs.jsonl` (combined, 1475 records) |
| 2.0MB | `generated_repairs_D.jsonl` |
| 2.0MB | `generated_repairs_B.jsonl` |
| 2.0MB | `generated_repairs_C.jsonl` |
| 1.9MB | `generated_repairs_A2.jsonl` |
| 1.4MB | `generated_repairs_A1.jsonl` |
| 915KB | **`eval_results.jsonl`** (Docker eval 结果, 非 verification_results.jsonl) |
| 170KB | `docker_eval.log` |
| 7.3KB | `generation_bcd.log` |
| 4.8KB | `generation.log` |
| 1.0KB | `analysis_summary.json` |

---

## 总结诊断

1. **标签映射正确**, B 使用了真实 CLS 预测 (非 random fallback)
2. **结果反直觉的根因是双重的**:
   - **Error rate 混淆**: 详细诊断 → 更大修改幅度 → 更高 patch apply failure rate (A1: 26.8% vs B: 44.1%)
   - **即使排除 error, A1 仍领先**: Qwen3-8B 在收到详细诊断后反而"过度修改", 引入新问题
3. **Oracle (C) ≈ Random (D)** 说明这个 8B 模型可能根本不会利用 per-test 标签信息, 无论准确与否
4. **13/44 instances 系统性 patch apply failure** 是噪声主因, 需要改进 diff 后处理或过滤

---
