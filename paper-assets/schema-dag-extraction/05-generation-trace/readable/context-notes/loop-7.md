# director / loop_7.md

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_7.md`
- **Structured JSON:** [`fa058762d5c3cf24177e.json`](../../sessions/fa/fa058762d5c3cf24177e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_messages
updated: '2026-05-16T19:08:37+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 只有 cqa1-38874 cuda:0（单卡），不可用其他设备
- 论文正文必须 ≤8 页（ACL ARR 格式），每次文本修改后必须编译验证
- "additive separability" / "cleanly separable" 已全文删除，禁止重新引入——统一用 "bounded interaction"
- TOST SESOI 不能用 prompt-noise (~25pp) 锚定——已被审稿人三轮否定
- 提交 ARR May 25（距今 9 天），不可误 DDL

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-38874 (connect.cqa1.seetacloud.com)，账号 root
- 工作目录：/root/schema-dag-extraction
- Python 环境：需 SSH 探测确认（aml-train 镜像，大概率 conda base）
- 论文本地路径：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/`
- 活跃进程：tmux session `d051_batch2`（count curves 25 batches + 3-seed variance），预计 8-12h 总时长
- Registry: `exp_d051_count_curves_25` = RUNNING
- Cron 监控：每 5 分钟轮询 d051_batch2 session

### 3. 📊 当前状态
- **D051 Batch 1（文本修改）已完成并验证通过** — W1-W5 全部 critical + S3-S9 should-fix/info，Reviewer PASS
- **D051 Batch 2（GPU 实验）正在跑** — FewRel/Few-NERD 各 25 batches × 7/6 count levels + 3 seeds variance decomposition
- **Round 9 审稿**: 3.0/3.0 Weak Reject，三人共识 Findings-level
- **已向用户报告**: Main <20%, Findings >90% 概率评估，等用户最终决策 Main vs Findings 定位
- **MW2 unconditional Monte Carlo 已完成**: R²=0.044 (5× gap from observed 0.218)
- **R5-W1 split-origin covariate 已完成**: BCS partial effect 不变 (p=0.245 for origin)

### 4. 📋 待办
- Batch 2 cron 回调（exp_d051_count_curves_25 完成）→ 派 Worker 重新生成 Figure 1a (±1SD error bars) + variance decomposition table → 更新论文 → 编译验证
- Figure 更新完成 → submit_paper_to_review Round 10 (recommend: continue mode) 验证全部 D051 修复
- 用户回复 Main/Findings 定位 → 如果 Findings，无需额外行动（ARR 提交后 commitment 阶段勾选 "open to Findings"）；如果坚持 Main，评估是否需要加模型验证
- Round 10 通过 (score ≥3.5) → 准备 ARR 提交材料（Anonymous GitHub、supplementary）
- Round 10 仍 ≤3.0 → 建议用户接受 Findings 定位，不再迭代

### 5. 🎯 战略上下文
- **核心瓶颈是 novelty，不是 rigor** — 审稿人一致认为 "count > confusability" 是 confirmatory finding。文本修复已做到极限，分数卡在 3.0-3.25 四轮未突破。
- **易错判断 #1**: 不要以为再修一轮文本就能到 3.5。结构性问题（confirmatory nature）无法靠措辞解决。
- **易错判断 #2**: Split-origin covariate 和 unconditional Monte Carlo 是防守性证据（驳斥 confound），不是进攻性证据（提升 novelty）。不要期望它们影响分数。
- **决策链**: D049(R7修复) → D050(R8修复) → D051(R9修复+GPU补实验)。每轮修的都是同一批 systemic issues 的不同措辞版本。
- **TOST 死循环**: ±3pp margin > 2.2pp typical effect 是数学事实，无论怎么论证都无法消除这个矛盾。当前策略是诚实报告 sensitivity (±1/2/3/5pp) 并承认 ±1pp inconclusive。不要再尝试新的 SESOI 论证角度。
- **review_issues.yaml** 是跨轮次追踪的权威来源，已更新到 D051 状态。


---
