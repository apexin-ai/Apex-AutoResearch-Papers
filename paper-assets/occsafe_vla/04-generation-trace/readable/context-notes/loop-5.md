# director / loop_5.md

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_5.md`
- **Structured JSON:** [`e66bbe9789084139b9cf.json`](../../sessions/e6/e66bbe9789084139b9cf.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_messages
updated: '2026-05-23T19:46:33+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-10894 cuda:0-3 + westd-34685 cuda:0-3，共 8 张，不可用其他服务器/卡
- `--vla_path` 必须指向基模型 `/root/autodl-tmp/models/openvla-7b`，不可指向中间 checkpoint（M040 教训：清理脚本会删 checkpoint 导致训练崩溃）
- 所有训练必须用 `submit_training_job`（不是 ssh_execute+tmux），必须带 `--num_images_in_input 2 --use_proprio True`（M037 教训）
- eval 用 `evaluate_safelibero.py`（不是 `eval_safelibero.py`），50 rollouts，`MUJOCO_EGL_DEVICE_ID` 必须匹配物理 GPU 号
- checkpoint_rotation 脚本 `/root/occsafe_vla/cleanup_old_checkpoints.sh` 在 westd-10894 后台运行（PID 453371），覆盖 detach_ln_s0/s1/s2 + cutoff_s2_v2
- 目标会议 **CoRL 2026**（Abstract May 26, Paper May 29），禁止建议降级

### 2. 🖥️ 基础设施快照
- **westd-10894**: connect.westd.seetacloud.com, root, `/root/occsafe_vla`, 磁盘 214G 可用
- **westd-34685**: connect.westd.seetacloud.com, root, `/root/occsafe_vla`, 磁盘 240G 可用
- Python: `/root/miniconda3/bin/python`（conda base）
- 模型: `/root/autodl-tmp/models/openvla-7b`
- 分析脚本: `/root/occsafe_vla/analysis/`（gradient_analysis.py, cka_analysis.py, plot_gradient_figure.py, run_full_analysis.sh, bootstrap_ci.py）
- 训练监控: `/root/occsafe_vla/scripts/monitor_training.sh` 后台运行两台服务器，日志在 `/tmp/training_monitor.log`
- 论文: 远程服务器 `/root/occsafe_vla/paper/`，已切换 CoRL 2026 模板，~8 页主体
- Paper Agent session 活跃，已完成 D026 collapse prevention 叙事更新 + gradient figure 替换

### 3. 📊 当前状态
**刚完成**：D026 梯度分析确认 collapse prevention 机制（Vanilla ≈ gradient-flow 条件，Detach 梯度崩塌至 1-13%）。论文已全面更新（Abstract/Intro/Results/Discussion/Conclusion）。Gradient figure 已生成并替换占位框。

**RUNNING 实验（8/8 GPU）**：

| 实验 | 服务器:GPU | 进度 | ETA (UTC) |
|------|-----------|------|-----------|
| reverse_cutoff_s0 | 34685:2 | ~87% | ~20:30 May 23 |
| cutoff_25k_s0 | 34685:3 | ~87% | ~20:15 May 23 |
| cutoff_45k_s0 | 34685:0 | 刚启动 | ~07:30 May 24 |
| cutoff_15k_s0 | 34685:1 | ~2% | ~07:00 May 24 |
| cutoff_s2_v2 | 10894:0 | ~50% | ~06:30 May 24 |
| detach_ln_s0 | 10894:1 | ~5% | ~06:30 May 24 |
| detach_ln_s1 | 10894:2 | ~5% | ~06:30 May 24 |
| detach_ln_s2 | 10894:3 | ~5% | ~06:30 May 24 |

**等待中**：Agent 正在处理 reverse_cutoff/cutoff_25k 完成回调（eval 命令已准备好）。Cron 监控全部注册。

### 4. 📋 待办（条件触发式）
- reverse_cutoff_s0 / cutoff_25k_s0 完成（~20:30 UTC）→ 立即 submit eval（GPU 2/3），eval 完后 GPU 2 跑 vanilla_retrain_s0_eval
- detach_ln_s0/s1/s2 完成（~06:30 May 24）→ eval 3 seeds → CAR 结果判定 BN artifact（场景 A: ≈Vanilla → BN 是根因；场景 B: ≈Detach → gradient flow 是真机制）→ 选择 scenario_variants.tex 对应段落填入 §5.2
- detach_ln_s0 eval 后 → 在 westd-34685 用 seed 42 重跑 3 条件梯度分析（vanilla_retrain_s0 + full_occ_retrain_s0 + detach_ln_s0），random_occ 用 seed 44 补充，figure caption 注明
- cutoff_s2_v2 完成 → eval → 更新 Table 1 为 3-seed cutoff + bootstrap CIs
- cutoff_15k/45k 完成 → eval → 填充 dose-response 5 点曲线（0K/15K/25K/35K/45K）
- 全部 eval 完成 → Paper Agent 填入所有数据 → 重新编译验证 → submit_paper_to_review
- Manager GPU 扩容回复 → 如批准，开 AutoDL 实例跑 plan_028（LIBERO-Object 4 条件 × 3 seeds）

### 5. 🎯 战略上下文
- **核心结论链**：D022（梯度流是必要条件）→ D024（Dream 分析，best=borderline）→ D025（目标切换 CoRL 2026）→ D026（collapse prevention 机制确认，"sufficient" 措辞）
- **plan_027 是 make-or-break**：detach_ln 结果决定 §5.2 最终版本。场景 B（gradient flow genuine, ~45%）是最强 story；场景 A（BN artifact, ~40%）需要 nuanced reframe 但仍可发表
- **易错点**：
  - 不要用 "amplification" 措辞——已被 D026 证伪（旧版有 "8-69×" 表述，全部删除）
  - 不要用 "necessary"——Reviewer 明确说证据只支持 "sufficient"（未排除 weight decay 等替代方案）
  - detach_ln 从头重跑是干净的 50K，没有 resume confound（之前两次 resume 都出事，M039/M040）
  - 梯度分析当前用了不同 seed 的 checkpoint（detach=s2/seed44, vanilla/full_occ=retrain_s0/seed42），论文需注明，detach_ln 完成后做 same-seed 重分析
  - Discussion §5.1 EWC 类比已替换为 deep supervision（Reviewer warning）
- **已向 Manager 申请 4 GPU 扩容**（¥1,440, 5 天）用于第二 benchmark，尚未回复
- **错题本重点**：M035(checkpoint 删除), M036(cron 不触发 eval), M037(config 不匹配), M038(磁盘满), M039(resume 失败), M040(清理脚本删依赖)——这个项目运维事故密集，新实验启动后 5 分钟内必须验证 /proc/PID/cmdline


---
