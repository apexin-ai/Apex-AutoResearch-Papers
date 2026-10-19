# agent / loop_1.md

**error diag dpo recovery** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`7b2fa0ac042df813ba71.json`](../../sessions/7b/7b2fa0ac042df813ba71.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-12T15:57:38+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**只能用 cuda:0 和 cuda:1**（cqa1-21977）。之前两次违规（cuda:2, cuda:3）被 Director CRITICAL。所有 ssh_execute 命令必须以 `CUDA_VISIBLE_DEVICES=0` 或 `CUDA_VISIBLE_DEVICES=1` 开头，脚本内 `--gpu 0`
- 不要用 `submit_training_job` 提交轨迹收集——用 screen session + Worker 监控。submit_training_job 走 tmux，与 screen 冲突
- 分类/收集脚本修改后，**ICL 前缀长度必须在 classify_errors.py 和 collect_trajectories.py 之间保持同步**。1 example = 12 msg prefix，3 examples = 需要重新计算

### 2. 🖥️ 基础设施快照
- 服务器：**cqa1-21977**，工作目录 `/root/autodl-tmp/error_diag_dpo_recovery/`
- Python：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`（conda 环境，不是 venv）
- 8B 模型：`/root/autodl-tmp/.hf_cache/Qwen3-8B`
- 14B-AWQ 模型：`/root/autodl-tmp/.hf_cache/` 下（具体子目录需 ls 确认，Worker 之前找到过）
- Expert 数据：`/root/autodl-tmp/error_diag_dpo_recovery/eto_repo/data/alfworld_sft.json`（3,119 条）
- 失败轨迹 v1：`data/trajectories/train_part0.jsonl`(61) + `train_part1.jsonl`(28)，全部 reward=False（action 翻译 bug 导致）
- 分类结果 v1（无效）：`data/classified/classified_errors.jsonl`（88 条，ICL 前缀 bug 导致 failure_step=5 集中）
- ALFWorld 数据：`/root/autodl-tmp/alfworld_data`，环境变量 `ALFWORLD_DATA` 指向此路径
- ETO prompt：`eto_repo/eval_agent/prompt/`（instructions/ + icl_examples/）
- 活跃进程：**Worker worker_exec_v3-diagnose-fix-relaunch 正在运行**，执行 Step A→B→C（排查崩溃→修 ICL→两卡启动收集）

### 3. 📊 当前状态
**正在执行 Director 批准的方案 A：修复后用 8B 重新收集 200+ 多样化轨迹。**

刚做完：
- Step 1A/1B：失败诊断完成（prompt 错配 + 86/87 overlap 确认）
- Step 2 分类完成但结果无效（classify_errors.py ICL 前缀 bug → failure_step=5 集中 75/88）
- Episode 边界检查：确认 episode 逻辑正确，bug 在 classifier 的 format_trajectory
- ICL 14B 测试：**78% 成功率**，P1 gate PASS。关键发现：0% 是 action 格式不匹配（put→move），不是模型能力问题
- v3 250-task 首次收集崩溃（train.jsonl=0 字节）

Registry:
- `datagen_traj_v3_collect`: DONE(failed) — 250-task 崩溃
- `datagen_classify_v2`: PREPARING — 等新轨迹数据
- 其他 4 个 datagen 实验: DONE(failed)

等待中：
- **Worker 回调**：worker_exec_v3-diagnose-fix-relaunch（正在做 A→B→C）
- Worker 完成后需注册两个新 registry 实验（v3_part0, v3_part1）并用 `register_cron` 监控

### 4. 📋 待办
- v3-diagnose-fix-relaunch Worker 回调到达 → 读取结果，确认两个 screen session PID + GPU 占用 → 注册 registry（datagen_traj_v3_p0, datagen_traj_v3_p1）+ 注册 cron 监控 → 汇报 Director
- 收集完成（~60-90 min 后 cron 回调）→ 统计 success/failure 分布 + 按 task_type 拆分 → 如果成功率 30-50% 进入分类；如果 <10% 需汇报 Director 调整策略
- 分类完成 → 检查 error type 分布是否均衡 → 计算 correction span → Kruskal-Wallis P1 gate 检验
- P1 gate PASS → 构建 DPO pairs（expert as chosen + failure as rejected）→ 7-run 训练矩阵
- P1 gate FAIL → 产出 Framing 调整提案给 Director

### 5. 🎯 战略上下文
- **ETADN 核心假设**：不同 error type 需要不同时间折扣 γ_e（action≈0.85, verification≈0.92, planning≈0.97）。P1 gate = correction_horizon 在三类间有统计显著差异
- **数据策略已 pivot 两次**：自我纠正（0% 成功）→ Expert as Chosen（当前方案）。Expert 来自 ETO repo 的 alfworld_sft.json
- **0% 成功率的根因已确认**：不是模型能力问题，是 ALFWorld action 格式不匹配（`put` vs `move`）+ ICL 示例太弱（1 example）。translate_action() + 3 examples 修复后 14B 达 78%
- **易踩的坑**：
  - classify_errors.py 的 ICL 前缀跳过数（硬编码）必须与 collect_trajectories.py 的 ICL 示例数量同步，否则又会出现 failure_step 聚集
  - ALFWorld 不支持 deterministic replay（同 game_file 不同 run 环境状态不同），不要尝试 replay-then-correct 策略
  - screen session 内必须显式 `source conda` 激活环境，否则找不到 Python 包


---
