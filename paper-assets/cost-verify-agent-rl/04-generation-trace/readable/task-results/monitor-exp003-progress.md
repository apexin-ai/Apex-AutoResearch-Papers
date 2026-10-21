# monitor exp003 progress

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp003_progress_20260513T214414_result.json`
- **Structured JSON:** [`011dbef9d0a8ea79287d.json`](../../sessions/01/011dbef9d0a8ea79287d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp003 状态汇报：**

1. **当前步数：0/100** — 尚未完成任何训练步。日志仍在初始化阶段（加载模型 → 初始化 AlfWorld 环境 → 加载 eval 数据集 140 games）。`actor_rollout_generate_sequences` 正在运行，推测正在执行第一轮 rollout。

2. **无报错** — grep 未找到任何 Error/Traceback/Exception。

3. **关键指标：暂无** — 尚未产出 advantages/pg_loss/success_rate/reward 等训练指标（grep "advantages" 返回空）。

4. **GPU 利用率：**
   - GPU 0: 63%, 41,627 MiB / 97,887 MiB (42.5%)
   - GPU 1: 63%, 41,645 MiB / 97,887 MiB (42.5%)
   - 两卡均在活跃计算中，显存占用合理。

5. **dashboard_agent：运行中** (PID 158538, `ray::DashboardAgent`)

6. **状态：正常初始化中。** 进程 05:39 UTC 启动，运行约 5 分钟。Qwen3-1.7B 模型已加载到 2×GPU（FSDP），AlfWorld 训练集 3553 games 和 eval 集 140 games 已就绪，正在进行第一轮 rollout。一切正常，预计几分钟后会出现 step 1 的指标。

---
