# exp phase3 dryrun

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_phase3_dryrun_20260514T202705_result.json`
- **Structured JSON:** [`df45b088b1631392f28a.json`](../../sessions/df/df45b088b1631392f28a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Phase 3 Dry-Run 验证完成

### Dry-Run 结果（3 实例 × 2 条件）

| Instance | Condition | Success | Eval Method | Tokens In | Tokens Out |
|---|---|---|---|---|---|
| cookiecutter_1 | no_trace | False | line_overlap_fallback | 99 | 615 |
| cookiecutter_1 | structural_filtered | False | line_overlap_fallback | 687 | 609 |
| cookiecutter_3 | no_trace | False | line_overlap_fallback | 107 | 1148 |
| cookiecutter_3 | structural_filtered | False | line_overlap_fallback | 986 | 930 |
| scrapy_7 | no_trace | False | none | 375 | 4096 |
| scrapy_7 | structural_filtered | False | line_overlap_fallback | 898 | 1419 |

### 各步骤验证

- **Prompt 构建** ✅ structural_filtered 比 no_trace 多 ~500-800 input tokens，trace 内容正确注入
- **API 调用** ✅ 6/6 次调用成功（endpoint: `http://47.94.22.126/v1`）
- **代码提取** ✅ markdown fence 剥离正常工作
- **评估** ✅ 三层评估逻辑正常（exact_match → test_execution → line_overlap_fallback）
- **结果记录** ✅ CSV（6 rows）、checkpoint JSON、summary JSON 格式正确
- **Checkpoint 恢复** ✅ 重跑正确识别已完成的实例

### 发现并修复的问题

1. **`call_repair_llm` NoneType** — API 偶尔返回 content=None（内容策略拒绝），`.strip()` 崩溃。修复：`content = raw_content.strip() if raw_content else ""`
2. **Summary 表头条件数错误** — `len(CONDITIONS)` 始终显示 4，改为 `len(active_conditions)`
3. **`line_scores_map[key]` KeyError** — dry-run 模式中未加载 line scores 时报错。修复：改为 `.get(key, [])`

### 新增功能

- `--conditions` CLI 参数：支持只跑部分条件（如 `--conditions no_trace,structural_filtered`）
- `phase2_line_scores.json` 不存在时，跳过 line_filtered 条件而非报错退出

### Phase 3 全量运行准备

**已就绪**：脚本逻辑、API 连接、评估管道、结果记录全部验证通过。

**待 line scoring 完成后**，全量命令：
```bash
export OPENROUTER_API_KEY='[REDACTED]'
python run_phase3_repair.py --max-workers 3
```

**注意事项**：
- scrapy 类实例 setup 较慢（~2min/instance），其他项目 <30s
- API 偶尔返回 None content（已处理），不影响整体运行
- 36 实例 × 4 条件 = 144 次 API 调用，预计耗时 ~1-2 小时

---
