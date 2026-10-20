# director / loop_2.md

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`f2dc194af239bcc9bc13.json`](../../sessions/f2/f2dc194af239bcc9bc13.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-15T16:52:04+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 autodl-5090 的 cuda:0-3，不得跨服务器
- Primary metric 已锁定 binary LOGO F1=0.723（D017），不可回退到 3-class 作为 headline
- D019 已撤回 instruct "inverted DDR" 叙事（长度伪影），论文不能再把 instruct 方向反转当发现报告
- EMNLP 2026 ARR DDL 2026-05-25，不可 fallback 到低级会议
- 审稿阶段（Group C 独立审稿团队在 review_chat_id=oc_999770e4e57bfc6eabd12fc1f64af1ef），Research Director 不参与论文格式/投稿材料准备

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090 (connect.bjb2.seetacloud.com)，账户 root
- 工作目录：/root/gen-depth-fingerprint
- GPU：4× RTX 5090 (cuda:0-3)，当前全部空闲
- Python/conda：aml-train 镜像，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- W&B：未配置；弹性 GPU：未启用
- 活跃进程：review-p1c-olmo-instruct 状态为 ANALYZING（可能已完成等待处理）
- Agent 队列：空闲（idle 57s，无 pending 消息）

### 3. 📊 当前状态
Round 2 审稿修复接近尾声，准备提交 Round 3。55 个实验（36 成功 / 2 负向 / 8 失败）。

**Round 2 修复进展**：
- ✅ 已完成：Rd2-N1 CI误用、Rd2-N2 gen-0泄露(binary F1)、Rd2-N4 cross-scale、Rd2-W1/W3/W5/W6、Rd2-M1-M6、P2-F cross-ref bias
- ⏳ 未完成：abstract/intro 数字更新(binary F1 headline)、related_work CI width 残留、P1-E ordinal 结论写入论文、P1-C instruct 最终决定、全文数字一致性验证

**ANALYZING**：review-p1c-olmo-instruct — OLMo instruct 实验，结果待处理

**待处理实验（PREPARING）**：review-sampling-ablation、plan-010-human-edit、plan-004-prep 等（低优先级，EMNLP 冲刺期间可能不做）

### 4. 📋 待办（条件触发式）
- review-p1c-olmo-instruct 出结果 → 综合所有 instruct 数据决定论文 scope（D019 已确认 base-only scope narrowing，instruct 作为 appendix/future work）
- abstract/intro 更新完成 + P1-E 写入完成 → post_to_reviewer 做全文数字一致性检查
- 一致性检查通过 → submit_paper_to_review 提交 Round 3（recommended_review_mode="continue"）
- Round 3 通过 → 准备 EMNLP ARR 提交材料（Group C 负责）
- 4 张 GPU 全空闲 → 派 Agent 跑 review-sampling-ablation 或其他 pending 实验填满（禁止空卡 >10min）

### 5. 🎯 战略上下文
- **核心发现**：递归 LLM 生成链展现 differential depth response——central-tendency/diversity 特征随深度漂移(H2)，shape 特征近稳态(H1)。7-feature ensemble 跨 3 families / 6 base models 验证。
- **决策链关键节点**：D002(MVP pass) → D004/D005(dual dynamics framing) → D007(reframe to DDR) → D015(baseline 反超→honest reporting) → D017(binary F1 as primary) → D019(撤回 instruct inverted DDR)
- **Claim 3 (Downstream Utility) 已确认 negative (D009)**，论文定位为 diagnostic-not-curative
- **易错点**：(1) Qwen 系列模型(0.6B/1.7B/Qwen3)生成链全部失败（8个实验），不要再尝试 Qwen 做生成器；(2) gen-0 数据在 3-class 设置下有 train/test 泄露风险（同一篇 seed text 跨 split），binary eval 已解决此问题；(3) instruct 模型的 depth signal 方向反转主要是长度伪影，不是真实发现
- **DDL 紧迫**：5/25 还剩 10 天，当前首要任务是完成论文文字修复 → Round 3 审稿 → 提交，GPU 实验优先级让位于写作收尾


---
