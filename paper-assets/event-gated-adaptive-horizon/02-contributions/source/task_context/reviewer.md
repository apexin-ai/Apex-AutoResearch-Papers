---
loop: 27
reason: max_wall_time
updated: '2026-05-29T08:20:01+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-51268 只有 1 张 GPU：cuda:0。**cuda:1 物理不存在**（torch.cuda.device_count()=1）。任何指定 cuda:1 的命令必须拦截。
- D171 数据锁定：Walker/Cheetah 已有实验数据和论文数值**冻结**，禁止修改任何已有数值/统计/表格/图表数据。新环境实验不受限。
- Humanoid Walk **已排除**（D177/D178）：baseline NVE=12.97×，不适合 CIVO 验证。不要批准任何 Humanoid 相关实验。
- Humanoid baseline 的 value overestimation 是 **generic bootstrap overestimation**，**不是 CIVO**（CIVO 需要 trained dt-embedding）。Agent 的 analysis report 里错误使用了 CIVO 术语，已向 Director 发过 critical 更正，但 artifact 文件未修改。

### 2. 🖥️ 基础设施快照
- 服务器：westd-51268 (root)，1× RTX PRO 6000 Blackwell (96GB)
- 工作目录：`/root/autodl-tmp/event-gated-adaptive-horizon`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 论文本地路径：`projects/event-gated-adaptive-horizon/docs/paper/`
- 活跃进程：exp_quadruped_baseline_s0_r2 (PID 42263, tmux, cuda:0)，运行 3h+，~115K/200K
- 日志：`~/runs/event-gated-adaptive-horizon/exp_quadruped_baseline_s0_r2.log`

### 3. 📊 当前状态
**刚完成**：ROADMAP D179 审查（Quadruped contingency plan），Table error bars worker 审查（PASS），citation audit 三 worker 交叉验证（Worker A 不可靠/hallucinated errors，Worker B/C 可靠，45/45 citations real）。

**RUNNING**：exp_quadruped_baseline_s0_r2 — Quadruped Walk baseline (dt=1, no gate)，~115K/200K，NVE@115K=2.3×，**不乐观**。value_mean 单调增长 10→407（40×），6/10 观测点 NVE>2.0。预计 ~1.5h 后完成。

**QUEUED**：exp_quadruped_008d_s0（等 baseline healthy），exp_walker_no_dt_emb_s0（re-run，等 GPU）。

**等待**：quadruped baseline 完成的 cron 回调。

### 4. 📋 待办
- exp_quadruped_baseline_s0_r2 cron 完成通知 → 审查最终 NVE：
  - NVE < 2.0 → 确认 baseline healthy，批准 008d 进行
  - NVE 1.8-2.2 borderline → 向 Director 报 warning，让 Director 决定
  - NVE > 2.0 clearly → 向 Director 报 critical，Quadruped 排除，触发 contingency（Hopper 作为关键第三数据点）
- exp_quadruped_008d_s0 完成 → 对比 baseline NVE，判定 CIVO 是否在 Quadruped 复现
- 任何新 Worker 写论文章节 → 模式 B 对抗审查（先 Read paper-quality-lessons skill）
- exp_walker_no_dt_emb_s0 提交 → 验证 GPU 在 cuda:0 白名单内

### 5. 🎯 战略上下文
**核心结论**：CIVO 是 trained dt-embedding + multi-rate exposure + multi-joint locomotion 的交集现象。NVE≥2.0 阈值完美分类 n=36（AUROC=1.000）。Frozen/removed embedding 0/10 onset，trained 6/9 onset。

**最大风险**：Quadruped baseline 大概率（~60%）NVE>2.0，与 Humanoid 同样不可用。如果发生，scope expansion 两个候选全军覆没，论文仅基于 Walker/Cheetah/Cartpole。Contingency 路径是试 Hopper (3-4 DoF)，ICLR DDL ~10月还有 4 个月。

**容易判断错的事**：
1. **不要被单个 eval checkpoint 误导**——Quadruped eval 极度 volatile（22.5→217.4→173.5），必须看完整轨迹+value_mean 趋势，不是单点 NVE
2. **区分 generic bootstrap overestimation 和 CIVO**——高 DoF 环境（Humanoid/Quadruped）baseline 本身会 NVE>>2.0，这不是 CIVO（没有 dt-embedding），不能用 CIVO 术语描述
3. **Worker A citation audit 不可信**——3/4 findings 是 hallucination，已 retracted。只信 Worker B/C 的结果
4. **D176 vs ROADMAP 投稿目标**——D176 写 AAAI 2027，但后续决策覆盖为 ICLR 2027，ROADMAP 已标注
