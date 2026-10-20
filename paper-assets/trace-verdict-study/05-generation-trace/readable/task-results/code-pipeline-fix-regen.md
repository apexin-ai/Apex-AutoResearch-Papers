# code pipeline fix regen

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pipeline-fix-regen_20260514T171414_result.json`
- **Structured JSON:** [`71749462b06e0ac1dbd0.json`](../../sessions/71/71749462b06e0ac1dbd0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

VOTA 三级策略全部恢复工作。汇报如下：

---

## 修复汇报

### 1. Bug 修复内容

**Bug 1 (trace_worker.py — 帧过滤)**:
- `Tracer.__init__`: `self.target` → `self.targets`（set），接受 `{"&lt;solution>", "&lt;test>"}` 
- `Tracer.__call__`: `fname != self.target` → `fname not in self.targets`
- 每条事件新增 `source` 字段（`"test"` / `"solution"`）
- `test_tracer` 从 `Tracer("&lt;solution>")` 改为 `Tracer({"&lt;solution>", "&lt;test>"}, source_map)`

**Bug 2 (generate_data.py — 缺 test_code)**:
- 输出 JSON 新增 `"test_code": prob["test_code"]`

**Bug 3 (trace_worker.py — exception 格式)**:
- `entry["exception"] = str(arg[1])` → `entry["exception"] = {"type": type(arg[1]).__name__, "message": str(arg[1])}`

**assert_decompose 集成**: tracer 在 `event=="line"` 时查源码，若以 `assert ` 开头则调用 `AssertDecomposer.decompose()`，结果写入 `actual/expected/assert_match/assert_expression` 字段。MBPP 逐行编译时动态更新 `source_map`。

**vota.py 补丁**: 新增 Strategy 0 读取 event 顶层 `actual/expected`；assertion 提取过滤 `source=="test"` 避免 solution 帧行号误匹配。

### 2. 新数据统计

| 指标 | 值 |
|------|-----|
| 总样本数 | 5,910 |
| Pass | 3,958 (67.0%) |
| Fail | 0 (0.0%) |
| Error | 1,952 (33.0%) |
| 平均 trace 长度 | 106.7 行 |
| 文件大小 | 239.1 MB |
| 生成耗时 | 468.7s |

### 3. VOTA 验证结果（10 条样本）

| Sample | Verdict | Problem | Assertions | actual/expected | Exceptions | Loops | VOTA Ratio |
|--------|---------|---------|------------|-----------------|------------|-------|------------|
| 1 | PASS | HumanEval/0 | 8 | Yes | 0 | 9 | 26.8% |
| 2 | PASS | HumanEval/0 | 8 | Yes | 0 | 4 | 22.8% |
| 3 | PASS | HumanEval/1 | 6 | Yes | 0 | 6 | 15.3% |
| 4 | PASS | HumanEval/1 | 6 | Yes | 0 | 2 | 10.9% |
| 5 | PASS | HumanEval/1 | 6 | Yes | 0 | 5 | 11.3% |
| 6 | FAIL | HumanEval/2 | 1 | Yes | 0 | 0 | 83.3% |
| 7 | FAIL | HumanEval/2 | 1 | Yes | 0 | 0 | 83.5% |
| 8 | FAIL | HumanEval/6 | 3 | Yes | 2 | 3 | 57.9% |
| 9 | FAIL | HumanEval/6 | 3 | Yes | 2 | 3 | 58.3% |
| 10 | FAIL | HumanEval/6 | 3 | Yes | 2 | 3 | 57.9% |

FAIL 样本的 assertion snapshots 正确展示了错误的 actual vs expected（如 `actual=[1, 2, 0, 2], expected=[2, 3, 1, 3], match=False`），exception summaries 正确显示 `[ERROR] AssertionError at line X`。

### 4. 压缩比

- **Overall VOTA/Full ratio: 26.67%**
- **Compression factor: 3.7x**
- Full trace: 347,347 chars → VOTA: 92,646 chars

---
