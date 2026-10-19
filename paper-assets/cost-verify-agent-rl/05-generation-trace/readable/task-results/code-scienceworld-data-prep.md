# code scienceworld data prep

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_scienceworld-data-prep_20260519T115245_result.json`
- **Structured JSON:** [`131f4efa2e8f9ffe99b4.json`](../../sessions/13/131f4efa2e8f9ffe99b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进度：144/2989 episodes（~5%），约 10 分钟已过。估算剩余约 3-4 小时完成。

当前状态总结：

| 项目 | 状态 |
|------|------|
| 提取脚本 | PID 23069 运行中，144/2989 episodes |
| parquet 转换脚本 | 已准备，待提取完成后运行 |
| bjb1 ScienceWorld 适配器 | 已同步（3 文件 + __init__.py 注册）|
| 预计完成时间 | ~3-4 小时 |

**待提取完成后的操作：**
1. 运行 `python3 /root/autodl-tmp/convert_sft_jsonl_to_parquet.py`
2. 最终统计报告

**格式注意：** SFT 数据的 user message 包含 "Turn X:", "Reward:", "You have X actions left" 等信息，而 RAGEN ScienceWorld env adapter 的 `_format_observation` 不包含这些。SFT→RL 过渡时可能需要对齐格式。

需要我继续监控提取进度，还是等完成后再通知你？

---
