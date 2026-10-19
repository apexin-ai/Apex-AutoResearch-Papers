# agent / loop_18.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_18.md`
- **Structured JSON:** [`82fe5c2ba3702812aba7.json`](../../sessions/82/82fe5c2ba3702812aba7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 18
reason: idle_timeout
updated: '2026-05-17T11:10:51+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单严格按 `get_project_status` 的 `execution.gpu_ids`，当前 4 台服务器：bjb1-18228, bjb1-32546, bjb2-28827, bjb2-40593
- bjb2-40593 磁盘 `/usr/bin/nvidia-smi` 分区已用 90%（仅剩 46GB），不要在该服务器启动写大量 checkpoint 的实验（eval log 很小可以用）
- Narrative B 已锁定 (D043)，论文 framing 不可改动除非 Director 明确批准
- `eval-direct-correction` 前两次 SIGTERM 是资源冲突（非代码 bug），r3 已成功完成 SR=14%，不需再重试
- pooled Fisher test 统计必须从 raw JSON 读取实际 trial counts，不能硬编码（翻倍 bug 教训）

### 2. 🖥️ 基础设施快照
- **4 台服务器**: bjb1-18228, bjb1-32546, bjb2-28827, bjb2-40593
- 工作目录: `/root/acr-vla-conformal-refinement/`
- Python: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`（submit 命令必须 bash -c 包裹）
- CRM checkpoint: `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`（obs_only 327K params）
- 评测命令: `python -u src/evaluate.py --mode {mode} --benchmark object --seed {seed} --max_correction_norm {norm} --crm_checkpoint ... --n_rollouts 10 --output_file results/...`
- W&B: 未配置（eval 实验不走 W&B，cron 通过进程存活 + log 检测完成）
- 活跃 GPU 进程: 12 experiments RUNNING（cron 监控中），详见 registry

### 3. 📊 当前状态
**刚做完**: session-start 初始化 + 批量新结果处理。发现 5 个实验完成（obs-only-seed46=15%, direct-correction-r3=14%, perdof-norm03-seed44=4%, obs-only-norm03-seed45=14%, vla-mean-seed45=13%）。已向 Director 汇报。

**已派发 2 个 Worker**（等回调）:
- `worker_ssh_deploy-preparing-experiments-batch5_20260517T070743`: SSH 检查空闲 GPU + 部署 4 个 PREPARING 实验 (norm01 seed46/47 obs_only+perdof)
- `worker_analysis_batch-results-update-20260517_20260517T070805`: 更新 pooled 统计 + memory.md

**RUNNING 实验 (12)**:
- perdof ablation: norm01-seed44/45, norm02-seed44/45, norm03-seed45-r2, default-seed44
- obs_only: default-seed45, norm01-seed45, norm02-seed47
- scalar: seed45
- argmin: seed46, seed47

### 4. 📋 待办
- deploy Worker 回调 → 确认 4 PREPARING 实验成功启动，更新 registry 为 RUNNING
- analysis Worker 回调 → 确认 memory.md 更新，检查 pooled 统计正确性
- argmin seed46/47 完成 → 计算 6-seed pooled Fisher p（目标: obs_only 17% vs argmin ~13%, 预估 p~0.08-0.12）
- perdof norm01/02/default seed44/45 全部完成 → 汇总 magnitude curve multi-seed error bars，准备论文 figure 数据
- 所有 eval 完成 → 汇报 Director 最终统计 + 建议启动 paper figures matplotlib 脚本
- Director 回复建议（paper figures / 下一步）→ 执行

### 5. 🎯 战略上下文
- **核心结论**: obs_only CRM (ε=0.2) 唯一存活。5-seed pooled: obs_only 17.0% vs argmin 13.5%, +3.5pp。Narrative B = mechanism insight（magnitude robustness）为主线
- **新关键数据点**: direct-correction=14% ≈ argmin → 证明 CRM 价值在 selection signal 而非 correction itself。这完成了 Claim 1 的 ablation 证据链
- **投稿**: CoRL 2026，abstract DDL ~May 26，full paper DDL ~Jun 2（剩 ~10 天）
- **决策链**: D038(ε=0.2最优) → D039(perdof default=0%崩溃) → D042(claim结构) → D043(Narrative B锁定) → D044(Claim 1降级)
- **易错点**:
  - magnitude curve 数据来自不同 seed，论文 figure 用 seed42 单线（已有完整 6 点），multi-seed 做 error bar 是补充
  - 5-seed obs_only pooled (85/500) 目前只能和 4-seed argmin (54/400) 比（不对称），等 seed46/47 argmin 完成才能做 paired 6-seed Fisher
  - perdof norm=0.3 两个 seed 都是 4%（deterministic collapse），但 obs_only norm=0.3 有波动（19% vs 14%），报告时注意标注 variance


---
