# reviewer / loop_3.md

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`368e6f73d578f2f6f48f.json`](../../sessions/36/368e6f73d578f2f6f48f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-14T08:21:59+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：westd-22162 cuda:0/1/2/3（4 张 RTX PRO 6000 Blackwell）。无越界历史，但须持续监控。
- 论文数据必须基于 bf16 实验（D019/D020 决议），fp16 v6 系列因 NaN 选择偏差（15.3% 跨条件不一致）已废弃，不可用于 claim。
- Bootstrap B 值：bf16 系列 n_bootstrap=10000，论文才能声称 B=10,000 + p<10⁻⁴。实际 fp16 系列只有 B=1000（D023 确认）。
- 论文 high-phase II 统一用 median 报告（D027），gradient 用差值 ii_low−ii_high（D031/D032），ratio 降为 appendix。
- Qwen s015 Cohen's d=0.28 CI含0 不显著（D037/D038），论文 dose-response claim 须写 "s≥0.20 for Qwen, s≥0.15 for DeepSeek"。
- DeepSeek Cohen's d 实际值 0.44→0.52→0.68→0.80（D035/D036），D033 原值 0.60→1.12 高估 25-45%，已废弃。

### 2. 🖥️ 基础设施快照
- 服务器：westd-22162（root），4× RTX PRO 6000 Blackwell Server Edition 97GB
- 工作目录：`/root/autodl-tmp/pacs`
- Python：`/root/miniconda3/bin/python`（conda base 环境），dtype=bf16
- 模型：DeepSeek-R1-Distill-Qwen-7B 在 `/root/autodl-tmp/pacs/checkpoints/`；Qwen2.5-7B-Instruct 下载中（ModelScope PID 89564 + HuggingFace CLI PID 58322 双路下载）
- 数据：`/root/autodl-tmp/pacs/data/math500.json`（50 problems）
- 活跃进程：
  - c4_entropy（PID 93190，tmux=c4_entropy 实际在 pts/4，cuda:1，~15GB VRAM，进度 19/30+）
  - Qwen 模型下载 ×2（PID 89564 ModelScope + PID 58322 HuggingFace CLI）
- bf16 profiling 输出：`/root/autodl-tmp/pacs/profiling_output_bf16_*`
- 无 wandb 配置（不检查 wandb）
- 无 cron 任务活跃

### 3. 📊 当前状态
**我刚完成的审查**：
- Qwen importance 4/4 PASS（C5 confirmed，D034）
- DeepSeek Cohen's d 修正审查（D035/D036 PASS）
- Qwen Cohen's d 审查（D037/D038：s015 不显著，需叙事调整）
- bf16 DeepSeek random 全系列审查（4/4 FAIL as expected，D029/D30 outlier 问题已标记）

**Registry 活跃实验**：
- `c4_entropy` — RUNNING，cuda:1，C4 mechanism 直接验证（attention entropy + Gini），19/30+
- `bf16_qw_rand_s015` — ANALYZING（刚完成，待 Worker 分析）
- `bf16_qw_rand_s020` — ANALYZING（刚完成）
- `bf16_qw_rand_s025` — ANALYZING（刚完成）
- `bf16_qw_rand_s030` — QUEUED（等 GPU，cuda:0/2/3 现已空闲）

**等待中**：
- 3 个 ANALYZING 实验的 Worker 回调已触发（hook on_complete），等 Agent 分析结果
- bf16_qw_rand_s030 需 Agent 启动到空闲 GPU

### 4. 📋 待办（条件触发式）
- bf16_qw_rand_s015/s020/s025 分析结果出来 → 核实 random 4/4 FAIL（median flat ~1×，无 phase gradient）；检查是否复现 D029/D030 的 mean-based outlier 问题
- bf16_qw_rand_s030 完成 → 核实 Qwen random 全系列 FAIL，与 DeepSeek random 模式一致
- c4_entropy 完成 → 独立核实 entropy collapse + Gini 数据是否支持 C4 claim；检查 importance vs random 分组对比
- Qwen random 全部完成 → cross-model permutation test 需审查：difference statistic（非 ratio），Bonferroni 校正
- 论文 §5 Results 初稿 → 按写作审查模式 B 审查，重点：数字与 registry 一致性、bf16 数据源、Cohen's d 用修正值、Qwen s015 caveat
- Cohen's d 计算文件 `cohens_d_bf16.json` 需核验存在且论文引用正确值

### 5. 🎯 战略上下文
**核心结论**：Phase-modulated compound sparsity severity——importance-based eviction 的 compound interaction severity 随 sparsity 单调递增（DeepSeek median diff: 0.39→1.48→7.16→14.59；Qwen: 0.039→0.235→1.268→2.943），random masking phase-independent（全部 FAIL）。Cross-model direction 一致，Qwen magnitude ~1/5 DeepSeek。

**决策链精要**：D001 MVP（phase reversal）→ D010 FAIL pivot → D013 importance metric bug → D014 发现 phase-modulated severity → D015/D016 GO → D017 bootstrap CI confirmed → D019/D020 fp16 NaN 强制 bf16 重跑 → D031/D032 差值替代 ratio → D033-D038 Cohen's d 修正 + Qwen cross-model

**下一个"我"最容易踩的坑**：
1. **不要信 ratio 类 gradient 数字**——registry 中 gradient_paired_aggregate 字段定义跨实验不一致（D033），有的是 median ratio，有的是 mean difference。论文只用差值。
2. **Random baseline 的 mean 不可信**——1-2 个 outlier 可把 mean 从 ~1 拉到 -230（D029/D030）。审查 random 实验时看 median，mean 如果偏离 median >10× 就是 outlier artifact。
3. **c4_entropy 脚本有小问题**（sys.path.insert, torch_dtype→dtype），但不影响结果正确性，低优先级。
4. **两路 Qwen 模型下载同时在跑**（ModelScope + HF CLI），可能是 Worker 误操作，不影响实验但浪费带宽。
5. **EMNLP 2026 ARR 截稿 5/25，距今 11 天**。GPU 预算充足（~18h/250h），不构成 deadline 风险。论文 §1/§7/§8/Abstract 未开始，但以 AI 速度不构成瓶颈。


---
