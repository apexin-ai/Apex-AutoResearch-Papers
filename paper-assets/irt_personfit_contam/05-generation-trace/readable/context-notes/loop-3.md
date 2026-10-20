# director / loop_3.md

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`c043b77e42cf34438760.json`](../../sessions/c0/c043b77e42cf34438760.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-24T03:08:26+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 分配：westd-35694 的 4 张卡（cuda:0-3），项目配置内，但当前无实验需要跑
- 匿名 repo 只能用 HTTPS+token push（SSH deploy key 绑错了 repo），URL: `https://github.com/anonymous-nlp-2026-2/irt_personfit_contam`
- 论文已进入提交等待状态，**禁止再改论文内容**——数据审计已完成（9处修复），Reviewer 最终审查 5 维度全 PASS，任何修改都有引入新错误的风险
- Mistral 5%/25% 补充实验已正式决定不做（Reviewer 评估 soft spot 非 critical，DDL 前风险 > 收益）

### 2. 🖥️ 基础设施快照
- 服务器：westd-35694 (connect.westd.seetacloud.com)，4×GPU，root 用户
- 本地论文目录：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/`
- 匿名 repo 最新 commit：`2421ca8`（54 files）
- 最终 PDF 已上传群聊：`IRT_PersonFit_EMNLP2026_FINAL.pdf`
- 活跃进程：无（全部实验完成，无 tmux/cron/worker）
- GPU 状态：4/4 空闲

### 3. 📊 当前状态
论文全部就绪，唯一阻塞项是用户（游承松）在 OpenReview 手动提交。

已完成：
- 数据审计：66+ 数据点验证，9 处不一致修复
- Reviewer 最终审查：Story/负面结果/攻击面覆盖/数字精度/写作质量 全 PASS
- 写作 polish：5 处改进（transitions、table headers、captions）
- ARR 表单字段：全部英文版已提供（Keywords/Research Area/Checklist A1-E1）
- Appendix L "Use of AI Assistants" 已添加（E1=Yes）
- 匿名 repo 同步完成

registry：113 个实验，无 RUNNING/PREPARING。所有实验已完成。

已发 4+ 次提醒给用户（22:22, 23:01, 00:35, 03:06 UTC），均无回复。前一个 session 在 ~02:35 通知了 Manager 协助跟进。

### 4. 📋 待办
- 用户回复确认提交 → 回答任何最后问题，协助提交流程
- 用户说需要重发材料 → 重新编译 PDF / 重发表单字段
- 用户确认已提交 → 更新 ROADMAP，标记提交完成，考虑释放 westd-35694（先备份数据）
- 如果 DDL 过了用户仍未提交 → 与 Manager 讨论下一步（下一个 ARR cycle？）
- 如果收到审稿报告（Review Director 发来 `[审稿报告]`）→ 按 review-report-action skill 处理

### 5. 🎯 战略上下文
- **投稿目标**：EMNLP 2026 via ARR，DDL 2026-05-25 AoE，用户目标评分 4.0（Conference level）
- **核心贡献**：IRT person-fit statistics (ℓz*) 用于检测 SFT 阶段 LLM benchmark contamination，三个 7-8B 模型家族（Llama/Qwen/Mistral），发现三个行为边界（θ-shift absorption、detection-diagnosis tradeoff、non-monotonic dose-response）
- **关键数据点**：Llama clean baseline mean=+0.262 SD=1.542（V2 re-eval 定论），所有 Cohen's d ≥ 1.44（大效应量），GRPO pilot 证明 ℓz* 在 RL 后仍有信号（MIA AUC 降至 0.493 随机水平）
- **易错点**：不要再碰论文数字——所有数值已经过交叉验证并锁定；不要补 Mistral 5%/25%——这是已决策的 trade-off
- **服务器释放**：提交确认后可释放 westd-35694，但需先备份实验 artifacts 到 S3


---
