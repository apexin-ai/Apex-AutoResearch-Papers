# diagnose eval supp long k2mean s47 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-supp-long-k2mean-s47-r2_20260524T154330_result.json`
- **Structured JSON:** [`8eb09f034c87cd162133.json`](../../sessions/8e/8eb09f034c87cd162133.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**这是一个误报（false failure）。实验实际上已成功完成。**

日志显示全部 10 个 task × 20 rollouts = 200 rollouts 正常跑完，overall success rate = **54.5% (109/200)**，结果已保存到 `logs/eval_long_vla_only_seed47.json`（May 24 23:32 写入，1791 bytes）。进程正常退出后 cron 探测到 process dead 且无 sentinel/W&B 信号，连续 5 次判定后自动标记为 failed。

**output_file 命名问题**：该进程启动时用的是 M083 修复前的代码，文件名为 `eval_long_vla_only_seed47.json`（缺少 `k2mean` 标识）。当前服务器上的代码（line 827）已修复，重跑会正确生成 `eval_long_k2mean_seed47.json`。

**结论**：
- **不需要重试** — 数据已完整，JSON 内容正确（含 `"baseline_mode": "mean"` 字段）
- 只需将现有结果 `eval_long_vla_only_seed47.json` 重命名为 `eval_long_k2mean_seed47.json`（或在汇总脚本中识别它）
- 如果后续需要规范文件名，可跑一次 rename 或用当前修复后的代码重新 evaluate（但浪费 GPU 时间）

---
