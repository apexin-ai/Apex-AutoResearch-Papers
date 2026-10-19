---
loop: 10
reason: max_messages
updated: '2026-05-29T09:03:21+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 westd-35807 和 westd-45947 上已分配的卡，不可跨项目抢卡
- westd-45947 磁盘仅剩 ~10GB，禁止在上面下载大文件/模型
- 论文已进入 CoRL 2026 审稿阶段（review_chat_id: `oc_ec359a7b7a5e3b28b379b61588c6e853`），Review Director 团队独立负责审稿，Research Director 不参与格式/投稿材料准备
- `vlariskanon2026` 已从 bib 删除（ICLR 2026 拒稿），绝不能重新引入
- paper_switch 有 Scenario B 和 Scenario C 两套叙事，修改正文后必须跑 `paper_switch.py --verify` 确认 19/19 anchors OK

### 2. 🖥️ 基础设施快照
- 服务器：westd-35807 (connect.westd.seetacloud.com, 1/4 GPU 可用, 磁盘 77%) + westd-45947 (1/2 GPU 可用, 磁盘 96%)
- 代码路径：`/root/colliforce-vla`（远程）
- 论文路径：`/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/`（本地）
- 最终 PDF：`docs/paper/main.pdf`（v7，已上传用户）
- RUNNING 实验 2 个：`train_pi05_a1_obj_s3_l01_v2`（westd-45947）、`train_pi05_lora_baseline_s3_v2`（westd-35807）——seed3 rebuttal 统计 power 用
- W&B / Git 未配置
- 137 个实验总计，134 完成

### 3. 📊 当前状态
本轮完成了投稿前最后一轮排版修改：
- 引用审计修复 7/7（删除 3 条问题引用，33→30）+ 匿名化扫雷（0 残留）
- Figure 3（scatter+oracle bar）和 Figure 5（lambda curve+fingerprint）合并为 subplots 单图，高度对齐问题彻底解决
- 从 Appendix 提升 3 项素材到正文（displacement 图、SSR 表、cross-scene 表），正文填充到第 8 页
- Table 3 note 合入 caption
- PDF v7 已交付用户，等用户确认后提交 CoRL 2026 OpenReview
- 两个 seed3 实验仍在 RUNNING，不阻塞提交

### 4. 📋 待办
- 用户确认 PDF → 提交 CoRL 2026 OpenReview（检查 supplementary / 所有字段是否就绪）
- 用户对论文定位有疑虑（刚问"这篇是方法性文章吗"）→ 如果用户想调整 framing，需要快速响应，DDL 是 2026-05-29
- seed3 实验完成回调 → 记录结果到 registry，不影响当前论文版本（rebuttal 储备数据）
- 如果用户要求 resubmit_paper_to_review → 调 `submit_paper_to_review` 提交新版给 Review Director

### 5. 🎯 战略上下文
- 这是 **empirical analysis / negative-result** 论文，不是方法论文。核心贡献：(1) dfCAR 度量揭示 action collapse 污染 CAR；(2) EE-only SDF 监督无法提供全身碰撞规避（oracle + 训练均为 negative）
- 论文叙事有 Scenario B（SDF redundancy confirmed）和 Scenario C（marginal signal），paper_switch 控制。当前用 Scenario C
- 用户问论文定位可能暗示对 negative-result 投 CoRL 有顾虑——如果用户进一步追问，不要主动建议降级会议（L1 红线），可以强调 negative result 对社区的价值
- D044 决策：审稿回应策略——写作级修复 + 统计重分析，Claim 3 降级，scope 收窄到 single VLA family
- 45 条决策日志在 `decisions.yaml`，错题本在 `mistakes.yaml`
