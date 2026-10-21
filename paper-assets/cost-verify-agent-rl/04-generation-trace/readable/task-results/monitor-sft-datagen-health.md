# monitor sft datagen health

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_sft_datagen_health_20260524T081057_result.json`
- **Structured JSON:** [`6a59989cf053b34f8618.json`](../../sessions/6a/6a59989cf053b34f8618.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 健康检查报告

| 检查项 | 结果 |
|--------|------|
| **PID 110512（主进程）** | ALIVE — 运行 3h46m，CPU 36.1%，RSS 379MB |
| **PID 110513（Java backend）** | ALIVE — 运行 3h46m，CPU 62.4% |
| **输出文件** | `/root/autodl-tmp/expert_sft/` 有 2 个文件，但都是 **5月14日** 生成的旧文件（train 11.5MB, val 613KB），**本次运行未写入新文件** |
| **日志** | 2999 行，最新到 `train var 151`（score=100, steps=27）。日志在两次采样间**无增长** |
| **进度** | 已完成 151 个 variation，全部 score=100 |

## 判断：⚠️ CRITICAL — 疑似卡死

依据：
1. **日志停滞** — 两次读取间 log 行数不变（均为 2999 行），最后一条停在 var 151
2. **无新输出文件** — 输出目录文件时间戳为 5月14日，本次运行未产出任何新 jsonl
3. CPU 仍有占用（36%/62%），说明进程未崩溃但可能在某个 variation 上无限循环或等待响应

**可能原因**：var 152 的环境交互卡住（ScienceWorld Java 后端死锁或 API 调用超时无退出）。建议 kill 后排查 var 152 的具体 task，加 timeout 机制后重跑。

---
