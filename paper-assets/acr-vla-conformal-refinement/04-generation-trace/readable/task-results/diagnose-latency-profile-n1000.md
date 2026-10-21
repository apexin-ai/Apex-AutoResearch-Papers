# diagnose latency profile n1000

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_latency-profile-n1000_20260520T081949_result.json`
- **Structured JSON:** [`a903f7754d3e2156d28c.json`](../../sessions/a9/a903f7754d3e2156d28c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**实验 `latency-profile-n1000` 实际上成功完成了，是监控系统误报。**

**根本原因**：`profile_latency.py` 脚本不创建 sentinel 文件，而 cron 监控以 sentinel 存在作为成功判据。脚本正常完成 → 监控找不到 sentinel → 判定失败 → 重启，循环 5 次。

**证据**：
- `logs/latency_profile_n1000.log` 显示全部 9 个阶段完成，打印了完整 summary
- `logs/latency_profile_n1000.json`（5589 bytes）包含 17 个组件的完整测量数据（每组件 1000 次迭代）
- `logs/sentinels/` 目录为空，脚本中 grep "sentinel" 无匹配
- GPU cuda:4 已空闲，进程正常退出

**修复**：在脚本末尾加 sentinel 文件创建逻辑，或修改监控策略改为检查输出 JSON 是否存在。

诊断报告已注册为 artifact `art_20260520_de306f`。

---
