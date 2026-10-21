# ssh n32 verify and fix restart

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_n32_verify_and_fix_restart_20260522T161351_result.json`
- **Structured JSON:** [`f1c58dac7c68ecdbff56.json`](../../sessions/f1/f1c58dac7c68ecdbff56.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

新进程已正常启动并运行。

## 汇报

| 项目 | 状态 |
|------|------|
| **PID 387768**（旧 N=32） | 已死，无需操作 |
| **PID 155692**（v2） | 已 kill — 启动于 `23:52:42`，sampling.py 修复于 `23:53:52`，进程加载了旧代码 |
| **sampling.py fix** | 已确认：L671 `open(..., errors="replace")` + L686 同样修复 |
| **新进程** | PID **157469**（VLLM::EngineCore），GPU 3，29834MiB，tmux session `exp_fewnerd_pretrained_n32_s42_v2` |
| **当前状态** | 模型加载完成，正在 Rendering prompts（37648 条，~9% at ~414 it/s），预计约 1.5 分钟完成 prompt 渲染 |
| **代码确认** | 新进程在 sampling.py 修复后启动，加载的是修复版代码 |

---
