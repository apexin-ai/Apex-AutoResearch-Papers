# code d023 llm original type

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d023_llm_original_type_20260512T193704_result.json`
- **Structured JSON:** [`9b2a9437bed214371655.json`](../../sessions/9b/9b2a9437bed214371655.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

v5 数据 dry-run 也跑通了。P1 GATE 显示 FAIL 是因为 action 组 N=0（v5 数据没有 correction_span ≤ 3 的轨迹），导致 ordinal 检查返回 None — 这是符合预期的数据特征，不是代码问题。

代码修改完成，总结已做的变更：

**classify_errors.py 修改内容（650 → 728 行）：**

1. **`llm_original_type` 字段**：每条输出记录新增 `llm_original_type` 和 `llm_original_type_source`
   - Full run: PCB 轨迹保存 LLM 原始分类结果（`source="llm"`），再 override `error_type` 为 verification
   - Dry-run: PCB 用 rule-based 分类做代理（`source="rule-based"`）

2. **`run_dual_analysis` 重写**：三版 KW + P1 gate 判定
   - `with_override`: PCB → verification（现有逻辑）
   - `without_override`: 用 `llm_original_type` 分组
   - `pcb_excluded`: 排除 PCB 轨迹
   - 每版都做 Full + Deduplicated 子分析
   - P1 pass 条件：`with_override` 显著 **且** （`without_override` 或 `pcb_excluded` 显著），三组均需 ordinal = True

3. **保留原有功能**：task-type stratified 分析、dedup 逻辑、JSON 输出格式均兼容

**不需要单独创建 `analyze_correction_span.py`** — 分析逻辑已内嵌在 `run_dual_analysis` 中。

---
