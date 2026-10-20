# director / loop_2.md

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`bdd5fa37c53f320e1e1d.json`](../../sessions/bd/bdd5fa37c53f320e1e1d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-14T17:41:51+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 autodl-rtx6000pro 的 cuda:0（唯一分配的卡）
- 服务器上 vLLM 和 pipeline 共用 cuda:0，不要同时启动第二个 vLLM 实例
- Pipeline 使用 Qwen3-32B（本地 vLLM serving），不要换成 API 调用或其他模型
- AutoDL 实例重启后 SSH 端口会变，连接失败先让用户查控制台

### 2. 🖥️ 基础设施快照
- 服务器：autodl-rtx6000pro (connect.westd.seetacloud.com) + westd-32608，工作目录 /root/autodl-tmp/crdd
- Python：AutoDL aml-train 镜像，conda base 环境（/root/miniconda3/bin/python）
- 模型：Qwen3-32B 通过本地 vLLM 服务（cuda:0）
- 数据集：FOLIO validation set，204 样本
- 活跃进程：v4 pipeline PID 42651，已完成 124/204 样本，预计 ~06:15 UTC 完成
- W&B：未配置
- HF_HOME：/root/autodl-tmp/.hf_cache

### 3. 📊 当前状态
mvp_pipeline_004 ANALYZING (success)——v4 全量 pipeline 正在跑，124/204 完成。中期快照 4/5 PASS（C5 localization 45.8% < 60% 是唯一 FAIL）。Reviewer 确认 PID 42651 存活正常。

Registry 状态：mvp_pipeline_004 标记为 ANALYZING 但实际仍在跑（registry 未正确更新为 RUNNING，不影响执行）。其余 5 个实验全部 DONE。

等待：v4 pipeline 完成回调 → 需要运行 evaluate_mvp.py 做最终评估。

### 4. 📋 待办
- v4 pipeline 完成（PID 42651 结束）→ Agent 运行 evaluate_mvp.py 生成全量 204 样本的 C1-C5 评估
- 全量 5/5 PASS → complete_mvp() 进入 research 阶段 → 启动 post-mvp-kickoff skill
- C5 仍 FAIL（全量 <60%）→ 分析 C5 失败样本，判断：(a) 算法改进空间 → v5b pipeline；(b) 阈值过严 → 考虑调整到 50% 或 45%
- 全量 C1/C2 也 FAIL（不太可能）→ 启动 ProofWriter pivot 备案

### 5. 🎯 战略上下文
- 核心假设：FOL vs Code 双表征分歧可诊断 LLM 推理错误。v4 中期 4/5 PASS 说明假设基本成立
- FOL-Code 不对称性 9:1（FOL 几乎总是对的，Code 几乎总是错的）——post-MVP framing 不能 claim bidirectional，需要诚实处理为"Code 错误的诊断工具"
- AGREE_WRONG 7.7% 是分歧方法的结构性盲区，论文需要坦承
- 决策链：D001 立项 → D002 Reviewer 反馈修订 MVP 标准 → D004 回退到 Qwen3-32B → D005 v1 失败根因是工程非假设 → D006 v2 部分修复 → D007 撤回 v5 closed-world 改为 v5b
- 易错：不要因为 C5 一个指标 FAIL 就判定 MVP 失败——先分析失败样本再决策。用户已收到完整状态汇报（刚回复过一次），不需要重复发


---
