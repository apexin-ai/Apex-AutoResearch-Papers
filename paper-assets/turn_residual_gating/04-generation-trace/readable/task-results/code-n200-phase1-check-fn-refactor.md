# code n200 phase1 check fn refactor

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_n200_phase1_check_fn_refactor_20260522T103830_result.json`
- **Structured JSON:** [`968f936fd8784852bed4.json`](../../sessions/96/968f936fd8784852bed4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**修改内容** (`src/eval_instruction_retention.py`, 从 514 行 → 682 行)：

1. **新增 16 个工厂函数**（`make_starts_with`, `make_ends_with`, `make_contains`, `make_not_contains_word`, `make_not_contains_char`, `make_count_sentences`, `make_count_words`, `make_count_paragraphs`, `make_count_emoji`, `make_regex_match`, `make_format_bullet_points`, `make_format_numbered_list`, `make_all_caps`, `make_all_lowercase`, `make_no_contractions`, `make_compound`）

2. **新增 `CHECK_FACTORIES` 注册表** — 映射 `check_type` 字符串到工厂函数

3. **新增 `resolve_check_fn()`** — 优先查 `CHECK_FNS`（旧格式），回退到 `CHECK_FACTORIES`（新格式），支持 `compound` 组合

4. **3 处调用点替换**：
   - L319: `evaluate_prompt` 中的 check_fn 解析
   - L345: record 中的 `check_fn` key 兼容新格式
   - L570: main 中的验证逻辑

**验证结果**：
- 18 个旧格式 prompt 全部正确 resolve
- 3 个新格式测试 prompt（starts_with / not_contains_word / compound）断言全通过
- 测试文件已写入 `data/test_parametric_prompts.json`

---
