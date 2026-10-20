# Project coordination (archived snapshot) — Part 8 of 8

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Conversation logs

[← Part 7](part-007.md) · [Transcript overview](../coordination-coordination-20260525-061056.md) · [Structured JSON](../../../sessions/1f/1f1d3a10fb25188e04dc.json)

## Round 272

### User

_source line 3898 · 2026-05-25T06:10:05.264191+00:00_

[WRITE HANDOFF] 请立即写你的 handoff。

**格式硬约束**:
- 整条回复**只能**是 &lt;handoff>...&lt;/handoff> 标签包裹
- 禁止在标签外写任何寒暄 / 说明 / 确认（"好的"/"我开始写"/"写完了"等）

**必须覆盖以下 5 个 section（缺一不可，无内容写 N/A）**:

### 1. 🔴 硬约束 / 红线
  本项目特定的不可违反约束（GPU 设备号、服务器名、账号、路径限制等）。
  写本项目特定的，不要抄 CLAUDE.md 通用 L1 红线。
  下一个"你"第一眼看到的就是这里，写错了会被 Director CRITICAL。

### 2. 🖥️ 基础设施快照
  - 服务器名 + 工作目录 + Python 路径 + conda env
  - 模型路径 / 数据集路径 / wandb config / HF cache
  - 活跃进程：PID + tmux session + cron 任务 ID
  写一次就稳定，下一个"你"不用再 SSH 探查。

### 3. 📊 当前状态
  - 你刚做完什么 / 正在做什么
  - registry 里 RUNNING/PREPARING 的实验列表 + 一句话摘要
  - 等待中的 Worker 回调 / Cron / Director 决策

### 4. 📋 待办（条件触发式）
  格式 "条件 X 满足 → 动作 Y"。例如:
  - "Falcon-H1R 下载完成 → sed 修 MODEL_PATH → dry-run → 提交"
  - "pilot_011 出 GC4 结果 → ≥2pp 转架构 narrative，<2pp 写 null-result"

### 5. 🎯 战略上下文
  - 项目核心结论 / 决策链（D001..）
  - 下一个"你"最容易判断错的事 / 容易踩的坑

**写作原则**：
- 第 1 节必须是项目特定的（不是通用 L1 红线）
- 第 2 节让下一轮 BOOT 后能立即开工，避免重新 SSH 探查
- 简洁 > 完整：每节 5-10 行足够，长 handoff 不等于好 handoff

示例格式:
&lt;handoff>
### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:4 / cuda:5（之前两次违规 cuda:0 被 Director CRITICAL）
- submit_training_job 不支持 shell builtin（source/conda activate 全不行）

### 2. 🖥️ 基础设施快照
- 服务器：westd-8x6000，工作目录 /root/autodl-tmp/hybrid_reasoning_phases
- Python：/root/miniconda3/bin/python（绝对路径，不走 conda activate）
- 模型：/root/autodl-tmp/qwen35_4b_direct
- 活跃：pilot_011 (PID 203221, tmux=pilot_011, cuda:4)

### 3. 📊 当前状态
我刚完成 pilot_010 分析，正在等 pilot_011 (Falcon-H1R) CoT 生成完成（6/50）。
registry: pilot_011 RUNNING；其他全 DONE。

### 4. 📋 待办
- pilot_011 cron 回调 → spawn worker 跑 probe + GC4 计算
- GC4 ≥2pp → 转架构 narrative；<2pp → null-result paper outline 已就绪

### 5. 🎯 战略上下文
Falcon-H1R 是最后一个数据点。已知 4B/9B GC4 都 FAIL。
易错：不要把 GC4-par (Falcon parallel) 和 GC4-seq (Qwen sequential) 直接对比。
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c8e1a57f5b1c63676dddeadba42e57b8",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 3899 · 2026-05-25T06:10:56.818677+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- 本项目无 GPU 分配，所有分析为纯 CPU 统计计算（response matrix 操作）
- 匿名仓库 token `[REDACTED_GITHUB_TOKEN]` 绝不能提交到任何文件中
- 论文分支是 `rebuttal-b1-b7`，不要在 main 上改 paper/
- 数据源 truth: `artifacts/` 下的 CSV/JSON，不是论文 .tex 中的数字

### 2. 🖥️ 基础设施快照
- 服务器：本地 Ubuntu (ip-172-31-8-29, ap-northeast-1)，无远程 GPU 服务器
- 工作目录：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen`
- Python：系统 python3（无 conda/venv，纯 numpy/scipy/pandas 分析）
- 匿名仓库：`https://github.com/anonymous-nlp-2026-2/irt_equated_bench_regen`（public，3 commits by Anonymous）
- 活跃进程：无（全部实验已完成）
- Crons：无活跃

### 3. 📊 当前状态
论文技术侧 100% 就绪，DDL 2026-05-25 AoE。最终数据自查已通过（无需修正）。

已完成的 rebuttal 任务：
- B1-B9 should-fix commits（rebuttal-b1-b7 分支）
- E1-E3 Tier 1 实验（K=3 power, interaction regression, mixed-mechanism）
- R15/R16/R17/R22 审稿分析（temporal DIF, threshold calibration, DEFF downstream, score inflation）
- W2 k=30,40,50 multi-subject injection 扩展
- 匿名仓库 push（code + paper source）
- 数据正确性审计 2 轮（130+ 数字核查，6 处已修正，最终确认 0 问题）

Registry: 所有实验 DONE（成功 14 / 负向 6 / 失败 0）。无 RUNNING/PREPARING。

等待：用户完成 ARR OpenReview 提交（匿名仓库已 public，论文已编译）。

### 4. 📋 待办
- Director 说 "提交完成" → standby 结束，进入 post-submission 阶段
- 如果 Director 发现任何 last-minute 数字问题 → 改 .tex → 编译 → commit rebuttal-b1-b7 + push 匿名仓库
- Camera-ready 阶段需修正 2 处低风险：§5.1 AUC "0.93-0.94"→"0.92-0.93"，Table 5 一个 cell 0.915→0.914

### 5. 🎯 战略上下文
这是 EMNLP 2026 ARR 投稿（MH-DIF psychometric audit of LLM benchmarks）。核心 claim：temporal DIF C%=31.3%（DEFF-adjusted 13.5-29.2%），50× above random null，ranks preserved (ρ=0.997)，orthogonal to web-overlap (Jaccard=0.206)。

易错点：
- "≥22×" enrichment 精确值是 21.8×（13.5%/0.62%），Director 已知并接受
- Table 1 Ability quintile N 是 ~2,090 不是 ~2,600（已修正，别改回去）
- summary_by_k_full.csv 包含 k=1,2,3,5,10,20,30,40,50（不只是原始的 1-20）
- 匿名仓库 git author 必须是 "Anonymous &lt;anonymous@example.com>"，不要用真实身份 push
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c8e1a57f5b1c63676dddeadba42e57b8"
}
```

</details>

---
