# code bugfix cliff and gate

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bugfix-cliff-and-gate_20260513T231939_result.json`
- **Structured JSON:** [`c976c6ab24c70109e145.json`](../../sessions/c9/c976c6ab24c70109e145.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 bug 均已修复并验证通过。

---

### 产出报告

**Bug 1: cliff_test.py cliff detection 使用 `abs()` 的语义错误**

- **根因**: 第 171 行 `is_cliff = abs(delta) > self.baseline_ppl * 0.1` 和第 178 行 `cliff_count` 计算都使用了 `abs()`，会把 PPL 大幅**下降**的 head 也误判为 cliff。但 cliff 定义是 ">10% PPL increase"（仅增加方向）。
- **修复**: 移除两处 `abs()`，改为 `delta > self.baseline_ppl * 0.1` 和 `r["ppl_delta"] > self.baseline_ppl * 0.1`。
- **数据验证**: 当前 1.5B 数据中无大幅负 delta，cliff_count 碰巧正确（2-bit=2, 4-bit=1, 8-bit=0），无需更新 JSON。

**Bug 2: run_mvp.py 缺少 PPL > 3× baseline 过滤**

- **修复位置**: run_mvp.py 第 177-215 行（summary 区域）
- **逻辑**: 对 full MCKP、quant-only、uniform 4-bit 的 PPL 分别检查是否 > 3× baseline_ppl。任一超标则：
  - 表格中标注 `[COLLAPSE]`
  - 输出 `FAIL (分配导致 PPL 崩溃)`
  - Overall 判定纳入 `not ppl_collapsed` 条件

---
