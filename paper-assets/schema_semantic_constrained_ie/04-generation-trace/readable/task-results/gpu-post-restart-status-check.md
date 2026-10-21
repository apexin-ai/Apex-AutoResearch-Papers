# gpu post restart status check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_post_restart_status_check_20260520T032503_result.json`
- **Structured JSON:** [`94b12db02457a6fbdb57.json`](../../sessions/94/94b12db02457a6fbdb57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### westd-16980

| GPU | 任务 | PID | 进度 | 预计完成 |
|-----|------|-----|------|----------|
| GPU0 | LLaMA greedy **unc** 4096 | 697390 | **461/998** (46%) | ~13:33 CST |
| GPU1 | LLaMA greedy **con** 4096 | 698086 | **421/998** (42%) | ~13:53 CST |

**Watcher sessions (均存活)**:
- `d065_watcher` (PID 716653) — 监控 LLaMA 两进程，结束后启动 Qwen con
- `d066_qwen_beam_sweep` (PID 712981) — 等 LLaMA unc 结束后启动 Qwen DocRED beam sweep

**d066 已完成文件 (16980)**:
- `qwen_docred_200_greedy_s1.jsonl` — 200/200 ✅
- `qwen_docred_200_greedy_unc.jsonl` — 200/200 ✅

---

### westd-21461

| GPU | 任务 | PID | 进度 | 预计完成 |
|-----|------|-----|------|----------|
| GPU0 | Qwen greedy **unc** 4096 | 167691 | **36/998** (3.6%) | ~16:20 CST |
| GPU1 | d066 SciERC beam8 **con** | 165391 | **290/551** (53%) | ~11:47 CST |

**Watcher sessions (均存活)**:
- `d065_qwen_greedy` (PID 167684) — 运行 Qwen unc，完后自动启动 con
- `d065_block_con` (PID 169446) — 监控 Qwen unc，结束后 kill 自动启动的 con（按设计）

**d066 SciERC beam sweep 完成情况 (21461)**:
| Config | unc | con |
|--------|-----|-----|
| beam1 | 551/551 ✅ | 551/551 ✅ |
| beam2 | 551/551 ✅ | 551/551 ✅ |
| beam4 | 551/551 ✅ | 551/551 ✅ |
| beam8 | 551/551 ✅ | **290/551** 🔄 |

---

### 总结

所有进程在主 Agent 重启期间**正常运行**，无异常。watcher 脚本均存活且正确等待。d066 SciERC beam sweep 只剩 beam8 con 约 20 分钟完成。16980 上 LLaMA 两任务约 2-2.5 小时后完成，之后 watcher 会自动触发 Qwen con 和 d066 beam sweep。21461 的 Qwen unc 刚启动，约 5 小时完成。

---
