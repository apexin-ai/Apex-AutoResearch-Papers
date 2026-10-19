---
loop: 5
reason: max_wall_time
updated: '2026-05-25T14:43:31+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-29046 只能用 cuda:0 和 cuda:1，越界立即 CRITICAL
- exp-003-s3 训练在 cuda:1（PID 31718），不要 kill 或抢占
- exp-003-s2 eval 在 cuda:0（PID 33822），sequential chain 会自动跑 ckpt-3000
- 论文 abstract ≤ 200 words，正文 ≤ 8 pages，Limitations 在正文内且只能有一个

### 2. 🖥️ 基础设施快照
- 服务器：westd-29046 (root)，2× NVIDIA RTX PRO 6000 Blackwell 96GB
- 远程代码：`/root/contrastive_entrain_calib`
- 本地 paper：`/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/`
- Python：`/root/miniconda3/bin/python`（conda base，不用 venv）
- 模型：`/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B`
- HF 必须 `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1`（网络不通）
- 活跃进程：
  - PID 31718 (tmux=exp-003-s3, cuda:1)：R3-only GRPO seed=44 训练，step ~124/8000，ETA ~56h
  - PID 33822 (cuda:0)：exp-003-s2 eval chain，ckpt-2500 进行中，ckpt-3000 自动排队

### 3. 📊 当前状态
刚完成的审查：
- fig_teaser v3 通过（数据与 Table 3 逐点一致）
- fig_framework v2 通过（所有数字与 registry 匹配，5.1× vanilla 已验证）
- fig_probe_trap_mechanism v2 通过
- paper-data-audit 通过（appendix.tex 一处修改正确）
- appendix-ref-audit 通过（两处交叉引用补充正确）
- seed4 eval 全部完成：peak 0.368 at ckpt-1500，pattern 与 seed2/3 一致但 terminal SYCONScore 显著不同（0.343 vs 0.085）
- exp-act-256 CRITICAL 已报：训练 killed at step 200/8000，无 checkpoint，GPU 1 空闲后被 exp-003-s3 接管
- github anonymous push 通过，但 git commit email 未修改（仍含 AWS 区域信息）

等待中：
- exp-003-s2 eval (ckpt-2500 + ckpt-3000) 结果，预计 ~2.5h 完成
- exp-003-s3 训练完成，预计 ~56h
- exp-act-256 是否重新启动（Director 未回复）
- git email fix 是否重做 force push（Director 未回复）

### 4. 📋 待办
- exp-003-s2 eval 完成 → 读取 ckpt-2500/3000 结果，更新 registry，编译 s2 完整轨迹（已有 ckpt4000/7500/8000 旧结果）
- exp-003-s3 每个 save_steps checkpoint → 可以开始 eval（但需等 cuda:0 空闲或 s2 eval 完成）
- Director 决定重启 exp-act-256 → 审查新启动的 GPU 合规和脚本修改（建议 save_steps=200）
- 论文更新 "two seeds (42, 43)" → "three seeds (42, 43, 44)" → 审查修改一致性
- 任何 paper_agent_request_review → 加载 paper-quality-lessons.skill.md，按 §5.3 模板评分

### 5. 🎯 战略上下文
- 核心结论：d_syc 方向能诊断不能当 reward。三条证据链：cosine R1 结构性失败 → probe reward trap（行为死亡领先分布崩溃 1300 步）→ ACT per-token SFT 成功（31/31 > vanilla）
- 论文 Goodhart 定位：regressional variant，不是 extremal/causal/adversarial
- **易错点 1**：probe_trap.tex L10 写 "~30 steps" 但 registry 实测 ~50-60 steps，已报 warning 但未修改
- **易错点 2**：seed4 terminal SYCONScore (0.343) 远高于 seed2/3 (0.085)，不能简单 claim "所有 seed 最终退化到 vanilla 以下"
- **易错点 3**：paper 中 "31/31" 是 ACT 的，不是 SFT probe penalty 的。SFT probe penalty 三 seed 是 11/15 > vanilla
- **易错点 4**：discussion.tex 的 held-out 值已从 0.205/3.7× 更新为 0.284/5.1×，旧值不再出现
- exp-act-256（ACT 256 样本消融）是消除 data-size confound 的关键实验，死了需要重启
