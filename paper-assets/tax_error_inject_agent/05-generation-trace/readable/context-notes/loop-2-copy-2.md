# agent / loop_2.md

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`2229f2ed9ffa5998dc2a.json`](../../sessions/22/2229f2ed9ffa5998dc2a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-14T17:34:27+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：autodl-5090 cuda:0/1/2/3，其他 GPU 一律 push back Director
- eval/recovery.py 用 `--device cuda:0`（不是 `--gpu 0`），已因此连续失败两次
- checkpoint 查找必须 `ls -dt .../v0-*/ | head -1` + `sort -V`，禁止硬编码路径（v0-20260514-122641 vs v0-20260514-201441 踩坑两次）
- submit_training_job 命令必须 `bash -c "..."` 包装，tmux 用 sh 不支持 source/conda
- 禁止派 Worker 执行 `tmux kill-session` 除非先 `ps -p &lt;PID>` 确认进程已死（SIGHUP 误杀事故教训）
- **v4 Gate 3a/3b 均 FAIL，已向 Director 提交 Framing 调整提案，等 Director 决策前禁止动 paper、禁止默默跑下一个实验**

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090，account=root，工作目录 `/root/autodl-tmp/tax_error_inject_agent`
- Python：`/root/miniconda3/bin/python`，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：`/root/autodl-tmp/models/Qwen/Qwen3-8B`
- ms-swift 4.2.0（已安装）
- v4 checkpoints：
  - vanilla: `checkpoints/mini_vanilla_sft_v4/v0-20260514-201441/checkpoint-1635`
  - taxei: `checkpoints/mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387`
  - random: `checkpoints/mini_random_sft_v4/v1-20260514-213104/checkpoint-3387`
- 数据：`data/mini_pipeline_v4/sft_{taxei,random,vanilla}_v4.jsonl`（9029/9029/4358）
- 轨迹：`data/trajectories/successful_trajectories.jsonl`（501 条，已完成）
- TMPDIR：`/root/autodl-tmp/tmp`（防 /tmp 满）
- 活跃进程：**全部空闲**，4 张 GPU 无任务，无活跃 tmux/cron
- 分析脚本就绪：`scripts/analyze_gate3.py`（已验证）、`scripts/run_v4_eval.sh`（已修复 sort bug）

### 3. 📊 当前状态
刚完成 v4 三组 eval 正式判定并向 Director 提交了 Framing 调整提案（含 3 个 Option）。

**v4 正式结果**：vanilla 61.7% = taxei 61.7% < random 66.0%。Gate 3a FAIL (0pp, p=1.0), Gate 3b FAIL (-4.3pp, p=0.754), Gate 4 PASS。

Registry 关键实验：
- v4-taxei-eval: conclusion=negative, 61.7%
- v4-random-eval: conclusion=negative, 66.0%
- v4-vanilla-eval-r3: conclusion=success, 61.7%
- traj_collect_500: 501 条完成

**等待中**：Director 对 Framing 调整提案的决策（Option A/B/C 三选一）。决策到手前 GPU 可跑其他矩阵格子但不动 paper。

### 4. 📋 待办
- Director 选 Option A (data augmentation pivot) → 重写 paper framing，random injection 作为主角
- Director 选 Option B (task-type dependent) → 需扩大 eval set（n=47 太小），补充 per-task 分析
- Director 选 Option C (recovery eval) → 需开发 injected eval pipeline（eval 时注入错误测 recovery），这是我推荐的方向
- Director 选 pivot → 按 framing-reaudit skill 做全文 re-audit
- 任何新实验提交前 → 先确认 Director 决策，禁止默默跑
- 如果要跑 injected eval → 需修改 eval/recovery.py 去掉 --no_inject，确认 inject eval 逻辑

### 5. 🎯 战略上下文
- 核心科学问题："taxonomy-guided injection 是否优于 random perturbation?"——**答案目前是 No**
- 但有一个关键盲点：当前 eval 只测 clean tasks（--no_inject）。TaxEI 标注的是错误类型，其价值应在遇到同类错误时体现。所以 Option C（recovery eval）逻辑最自洽
- v3 和 v4 趋势方向不一致（v3: vanilla>taxei>random; v4: random>taxei=vanilla），证明 v3 数据不平衡确实是混淆变量，v4 同源方案是对的
- TaxEI 在 pick_two_obj 上严重退化（28.6% vs 57.1%），这是最值得调查的异常
- 决策链：D001(加random baseline) → D002(Gate定义) → D003(不over-claim) → D004(RandomInjector重设计) → D005/D006(v4同源方案) → 待定(Framing pivot)
- **易错**：不要把 v3 结果和 v4 结果混用对比（数据来源不同）。v4 是唯一正式判定


---
