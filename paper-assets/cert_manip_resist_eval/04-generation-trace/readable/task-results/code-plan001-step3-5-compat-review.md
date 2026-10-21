# code plan001 step3 5 compat review

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan001-step3-5-compat-review_20260522T103145_result.json`
- **Structured JSON:** [`b0a9793311ed390b6f86.json`](../../sessions/b0/b0a9793311ed390b6f86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有依赖就绪。

## 审查总结

**兼容性状态：全部通过（1 个 bug 已修复）**

### 发现并修复的问题

`scripts/run_plan001_confound_diagnosis.py` — `load_local_individual_asr()` 未对 `position_bias` 攻击分数执行 A↔B 反转。position_bias 攻击交换了 response_a/b，checkpoint 中存储的是原始模型输出，需要反转 winner 才能与原始 ground_truth 正确比较。已添加 `_invert_winners()` 并在 `attack == "position_bias"` 时调用。（Step 4/5 已有此逻辑，仅 confound diagnosis 遗漏。API 模型不受影响，因为直接读取预计算 ASR。）

### 验证通过项

- 文件名双下划线格式 `{model}__{ds}__{condition}.json` — 一致 ✓
- JSON 字段（`scores`, `winner`, `asr`, `ground_truth_winner`）— 一致 ✓
- 15 个 model ID — 一致 ✓
- 6 个攻击名 — 一致 ✓
- 本地/API 数据源分离读取逻辑 — 正确 ✓
- 所有 Python 依赖 — 已安装 ✓
- 数据流端到端测试（7 项）— 全部通过 ✓

### 当前状态

- 已完成：claude-3-haiku（全部条件）、gpt-4o（部分条件）
- 未完成：7 个 API 模型仍在运行
- Step 3-5 脚本支持优雅降级（跳过缺失模型的 panel）

### 产出

- 修复：`scripts/run_plan001_confound_diagnosis.py`（服务器 + 本地）
- 新增：`scripts/run_plan001_pipeline.sh`（服务器 + 本地）

---
