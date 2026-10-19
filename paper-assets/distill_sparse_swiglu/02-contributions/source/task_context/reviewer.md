---
loop: 15
reason: idle_timeout
updated: '2026-05-25T17:59:26+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westd-34887 的 GPU 白名单需从 `execution.gpu_ids` 读取，每次审查训练实验必查 `nvidia-smi` 核对进程是否越界
- SVD-CSP bib 标题仍是错的（references.bib L7），实际标题 "SVD Contextual Sparsity Predictors for Fast LLM Inference"，当前是 AI 编造标题——提交前必须修复，已标 CRITICAL 两轮但截至 f62442f 仍未改
- Qwen14b GSM8K s456（0.2608）使用了 batch_size=8，与 s42/s123 的 bs=1 不一致，论文已改为 2-seed mean（35.8）并脚注排除 s456——不要把 s456 数据当可信结果引用
- STE 30% 实际 sparsity 仅 20.8%（M042），已从 Table 4 排除（D090）——不要在任何对比中把 ste_30_s42 当 30% sparsity 实验

### 2. 🖥️ 基础设施快照
- 服务器：westd-34887(root)，代码根目录 `/root/distill_sparse_swiglu/`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/`
- 论文源文件在本地 workspace `paper/` 目录，不在远程服务器
- 匿名仓库最后同步 commit：`c237706`（abstract polish）+ `2ba3c9f`（orphaned appendix refs fix）
- 本 session 全程 GPU idle，无活跃训练进程
- registry 中 PREPARING：`mistral_kl30_s42_ppl`、`qwen14b_kl30_s456_gsm8k_bs1`（均未实际启动）

### 3. 📊 当前状态
DDL 日（2026-05-25 EMNLP ARR）。我完成了：
- Round 30 行动方案独立审查（5 问全答，已 post to Director）
- W4（STE sparsity）+ W6（SVD-CSP）补充项审查
- P1-P8 claim-strength calibration 逐项对抗审查（commit 08f0ce8）
- P6/P7 修订版审查（commit f62442f）

**审查结论**：P1-P6, P8 全部 PASS。P7 bib 标题仍错（CRITICAL），其余均通过。Conclusion L5 缺 "shared hyperparameters" 限定（INFO 级建议）。

等待中：Director 处理 bib 标题修复 + 最终 PDF 编译 + 匿名仓库同步。无 Worker 回调或 Cron 待触发。

### 4. 📋 待办
- bib 标题修复 commit 出现 → 验证 references.bib 标题与 arXiv 2603.14110 一致
- 最终 PDF 编译完成 → 如果 Director 要求视觉审查，加载 `paper-visual-review` skill 检查排版
- 提交后如有新审稿意见（ARR R1/R2 反馈）→ 加载 `rebuttal` skill 辅助回应
- `qwen14b_kl30_s456_gsm8k_bs1` 如果被启动 → 核查是否用 bs=1、结果是否改变 3-seed 统计

### 5. 🎯 战略上下文
核心结论链：KL > BCE/MSE/JSD/RKL（signal type gap 9.47 PPL under shared HP, narrows to 8.45 with fair-LR MSE）→ target-swap ablation 证明 KL 的价值在于发现更好 mask pattern 而非 E2E coupling → knowledge regression 是 allocation-induced + output-distribution 双因素（非 "systematic"）→ cross-arch generalization on PPL, directional decline on knowledge tasks (n=3)

最容易判断错的事：
1. **MSE 的 18.52 和 per-layer MSE 的 18.52 是同一个数**——MSE 天然 per-layer，不存在"E2E MSE coupling"，所以 signal type gap 计算直接受 MSE LR sweep 影响
2. **"systematic" 不是全部要删**——conclusion L4 "systematically compared"、experiments L73 "gap is systematic" 是 methodical/consistent 语义，合法保留
3. **匿名仓库和本地 workspace 是两套**——论文修改在本地 `paper/`，需要额外 sync 到匿名仓库才能提交
