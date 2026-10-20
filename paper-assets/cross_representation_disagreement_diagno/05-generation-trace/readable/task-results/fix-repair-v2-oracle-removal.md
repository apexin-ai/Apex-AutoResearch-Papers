# fix repair v2 oracle removal

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_repair_v2_oracle_removal_20260515T072024_result.json`
- **Structured JSON:** [`15aa005b9507fdf7172b.json`](../../sessions/15/15aa005b9507fdf7172b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。汇总：

### 改动对比

**repair.py 行 105-106**（函数签名）：
- 改前：`ground_truth: str,` 后直接是 `max_rounds: int = MAX_REPAIR_ROUNDS,`
- 改后：插入 `predicted_error_side: Optional[str] = None,`

**repair.py 行 109-113**（策略分支条件）：
- 改前：`if other_verdict != ground_truth:` — oracle，依赖推理时不可用的 GT
- 改后：`if predicted_error_side in ("both", "ambiguous", None):` — GT-free，用 stability check 的预测结果

**pipeline.py / repair_only.py**（4 个调用点）：
- 改前：无 `predicted_error_side` 参数
- 改后：新增 `predicted_error_side=rec.get("stability", {}).get("predicted_error_side")`

### 验证结果
- 三个文件语法检查通过
- `from repair import *` 导入正常
- `grep ground_truth src/repair.py` 仅出现在：参数声明（L105）、blind_regeneration 透传（L114）、最终成功判断 `ex.verdict == ground_truth`（L149, L202）。**无 ground_truth 出现在策略路由条件中**。
- (b) overcorrection fallback 未动，保持原样。

---
