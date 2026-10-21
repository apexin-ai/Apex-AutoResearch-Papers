# research 3B para aligned gap check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_3B_para_aligned_gap_check_20260515T153248_result.json`
- **Structured JSON:** [`e78b26edbc9287e6c586.json`](../../sessions/e7/e78b26edbc9287e6c586.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 3B s42 para_aligned eval 完整性汇总

**当前命名（无 v2/v3）的 para_aligned 结果：**

| Dose | 目录 | 状态 |
|------|------|------|
| d000 | `Qwen2.5-3B_d000_s42_para_aligned` | ✅ 完成（.done + 3 文件，23:28） |
| d005 | `Qwen2.5-3B_d005_s42_para_aligned` | ⚠️ 3 个结果文件齐全（~1.9MB），但**无 .done 标记** |
| d025 | — | ❌ **不存在** |
| d100 | `Qwen2.5-3B_d100_s42_para_aligned` | ✅ 完成（.done + 3 文件，23:27） |

**注意：** `Qwen2.5-3B_d025_v2_s42_para_aligned` 存在且完整（.done），但这是 v2 版本，不是当前命名。

**SFT checkpoint 可用性：**
- `Qwen2.5-3B_d025_s42/lora_adapter` ✅ 存在，可直接用于 eval

**结论：**
- **缺 1 个条件：d025 para_aligned**
- d005 文件齐全但缺 .done，需确认是否要重跑或补 .done
- d025 checkpoint 就绪，可立即在 cuda:4 或 cuda:5 上提交 `Qwen2.5-3B_d025_s42_para_aligned` eval

---
