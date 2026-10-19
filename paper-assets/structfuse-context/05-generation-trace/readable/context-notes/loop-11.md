# director / loop_11.md

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_11.md`
- **Structured JSON:** [`a54852e2a2e2c422acd5.json`](../../sessions/a5/a54852e2a2e2c422acd5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_messages
updated: '2026-05-15T18:14:12+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只有 bjb1-42106 的 cuda:0 和 cuda:1，严禁使用其他设备
- Claim 1 delta 2-seed mean ≈ 0 (D056)，embed_s42 是 swing vote —— 不要在 embed_s42 结果出来前 pivot 或降级 claim（D018/D019 原则）
- D051: 论文结果必须报告 mean ± std across seeds，禁止 cherry-pick 单 seed
- D049: Claim 1 采用双轨并报 + 软化 framing（"improves" → 条件性表述），paper_framing.md 已更新
- Watcher PID 966920 管理 s42 supplement 自动触发链，不要手动干预或 kill

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-42106 (connect.bjb1.seetacloud.com)，账号 root
- 工作目录：/root/structfuse
- GPU：2× RTX PRO 6000 96GB (cuda:0, cuda:1)
- 活跃进程：
  - m2_full_qwen_continued: cuda:0, dataflow_s43 running (4/7 done)
  - m2_full_starcoder_resumed: cuda:1, random_s44 ~48% (1/6 done), PID 519791
  - m1_reextract_v2: CPU 任务, 处理 MONAI 大 repo
  - Watcher PID 966920: 等 Qwen 主链完成后自动触发 embed_s42+dataflow_s42+bm25_s42
- W&B/弹性 GPU/Git：均未配置

### 3. 📊 当前状态
- **Qwen (cuda:0)**: dataflow_s43 running，主链 ETA ~May 16 08:00 CST，之后 watcher 自动触发 s42 supplement (~18h)，全部 Qwen ~May 17 02:00
- **StarCoder (cuda:1)**: random_s44 ~48%，ETA ~May 19-20
- **m1_reextract_v2**: 44,173 行处理中，略晚于原 ETA
- **写作**: Intro/Method/Related Work/Conclusion v1 内审 PASS；Abstract v2 + Experiments v1 修复中 (D055 bootstrap 脚本已修复)
- **审稿阶段已启动** (review_chat_id: oc_2a0777e0289fb54872621f6b14e6e4ee)，Group C 独立处理
- **Reviewer 刚 RESET**（本次 handoff 的原因）

### 4. 📋 待办（条件触发式）
- Qwen 主链完成 (~May 16 08:00) → 验证 watcher PID 966920 活性 → s42 supplement 自动触发
- embed_s42 结果出来 → 立即计算 3-seed mean Δ，决定 Claim 1 走 A (Δ>0.5pp 站住) / B (CI 跨零但 trend 正) / C-D (应急 D052)
- Qwen 全部完成 (~May 17) → pool=50 重评估 + cluster bootstrap (D045/D055) + plan_005 分层分析
- M2 全部完成 → BM25 Phase 2 watcher 自动触发 (plan_018)
- plan_003 SWE-bench eval 需 Qwen3.6-27B API key，待解决
- 目标 May 18 正式提交审稿

### 5. 🎯 战略上下文
- **核心论点**: Embedding-distance mining improves contrastive code retrieval at zero additional inference cost. 已软化 framing (D049)。
- **最大风险**: Claim 1 的 2-seed mean Δ ≈ 0 (D056)。s44 random 是 outlier (+4.7pp 高于均值)，embed_s44=0.5942 本身高于 non-outlier random 均值。embed_s42 是翻盘关键。
- **决策链**: D048(s43 正向) → D049(软化 framing) → D051(多 seed 报告) → D052(应急方案) → D055(cluster bootstrap) → D056(2-seed mean ≈ 0) → D057/D058(trajectory 发现降级为 §4.3)
- **易错点**: 不要把不同 seed 的 random baseline 直接横向对比（s44 random 是 outlier）；pool=50 重评估可能改变 best checkpoint 选择；BM25 watcher 需要 s42 regime 修复 (D050)
- **ARR May 25 DDL**: StarCoder ~May 20 完成，post-M2 窗口仅 5 天，需高效并行 pool=50 + stats + plan_005 + BM25


---
