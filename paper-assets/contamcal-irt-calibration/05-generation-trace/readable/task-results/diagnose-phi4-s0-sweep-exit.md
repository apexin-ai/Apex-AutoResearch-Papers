# diagnose phi4 s0 sweep exit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_phi4-s0-sweep-exit_20260520T052403_result.json`
- **Structured JSON:** [`7ffabefaabdc49166964.json`](../../sessions/7f/7ffabefaabdc49166964.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结果：

**Sweep 仍在正常运行，不需要更新 registry。**

| 项目 | 状态 |
|------|------|
| **当前进程** | PID 286341，GPU 0，训练 d005 (100/3177 steps, 3%) |
| **参数确认** | lora_alpha=32, lr=5e-5 ✓ |
| **d000** | ✅ 完成 — 有 final adapter + checkpoint-3125 |
| **d005** | 🔄 训练中 (3%, ETA ~2h) |
| **d025/d050/d100** | ⏳ 待训练 |
| **进度** | 1/5 完成，2/5 进行中 |

Cron 报告的"进程退出"是 d000 子进程正常结束，sweep 脚本已自动切换到 d005。

**westd GPU 状态**：
- GPU 0: 占用 (phi-4 d005 sweep)
- GPU 1: 空闲
- GPU 2: 占用 (PID 280811, 66.7GB)
- GPU 3: 空闲

---
