# monitor m1 progress check2

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_m1_progress_check2_20260512T212517_result.json`
- **Structured JSON:** [`4e57841f0a919f6f02d4.json`](../../sessions/4e/4e57841f0a919f6f02d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## M1 提取进度报告

### 1. 进程状态：**RUNNING**
- PID 577864，已运行 **37 分 31 秒**
- CPU 0.0%（快照瞬时值，日志显示 05:25 仍有活跃输出）

### 2. 已处理 repo 数：**12 / 131**（+ 1 个 skip）
已输出 JSON 的 12 个 repo：
`Cog-Creators__Red-DiscordBot`, `Suor__funcy`, `agronholm__typeguard`, `bottlepy__bottle`, `cknd__stackprinter`, `jd__tenacity`, `madzak__python-json-logger`, `oauthlib__oauthlib`, `pudo__dataset`, `pygments__pygments`, `pytest-dev__iniconfig`, `seatgeek__thefuzz`

跳过 1 个 repo：`pdfminer__pdfminer.six`（660 个 instance 全部 clone_failed）

### 3. Instance 数
- 已完成提取：**865** 个 JSON 文件
- 已跳过：**660** 个（clone_failed）
- 合计已处理：**1,525 / 50,869**（3.0%）

### 4. 速度与预估
- ~37 分钟处理 865 个 instance → **~23 instance/min**
- 剩余 ~49,344 instance → 预估 **~35.7 小时**
- 注意：当前处理的是小型 repo，后续大型 repo（如 scikit-learn、django 等）CodeQL 分析时间会显著增加，实际可能更久

### 5. 磁盘
- 产出目录：195MB（865 个 JSON）
- `/root/autodl-tmp/`：92G / 169G 已用（**54%**），剩余 78G，充裕

### 6. 异常
- `pdfminer__pdfminer.six` 全部 660 个 instance clone_failed — 可能是 repo URL 失效或网络问题
- 日志路径在 `/tmp/m1_extraction.log` 而非任务描述中的 `/root/structfuse/data/m1_extraction/`，数据实际写在 `/root/autodl-tmp/structfuse/m1_extraction/`
- 进程 CPU 瞬时为 0，但日志持续更新，正常运行中

---
