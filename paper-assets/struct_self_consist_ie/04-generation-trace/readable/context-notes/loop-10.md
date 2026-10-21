# director / loop_10.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_10.md`
- **Structured JSON:** [`bc5f514fa2d9956db2bb.json`](../../sessions/bc/bc5f514fa2d9956db2bb.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_messages
updated: '2026-05-21T04:42:06+00:00'
---

### 1. 🔴 硬约束 / 红线
- Probe AUROC 只能引用 GroupKFold 数字（CoNLL 0.882, FewNERD 0.636, SciERC 0.630）。StratifiedKFold 数字（0.920/0.957/0.977/0.980）因 entity-level CV leakage 已作废，任何场景都不能引用
- 论文中 "majority vote" vs "LP-weighted" 标签已修正过一次（D214 claim audit CRITICAL），不要回退
- LSC baselines: greedy=0.794, MV=0.792, oracle=0.882。之前被错写为 greedy 0.779 / MV 0.837 / oracle 0.867，已修正
- GPU 白名单：autodl-5090 (cuda:0-3), autodl-5090-b (cuda:0-3), autodl-5090-c (cuda:0-3)，共 12 卡

### 2. 🖥️ 基础设施快照
- 服务器 3 台：autodl-5090 / autodl-5090-b / autodl-5090-c
- 工作目录：/root/autodl-tmp/struct_self_consist_ie
- 论文本地路径：projects/struct_self_consist_ie/docs/paper/（main.tex 入口）
- GroupKFold 最终数据：服务器 output/entity_probe_fulldata/groupkfold_probe_results.json
- 本地 artifact：artifacts/exp_hidden_state_probe/data/groupkfold_probe_results.md（500-inst 子集，仅参考）
- 活跃进程：FewNERD T=0.5/1.2 s456 (5090-b), 7B N=16 (5090-c:2), 14B FewNERD (5090-c:0), 8 GPU 填充 Worker 正在启动

### 3. 📊 当前状态
刚完成：Narrative B 补丁（probe GroupKFold 数字 + 复杂度依赖 introspection boundary）已落地到论文全部 11 处。编译通过，8 页正文，0 critical warnings。

已提交 pre-submission 审稿（apr_20260521T042646_3z9n, continue 模式），等用户审批卡片。

Agent 刚报告：32B FewNERD 完成（greedy 0.800, oracle 0.879），T-ablation 3-seed 大部分完成（FewNERD T=0.5/1.2 s456 还在跑），CoNLL N=16 PASS。12 个实验批量更新到 registry。

RESET_BOTH 已批准，本 handoff 后 Agent 和 Director 都会重建 session。

### 4. 📋 待办
- 用户审批审稿卡片 → Review 团队启动最终审查 → 收到审稿报告后按 review-report-action skill 处理
- FewNERD T=0.5/1.2 s456 完成 → 3-seed T-ablation 表完整，更新论文 mean±std
- 14B FewNERD 完成 → 分析 scale curve（8B vs 14B vs 32B），决定是否写入论文
- 7B N=16 完成 → N-scaling curve 数据点补全
- Review 团队报告页面超限 → Paper Agent 处理 page fitting（当前正文约 8.3 页，Conclusion 在第 8-9 页边界）
- Reviewer #23 flagged degeneracy 不一致（FewNERD T=1.2 = 24.7% vs discussion.tex SciERC T=1.2 = 14.9%）→ 已确认无误，两个是不同数据集，discussion.tex line 4 的 14.9% 是 SciERC（Table tab:t_degeneracy 明确标注 SciERC）

### 5. 🎯 战略上下文
- DDL 2026-05-25（~4 天）。论文核心内容已完成，当前在 polish + 补充实验阶段
- 核心贡献：correlation-selection gap（4-stage diagnostic cascade）+ self-verification ceiling（7 methods all fail）+ introspection boundary（probe 0.63-0.88, complexity-dependent）+ prescriptive escape routes（LP construction +1.40pp, cross-model +0.42pp, LP selection +1.39pp）
- D216 决策：introspection boundary 是 complexity-dependent（Narrative B），不是 "probe >> MV"（旧 Narrative A）
- API 余额耗尽 — Frontier SC 实验（GPT-5.5 等）被阻塞，用户多次被问但未解决
- 易错点：(1) 不要把 appendix tab:t_degeneracy 的 SciERC 数字和 FewNERD 数字混淆 (2) CoNLL probe 0.882 vs MV 0.87 是 borderline，论文用 "only marginally exceeds" 措辞 (3) 32B 是 Qwen2.5-72B zero-shot（论文写 72B），不是 Qwen3-32B


---
