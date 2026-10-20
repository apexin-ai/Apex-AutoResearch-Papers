---
loop: 17
reason: max_messages
updated: '2026-05-29T08:03:13+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-51268 只有 1 张 GPU（cuda:0）。cuda:1 不存在，resources.yaml 误配。不要尝试在 cuda:1 上启动任何实验。
- D171 数据锁定：已有 Walker/Cheetah 实验数据冻结，不能重跑或修改。新环境（Quadruped）实验不受限。
- D177/D178：Humanoid 环境已排除（baseline NVE=12.97×，CIVO-prone baseline 无法做有效对照）。不要再安排 Humanoid 实验。
- 论文投稿目标 ICLR 2027（~10月 DDL），当前处于环境扩展阶段。不要 fallback 到更低会议。

### 2. 🖥️ 基础设施快照
- 服务器：westd-51268，工作目录 /root/event-gated-adaptive-horizon（推测，需确认）
- GPU：1× NVIDIA RTX PRO 6000，cuda:0
- Python/conda：aml-train 镜像，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 活跃进程：exp_quadruped_baseline_s0_r2（PID 42263，cron 监控中）
- 磁盘：根分区 4% 使用（400GB 可用）
- 论文本地路径：`/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/`

### 3. 📊 当前状态
**刚完成**：论文全套自检（数据审计 10+ fixes、前向引用 8 fixes、匿名化 5 fixes、引用审计 4 fixes、Limitations 重写、8 页布局调整）。编译 0 errors 0 warnings。
**RUNNING**：exp_quadruped_baseline_s0_r2（Quadruped Walk dt=1 baseline，200K steps，上次报告 112K/56%，预计再 ~2h）
**QUEUED**：exp_quadruped_008d_s0（等 baseline 完成后串行提交到 cuda:0）
**待确认**：上一轮 Agent 有个 Worker 在做"Table error bars/std 补充"，session reset 前未汇报。已派新 Agent 跟进。

### 4. 📋 待办
- quadruped_baseline 完成 → 检查 NVE 是否全程 <2.0（确认 baseline-healthy）→ 如 healthy 立即启动 exp_quadruped_008d_s0
- quadruped_baseline NVE 持续 >2.0 → Quadruped 也排除，需讨论新环境选择
- exp_quadruped_008d_s0 完成 → 与 baseline 对比，判定 Quadruped 是否复现 CIVO → 更新论文 scope expansion 数据
- Table error bars 完成 → 检查 Table 1/3 多 seed 行是否已补 std → 重新编译 PDF
- GPU 空闲时间 >10 min → 从 ROADMAP 待排队实验中找下一个填充

### 5. 🎯 战略上下文
- 核心结论：CIVO 是 trained dt-embedding + multi-rate exposure 在 imagination-based AC 中的系统性失败模式。Walker/Cheetah 已充分验证（103 成功实验），当前在做环境扩展（Quadruped）加固 generalization claim。
- 44 个 negative 结果（干预失败）本身是论文贡献的一部分（"interventions fail" 是 core finding），不是 story 的弱点。
- Quadruped baseline 的 NVE@95K 有一次 transient spike 到 17.4，@105K 回落到 1.85。这是小分母效应（eval@95K=22.5），不是系统性 CIVO。如果后续稳定 <2.0 则 baseline healthy。
- 易错：不要把 resources.yaml 中的 cuda:1 当真——物理上不存在。需要并行只能申请新服务器。
