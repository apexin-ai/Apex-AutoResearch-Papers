# fix mvp c2 configs

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_mvp_c2_configs_20260518T175948_result.json`
- **Structured JSON:** [`d449a23781b8c4862501.json`](../../sessions/d4/d449a23781b8c4862501.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**根因**：配置文件存在但文件名不匹配。`mvp_c2_s42` 提交时引用了 `condition2_position_reset.yaml`，实际文件名为 `condition2_pos_reset.yaml`。

**修复**：创建了两个符号链接：
- `condition2_position_reset.yaml` → `condition2_pos_reset.yaml`
- `condition3_bridge_standard_pos.yaml` → `condition3_bridge_standard.yaml`

**4 个条件配置内容确认正确**：

| 条件 | `use_bridge_tokens` | `use_position_reset` | `num_bridge_tokens` |
|------|---------------------|---------------------|---------------------|
| C1 (lora_only) | false | false | 0 |
| C2 (pos_reset) | false | **true** | 0 |
| C3 (bridge_standard) | **true** | false | **4** |
| C4 (full_tbab) | **true** | **true** | **4** |

两个符号链接文件均可被 Python yaml.safe_load 正常加载。`mvp_c2_s42` 可以重新提交。

---
