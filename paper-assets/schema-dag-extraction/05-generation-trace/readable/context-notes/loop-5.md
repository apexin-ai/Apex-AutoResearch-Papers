# director / loop_5.md

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_5.md`
- **Structured JSON:** [`4a2cc3767450073fb190.json`](../../sessions/4a/4a2cc3767450073fb190.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_messages
updated: '2026-05-16T10:20:20+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:0（cqa1-38874 单卡 RTX PRO 6000 Blackwell 98GB）
- C001 约束：count_40 子集必须写 "40-rel subsets sampled from the 80-relation pool"
- exp-018 batch composition 结果是 **null result**（+1.4pp, p≈0.19）——绝不能 claim "significantly improves"，Conclusion/Abstract/Intro 已统一为 "inconclusive"
- Title 已从 "Drive" 改为 "Shape"（D044），不能改回因果语言
- 80-rel full condition 回归不显著（p=0.762），必须在正文并列讨论，不能只放 footnote
- exp-017 GPT-4o-mini 已放弃（D041，TUM proxy 未部署），不要再尝试

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-38874 (connect.cqa1.seetacloud.com), root, 1× RTX PRO 6000 Blackwell 98GB
- 工作目录：/root/schema-dag-extraction
- Python：aml-train 镜像，conda base (`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`)
- 模型：Qwen3-32B-FP8 via vLLM（本地加载）
- 数据：FewRel/Few-NERD/MAVEN/DocRED 在 /root/schema-dag-extraction/data/
- OpenAI key 已存储（openai_key_exp017）但 proxy 不可用
- 活跃进程：无（GPU 空闲，exp-018 已完成）
- 审稿群：review_chat_id = oc_ac7ab7270b6b5caecee04f89b11aab3e

### 3. 📊 当前状态
**正在执行**：D044 Action Matrix（Round 4 审稿修复）。Agent 队列深度 6，正在处理 worker done 回调 + 后续修正指令。

**已完成的 D044 修正**：
- C1 Title "Shape" ✅, confound disclosure ✅, "quasi-experimental"→"controlled stratified comparison" ✅
- C2 Abstract/Intro framing 反转（typical 2.2pp 为 headline）✅, amplification 论证 ✅
- C3 80-rel null result 提升到正文 ✅
- C4 +1.4pp 降级为 inconclusive ✅（但 Conclusion 修正需确认）
- §4 fixes 全部 PASS（S8 DocRED R², S10 RE tautology）
- §5 扩展 + Discussion 扩展 ✅
- Abstract MAVEN 语义修正 ✅

**Agent 队列中待处理**：
- FewRel balanced design 一句话（"700 instances per type eliminates frequency confound"）
- §5 "chunk boundaries"→正确术语修正
- Discussion "SCS > 0.75"→软性 percentile 表述
- 多个 worker done 回调待 Agent 消化

**尚未执行的 D044 项**：
- S2: Embedding 循环性讨论（MiniLM r=0.172 vs Qwen3 r=0.112 消除 circularity concern）
- S5: 加 error taxonomy figure 到 §4.4（4 轮要求）
- S11: Bib 清理（11 orphan 条目 + cite 4 已有未引用文献）
- S1: MAVEN cross-domain scope 在 Discussion 显式标注
- 页数确认（目标 ≤8 页正文）
- 最终编译检查

### 4. 📋 待办（条件触发式）
- Agent 消化完当前队列 → 检查 S2/S5/S11/S1 是否已被 D044 综合指令中的 Worker 3-5 执行，未执行的追派
- 全部 D044 修正完成 → post_to_reviewer 做压缩后一致性审查（数值 / framing 全文一致性 / 页数）
- Reviewer 全 PASS → submit_paper_to_review Round 5（recommend "continue"，验证 C1-C4 修复）
- Round 5 ≥ 3.5 → 准备提交 ARR May 25
- Round 5 < 3.5 → 评估是否还有时间修复，或接受 Findings track（commitment DDL Aug 2 Main / Aug 26 Findings）
- GPU 空闲 + 有价值的实验 → 考虑 FewRel pairwise r=0.187 加入 Table 2（Reviewer info 建议，当前 hold）

### 5. 🎯 战略上下文
- **决策链**：D037(Round 2 修复) → D038(BCS MEAN) → D039(MEAN选择) → D040(v2 n=25 task-inherent) → D041(放弃GPT-4o-mini) → D042(exp-018成功) → D043(exp-018降级:null result) → D044(Round 4 framing全面降调)
- **论文核心定位已降调**：从 "confusability drives degradation" 降为 "confusability is a statistically detectable, practically modest but theoretically informative factor"。batch-level R²=22-53% 是保留的最强论据。
- **最容易判断错的事**：exp-018 +1.4pp 看起来是正面结果但实际是 null (p≈0.19, n=1, 2 个 random seed 更高)。任何写法都不能暗示显著。
- **4 轮持续问题仍未解**：正文仅 1 Figure（S5）、§5 过短（S4 部分解决）、orphan bib（S11）。这些是 "reviewer fatigue" 因素，每轮重复出现会降低审稿人耐心。
- **页数预算极紧**：当前 ~7 页，D044 增加内容后预估 ~7.9 页，≤8 页红线。如果超了优先砍 Discussion 中无数据支撑部分。
- **投稿策略**：仍投 Main track，AC 可 redirect to Findings。不预先降级。ARR May 25 提交，commitment 8月决定。


---
