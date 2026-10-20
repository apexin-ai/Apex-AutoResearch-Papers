---
loop: 7
reason: max_messages
updated: '2026-05-23T03:03:29+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 rtx6000-diagprobe 的 cuda:0 和 cuda:1（项目配置白名单，不可用其他服务器/GPU）
- 论文主文严格 8 页限（当前恰好 8 页，零余量——任何新增内容必须等量删减）
- Table 3 数据更新后必须 grep 全扫引用该数值的所有位置（exp_016 整合时 .232→.295 涉及 10 处，极易遗漏）
- checkpoint 存 /root/autodl-tmp/spectral_collapse_ews/，禁止存根分区（exp_014 因磁盘满崩溃过）
- Round 2 审稿已提交（apr_20260522T183554_d8x0），等用户确认审稿模式（推荐 continue）

### 2. 🖥️ 基础设施快照
- 服务器：rtx6000-diagprobe (connect.westd.seetacloud.com)，root 用户
- 工作目录：/root/spectral_collapse_ews
- Python：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，pip/python 在 /root/miniconda3/bin/
- 模型：EleutherAI/pythia-410m-deduped + pythia-1b-deduped（已缓存服务器）
- GPU：2x NVIDIA RTX PRO 6000 Blackwell Server Edition (98GB each)
- 活跃进程：exp_017 (cuda:1, r=0.2 seed43), exp_018 (cuda:0, r=0.5 seed43)
- lm_eval 输出格式：results_TIMESTAMP.json（非 results.json），脚本需 glob 匹配
- 数据收集脚本：scripts/collect_phase_table_stats.py

### 3. 📊 当前状态
刚完成：论文 Round 2 全部修订（7 commits）、response letter 定稿、exp_017/018 整合模板预写、Reviewer narrative 升级评估、Director handoff 写入 memory.md。已派 Agent 做论文全文写作质量通读 + 派 Reviewer 做 narrative arc 专项审查（用户明确要求写作流畅度）。

RUNNING 实验：
- exp_017 (r=0.2 seed43, cuda:1): Gen 9/10，预计 ~1-2h 完成，Type II 几乎确认
- exp_018 (r=0.5 seed43, cuda:0): Gen 5/10，预计 ~8-10h 完成

等待中：Agent 写作通读报告回复 + Reviewer narrative arc 审查报告

### 4. 📋 待办
- Agent 写作通读报告到手 → 评估哪些改动在页面零余量下可行，派 Agent 执行（等量删减+改写）
- Reviewer narrative arc 报告到手 → 判断是否需要结构性调整（慎重，零余量）
- exp_017 完成回调 → 按 artifacts/plan_018/exp017_integration_template.md 整合 r=0.2 2-seed 数据（Table 3 L175, §3.5 L131, Figure 2 caption L123, Limitations L5, response letter R1-W2 表格）
- exp_018 完成回调 → 按 artifacts/plan_018/exp018_integration_template.md 整合 r=0.5 2-seed 数据
- 用户确认审稿模式 → Round 2 审稿启动；审稿报告到手 → 按 review-report-action skill 处理
- 两实验都 success 后 → response letter 加定性升级措辞："Trajectory type classification is reproducible across seeds at all five tested mixing ratios"（Reviewer 已预审通过，不可升级为定量 claim）
- exp_017/018 都完成且 GPU 空闲 → 考虑是否补 r=0.2/0.5 第三 seed（取决于 Round 2 审稿反馈）

### 5. 🎯 战略上下文
- 目标：EMNLP 2026 ARR，Round 1 得分 3.0 (Findings)，目标 3.5 (Borderline Conference)
- 核心 claim：SLV 三阶段谱特征化 + r_crit ∈ (0.25, 0.3] phase boundary + signal attenuation 是 controller 固有局限（非 paradox）
- Round 2 修了 4 个 Must-Fix（页限/SLV公式/种子数/attenuation framing），r=0/0.25/0.3 已 3-seed
- 易错点：(1) 2-seed 条件不能报 CV 做定量 claim（Reviewer 明确否决）；(2) Table 3 数值更新必须全文 grep 同步；(3) 页面零余量——改一个地方必须删等量内容；(4) D-4 高方差是已知现象（r=0 Gen10 三种子 CV 远高于 SLV），不是 bug
- 用户关注写作质量和叙事流畅度（刚明确提出），这是当前最高优先级
- decisions.yaml 有 36 条决策记录，experiment_plan.yaml + paper_framing.md 是战略锚点
