---
loop: 24
reason: max_messages
updated: '2026-05-25T07:04:00+00:00'
---

### 1. 🔴 硬约束 / 红线
- 匿名仓库 token 在 `_anonymous_repo.json`（已 .gitignore），绝不能 commit 此文件
- 论文正文 ≤ 8 页（EMNLP 2026），Limitations/References/Appendix 不计入
- Abstract ≤ 200 words（当前 ~151 words）
- TOST p=0.007 仅来自 Qwen3 5 seeds；DeepSeek 2 seeds 仅 "directionally consistent"，不可声称 "across both families" 通过 TOST
- 匿名仓库 push 必须用 HTTPS+token（`_anonymous_repo.json` 中的 push_url），SSH deploy key 不通

### 2. 🖥️ 基础设施快照
- 服务器：seetacloud-westd-4x5090（4× RTX 5090 32GB）
- GPU 状态：CWM eval 已全部完成（GPU 0-3 均空闲），无活跃训练
- 论文目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/`
- 匿名仓库：`https://github.com/anonymous-nlp-2026-2/exec-sim-repair-verifier`（最新 push: commit a0c2cf8）
- GOOGLE_API_KEY 已 store_secret（key_id=`google_api_key`），供 PaperBanana 使用
- 无活跃 tmux/cron/PID

### 3. 📊 当前状态
**刚完成：**
- 摘要重写为单段（去数据堆砌，~151 words）
- Em-dash 批量清理 19 处（commit ce7b281）
- 缩写首次定义检查 11 处修复（commit 370679f）
- Intro "across both families" 精确化 + "recommendations" → "observations"（未 commit）
- Paper audit 处理完毕（0 critical remaining）

**Agent 正在处理：**
- Figure 1 PaperBanana 重画（概念图，统一色系 CLS 蓝/CWM 橙/TRAJ 绿）
- 新增附录图表（CWM unparseable rate、TOST sensitivity、per-mutation heatmap）
- 正文 Fig 3（oracle-stratified 或 repo-level 对比）

**等待：** Agent 回复图表任务结果

### 4. 📋 待办
- Agent 图表任务完成 → 检查每张图质量和色系一致性 → 编译验证页数 → commit + push 匿名仓库
- 如果 PaperBanana 失败（API key 无效/安装问题）→ fallback 到 draw-paper-figure 手工画 Figure 1
- 图表全部完成后 → 重新编译检查正文是否仍 ≤ 8 页（新增正文图可能挤占空间）→ 超页则只放附录
- Intro 的两处修改未 commit → 图表完成后一起 commit
- 所有改动完成后 → push 到匿名仓库（用 _anonymous_repo.json 中的 push_url force push）

### 5. 🎯 战略上下文
- 论文已 finalize 并准备 ARR 提交（DDL 2026-05-25 即今天），核心实验结论不变
- Review score 稳定在 3.0（Findings），这是 empirical comparison paper 的天花板，非写作问题
- CWM ckpt-6100 reeval 结果（70.2% accuracy）可作为 author response 材料（reviewer 质疑 CWM 性能时），但仍低于 majority baseline 72.96%
- 用户（曹晓玉）对摘要和图表质量有高标准，明确要求"高级感"——图表不能用 matplotlib 默认样式
- ckpt300/seq2048 reeval 与 Table 2 有三重 confound（seq/max_new_tokens/ckpt），不可直接对比验证 Table 2
- 易错点：匿名仓库 push 需要 force push（remote 有旧历史），用 `git push --force <push_url> master:main`
