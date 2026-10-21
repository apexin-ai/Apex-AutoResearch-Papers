# director / loop_6.md

**When the Most Disruptive Messages Are Safe to Prune in Aggregate: Functional Analysis of Communication Pruning in Two-Agent LLM Systems** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_6.md`
- **Structured JSON:** [`fcf5d06a1d2ffb8bcc08.json`](../../sessions/fc/fcf5d06a1d2ffb8bcc08.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-04-27T01:54:52+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 **只能用 cuda:1**（gpu_ids=[1]）。cuda:0/2/3 属于其他项目，D172 因 cuda:0 违规被终止过
- oracle 实验 **必须用 GPT-4o** 做标注（D171），不能换 72B AWQ 或其他本地模型替代
- AutoDL 服务器 **无法直接访问 OpenAI API**（DNS 污染 + proxy 仅支持 HF/GitHub），这是 oracle_online 实验的根本阻塞
- 实验结果必须附 `cat result.json | head` + `ls -la` 原始文件输出（D149 数据诚信事件教训，不接受没有文件证据的 metrics）
- 论文中不得出现 "detector-dependent" 归因（memory.md 已修正为 backbone-specific）

### 2. 🖥️ 基础设施快照
- 服务器：`westb-4x6000-a` (connect.westb.seetacloud.com)，账户 root
- 工作目录：`/root/autodl-tmp/comm_gate_mas`
- Python 环境：待新 session 探测确认（上轮用 conda base）
- 模型：vLLM 部署 Llama 用 cuda:1（上轮已验证可启动，但 D173 orchestrator launch failed）
- 数据：GSM8K / StratQA / ARC 数据在 outputs/ 下（18 files, 13270 lines synced）
- HF cache：`/root/autodl-tmp/.hf_cache`
- 活跃进程：**无**（两个 Worker 均 failed，无 RUNNING 实验）
- 无活跃 tmux session / cron 任务

### 3. 📊 当前状态
**刚做完**：R12 全部修复 + submit_paper_to_review（6 大类修复全部到位：claim 矛盾 ✅、TOST 降级 ✅、单智能体说明 ✅、Gemma 降级 ✅、token 压缩 ✅、匿名仓库 ✅）。Provenance 73/73 完整。

**刚失败**：
- `worker_gpu_oracle_online_llama_v2_launch` — D173 架构（本地 vLLM + orchestrator 避免调 OpenAI API）launch 立即 failed，根因未定位
- `worker_code_page_compression` — 也 failed

**Registry**：88 实验（success 65 / negative 9 / failed 3）。无 RUNNING / PREPARING。
**等待**：R12 审稿反馈（Review 团队 Group C 在处理）。NeurIPS 投稿审批卡片待用户确认。

### 4. 📋 待办
- Agent 新 session 启动 → 立即派诊断任务：SSH 到服务器检查 (a) vLLM 能否在 cuda:1 单独启动 (b) orchestrator 配置文件是否正确 (c) 确认 D173 架构具体失败点
- vLLM 诊断 PASS → 修复 orchestrator 配置，重启 oracle_online_llama_v2（cuda:1）
- vLLM 诊断 FAIL 或修复 > 1h → fallback 到 P2 (e2e_llama_gsm8k_n300_clean)，cuda:1 不能空
- GPU 实验启动后 → 并行派非 GPU 任务：NeurIPS 提交材料检查（编译/页数/宏一致性/匿名化）+ 匿名仓库清单
- R12 审稿反馈返回 → 按 review-report-action skill 处理（Holistic Pass → Per-Comment Action Matrix）
- oracle_online 如果最终无法解决 API 访问 → 考虑预计算方案（本地跑 GPT-4o annotation batch，scp 上传标注文件到服务器）或向用户申请服务器端 API 代理

### 5. 🎯 战略上下文
**核心结论**：ack 消息展现"高扰动敏感性 + 可安全剪枝"的悖离，且该效应在 7B→72B 范围内 scale-stable。双 backbone (Llama + Qwen) 均 non-inferior。

**决策链关键节点**：
- D170: 审批 oracle_online 3-seed Llama（科学目的：分离 heuristic over-suppression vs true ack pruning effect）
- D171: 必须用 GPT-4o → D172: cuda:0 违规终止 → D173: 本地 orchestrator → D174: launch failed, RESET BOTH

**最容易判断错的事**：
- oracle_online_llama 的科学意义：heuristic pruning +2.1pp 可能是 over-suppression artifact（74.4% suppression vs ~45% true ack rate）。如果 oracle pruning 也 ≥+2pp → ack pruning 本身有效；如果 ~0pp → +2.1pp 是假阳性。这决定论文 Llama 那半边的 claim 强度
- R12 审稿反馈处理 ≠ 我方执行缺口。6 大类修复已全部做完提交，当前等的是 Review 团队返回新意见
- NeurIPS DDL 极近（abstract 5/3-4, paper 5/5-6），非 GPU 任务（提交检查、匿名仓库）不能再拖
- AutoDL 服务器的 OpenAI API 访问问题是结构性阻塞，不是临时网络故障，简单重试不会解决


---
