# data val sweep compilation audit

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_val-sweep-compilation-audit_20260515T081714_result.json`
- **Structured JSON:** [`7dedf076f632f3077314.json`](../../sessions/7d/7dedf076f632f3077314.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计结果

### 已完整（无需修改）
| 数据组 | 检查点数 | 状态 |
|--------|---------|------|
| 8B s42 val@8192 | 8/8 | ✅ 全部准确 |
| 8B s42 test@8192 | 7/7 | ✅ 全部准确 |
| seed123 val@8192 | 5/5 | ✅ 含 ckpt-6633 ⏳running |
| 4B v5 val@5120 | 5/5 | ✅ 全部准确 |
| 4B v5 test@5120 | 2/2 | ✅ 全部准确 |

### 已修正
| 问题 | 修正内容 |
|------|---------|
| seed123 test ckpt-3000 | ⏳running → **85.60%** |
| Summary 表缺行 | 新增 `8B seed123 test@8192 (val-selected) ckpt-3000 85.60%` |
| JSON 缺 `8b_seed123_test8192` | 新增完整数据块 |
| JSON 缺 `4b_v5_test5120` | 新增完整数据块（原主文件 JSON 已有表格但 JSON 段遗漏） |
| 报告副本严重过时 | 整体同步为最新版 |

### 仍为 ⏳running（非本次审计范围）
- seed123 val ckpt-6633

---
