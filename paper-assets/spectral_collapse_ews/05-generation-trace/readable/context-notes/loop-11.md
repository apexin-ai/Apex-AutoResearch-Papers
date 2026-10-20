# reviewer / loop_11.md

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_11.md`
- **Structured JSON:** [`2fd2264552c16742649c.json`](../../sessions/2f/2fd2264552c16742649c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_wall_time
updated: '2026-05-25T05:23:29+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 分配：cuda:0 和 cuda:1 均可用，但每个实验必须独占指定 GPU，不得多进程共享
- 本轮已发生 GPU 红线违规：epsilon-clipping-gen10 worker 在 cuda:0 上启动未注册的 10 代重训练（PID 885060/885409），已 kill。**下一个"你"看到 cuda 上有非 registry 注册的进程 → 立即 critical**
- ssh_read_only 不支持管道 `|`、分号 `;`、`$()`。需要复合命令必须用 ssh_execute（Reviewer 没有 ssh_execute 权限，只能报告）
- `amin2025escaping` bib 条目的 author 字段用了 `others` 占位，需补全为：Amin, Kareem and Babakniya, Sara and Bie, Alex and Kong, William and Vassilvitskii, Sergei and Syed, Umar

### 2. 🖥️ 基础设施快照
- 服务器：rtx6000-diagprobe，account=root
- 远程代码根：`/root/spectral_collapse_ews`
- 远程结果：`/root/spectral_collapse_ews/results/`
- Checkpoint：`/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1_gpt2m/`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/`
- 本地论文：`workspace/paper/`，figures 在 `paper/figures/`
- 活跃进程：**无**（两卡均已释放，exp_020/022c/023 全部完成）
- 无 W&B 配置

### 3. 📊 当前状态
**刚完成的工作**：
- exp_023 (GPT-2-medium r=0.25, 3-gen) 和 exp_022c (r=0.3, 3-gen) 均已完成，数据已验证
- exp_020 (GPT-2-medium r=0, 10-gen) 之前已完成验证
- ε-clipping 验证完成：所有条件下 σ_min > ε 八个数量级，clipping 从未激活
- 引用验证完成：10 条全部真实，仅 amin2025escaping 需补全作者
- 图表 v2 重绘完成（7 张 + 新增 pipeline_overview），质量合格
- GPU 红线违规已处理（PID 885060/885409 已 kill）

**Registry 状态**：
- exp_022c：实际 DONE 但 registry 仍卡在 RUNNING — Agent 需更新
- exp_023：ANALYZING → 分析报告已完成，待转 DONE
- 其他实验全部 DONE

**等待中**：
- Agent 写入 §3.6 Cross-Architecture（目前整段注释）
- Agent 移除 Abstract 中的 TODO 注释（`% TODO: Add cross-architecture confirmation sentence once exp_020 completes.`）
- Agent 更新 exp_022c registry status

### 4. 📋 待办
- §3.6 写入完成 → 审查模式 B 对抗审查，重点检查：r_crit claim 强度是否用 "consistent with" 而非 "confirms"（3-gen 数据不足以区分 Type II/III）
- Abstract TODO 移除 → 确认新句子准确反映跨架构结论
- 论文编译完成 → 用 paper-visual-review skill 做视觉审查（页数是否达到 8 页、图表排版）
- 如 Director 触发 Step 5 论文评审 → 加载 paper-quality-lessons skill，按 §5.3 评分模板输出
- exp_022c registry 更新 → 验证 metrics 与实际数据一致

### 5. 🎯 战略上下文
**项目核心结论**：递归合成训练导致三相光谱崩溃轨迹（decompression→onset→acceleration），SLV 是最佳早期预警指标，但信号衰减使反应式控制器在 r ≥ r_crit 时失效。

**最容易判错的事**：
1. **GPT-2-medium PPL 方向与 Pythia 相反**：r=0.25 下 GPT-2m PPL 从 15.5 降到 12.1（改善），Pythia 则从 9.6 升到 11.0（恶化）。写 §3.6 时不能简单推广 "PPL increases during decompression" 的 Pythia 结论
2. **3-gen 数据的 claim 边界**：r=0.25 和 r=0.3 的 EMA 轨迹在 3 代内几乎相同（终值差 <2），Pythia 上的 Type II/III 区分要到 Gen 5+ 才显现。"confirms r_crit" 是过强 claim
3. **exp_022c registry 滞后**：实际完成但 registry 没更新，不要误判为还在跑
4. **DDL 是 2026-05-25（今天）**：所有实验数据已就绪，剩余工作是纯写作（§3.6 + Abstract + 编译）


---
