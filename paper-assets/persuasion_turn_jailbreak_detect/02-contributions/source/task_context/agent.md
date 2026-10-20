---
loop: 4
reason: idle_timeout
updated: '2026-05-25T06:49:35+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目当前无分配 GPU（gpu_ids=[]），不可启动任何训练实验
- 服务器 autodl-5090 和 gpu-5090-4x-3 已下线（同一 IP，不可达），不要尝试连接
- westd-33183 磁盘仅 4.2GB 可用，禁止在上面下载大文件或跑新实验
- 匿名仓库 PAT 在 remote URL 中，push 时不要泄露到日志；仓库名 anonymous-nlp-2026/persuasion_turn_jailbreak_detect
- EMNLP 2026 ARR May DDL = 2026-05-25（今天），主文严格 8 页（Limitations/References 不计）
- fig4_svd_subspace / cka_heatmap / embedding_tsne 保持当前样式，Director 已决定 DDL 前不改
- Figure 1 (v4 architecture) Director 说"先不动"，用户在单独修 PaperBanana bug

### 2. 🖥️ 基础设施快照
- 服务器：westd-33183，account=root，工作目录 `/root/persuasion_turn_jailbreak_detect`
- Python：需 SSH 探测（之前用 aml-train 镜像，conda base 环境）
- 模型 checkpoints：`/root/autodl-tmp/persuasion_turn_jailbreak_detect/checkpoints_archive/`（plan_002=9class, plan_003=scrambled, plan_017=MLM）
- 本地论文目录：`/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/`
- 本地图表脚本：`docs/paper/figures/paper/*.py`（fig2/fig3/fig_hierarchy_reversal/fig_fpr_adaptation/fig_layerwise 已统一样式）
- 无活跃进程 / 无 tmux session / 无 cron 任务

### 3. 📊 当前状态
刚完成 DDL 前最后一轮修改：
- **R23 审稿修复**（Tier 1-3 写作修正全部完成）：abstract MF2/M1、intro MF3、experiments SF7、appendix SF3/SF4/SF10、conclusion SF8
- **新增 2 张主文图**：fig_hierarchy_reversal（Discussion）+ fig_fpr_adaptation（Section 4.8），已插入 tex
- **FPR 图数据修正**：ShareGPT N=10 从 7.5→10.5%，N=25 从 1.0→2.7%（3-seed mean），OASST2 标注 single seed，加 error bar
- **ShareGPT 文字补充**：Section 4.8 加 "(consistent across WildChat, OASST2, and ShareGPT; ...)"
- **Related Work + Setup 压缩**：腾出 ~15 行排版空间容纳新图
- **图表统一美化**：6 张图统一 serif/300DPI/pdf.fonttype42
- **编译确认**：Discussion/Conclusion/Limitations 在第 8 页，References 第 9 页 ✓
- Registry：无 RUNNING/PREPARING 实验
- 无等待中的 Worker/Cron 回调

### 4. 📋 待办
- Director 确认所有修改 OK → spawn worker 同步到匿名仓库（`/tmp/anon_repo/`，上次 commit 09cb5f8 只含匿名修复，R23 修改 + 新图尚未 push）
- 提交前 → 全文 PDF 逐页视觉检查（特别关注：表格是否有 resizebox、图表是否被裁切、cross-reference 是否正确）
- 提交前 → abstract word count 确认 ≤200 words
- 提交前 → 检查 `\ref` 和 `\cite` 无 `??` 未解析引用
- 如 Director 要求最终 S3 备份 → 用 `backup_project_to_s3`

### 5. 🎯 战略上下文
- **核心发现**：classification DAPT 在 synthetic OOD 上恢复检测（F1 0.97-1.0 vs vanilla 0.26-0.31），但 hierarchy 在 human single-turn 上反转（MLM 0.837 vs classification 0.596）——condition-specific，非 universal
- **论文 framing**：ablation framework（非 SOTA 方法论文），7 个 DAPT 变体 × 多 OOD 条件的 controlled decomposition
- **易错点**：
  - ShareGPT 在图中但不在 appendix 表格中，只有 exp66 artifacts 里有数据——如果 reviewer 追问需要补 appendix 表
  - OASST2 适应曲线全部 seed 42，WildChat 适应曲线除 N=0/10 外也是 seed 42——这是 Limitations 中已覆盖的点
  - PaperBanana (gemini-2.5-pro) VLM critic 有 bug（thinking model 返回 None），所有图都走 matplotlib 手写，不要再试 PaperBanana
  - 匿名仓库 push 需要用 `/tmp/anon_repo/` 中的 PAT remote，不要用主仓库 remote
