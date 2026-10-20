---
loop: 12
reason: idle_timeout
updated: '2026-05-25T15:40:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 分配：cuda:0 和 cuda:1 均可用，每实验独占一张卡，不得多进程共享
- 历史 GPU 红线违规：Loop #11 发现 epsilon-clipping-gen10 worker 在 cuda:0 启动未注册的 10 代重训练（PID 885060/885409），已 kill。**看到 GPU 上有非 registry 注册的进程 → 立即 critical**
- ssh_read_only 不支持管道 `|`、分号 `;`、`$()`，需要复合命令只能报告给 Director 让 Worker 用 ssh_execute
- `amin2025escaping` bib 条目 author 字段用了 `others` 占位，需补全为完整作者列表（Amin, Kareem and Babakniya, Sara and Bie, Alex and Kong, William and Vassilvitskii, Sergei and Syed, Umar）
- DDL 是 2026-05-25（今天），所有实验已完成，剩余只有写作修正

### 2. 🖥️ 基础设施快照
- 服务器：rtx6000-diagprobe，account=root
- 远程代码根：`/root/spectral_collapse_ews`
- 远程结果：`/root/spectral_collapse_ews/results/`（原始 JSON 在此）
- Checkpoint：`/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1_gpt2m/`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/`
- 本地论文：`workspace/paper/`，figures 在 `paper/figures/`
- 活跃进程：**无**（两卡均空闲 0%/0MiB）
- 无 W&B 配置

### 3. 📊 当前状态
Loop #12 完成 §3.6 Cross-Architecture 对抗审查，已 post 报告给 Director。

**发现两个 warning（已提交）**：
1. experiments.tex L197 σ₁ 数值错误："rising to 1593 by Gen~9" 应为 ~1571（1593 是 Gen 8 的值，Gen 9 实际 1570.7）
2. experiments.tex L202 "both conditions" 引用了 r=0.25 单一条件的精确数字（SLV +8.5%, r_eff 142, σ₁ −82%），r=0.3 实际是 +7.5%, 136, −80%，应改为范围表述

**Registry 状态**：全部 26 个实验 DONE，无 RUNNING/PREPARING。exp_022c 和 exp_023 status 已正确更新。

**等待中**：Director/Agent 修正上述两个数值问题 → 修正后需 re-verify

### 4. 📋 待办
- Agent 修正 σ₁ 和 "both conditions" 数值 → re-read L197/L202 确认修正正确
- 论文编译完成 → 用 paper-visual-review skill 做视觉审查（页数是否 ≤8 页、图表排版）
- Abstract 渲染后字数需手动核对（LaTeX 源码 wc -w=204，含命令；渲染后约 195-200，borderline）
- Director 触发 Step 5 论文评审 → 加载 paper-quality-lessons skill，按 §5.3 评分模板输出
- `amin2025escaping` bib author 修正 → 验证 references.bib 条目完整性

### 5. 🎯 战略上下文
**项目核心结论**：递归合成训练导致三相光谱崩溃轨迹（decompression→onset→acceleration），SLV 是最佳早期预警指标，r_crit ∈ (0.25, 0.3] 划分相边界，但信号衰减使反应式控制器在 r ≥ r_crit 时失效。

**最容易判错的事**：
1. **GPT-2m PPL 方向与 Pythia 相反**：r=0.25 下 GPT-2m PPL 从 15.5 降到 12.1（改善），Pythia 则上升。§3.6 已正确处理此差异，re-verify 时注意不要误判
2. **3-gen 数据的 claim 边界**：r=0.25 和 r=0.3 的 EMA 轨迹在 3 代内几乎相同，Type II/III 区分需 Gen 5+。论文 L204 已正确 hedge，但修改时可能丢失 hedge 语句
3. **Table 3 数值已全部验证正确**（vs 服务器原始 JSON），不需要重新验证表格，只需关注 body text 修正
4. **r=0.3 Type III 分类基于 EMA-smoothed SLV**（raw SLV 有 −1.18% dip），这是故意的设计选择不是错误
