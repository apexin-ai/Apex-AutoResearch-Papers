# ssh fix diversity monitor

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-diversity-monitor_20260515T014729_result.json`
- **Structured JSON:** [`d3600763ca70fc82a673.json`](../../sessions/d3/d3600763ca70fc82a673.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

39/39 tests passed.

修复完成。变更总结：

**`training/diversity_analysis.py`** — 核心 bug 修复：
- 原版用 `json.loads(output)` 重新解析模型原始输出文本。~9% 的 truncated 输出虽然被 `parse_model_output` 的 repair 逻辑正确解析（存入 `parsed_triples`），但 `json.loads` 直接失败导致这些 generation 被跳过
- 改为直接使用 JSONL 记录中的 `parsed_triples` 字段
- `normalize_triple` 增加了 `.get()` 安全访问和 `str()` 类型转换，与 `diversity_metrics.py` 保持一致
- 不再跳过任何 generation（包括空输出的），所有 N 个 generation 都参与 diversity 计算

**`training/rsft_generate.py`** — 已经使用 `build_triple_set` 和 `len(generations)`（之前已修复）

**`tests/test_diversity.py`** — 16 个测试覆盖：
- 8 个完全不同输出 → diversity=8
- 8 个完全相同输出 → diversity=1
- 混合情况（部分重复、空输出混入）
- JSON key 顺序不同但内容相同 → 视为相同
- 大小写/空白不敏感
- triple 顺序不影响 set 比较
- `compute_diversity_from_file` 端到端测试

---
