# monitor datagen progress check

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_datagen-progress-check_20260519T162448_result.json`
- **Structured JSON:** [`05e6704e9cc4819e510d.json`](../../sessions/05/05e6704e9cc4819e510d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个任务全部正常运行，汇总如下：

| GPU | 任务 | 进度 | 状态 | 预估剩余 |
|-----|------|------|------|----------|
| 0 | exp16 Llama jailbreak | **125/250** (50%) | ✅ 运行中 (89% GPU) | ~110 min |
| 1 | exp16 Llama benign | **72/250** (29%) | ✅ 运行中 (90% GPU) | ~208 min |
| 2 | exp17 Qwen jailbreak | **46/250** (18%) | ✅ 运行中 (88% GPU) | ~243 min |
| 3 | exp17 Qwen benign | **32/250** (13%) | ✅ 运行中 (87% GPU) | ~368 min |

**说明：**
- Llama jailbreak 的 jsonl 文件只有 2 行（脚本可能攒批写入），但日志显示已处理到 125 条
- Llama benign 的 jsonl 有 72 行，与日志进度一致（实时写入）
- Qwen 两个任务数据写入 `.progress` 文件，最终 `.jsonl` 在全部完成后生成
- Qwen benign 每条耗时较长（turn 数多，15-27 turns vs Llama 的 5-12 turns），预估 ~6 小时完成
- 无错误日志，4 个进程全部活跃

---
