# director / loop_8.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_8.md`
- **Structured JSON:** [`4bafbcaa7e3e135ce884.json`](../../sessions/4b/4bafbcaa7e3e135ce884.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_messages
updated: '2026-05-23T01:28:31+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只用 westd-19183 的 cuda:0 和 cuda:1（2 张卡）
- OpenVLA 是 VLA→VLA 转换（有 OXE 预训练），不是 VLM→VLA——论文 claim 必须分开处理，不能混入"convergent exit collapse"
- Bootstrap 统计必须用 canonical peak layer（从 full-data split 确定），禁止用 `np.max(boot_r2, axis=1)` per iteration（v1 的 winner's curse bug）
- 论文 DDL：Abstract 5/26，Paper 5/29（CoRL 2026）
- 用户要求审稿完成后通知他（memory: feedback_notify_on_review.md）

### 2. 🖥️ 基础设施快照
- 服务器：westd-19183 (connect.westd.seetacloud.com)，工作目录 /root/vla-ssd
- Python：conda base 环境，/root/miniconda3/bin/python
- 模型路径：/root/vla-ssd/models/（OpenVLA, TracVLA, NORA 三个 VLA + 对应 base VLM）
- Bootstrap 脚本：/root/vla-ssd/scripts/clustered_bootstrap_v2.py（joblib 并行，n=1000）
- Bootstrap 输出：/root/vla-ssd/artifacts/clustered_bootstrap/v2/（预期 20 个 JSON）
- 论文源码：本地 /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/
- 活跃进程：bootstrap v2 在双卡上运行，Agent 刚报告 2/20 完成，预估 ~03:00-03:30 UTC 全部完成

### 3. 📊 当前状态
- **Bootstrap v2 运行中**：2/20 条件完成，Agent 已被指派监控并在全部完成后生成 summary_table.md
- **早期 v2 结果**：TracVLA goal Δ=0.333 CI=[0.055, 0.342] ✅显著；OpenVLA goal CI 全负 ❌（符合预期，VLA→VLA 无 exit collapse）
- **Paper Agent**：14 项 major revision 全部完成（title 改、claim 调弱、格式合规、concurrent work 段落、NLP control 描述增强）。论文已编译通过（34 页，main body ≤8 页）
- **Research Reviewer**：48h+ PDF parse 循环无法工作，刚被 RESET
- **Registry**：clustered_bootstrap_reanalysis_v2 = RUNNING；其余 149 个实验全 DONE
- **Round 15 审稿**：Weak Reject 4.5/10，已完成 Holistic Pass + Action Matrix，所有 action item 已派发执行

### 4. 📋 待办
- Agent 报告 bootstrap v2 全部 20 个 JSON 完成 → 检查 summary_table.md，重点验证：(1) NORA Goal CI 不再异常 (2) VLM→VLA 5/5 显著 vs VLA→VLA 0/4 显著模式保持 → 派 Paper Agent Patch 指令集成 CIs 到 Table 2 + Experiments + Abstract
- Paper Patch 完成 → submit_paper_to_review(mode="continue") 提交 Group C 二审 → 审稿完成后 director_reply_to_user 通知用户
- 如果 NORA Goal CI 仍然异常 → 诊断是否 canonical peak layer 选择有问题（检查 NORA 的 full-data R² profile）
- 如果 VLM→VLA 显著率 <5/5 → 重新评估 claim 强度，可能需要从"all 6 cells"改为"majority"

### 5. 🎯 战略上下文
- **核心发现**：VLA fine-tuning 产生 R² exit collapse（mid-layer R² 高、exit-layer 降）仅在 VLM→VLA 转换中出现（TracVLA、NORA），VLA→VLA（OpenVLA with OXE pretraining）不出现。这实际上加强了论文——clean separation of transition types
- **D101 决策**：Round 15 Weak Reject 的核心问题是 pseudoreplication（63K 观测值的嵌套依赖）和 sign test 脆弱性（N=6）。解决方案：demo-level clustered bootstrap 替代 sign test + 描述性一致性
- **Temporal leakage 发现**：原始 random-split probing 有同 demo timestep 泄露，R² 从 0.7-0.9 降到 0.4-0.6。这是方法学改进，已写入论文
- **易错点**：(1) 不要把 OpenVLA 混入 VLM→VLA convergence claim（它是 VLA→VLA）(2) Counterfactual sensitivity 的 Cohen's d 只适用于 trained models，untrained 用 cosine distance，两者不可比 (3) L1 attention 是 base-model prior 不是 VLA training 效果
- **Paper framing**：从"提出方法"转为"系统性分析"——3 findings 结构：exit collapse + counterfactual sensitivity + L1 attention prior。paper_framing.md 有完整 story


---
