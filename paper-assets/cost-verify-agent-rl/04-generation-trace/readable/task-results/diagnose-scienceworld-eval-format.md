# diagnose scienceworld eval format

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_scienceworld_eval_format_20260519T181348_result.json`
- **Structured JSON:** [`ba685fd42b97478901d7.json`](../../sessions/ba/ba685fd42b97478901d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。核心发现：

1. **训练数据 action 格式错误**：SFT 数据用的是 ScienceWorld 内部 gold action sequence（如 "open door to kitchen"），但环境 player parser 不接受这种格式，只接受 "open door" 这种泛化格式。
2. **Admissible actions 被 connect 淹没**：939 个 valid action 中 506 个是 "connect X to Y" 排列组合，eval 只展示前 50 个全是 connect，有用 action（open/pick up/look 等）模型看不到。
3. **valid_action_rate metric 误报**：只检查 shown[:50]（全是 connect），即使模型生成了环境接受的 action 也报 0%。
4. **fmt rate 53-74%**：约 1/3 步骤格式解析失败，浪费回合。

**推荐路径**：先修 eval（过滤 connect、排序 useful verbs 优先、metric 用全量 list），确认 metric 准确后再决定是否需要重新生成训练数据重训。

---
