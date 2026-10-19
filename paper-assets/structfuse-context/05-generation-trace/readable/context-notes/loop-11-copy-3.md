# reviewer / loop_11.md

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_11.md`
- **Structured JSON:** [`7d5c18bd7e737b8464fa.json`](../../sessions/7d/7d5c18bd7e737b8464fa.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_wall_time
updated: '2026-05-15T14:06:09+00:00'
---

### 1. 🔴 硬约束 / 红线
- Qwen 训练只能用 cuda:0，StarCoder 只能用 cuda:1（bjb1-42106 服务器，项目 gpu_ids=[0,1]）
- 本 session 是 Reviewer 角色：**只读**，不执行实验、不修改文件，唯一输出渠道是 `reviewer_post_to_director`
- 审查"未改"类结论前必须双边核对：论文/文档在本地 workspace（`projects/structfuse-context/...`），训练代码/数据在远程 `/root/structfuse`
- ssh_read_only 不支持 `|`、`>`、`$(...)` 等 shell metacharacter

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-42106(root)，代码根 `/root/structfuse`，数据 `/root/autodl-tmp/structfuse/`
- 训练数据：`/root/autodl-tmp/structfuse/full_m2_training_data/`（14,288 instances/seed，4 策略×3 seeds）
- 训练输出：`/root/autodl-tmp/structfuse/full_m2_outputs/`（Qwen），StarCoder 路径待确认
- 训练脚本：`/root/structfuse/run_m2_full_qwen.sh`、`/root/structfuse/run_m2_full_starcoder_resume.sh`
- 活跃进程（截至 2026-05-15T21:00 CST）：
  - Qwen M2 chain: PID 337267 (cuda:0)，当前 embedding_distance_s44 (5/9)
  - StarCoder M2 chain: PID 519791 (cuda:1)，当前 random_s44 (3/8)
  - M1 reextract v2: 4 CPU workers，处理 MONAI + moto 剩余 repos
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/`
- 论文稿件：`artifacts/paper_drafts/`（method_v1 已 PASS，abstract_v2/experiments_v1/conclusion_v1 已审）

### 3. 📊 当前状态
**刚完成**：三章并行审查已提交（Abstract v2 PASS、Experiments v1 WARNING、Conclusion v1 PASS），以及 Claim 1 脆弱性预警。

**关键发现**：Qwen embedding_s44 best R@1=0.5942 < random_s44 的 0.6009（-0.67pp，方向反转）。两个已完成 seed 中 s43 +0.52pp、s44 -0.67pp，Claim 1 "reliable improvement" 面临 seed 噪声淹没风险。已通知 Director 关注 D052 Scenario C。

**RUNNING 实验**：
- `m2_full_qwen_continued`：5/9 done，embedding_s44 运行中，ETA ~May 17
- `m2_full_starcoder_resumed`：3/8（random_s44 running），ETA ~May 20
- `m1_reextract_v2`：MONAI 66.8% + moto 18.7%，ETA ~May 15 22:00
- `plan_018_bm25`：QUEUED（Phase 1 CPU done，Phase 2 GPU 等 M2 完成）
- `plan_005_stratified`：PREPARING（脚本 dry-run 通过，等 checkpoint）

### 4. 📋 待办（条件触发式）
- **embedding_s44 完成** → 核实 best R@1 是否锁定 0.5942，更新 Claim 1 fragility 评估
- **embedding_s42 完成** → 这是 Claim 1 成败关键：若 <0.56 则 mean delta ≈0 或负，立即触发 D052 Scenario C 升级为 critical
- **Qwen 9/9 全完** → 计算三 seed mean + bootstrap 95% CI，发布完整 Qwen 审查报告
- **StarCoder embedding runs 开始** → 核实用的是 StarCoder 模型做 self-mining（不是 Qwen 模型）
- **m1_reextract_v2 完成** → 核查新 structural coverage 数字是否影响论文中 34.3%/15,153 等数据
- **Director 转发 Paper Agent 章节修订** → 重新审查 Experiments v1 的 36.0% vs 34.3% 数字链问题和 14,288 溯源问题是否已修复

### 5. 🎯 战略上下文
- **D049 framing**："systematic comparison" + "reliable improvement at zero additional cost"，不说 novel/SOTA/we propose
- **Claim 1 是论文生死线**：embedding > random 必须 statistically reliable。当前 Qwen 2/3 seeds：+0.52pp / -0.67pp，方向不一致。paper_framing 有 D052 contingency（Scenario C: delta 被噪声淹没 → 弱化为 "competitive alternative"）
- **Claim 2 是 exploratory**：dataflow×encoder interaction，已降级为观察非结论，容错空间大
- **数字链陷阱**：15,897（extraction success）/ 15,153（non-empty structural, 34.3%）/ 14,288（resolvable positive, 用于训练）/ 11,308（per-seed train）— 四个层级容易混淆，Experiments v1 已 flag 过 36.0% vs 34.3% 不一致
- **s44 random 是已知 outlier**（0.6009 vs s42/s43 的 0.5527-0.5554），plan_005 stratified 分析计划加入 per-seed val set 难度校验（D050 追加）来解释这个方差
- **问题词黑名单**：consistent（无限定）/ orthogonal / fundamentally different / internalizes / novel method / state-of-the-art / we propose — 审查时逐词 grep


---
