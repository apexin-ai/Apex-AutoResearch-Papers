# director / loop_9.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_9.md`
- **Structured JSON:** [`170727c6b6c0c8dfa0e0.json`](../../sessions/17/170727c6b6c0c8dfa0e0.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_wall_time
updated: '2026-05-17T23:22:29+00:00'
---

### 1. 🔴 硬约束 / 红线
- cqa1-22115 只能用 cuda:0-3（gpu_constraint 白名单）
- westd-42896 只能用 cuda:0-1（云租卡，已加入 project config）
- Wikipedia 数据**不写入正文主线**（D054），放 Appendix + scorer confound caveat
- arXiv K*=3 表述必须写 "5/6 models"（OLMo capacity failure excluded），不能写 "5/5 100%"（Reviewer 已 flag cherry-picking 风险）
- 论文中所有数值区间必须覆盖实际数据点（已修两次 overclaim：cliff ratio 6-56×, JSD range 0.16-0.29）
- exp_008_retrain_chain (无 v2 后缀) 是 dead entry (conclusion=killed)，retrain-chain 数据源是 exp_027_retrain_bootstrap

### 2. 🖥️ 基础设施快照
- **cqa1-22115**: connect.cqa1.seetacloud.com, root, /root/autodl-tmp/gen-depth-contamination, 4×4090D
  - 全部空闲（exp_wiki_scorer_confound_1b5 刚审批分配 cuda:1，可能已开始或即将开始）
  - 磁盘：项目仅 1.2GB，/autodl-pub 97% 是共享盘问题
- **westd-42896**: 云租卡 2×RTX PRO 6000 96GB
  - cuda:0: exp_14b_c4 RUNNING（14B fp16, ~May 18 15:30 完成）
  - cuda:1: exp_32b_c4 RUNNING（32B fp16, ~May 20 07:00 完成）
- 论文本地路径：projects/gen-depth-contamination/docs/paper/
- Paper Agent session 已存在（自动复用）

### 3. 📊 当前状态
本轮（Loop #9 extended）完成了大量工作：
- **arXiv domain expansion**: 5/5 non-OLMo models K*=3（D055-D057）
- **Wikipedia domain expansion**: 6/6 models 完成，continuation mode 全线 K*=1（D058-D059）
- **D060 scorer confound**: Qwen Wiki K*=2 确认是 Qwen scorer artifact（Pythia scorer → K*=1）
- **Paper Agent patches**: Wikipedia overclaim 修正（4 处）、JSD data 修正（2 处）、scorer confound appendix section、D060 更新
- **θ sensitivity**: 完成，K* stable in [0.575, 0.625]

RUNNING/PENDING:
- exp_14b_c4: westd cuda:0, depth 2 进行中, ~May 18 15:30
- exp_32b_c4: westd cuda:1, depth 1 进行中, ~May 20 07:00
- exp_wiki_scorer_confound_1b5: cqa1 cuda:1, 刚审批分配（Qwen-1.5B Wiki cross-scorer 复验, <1h）

### 4. 📋 待办
- exp_wiki_scorer_confound_1b5 完成 → 预期 K*=1（与 D060 一致）→ 更新 appendix 表添加第二行 Pythia-scored 数据
- exp_14b_c4 完成（~May 18）→ 如果 K*=2 → clean win, scale invariance confirmed；如果 K*=1 → 启动 scorer confound contingency（用 14B 自身作 scorer 重新评分，westd 有空间）
- exp_32b_c4 完成（~May 20）→ 同上逻辑；32B K*=2 是 strongest scale evidence
- 14B/32B 结果出齐后 → Paper Agent 综合 patch：完整 domain×model table（含 14B/32B 行 + scorer confound 注释）、Mistral 3-domain case study highlight、scale invariance discussion
- 所有实验完成后 → submit_paper_to_review 提交 Group C 最终审稿

### 5. 🎯 战略上下文
**核心结论**: K* is domain-governed。arXiv K*=3 > C4 K*=2 > Wikipedia K*=1。Domain×Model matrix 中仅两个 genuine exceptions: Mistral C4 K*=1 (web-text-universal one-wash), OLMo arXiv K*=1 (capacity failure)。Wikipedia Qwen exception 被 D060 消解（scorer artifact）。

**决策链**: D049(arXiv K*=3 升级) → D050-D057(cross-model validation) → D058(Mistral domain profile) → D059(Wiki complete) → D060(scorer confound confirmed)

**易错点**:
1. 14B/32B 若 K*=1，**先怀疑 1.5B scorer 能力不足**（scorer capacity confound），不要直接下结论 "scale breaks K*=2"。Contingency: 用 14B 自身做 scorer 重新评分
2. Paper Agent 已多轮 patch，论文内部一致性需要 check_paper_consistency 验证（数字/claim 是否还对得上）
3. DDL May 25（~6 days），32B 实验 ~May 20 完成，留 5 天做 paper integration + final review，时间充足但不能再加大实验
4. EMNLP 2026 ARR 格式 ≤8 pages，当前 22 pages（含 appendix），注意正文不超页


---
