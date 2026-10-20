# code openhands lf fix

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_openhands_lf_fix_20260514T104722_result.json`
- **Structured JSON:** [`ec7704d7941e609a056e.json`](../../sessions/ec/ec7704d7941e609a056e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复成功。覆盖率对比：

| LF | 修复前 | 修复后 |
|---|---|---|
| **file_diff_delta** | 0.58% (903/154743) | **42.1%** (65096/154743) |
| **command_repetition** | 92.2% (不变) | **92.2%** (不变) |
| **outcome_backpropagation** | 6.5% (10000/154743) | **19.8%** (30612/154743) |

### 详细分布变化

**file_diff_delta**:
- 修复前：abstain=153840, stagnation=903, progress=0
- 修复后：abstain=89647, **stagnation=27517**, **progress=37579**
- 现在能正确检测 OpenHands 的 `str_replace`/`create`/`insert` 编辑操作

**outcome_backpropagation**:
- 修复前：abstain=144743, progress=4810, stagnation=5190
- 修复后：abstain=124131, progress=4636, **stagnation=25976**
- 新增覆盖来自 434 条 max-iteration 和 14 条 AgentStuckInLoop 轨迹（~448 轨迹 × ~31 windows ≈ 20612 新增 stagnation）

**majority_label 分布变化**:
- 修复前：progress=133667, stagnation=9390, abstain=11686
- 修复后：progress=119212, **stagnation=31440**, abstain=4091
- stagnation 标签从 6.1% 增加到 **20.3%**，标签多样性大幅改善，不再退化为 command_repetition 单一 LF 主导

### 修改内容

`labeling_functions.py` 三处改动：
1. `SEARCH_CMDS` 增加 `view`（OpenHands 的文件查看命令）
2. `_extract_edited_files` 增加 `str_replace`/`create`/`insert` 检测及路径提取
3. `lf_outcome_backpropagation` 的 exit_status 检查扩展为匹配 `maximum iteration`、`AgentStuckInLoop`、`Timeout`

---
