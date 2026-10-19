# diagnose exp029 per task t04 v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp029_per_task_t04_v2_20260519T150818_result.json`
- **Structured JSON:** [`916beaa34da391df8a2c.json`](../../sessions/91/916beaa34da391df8a2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：exp029_per_task_t04_v2 是 cron 误报，eval 实际已成功完成。**

- 134/134 OOD games 全部跑完，总成功率 19.4%（26/134），结果已保存到 JSON
- 失败原因：vLLM v0.18.1 关闭时的 EngineCore 进程清理竞争导致非零退出码 + 脚本没写 sentinel 文件/W&B run，触发 cron 的"无信号=失败"逻辑
- GPU 状态干净，无残留进程
- **不需要重跑**，数据完整可用

诊断报告已注册为 `art_20260519_2e381d`。

---
