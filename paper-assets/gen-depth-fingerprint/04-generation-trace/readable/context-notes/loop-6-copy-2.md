# agent / loop_6.md

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_6.md`
- **Structured JSON:** [`5c2d52f02c3db53462b8.json`](../../sessions/5c/5c2d52f02c3db53462b8.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: idle_timeout
updated: '2026-05-15T15:24:53+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：autodl-5090 cuda:0/1/2/3，不可用其他设备
- Primary metric 已切换为 **binary LOGO F1**（gen-1 vs gen-2+, gen-0 excluded due to shared-seed leakage）— D017 决策，所有论文 headline 数字必须用 binary 0.723，3-class 0.789 仅作 supplementary 且必须带 gen-0 caveat
- Claim 3 (Downstream Utility) 是 **confirmed negative** (D009)，论文中必须诚实报告为 "diagnostic not curative"，不得暗示 depth curation 有效
- 4-baseline ensemble 在 3-class 下反超 7-feature (0.796 vs 0.789)，但 binary 下 7-feature 赢回 (0.723 vs 0.712)——baseline 优势完全来自 gen-0 分类，论文必须说清这个 nuance，不得 cherry-pick 任何一边
- EMNLP 2026 ARR DDL: **2026-05-25**，10 天倒计时

### 2. 🖥️ 基础设施快照
- 服务器：**autodl-5090**，账号 root，工作目录 `/root/gen-depth-fingerprint`
- Python：conda 环境（aml-train 镜像），激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 数据：`/root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl` (996 seeds)
- W&B：项目名见实验 spec（各实验独立配置）
- 活跃进程：**无**。0 个 RUNNING 实验，0 个活跃 cron，0 个运行中 Worker
- review-p1c-instruct 的训练脚本：`bash run_p1c_instruct.sh`（Qwen3-1.7B-Instruct, 已完成训练，状态卡在 ANALYZING）

### 3. 📊 当前状态
**刚完成的 session 工作**：Round 2 审稿修复批量实验（P0-A/P0-B/P1-D/P1-E/P2-F 全部 success），论文 results/conclusion/method/discussion 已更新，abstract/intro 的 binary headline 更新 **尚未完成**。

**Registry 概览**：52 个实验，41 DONE (31 success / 1 negative / 8 failed / 1 killed)，10 PREPARING，1 ANALYZING，0 RUNNING。

**需要立即处理**：
- `review-p1c-instruct` 状态 ANALYZING — Qwen3-1.7B-Instruct 实验已跑完但**无 Worker 在分析**，需 spawn worker 提取结果
- 论文 abstract + intro 的 binary F1 headline 更新（从 3-class 改为 binary）尚未完成
- P1-E ordinal regression 结论尚未写入论文

**PREPARING 实验**：
- `review-rd2m7-bib-audit`：bib 年份验证（Rd2-M7 修复项）
- `review-p1c-qwen06b-instruct` / `review-p1c-olmo-instruct`：P1-C 额外 instruct 模型，等第一个 instruct 结果再决定
- `mvp-001-gen-s0/s1/s2/s3` + `plan-001-restore` + `plan-004-prep` + `review-p2f-cross-ref-bias`：历史遗留 PREPARING，实际工作已由其他实验完成，可视为 stale

### 4. 📋 待办（条件触发式）
- **立即** → spawn worker 分析 `review-p1c-instruct` 结果（SSH 读 log + 提取 metrics + update_registry）
- P1-C instruct 结果出来 → 若 instruct 也展现 depth response，scope 可扩至 instruct models（决定是否跑 Qwen-0.6B/OLMo instruct）；若不展现，维持 "base model scope" 不动 paper
- abstract/intro headline 更新完成 + P1-E ordinal 写入完成 + related_work CI 残留修复 → post_to_reviewer 做 Round 3 一致性检查
- Round 3 审查通过 → EMNLP ARR 提交材料准备（anonymization, appendix, supplementary）
- `review-rd2m7-bib-audit` → spawn worker 用 WebSearch 验证 3 个 bib 条目年份

### 5. 🎯 战略上下文
**决策链关键节点**：D001(MVP) → D004(dual dynamics) → D005(level/shape 分界) → D007(differential depth response 重命名) → D009(Claim 3 negative) → D012(恢复 EMNLP) → D015(baseline 反超 nuance) → D017(binary primary metric)

**核心结论**：递归 LLM 生成链的 distributional features 展现 differential depth response——central-tendency/diversity 漂移，shape 近稳态。7-feature ensemble binary LOGO F1=0.723 在 leak-free 评估下显著优于所有单检测器 baseline。

**最容易判断错的事**：
- `review-p1c-instruct` 看起来像"还在跑"但实际训练已结束、卡在 ANALYZING——需要主动 spawn worker 去收结果，不要等 cron 回调（没有活跃 cron）
- 10 个 PREPARING 实验中大部分是 stale（mvp-001-gen-s0~s3, plan-001-restore 等），不要试图"恢复"它们，它们的工作已被后续实验覆盖
- 论文当前存在 **两套副本**：`artifacts/_project/paper/*.tex` 和 `docs/paper/*.tex`，改一处必须同步另一处（git status 显示两套都有改动）
- 4 块 GPU 全部空闲——这是 EMNLP 冲刺期，应该把 P1-C 分析、bib audit、论文修改全部并行推进


---
