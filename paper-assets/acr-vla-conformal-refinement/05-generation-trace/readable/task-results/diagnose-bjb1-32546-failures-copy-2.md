# diagnose bjb1 32546 failures

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bjb1-32546-failures_20260526T092847_result.json`
- **Structured JSON:** [`0aef3449165b4506d0e9.json`](../../sessions/0a/0aef3449165b4506d0e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 根因：**监控误报（false alarm）**

所有 6 个实验**没有失败**。实际状态：

| 实验 | GPU | 状态 | 结果 |
|------|-----|------|------|
| goal-s42 | 0 | **已完成** | 83.5% (167/200) |
| goal-s43 | 1 | **运行中** | 正在跑最后一个 task (wine_bottle_on_rack 15/20) |
| goal-s44 | 2 | **已完成** | 83.0% (166/200) |
| object-s42 | 3 | **运行中** | chocolate_pudding 15/20 |
| object-s43 | 4 | **运行中** | chocolate_pudding 5/20 |
| object-s44 | 5 | **运行中** | chocolate_pudding 15/20 |

### 误报原因

监控系统以 "sentinel file + W&B run" 作为进程存活判据，但这批 π0.5 eval 脚本**两者都不产生**：
- `logs/sentinels/` 目录为空（自 5/17 起就没有新文件）
- 脚本通过 `tee` 写日志 + JSON 输出，未集成 W&B
- 监控连续 5 次未检测到 sentinel/W&B，判定为 "process dead"

### 服务器健康状态

- **GPU**: 6× RTX 4090，全部正常，无 ECC 错误
- **磁盘**: 根分区 34% 使用（20GB 可用），充裕
- **内存**: 1TB 总量，62GB 使用，无 OOM 风险
- **进程**: 4 个 python 进程活跃（PID 600104/600978/601242/601320），CPU 使用 228-236%

### 结论

- **不需要重跑**。2 个已完成（JSON 已写入），4 个正在跑，预计数小时内全部完成
- **建议修复**：eval 脚本启动时应写 sentinel file（如 `touch logs/sentinels/{job_name}.started`），避免监控误报

---
