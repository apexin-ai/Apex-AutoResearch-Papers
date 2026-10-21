# diag exp 064 extraction check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp-064-extraction-check_20260519T113500_result.json`
- **Structured JSON:** [`7ad921337afe7fbe0b30.json`](../../sessions/7a/7ad921337afe7fbe0b30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

### 当前状态
- **进度**: 60/204 (29.4%)，已跑 164 min，ETA ~394 min (~6.5h)
- **SICA**: 80.0%, **SC**: 80.0% (两者一致)
- **extraction_rate**: 40.3% (290/720 traces)

### 根因：`&lt;think>` 标签污染 extraction 输入

通过实际测试验证：

1. **当 extraction prompt 的输入 trace 含 `&lt;think>` 标签时**，DeepSeek-R1-Qwen3-8B 行为完全崩坏，输出不相关内容（测试中输出了 Tower of Hanoi 解答）。这是因为 `&lt;think>` 是该模型的特殊控制 token，出现在输入中时会破坏 chat template 的解析。

2. **当输入不含 `&lt;think>` 标签时**，模型能进入正常的 thinking + JSON 输出流程，`_strip_thinking` 可以正确处理。

3. **代码中 `_strip_thinking` 只处理 extraction 模型的输出**（line 330），**不处理输入 trace**。pipeline 把 DeepSeek-R1 的原始 trace（含 `&lt;think>...&lt;/think>` 占 trace 80-95% 长度）原样塞进 extraction prompt。

4. 40% 的成功率来自模型偶尔在混乱输入下仍产出可解析 JSON 的随机性。

### 能否修复到 >80%？

**可以**，修改方案：

**方案 A（推荐）**：在 `_build_prompt` 中 strip 输入 trace 的 `&lt;think>...&lt;/think>` 标签（保留 thinking 内容，只去标签），或只保留 `&lt;/think>` 后的 summary 部分。两种方式都能消除 `&lt;think>` 标签对模型的干扰。

**方案 B**：用 port 8001 的 Qwen3-14B（已禁用 thinking）或 port 8003 的 Llama-3.1-8B 做 extraction。但这需要改 pipeline 支持 trace 和 extraction 用不同 endpoint。

### 建议

**不建议 kill**。当前 SICA/SC = 80% 是有价值的数据点。但 extraction_rate 40% 意味着 SICA 没有充分利用 constraint 信号，accuracy 有提升空间。

- 可以让当前 run 跑完（ETA ~6.5h），之后用修复后的 extraction pipeline **re-extract**（代码中已有 `reextract_v3.py`），无需重跑 trace generation
- 或者 kill 后修复代码再重跑，但考虑到 trace generation 是大头耗时，re-extract 更高效

---
