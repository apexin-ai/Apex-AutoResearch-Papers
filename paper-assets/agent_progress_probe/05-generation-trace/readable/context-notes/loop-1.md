# director / loop_1.md

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`e7cc30e63ab055167776.json`](../../sessions/e7/e7cc30e63ab055167776.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-14T10:00:26+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 gpu-5090-2x-2 的 cuda:0 和 cuda:1（RTX 5090 32G × 2）
- autodl-5090 和 gpu-5090-2x-2 是同一台机器的两个 SSH alias，不要当两台用
- temporal-label-model 实验有门禁：gold set 上 accuracy 提升 ≥5pp vs majority vote，否则需 fallback
- human-annotation 已升为 P0（Reviewer 建议）——Claim 1 和 Claim 2 都依赖 gold set，必须向用户确认可行性
- Re-dream (dream_20260514T095527) 结果出来前，不批准 temporal-label-model 和 flyingsquid-baseline

### 2. 🖥️ 基础设施快照
- 服务器：gpu-5090-2x-2 (connect.bjb2.seetacloud.com)，工作目录 /root/autodl-tmp/agent_progress_probe
- Python：conda base 环境，/root/miniconda3/bin/python
- Embedding 模型：Qwen3-Embedding-0.6B（服务器本地已缓存）
- Embeddings 数据：/root/autodl-tmp/agent_progress_probe/embeddings/（1.1GB, 54,809 windows）
- Checkpoints：checkpoints/（conf≥2 probe-001）、checkpoints_full/（conf≥0 probe-002）
- 活跃进程：probe-002 和 baseline-meanpool-lr 均已完成，当前无 RUNNING 进程
- GPU 状态：cuda:0 和 cuda:1 均空闲

### 3. 📊 当前状态
**刚完成**：
- Dream 审稿分析（D009）：三档全 3/6 Weak Reject → framing pivot 到 temporal label model
- probe-002 全量数据结果（D010）：0.8468 macro-F1，LF All-Agreement (0.8543) 仍略高 0.75pp
- baseline-meanpool-lr 完成：GRU vs MeanPool gap = 4.83pp (conf≥2) / 12.74pp (全量)
- paper_framing.md 和 experiment_plan.yaml 已更新（temporal label model 为核心贡献）

**等待中**：
- Re-dream dream_20260514T095527（验证新 framing）—— 完成后会注入 [DREAM] 回调
- Agent 正在处理三个并行任务：(1) cross-agent OpenHands 数据准备 + embedding (2) lf-temporal-dynamics 分析 (3) error-analysis
- 两个 GPU 空闲！Agent 应该用 cross-agent 的 embedding 任务占满

### 4. 📋 待办
- Re-dream 回调到达 → Read dream-report-action skill → 按协议分析，目标 best ≥ 4/6
- Re-dream best ≥ Weak Accept → 批准 temporal-label-model + flyingsquid-baseline
- Re-dream 仍 Weak Reject → 回头再调 framing（考虑 HMM temporal label model 或更强的方法创新）
- Agent 回复 cross-agent 数据准备完成 → approve_experiment + director_allocate_gpus 分配两张卡
- Agent 回复 lf-temporal-dynamics 完成 → 验证 LF lead/lag 数字是否稳定（temporal model 的前提）
- FlyingSquid baseline 尽早跑（Reviewer warning：如果 FlyingSquid 已解决 LF correlation 问题，temporal model 需要在其基础上再提升）
- 向用户确认：(1) EMNLP 5/25 vs ACL 8月 deadline (2) human-annotation 400 windows × 3 annotators 是否可行
- baseline-llm-judge 需要 API key（Claude/GPT-4o）→ feishu_send_tum_key_request_card

### 5. 🎯 战略上下文
**决策链**：D001(MVP方案) → D007(MVP通过) → D008(LF Oracle发现：command_repetition > probe on conf≥2) → D009(Dream Weak Reject → temporal label model pivot) → D010(probe-002: LF All-Agreement仍>probe on full data)

**核心判断**：Probe 无法超越其自身标签来源（majority vote LF ensemble）。这不是 probe 的问题，是标签质量的瓶颈。temporal label model 是打破瓶颈的路径。cross-agent（OpenHands 迁移）是论文最关键的实验——在 LF 不可用的场景下 probe 是唯一选择。

**易错点**：
- 不要混淆 conf≥2 和 conf≥0 的结果——两个 test set 不同，不能跨数据集比较
- LF All-Agreement > Probe 仅在全量数据上成立（0.8543 vs 0.8468），在 conf≥2 上 probe 领先
- Dream 报告中的实验数据是想象的——通用建议（novelty/related work）可信，数据依赖建议需跨档验证
- paper_framing.md 中的 headline numbers（"improves by X%"）是占位符，待真实实验填充
- Reviewer 正确指出 "student exceeds teacher" 是两步假设链：temporal model 好标签 → probe 超 LF。任一环节失败都要调叙事


---
