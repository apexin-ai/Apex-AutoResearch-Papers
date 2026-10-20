# ops phase3 sft readiness v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_phase3-sft-readiness-v2_20260514T025400_result.json`
- **Structured JSON:** [`e64b702b0f7721927bc3.json`](../../sessions/e6/e64b702b0f7721927bc3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

检查完成，结果汇总：

### 就绪状态

| 检查项 | 结果 |
|--------|------|
| Dosage 数据 (d005/025/050/100) | ✅ 全部存在 (50826/54133/58266/66533 行) |
| 基础模型 (0.5B/1.5B/3B) | ✅ 全部存在 |
| 0.5B d005 checkpoint | ✅ |
| 0.5B d100 checkpoint | ✅ |
| 1.5B d100 | 🏃 GPU 0 仍在训练 (PID 251924, lora_adapter 为空) |

### GPU 现状
所有 6 GPU 均在使用中：GPU 0 跑 1.5B d100 SFT，GPU 1-5 跑各种 eval jobs。

### 修正
- 脚本实际参数用 **hyphen 格式**：`--model-name`、`--data-path`、`--batch-size`、`--grad-accum`、`--lr`、`--epochs`（非 underscore）
- 待做 SFT 实际是 **9 jobs**（用户列表里 1.5B d100 虽有 checkpoint 目录但尚未完成，仍在训练）

完整的 9 条 submit command 已保存到 `memory.md` 的 "Phase 3 SFT 提交计划" section。

---
