---
loop: 26
reason: idle_timeout
updated: '2026-05-25T06:13:07+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 cqa1-21977，项目 gpu_ids 需从 constraints.yaml 确认（2026-04-24 有越界事故）
- 论文 DDL: EMNLP 2026 via ARR，2026-05-25（今天）
- Phi-4/Gemma-2/OLMo-2 per-seed 原始数据在 westd server，cqa1 无法直接验证——但 Qwen-7B 三 seed GSM8K 数据已在 cqa1 验证完毕
- Table 2 Qwen-7B GSM8K Δ=+10.1pp 是 mean(s42, s123)，排除了 s0=+7.89pp 但无脚注——已 post warning 给 Director，等回复决定是加脚注/改值/保留

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977，远程代码根目录 `/root/contamcal-irt-calibration`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/`
- 论文源码：`docs/paper/`（main.tex 入口），图表脚本：`docs/paper/figures/` + `figures/paper/`
- 审计数据：`artifacts/data_audit_part3_crossseed_volume.md`
- 活跃进程：无（registry 0 RUNNING，42 PREPARING 全部 killed/failed/stale）
- 备份：3 个 tar.gz 共 7.8G；`/root/democalib/` 3.1G 非 git 数据仍在服务器

### 3. 📊 当前状态
刚完成 Loop #26 最终提交前全面检查，已 post 审查报告给 Director。

确认已修复：
- "three→four cross-family models"（experimental_setup.tex:9）✅
- Phi-4 跨图一致性（Fig3 range=(-0.17,+1.83), Fig4 mean=+0.73, CI=[-0.17,+1.39]）✅

确认合规：Abstract 188 words, Limitations 1段3点, 匿名化正确, ACL review mode ✅

新发现 1 warning：Table 2 Qwen-7B GSM8K s0 排除无脚注（已 post Director）

registry: 433 总实验，0 RUNNING/活跃。项目在最终提交阶段。

### 4. 📋 待办（条件触发式）
- Director 回复 Table 2 Qwen-7B warning → 确认修复方案（加脚注/改值/保留）→ 验证修改
- 提交完成 → 进入等待审稿状态，切换到 rebuttal 准备模式
- 收到 ARR reviewer comments → 加载 `rebuttal.skill.md`，逐条审查 reviewer 意见并辅助 response letter
- Appendix F internal label (`tab:s1_pipeline` / `tab:s1_domain`) 对读者不可见，不需要修

### 5. 🎯 战略上下文
- 论文核心贡献：(1) dose-response taxonomy（Immune/Benefit/Collapse/V-recovery），(2) DiD 排除 item-level memorization，(3) ContamCal IRT 框架的 domain-level γ_d 分析
- Social Sciences γ_d < 0（99.7% posterior probability）是最强 domain-level finding；pooled γ 不显著是 dilution masking 的证据
- 最容易判断错的事：
  - Table 1 的 Phi-4 Δacc "±0.5pp" 是定性描述（≈0），不是精确数值——s42 实际是 -0.17pp
  - cross_seed_ranges（Figure 3）是 raw min/max，cross_seed CI（Figure 4）是 BCa bootstrap CI on the mean——概念不同，不能直接比较 bound
  - Table 2 GSM8K 列各模型 seed 选择不统一：有的用 s42，有的用 mean(s42,s123) 排除 s0——OLMo-2 有脚注，Qwen-7B 没有。Qwen-7B 的 s0 (+7.89pp) 不是明显 outlier（不像 OLMo-2 s0 +9.2pp vs mean 2.05pp），排除缺乏明确 justification
  - "86% (6/7)" ARC direction agreement 包含 LLaMA-3.1，不含 Falcon3 ARC——这已验证正确但容易误查
  - Qwen-7B d005 GSM8K "+6.4pp" 用的是 s42（已验证：76.95-70.58=6.37pp），正确
