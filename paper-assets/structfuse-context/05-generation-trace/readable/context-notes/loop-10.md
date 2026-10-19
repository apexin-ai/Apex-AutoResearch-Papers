# director / loop_10.md

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_10.md`
- **Structured JSON:** [`f60291c040b856d76447.json`](../../sessions/f6/f60291c040b856d76447.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_messages
updated: '2026-05-15T14:06:41+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 只能用 cuda:0 和 cuda:1**（bjb1-42106 分配给本项目的卡）。D005 有过 GPU 越界事故（跑到 GPU 5），所有脚本必须强制 CUDA_VISIBLE_DEVICES
- ARR DDL **May 25**，不可 fallback 到低级别会议
- D051: 论文结果必须报告 mean ± std across seeds，禁止 cherry-pick 单 seed
- D055: 统计检验改为 instance-level cluster bootstrap (by repo)，不是 naive paired t-test
- BM25 Phase 2 有 tmux watcher 脚本，M2 完成后自动触发——**不要手动重复启动**

### 2. 🖥️ 基础设施快照
- **服务器**: bjb1-42106 (connect.bjb1.seetacloud.com), root 用户
- **工作目录**: /root/structfuse
- **GPU**: 2× RTX PRO 6000 96GB (cuda:0, cuda:1)，两卡满载 M2 训练
- **活跃进程**:
  - m2_full_qwen_continued (cuda:0): embed_s44 running，后续还有 embed_s43→embed_s44→dataflow×3 链
  - m2_full_starcoder_resumed (cuda:1): random_s44 running → embed×3 + dataflow×3 链, PID 519791
  - m1_reextract_v2: ~90.5% done, ETA May 15 19:00 CST (CPU 任务)
  - BM25 Phase 2 watcher: tmux session 就绪，等 M2 完成后自动触发
- **写作**: Paper Agent session 活跃。Intro/Method/Related Work v1 均 PASS。Abstract v2 + Experiments v1 + Conclusion v1 待 Reviewer 审查
- **审稿群**: review_chat_id = oc_2a0777e0289fb54872621f6b14e6e4ee

### 3. 📊 当前状态
本轮(4h)主要工作：分析 s43 结果发现 Claim 1 delta 缩水 (Δ+0.52pp vs pilot +2.0pp)，连续做了 D048-D055 八个决策应对——软化 framing (D049)、定义 Scenario C/D 应急 (D052)、升级 plan_005 到 P0 (D053)、确定 embed_s42 补跑优先级 (D054)、改统计方法 (D055)。

**RUNNING**: m2_full_qwen_continued (cuda:0, ETA ~May 17 21:00 CST)、m2_full_starcoder_resumed (cuda:1, ETA ~May 20 01:00 CST)、m1_reextract_v2 (~90.5%)
**ANALYZING**: 无
**等待中**: Paper Agent 的 Abstract/Experiments/Conclusion Reviewer 审查结果；m1_reextract_v2 完成回调

### 4. 📋 待办（条件触发式）
- m1_reextract_v2 完成 → 检查恢复率，更新 M1 总数据量，评估是否需要重新生成训练数据
- M2 Qwen chain 完成 (~May 17) → **立即并行启动**: (a) D045 统计分析 best_by_R@1 + leave-one-out + seed variance, (b) pool=50 重评估所有 best checkpoint, (c) plan_005 分层分析 (Claim 2 定量支撑), (d) D054 embed_s42 + dataflow_s42 补跑
- M2 StarCoder chain 完成 (~May 20) → BM25 Phase 2 自动触发 (watcher)；同时可启动 StarCoder 侧 pool=50 + 统计分析
- pool=50 结果出来 → **关键判断点**: Δ≥0.5pp+CI不跨零=Scenario A(当前 framing)；Δ<0.5pp=Scenario C(fixed-checkpoint + pool=50)；Δ≈0=Scenario D(叙事重心转 Claim 2+3)
- Paper Agent 汇报 Reviewer 结果 → 审查是否需要派 Patch 任务

### 5. 🎯 战略上下文
- **核心结论链**: M1 Z%=74% 确认结构信号 (D011) → pilot embed>random +2pp (D008) → s43 缩水到 +0.52pp (D048) → 软化 framing "reliably improves at zero additional cost" (D049) → 应急方案 C/D (D052)
- **最大风险**: Claim 1 delta 在 pool=8 下太小 (±0.5pp 噪声与 delta 同阶)，pool=50 是翻盘点——如果 pool=50 下 delta 显著，当前 framing 站得住；如果不显著，需要执行 Scenario C/D
- **易错判断**: 不要看到 s43 单点 +0.52pp 就恐慌——D049 已经定义了 fixed-checkpoint 均值 ~0.82pp 的备选报告方式，pool=50 还没跑。**等数据，不要提前 pivot**
- **时间线**: Qwen ~May 17 → StarCoder ~May 20 → post-M2 分析+补实验 ~May 20-23 → 写作收尾 ~May 23-25 → ARR May 25。StarCoder 是关键路径瓶颈
- **plan_018 BM25** 是论文最大结构性缺陷 (Dream 三档一致)，Phase 1 数据已就绪，Phase 2 在 M2 释放 GPU 后自动开始


---
