# director / loop_8.md

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_8.md`
- **Structured JSON:** [`571db46e90cd8a1e234d.json`](../../sessions/57/571db46e90cd8a1e234d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_messages
updated: '2026-05-17T07:49:50+00:00'
---

### 1. 🔴 硬约束 / 红线
- cqa1-38874 只有 cuda:0 一张卡，不可用其他设备
- westd-24295（2×RTX PRO 6000 96GB）已授权，仅用于 LLaMA 70B 跨模型验证，密码存在 secret store（key: westd_24295_password）
- 正文 ≤8 页 ACL ARR 格式，删除 \enlargethispage 后必须重新编译验证
- "additive separability" / "cleanly separable" 已全文删除，禁止重新引入
- TOST SESOI 不能用 prompt-noise (~25pp) 锚定——已被审稿人多轮否定
- 因果语言是 Round 10 SYSTEMIC_ISSUE："driven"→"predicted by", "channels"→"dimensions", "bounded interaction"→"bounded association (RE-specific)"。这是第二次被抓（Round 7 同根因），必须彻底修

### 2. 🖥️ 基础设施快照
- 服务器 1：cqa1-38874 (connect.cqa1.seetacloud.com), root, cuda:0, 工作目录 /root/schema-dag-extraction
- 服务器 2：westd-24295 (connect.westd.seetacloud.com:24295), root, 2×GPU, 环境搭建 worker 两次失败（API timeout），需重试。LLaMA 70B FP8 模型可能未下载完
- 论文本地路径：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/`
- cqa1 GPU 当前空闲（D051 + SDGD routing + prompt sensitivity 全部完成）
- 无活跃 tmux session / 无活跃 cron

### 3. 📊 当前状态
**刚收到 Round 10 审稿报告**（Borderline weak accept/borderline），已完成 Holistic Pass + Action Matrix 初稿，已发 Reviewer 做独立审查。**等 Reviewer 回复后定稿 Action Matrix → 派 Agent 执行**。

Registry:
- exp_d051_count_curves_25: DONE/success（3-seed × 25-batch，FewRel + Few-NERD）
- exp_sdgd_routing_strategies: DONE/negative（7 策略全 negative）
- exp_prompt_sensitivity: DONE/success（4 variants × 2 counts，BCS 跨 prompt 稳健）
- 无 RUNNING/PREPARING 实验

等待中：
- Reviewer 对 Round 10 Action Matrix 初稿的独立审查回复
- westd-24295 环境搭建重试（LLaMA 70B 跨模型实验前置）
- 用户还未回复 Main vs Findings 定位决策（Round 9 时提出）

### 4. 📋 待办
- Reviewer 回复 Action Matrix 审查 → 综合定稿 → 分 Batch 1 (text) + Batch 2 (需计算) 派 Agent → update_review_issues
- Action Matrix 中 C1-C4 全是 text modification，Agent 4-6h 可清完
- westd-24295 环境就绪 → 启动 LLaMA 70B count curves（25-batch × FewRel + Few-NERD）→ 如果 pattern 复现 → framing 升级 "architecture-independent phenomenon"
- Q3（FewRel train/val BCS distribution）需 Agent 补分析
- W1 删除 \enlargethispage 后需要压缩 §5（SDGD routing details 移入 appendix）才能保 8 页
- Round 10 修复完成 → submit Round 11 (recommend: continue)
- LLaMA 70B 完成 → 写入论文 → submit Round 12 (recommend: fresh，因为加了跨模型数据)

### 5. 🎯 战略上下文
- **核心瓶颈仍是 novelty**。审稿人共识：实验设计是最强贡献，但 SCS=cosine similarity 不新，typical effect 2.2pp 小。分数从 Round 9 的 3.0 提升到 borderline weak accept，但 Main acceptance 需要 C1-C4 全部修复 + 可能需要 70B 跨模型数据。
- **因果语言是复发性问题**：Round 7 修过一轮但不彻底，Round 10 又被抓。这次必须 grep 全文做到 zero tolerance——"driven/drive/channels/mechanism" 全部换掉。
- **易错判断 #1**：不要以为只改措辞就够了。C2（聚合推理链）需要重构 §4.3 的叙事逻辑，不是换几个词。observed R²=0.218 必须成为 primary claim，simulation 降级。
- **易错判断 #2**：W1 删除 \enlargethispage 后 8 页可能放不下。需要先评估压缩方案（§5 routing details 是最佳压缩候选）再删命令，不要先删再发现超页。
- **易错判断 #3**：Reviewer Divergence 中 R1 说 "三测两败" 不支持 bounded interaction——R2 的层级解读更合理（primary test passed, 2×2 is sensitivity check），但 margin anchoring 确实需要加强（Lakens 2017 SESOI）。
- **决策链**：D049(R7)→D050(R8)→D051(R9)→本轮(R10)。每轮 overclaiming 都被抓，说明根本问题是论文在 "mechanistic explanation" 和 "empirical characterization" 之间没有选边站。这次必须彻底站 "empirical characterization + predictive framework"。
- **ARR May 25 DDL 还剩 8 天**，时间够但不能再拖。Round 10 修复 → Round 11 验证 → 70B 数据写入 → Final polish → 提交。


---
