# diagnose pi05 fix3 status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_pi05-fix3-status_20260521T045609_result.json`
- **Structured JSON:** [`3ebc977ee76644789f28.json`](../../sessions/3e/3ebc977ee76644789f28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

**进程**: ✅ PID 831620 存活，cuda:0 13.5GB，已跑 15:56

**进度**: 1/10 tasks 完成（alphabet_soup: **0/5 = 0.0%**），其余 9 task 进行中

**fix3 修复效果**: 
- ✅ vision tower 437 keys 重命名成功（`[pi05] Fixed 437 vision tower keys`），模型加载无报错
- ❌ **没有 SR > 0% 信号**，第一个 task 仍是 0%，与之前全量评测 0/200 趋势一致

**日志**: `/tmp/eval_pi05_quicktest.log`（33 行，无 ERROR/OOM）

**其他 π0.5 进程**: 仅 831619/831620，无并发任务

**预估**: ~2h 后跑完全部 50 rollouts。fix3 路径下权重已正确加载但仍 0% SR，说明问题不在 key 名映射，可能在 tensor shape/layout 或 action head 解码

详细分析已写入 `artifacts/pi05_fix3_status_check.md`

---
