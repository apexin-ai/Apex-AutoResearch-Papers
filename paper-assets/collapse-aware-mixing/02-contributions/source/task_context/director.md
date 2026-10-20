---
loop: 6
reason: max_wall_time
updated: '2026-05-14T14:51:21+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只有 1 张 GPU：cuda:0（服务器 cqa1-38874 只有 1 张卡），不存在其他可用 GPU
- 用户已明确表态"成功率很低直接归档，没什么希望了"——seed0 r2 是最后一个实验，结果出来后大概率归档
- paper_framing.md 已标记 SUPERSEDED，当前 framing 参考 artifacts/narrative_draft.md
- 禁止在 seed0 r2 结果出来前启动任何新实验或做最终方向决策

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-38874 (connect.cqa1.seetacloud.com)，GPU: NVIDIA RTX PRO 6000 Blackwell 96GB × 1
- 工作目录：/root/collapse-aware-mixing
- 数据/输出：/root/autodl-tmp/（117GB 剩余）
- v7 数据：/root/autodl-tmp/output_v7/
- 分析脚本：analyze_seed0_vs_v7.py 已部署在服务器上，seed0 完成后可立即运行
- 活跃进程：mvp_seed0_replication_r2 (PID 122208, cuda:0)，cron 监控中
- Plan A 代码就绪：controller.py + controlled_pipeline.py + run_plan_a.sh，集成测试已通过

### 3. 📊 当前状态
刚完成 Manager 要求的新颖性自查报告（已发 A 群）。结论：新颖性中等偏弱，EMNLP Findings 或 Workshop 现实，Main Conference 不够。

Registry:
- mvp_seed0_replication_r2: RUNNING — seed=0 robustness 验证，G1 阶段进行中，预计还需 ~6-8h
- mvp_pilot_v8/v8_r2/v3/v2: 已标记 killed（清理完毕）
- 其余 7 个实验全部 DONE（0 成功 / 2 阴性 / 5 失败）

Agent 已发指令：seed0 完成后立即跑 analyze_seed0_vs_v7.py，重点看 G1/G2 holdout eff_rank 走向。

### 4. 📋 待办
- seed0 r2 完成 cron 回调到达 → Agent 跑 analyze_seed0_vs_v7.py → 逐代对比表汇报
- G1/G2 eff_rank 反升复现 → 向用户汇报，但用户已倾向归档，需用户明确 GO 才能继续 Plan A
- G1/G2 eff_rank 未复现 → archive_project("collapse-aware-mixing", reason="...") 归档释放 GPU
- 归档前更新 memory：沉淀"spectral eff_rank 在 iterative collapse 中反升"这一发现（无论是否发论文，这个 finding 对其他项目有参考价值）

### 5. 🎯 战略上下文
- 核心发现：eff_rank 在 model collapse 中反直觉上升（+0.96%），但只有 seed=42 一个数据点。seed=0 是最后验证
- D014 决策：原假设（eff_rank 是 leading indicator）definitively falsified
- D018 决策：MVP FAIL，三条路径全封
- Pivot B 也已阴性：generated eff_rank 比 n-gram entropy 无额外价值（检测延迟 2 倍）
- narrative_draft.md 的 Reviewer 修正已完成：seed0 改为 conditional 表述、573× 噪声比改为检测延迟对比、Claim 3 标注 speculative
- 易错点：不要因为 Plan A 代码就绪就冲动启动实验——用户已表态倾向归档，必须等 seed0 结果 + 用户明确同意
- 易错点：GPU 利用率 10-25% 是 autoregressive generation 阶段的正常水平（memory-bandwidth bound），不是问题
