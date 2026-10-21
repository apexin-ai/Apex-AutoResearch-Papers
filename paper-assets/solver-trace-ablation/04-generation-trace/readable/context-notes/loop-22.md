# agent / loop_22.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_22.md`
- **Structured JSON:** [`94f91934fd18a473eb02.json`](../../sessions/94/94f91934fd18a473eb02.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 22
reason: idle_timeout
updated: '2026-05-19T12:06:40+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只有 1 张 GPU：westd-39279 cuda:0（cuda:1 不存在，物理上只有 1 张 RTX PRO 6000 96GB）
- gpu_ids 白名单只有 cuda:0，任何其他 GPU 编号都是违规
- D134 pipeline 使用 `--no_wandb`，cron 靠 sentinel file 判断完成，没有 W&B metrics 是正常的
- DDL 2026-05-25 ARR May cycle，剩 6 天，D137/D139 已决定不追加新训练实验，聚焦统计完备性+文本质量
- 磁盘反复满过（s48 第一次就因 os error 28 crash），提交前必须 `df -h` 预检

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279，工作目录 `/root/autodl-tmp/`
- Python：`/root/miniconda3/bin/python3`
- 训练脚本：`scripts/train_grpo.py`，配置 `configs/grpo_additive_random_b01.yaml`
- 数据：`data/train_500_seed42.jsonl`（500 条）
- 模型：Qwen3-4B
- 输出目录：`/root/autodl-tmp/outputs/d134_4b_random_b01_s48/`
- D134 pipeline 脚本：`d134_random_pipeline_v2.sh`（auto-cleanup enabled，自动推进 s47→s48→s49→s50→s51）
- 磁盘：`/root/autodl-tmp` 对应 `/usr/bin/nvidia-smi` 分区 400G/439G 可用（截至上次 report）
- 活跃进程：无 RUNNING 实验；有 1 个诊断 Worker 在跑：`worker_diag_d134-4b-random-b01-s48_20260518T200431`

### 3. 📊 当前状态
**刚做完**：Session 初始化（read_registry + reconcile_crons + report.md + ROADMAP.md）。

**正在做**：已 spawn Worker 诊断 d134-4b-random-b01-s48 失败原因（SSH 读日志、查磁盘、查残留进程）。Worker 尚未回调。

**Registry 关键状态**：
- d134-4b-random-b01-s48：DONE/failed — "process dead 5× with no sentinel/W&B"（第二次失败，第一次磁盘满）
- d134-4b-random-b01-s49：ALLOCATED，等待提交
- d134-4b-random-b01-s50/s51：PREPARING
- d134-4b-random-b01-s47：DONE/success（上一个成功的 random seed）
- D134 ISR 侧 s47-s51 全部 success
- 总计 160 实验，56 success / 36 negative / 47 failed / 10 killed

**等待中**：
- Worker `diag:d134-4b-random-b01-s48` 回调 → 诊断报告
- 诊断完成后需决定：修复 s48 重跑 or 跳过，以及 s49-s51 如何推进
- 无 Director 待决策项

### 4. 📋 待办（条件触发式）
- 诊断 Worker 回调 → 根据失败原因决定修复方案：
  - 若磁盘满 → 清理旧 checkpoint 后重跑 s48，再推进 s49-s51
  - 若 OOM/CUDA 错误 → 检查是否需要调 batch_size，汇报 Director
  - 若 pipeline 脚本 bug → 修复后重跑
- s48 修复后 → 用 `submit_on_allocated` 提交 s49（已 ALLOCATED）
- D134 Random 全 5 seeds (s47-s51) 完成 → 整合 Table 1 数据（D140 决策：用 D134 5+5 matched cohort 替换原 5-seed）
- 全部 D134 数据就绪 → 更新论文表格 + 统计检验 + 提交外审

### 5. 🎯 战略上下文
- **核心结论**：ISR 作为 GRPO neurosymbolic formalizer 的诊断工具 + Goodhart's Law 案例研究。4 个 Claims 全部有实验支撑（C1 诊断 / C2 Goodhart dynamics / C3 Cross-logic / C4 Taxonomy）
- **D134 决策链**：D133（不追加）→ D134（推翻：扩 β=0.1 到 10 seeds）→ D135（Fisher 统计检验）→ D136（Claim 升级策略）→ D137（Table 1 用 D134 数据）→ D138（ISR 叙事 framing）→ D139（不追加训练，聚焦文本质量）→ D140（Table 1 保持 exploratory 5-seed + matched cohort）
- **关键风险**：D134 Random pipeline 卡在 s48，ISR 侧 5 seeds 已全部完成但 Random 对照组只有 s47 一个。matched cohort 需要 ISR+Random 各 5 new seeds，Random 缺 4 个会阻塞 Table 1 更新和统计检验
- **易错点**：
  - 这台服务器磁盘反复满，每次提交前必须预检 + 清理
  - `--no_wandb` 是 D134 pipeline 的设计选择，不要因为"没有 W&B metrics"就判断为异常
  - Pipeline 脚本有 auto-cleanup，但显然不够激进（s48 两次都 crash）
  - 9 轮内审已 PASS，论文结构基本定稿，不要大改


---
