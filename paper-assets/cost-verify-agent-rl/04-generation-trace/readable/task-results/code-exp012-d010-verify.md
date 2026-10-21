# code exp012 d010 verify

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp012-d010-verify_20260514T062706_result.json`
- **Structured JSON:** [`c7bd46c4a28fa4c587e9.json`](../../sessions/c7/c7bd46c4a28fa4c587e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过。

## 检查结果

| 项目 | 修复前 | 修复后 |
|------|--------|--------|
| env.py reward | D007 valid-action bonus (0.1) | **已恢复** → 二值 `score * won` |
| format_penalty | `-0.01` | **已修改** → `0` |
| group_size | 16 | ✓ 无需改 |
| resume_from_path | exp008 step 5 | ✓ 无需改 |
| es_manager.py | 从 config 读取 format_penalty | ✓ 无需改 |

**两项修复已完成：**
1. `env.py` — git checkout 恢复为原始二值 reward（won=10.0, else=0）
2. config — `format_penalty` 从 `-0.01` 改为 `0`

exp012 配置现在符合 D010 指令（纯 A2：去 format_penalty + 加大 group_size），可以提交启动。

---
