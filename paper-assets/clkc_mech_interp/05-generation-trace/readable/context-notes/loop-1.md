# director / loop_1.md

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`74ba9f86e5080a46f7d6.json`](../../sessions/74/74ba9f86e5080a46f7d6.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-23T20:01:31+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 westd-41302 的 cuda:0-3，不得使用其他服务器的卡
- 服务器 westd-41302 使用**密码认证**（非 SSH key），`backup_project_to_s3` 的 SCP 步骤会失败——需运维先配 SSH key 或走 Agent 手动备份
- 论文 abstract 严格 ≤200 words（EMNLP 2026 硬限）
- bootstrap n=2000（conflict/XNLI probes）、n=1000（cross-task transfer），Bonferroni 校正——这些是已发表数据的统计参数，不可更改

### 2. 🖥️ 基础设施快照
- 服务器：westd-41302 (connect.westd.seetacloud.com:41302)，账号 root
- 工作目录：/root/clkc_mech_interp
- Python：/root/miniconda3/bin/python（aml-train 镜像，用 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 数据：/root/clkc_mech_interp/data/（probe results、steering results、bootstrap JSONs）
- 无 wandb、无弹性 GPU、无 S3 备份
- 活跃进程：无。4 张 GPU 全部空闲
- 匿名仓库：https://github.com/anonymous-nlp-2026-2/clkc_mech_interp（2 commits, author=Anonymous）

### 3. 📊 当前状态
- 论文 submission-ready，EMNLP 2026 ARR DDL 2026-05-25
- 所有实验完成（62 个 registry 条目），无 RUNNING/PREPARING
- 运维请求了**计算服务器审计**——我已回复：westd-41302 归类为 C（可释放），但需先备份数据。备份因 SSH 密码认证失败，已告知运维两个解决路径（配 SSH key 或 Agent 手动备份），**等运维回复**
- 审稿阶段已启动（review_chat_id 已配置），Group C 团队并行处理中
- 无等待中的 Worker 回调 / Cron

### 4. 📋 待办
- 运维回复备份方案 → 执行备份 → 确认完整 → 回复运维可释放 westd-41302
- 如运维选"Agent 手动备份" → `director_post_to_main_agent` 让 Agent SSH 打包 data/ 目录上传 S3
- 如运维选"配 SSH key" → 等配好后重跑 `backup_project_to_s3(tag="pre-submission")`
- 收到审稿报告 `[审稿报告]` → Read `review-report-action.skill.md` → Holistic Pass + Per-Comment Action Matrix
- ARR 审稿结果返回（约 2-3 个月后） → 准备 rebuttal，可能需重新租卡跑补充实验

### 5. 🎯 战略上下文
- **核心发现**：跨语言知识冲突可通过 residual stream probing 检测（3 模型 75-78%），存在稳定的 ZH→EN > EN→ZH ~7pp 不对称性，XNLI 对照 + cross-task transfer 证明 piggyback 共享子空间假说
- **Detection ≠ Decision 解离**：probe peak 在 L28（88% depth）但 causal steering 仅 L13（41% depth）有效，12 configs 中仅 Llama L13 positive
- **M019 教训（最易踩的坑）**：lbfgs solver 在高维空间（d=3584）不收敛，曾制造虚假的 "Gemma L14-22 subspace collapse" narrative。所有 probe 实验必须用 liblinear solver + bootstrap
- **D018 覆盖 D016**：cross-task transfer 最初决定不加入论文（D016），后用户批准加入（D018）——论文已包含该结果
- 项目处于等待审稿状态，GPU 空闲是正常的（不要因 "GPU 不能空着" 规则强行派实验）


---
