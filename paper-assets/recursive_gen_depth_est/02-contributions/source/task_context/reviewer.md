---
loop: 18
reason: idle_timeout
updated: '2026-05-24T19:17:50+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 `gpu-6000pro-2`，GPU 白名单 `gpu_ids=[0]`（仅 cuda:0），审查训练实验时核对 CUDA_VISIBLE_DEVICES 是否越界
- 论文 FPR 数据：结论段已改为 "15–34%" raw / "below 7%" calibrated，不可回退到旧版 "2–3%"（RedPajama 6.98% 曾触发 CRITICAL）
- Wild data 解读约束 C004：RF 分类器 d1+ 预测是 OOD FPR，禁止说 "contamination" / "AI-generated content detected"
- fig_confusion_matrix 已移回附录，Figure 5 现在是 fig_transfer_comparison——不要误认为正文有 confusion matrix
- Abstract 硬限 200 words / Limitations 仅一个放正文 / appendix 不能有 limitations section

### 2. 🖥️ 基础设施快照
- 服务器：`gpu-6000pro-2`，远程代码根目录 `/root/autodl-tmp/recursive_gen_depth_est`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/`
- 论文目录：`docs/paper/`，编译产物 `main.pdf`（~25-27 页，8 页正文 + Limitations + References + Appendix）
- Registry：`registry.yaml`，150 实验（95 success, 14 negative, 17 failed）
- 活跃进程：无。全部实验已完成，GPU 空闲。Director 此前确认不再跑新实验。
- 无 tmux session / cron 任务 / W&B 活跃 run

### 3. 📊 当前状态
项目处于投稿前终态——论文定稿完成，等用户确认投稿/归档。本轮（Loop #18）仅执行了服务重启后的状态验证：
- Registry 确认 0 RUNNING 实验，2 PREPARING（accum_v2_mix25/mix50）均已标记 killed/SUPERSEDED
- report.md 最后更新 2026-05-23，ROADMAP 最后更新 2026-05-20
- 已向 Director 发送 info 级恢复确认
- 无等待中的 Worker 回调 / Cron / Director 决策

### 4. 📋 待办
- Director 要求审查论文修改 → 注意 8 个仍未引用的 orphaned appendix sections（app:depth4_ext, app:detector_baselines, app:zeroshot_prompt, app:e2e, app:ref_ablation, app:learned_estimator, app:multi_tau, app:domain_bias），优先级低但审稿人可能注意到
- 论文修改涉及 Discussion → 建议加一句 FPR 到 "Deployment considerations"（目前 FPR 只在 Limitations 提及）
- Contribution 3 措辞被质疑 → 建议 "Accumulation robustness" 改为 "Accumulation characterization"（claim 强度与证据更匹配）
- 用户决定投稿 → 检查 abstract word count、limitations 位置、appendix 无 limitations section

### 5. 🎯 战略上下文
- 论文核心结论：(1) perplexity tail features 主导 depth signal，(2) strategy effect > model effect，(3) scale attenuation at 14B
- 7B self-reference ceiling（52.1%, EDD=0）是关键发现，已整合到 Discussion 但未进 Abstract——审稿人可能追问
- 模拟审稿预测 Overall 3.0（Findings 线），修改后预期 3.0-3.5
- **易错点 1**：本地 workspace 和远程服务器可能有同名文件版本不同（论文在本地，代码/数据在远程）。断言"未修改"前必须双边核对
- **易错点 2**：cross-strategy 数据（64.9/59.0/53.3）是从附录表按模型取均值计算的派生值，不是 registry 直接记录的——修改附录表会连锁影响 Figure 5
- **易错点 3**：Explore agent 曾报告不存在的文本位于特定行号——永远用 Grep/Read 独立验证
