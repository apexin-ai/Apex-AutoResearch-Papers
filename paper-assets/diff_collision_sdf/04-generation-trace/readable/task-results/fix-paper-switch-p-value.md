# fix paper switch p value

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_paper_switch_p_value_20260527T205649_result.json`
- **Structured JSON:** [`0ee324cb5cab5bf2d528.json`](../../sessions/0e/0ee324cb5cab5bf2d528.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。汇报如下：

### 修改内容

**3 处修改**（文件：`artifacts/paper_switch.py`）：

| 行号 | 修改 |
|------|------|
| 411-412 | `v` 字典：`p_value` 从 `p_one` 改为 `p_two`（双尾），新增 `p_one_value`（单尾） |
| 263-267 | Scenario C dose-response 段落：在 `$p = {p_value}$` 后添加 `\footnote{}`，含单尾 p + directional prior 说明 |
| 287-290 | Scenario B dose-response 段落：同上添加脚注，说明即使用单尾检验仍不显著 |
| 424-425 | 修复打印输出：`p_one` 行打印 `p_one_value`，`p_two` 行打印 `p_value` |

### p 值结果

| 输入 | Scenario | p_one（脚注） | p_two（正文） |
|------|----------|--------------|--------------|
| s2=58 | C | 0.012 | 0.036 |
| s2=55 | B | 0.071 | 0.155 |

### 逻辑确认

- Scenario 判定仍用 `p_one < 0.05`（未改动）
- 正文所有 `{p_value}` 位置输出双尾 p（保守值）
- 脚注仅在 dose-response 段落出现，包含单尾 p + directional prior 说明
- `--dry-run` 功能不受影响

---
