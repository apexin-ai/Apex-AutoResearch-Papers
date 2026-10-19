# code fix eval v2 deadlock

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_eval_v2_deadlock_20260519T233720_result.json`
- **Structured JSON:** [`8973baceb9347fa980ea.json`](../../sessions/89/8973baceb9347fa980ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**1. 旧进程** — 已 kill（PID 187801 主进程 + 188069/188343/188344 vLLM workers + Java gateway）

**2. eval 脚本修改** — `eval_scienceworld.py` 新增：
- `--resume` 标志：从 JSONL 文件加载已完成结果并跳过
- `--episode_timeout 300`：每个 episode 5 分钟超时（signal.alarm），超时后 kill Java gateway 并重建 env
- 每完成一个 episode 立即追加写入 JSONL（增量保存）
- 异常/超时计数器在最终报告中展示

**3. 已提取结果** — 439 episodes 提取到 `eval_results_dev_v2.jsonl`，其中 163 OK（37.1% 成功率）

**4. 新进程** — PID 195848

**5. 验证** — 从 episode 440 正常继续，`[440/1796] OK inclined-plane-determine-angle v109`，GPU 已加载模型

---
