---
loop: 10
reason: max_wall_time
updated: '2026-05-29T17:49:05+00:00'
---

### 1. 🔴 硬约束 / 红线
- 两台服务器 GPU 白名单：westd-35807 cuda:0, westd-45947 cuda:0（各只有 1 张卡）
- 论文 page limit: 正文 8 页含 Limitations（CoRL 2026 硬性要求）——Limitations 溢出 ~2 行尚未确认修复
- Supplementary README 有 3 处 critical 超参错误（lr 5e-5→2.5e-5, batch 4→32, lambda {0,0.005,0.05,0.1}→{0.005,0.01,0.1}）——尚未确认修复+repack
- 论文数据全部用 rotation-fixed reeval v2 系列（eval_seed=7, n=200），不可混用旧 eval 数据
- LoRA s2 来自 `eval_lora_s2_30k_v2`（非 reeval 系列），协议一致性若被审稿人追问需说明

### 2. 🖥️ 基础设施快照
- **westd-35807**: Connection refused（实例关机，需用户登录 AutoDL 重启，端口可能变）
  - 工作目录: /root/colliforce-vla, Python: /root/miniconda3/bin/python, conda base
  - LeRobot 有 4 处手动 patch（lerobot_dataset.py + utils.py），重启后需 grep 验证
  - 训练任务: LoRA baseline seed3（可能已跑完，需检查 checkpoint）
- **westd-45947**: Connection refused（同上）
  - Checkpoints: /root/autodl-tmp/checkpoints/（250G，磁盘曾 100% 满，清理后 47G 可用）
  - 模型权重: /root/autodl-tmp/openpi_weights/ (32G，不可删)
  - 训练任务: SDF λ=0.01 seed3（从 step 2000 resume，可能已跑完）
- **Feishu API**: 月配额耗尽，无法通知用户
- **本地 workspace**: /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/
- 无活跃进程/tmux/cron（服务器均不可达）

### 3. 📊 当前状态
**刚完成**：对 rebuttal_prep.md（25 Q&A）完成二次验证全 PASS；审查了 seed3 contingency 版本（Version A/B）、per-task 分析、camera-ready polish checklist、supplementary zip。

**Registry**: 0 个 RUNNING。137 实验全部终态（73 success / 25 negative / 22 failed / 16 killed）。

**等待中**：
- 用户确认 PDF → 提交 OpenReview（阻塞于 Feishu API + 服务器不可达）
- 服务器恢复 → 启动 seed3 实验（restart plan 就绪：artifacts/seed3_restart_plan.md）
- Agent 正在补强 3 个统计方法论 Q&A + oracle n=1 标注（我审计要求的）

### 4. 📋 待办
- 服务器恢复 → 按 seed3_restart_plan.md 检查 checkpoint（可能已跑完）→ 优先 λ=0.1 seed3（信息量 > λ=0.01）
- seed3 数据到达 → 按 rebuttal_seed3_versions.md decision matrix 路由到 Version A 或 B → 替换 placeholder → 更新 rebuttal_prep.md
- Agent 提交统计 Q&A 补强 → 验证 3 项：one-tailed defense、s2 非异常值论证、permutation vs Welch justification
- PDF recompile 通知 → 验证 page overflow 是否修复（Limitations 必须在 page 8 内）
- Supplementary repack 通知 → 验证 README lr/batch/lambda 三处是否已修正

### 5. 🎯 战略上下文
**核心结论**：3 Claims——(1) CAR 被 action collapse 污染，99.6% fake safe，dfCAR 修正；(2) EE-only SDF oracle 全部劣于 baseline（73-77% vs 79%），结构性不足；(3) SDF 冗余，avoidance 来自 demo data（p=0.155 双尾，per-task fingerprint 完全一致）。

**最易判断错的事**：
- p=0.155 处于灰色地带——seed3 可能把 p 推向任一方向。Version B（signal recovered）需要 narrative shift 但不改变核心贡献。已有 pre-written 两版 Q&A。
- "26pp CAR improvement" 是 Pi0.5 baseline (28.5%) → LoRA (54.83%) 的差值，不是 SDF 贡献。容易混淆。
- displacement metric 有历史混淆：LOG 文件记录的是 obstacle displacement，JSON 记录的是 EE displacement。Claim 1 用 obstacle displacement。
- reference audit 发现的 2 处 citation context 错误（Diffusion Policy 非 VLA、loss collapse ≠ action collapse）和 3 处过时 venue 信息——不确定是否已修复，需跟踪。
