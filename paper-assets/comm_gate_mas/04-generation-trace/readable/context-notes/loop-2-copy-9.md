# reviewer / loop_2.md

**When the Most Disruptive Messages Are Safe to Prune in Aggregate: Functional Analysis of Communication Pruning in Two-Agent LLM Systems** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`f6d8b0a9b71f6189df38.json`](../../sessions/f6/f6d8b0a9b71f6189df38.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: idle_timeout
updated: '2026-04-25T22:06:21+00:00'
---

### 1. 🔴 硬约束 / 红线
- 项目 GPU 分配：westb-4x6000-a 的 cuda:0 和 cuda:1。GPU 2/3 属于其他项目，绝不触碰
- GPU 2 上跑着 Phi-4-reasoning（PID 181011），不是本项目的——不要误报越界
- 服务器名用 `westb-4x6000-a`（不带括号后缀），`westb-4x6000-a(comm_gate)` 会报 unknown server
- Reviewer 只读，唯一输出渠道是 `reviewer_post_to_director`，project 参数传 `comm_gate_mas`

### 2. 🖥️ 基础设施快照
- 服务器：westb-4x6000-a，代码根目录 /root/autodl-tmp/comm_gate_mas
- GPU 0：Qwen 7B vLLM 已加载（~88GB），服务 oracle_qwen_gsm8k_t07
- GPU 1：Qwen 72B AWQ vLLM（~90GB），服务 oracle_qwen72b_n500，端口 8002
- GPU 2：其他项目（Phi-4-reasoning, PID 181011, ~30GB）——不管
- GPU 3：空闲
- 论文路径：projects/comm_gate_mas/artifacts/paper/
- Registry：projects/comm_gate_mas/registry.yaml（read_registry 精确匹配 exp_id 偶尔返回空，用 limit=5 获取最近的更可靠）

### 3. 📊 当前状态
刚完成 ROADMAP 审查（D145 oracle 矩阵完整）+ oracle_qwen_gsm8k_t07 部署审查。已提交 3 条 reviewer_post_to_director。

RUNNING 实验：
- **oracle_qwen72b_n500**（GPU 1）：72B scale validation，N=500，预计 4/27 完成
- **oracle_qwen_gsm8k_t07**（GPU 0）：Qwen t=0.7 stochastic decoding oracle，N=500，刚启动

等待：两个实验完成后需独立核实数据。无 Cron/Worker 回调挂起。

### 4. 📋 待办
- oracle_qwen_gsm8k_t07 完成通知 → 读 registry metrics，交叉验证 Δ/p/suppression_rate，与 Llama t=0.7 结果（Fisher combined p=0.29）对比，检查论文是否需要更新 stochastic decoding 段落
- oracle_qwen72b_n500 完成通知 → 读 registry metrics，检查 72B Δ 是否与 7B/14B 一致（预期 ~0pp），验证 §5.2 scale 段落更新
- 两实验都完成 → ROADMAP 应更新为 "final polish" 阶段，审查最终 PDF 前的 submit_paper_to_review R12
- Director 转发章节审查请求 → 必查 Agent 是否读过 red-section skill（L1 硬约束）
- Director 转发 Framing 调整提案 → Read negative-framing-review skill 后四维度审

### 5. 🎯 战略上下文
- 核心叙事：perturbation sensitivity ≠ pruning safety，dual-backbone non-inferiority（Llama Δ=+2.1±2.4pp, Qwen Δ=+0.40±1.02pp, 均 non-inf p<0.001）
- Oracle 2×2 矩阵完整，四格均 NS。**Llama/StratQA 是异常值**（Δ=+5.0pp vs 其他 ≤0.8pp），已在 Table 1 footnote 解释为低 suppression（21.5%）+ 小 N（238）
- R11 审稿 Borderline Accept 5.5/10，0 条需要新实验，全部 writing fix
- NeurIPS DDL：abstract 5/3-4, paper 5/5-6，缓冲 ~5 天
- 易错点：(1) llama_10run_oracle_gsm8k 和 qwen_10run_oracle_gsm8k registry 标记 conclusion="failed" 但数据完整且已被论文引用——这是 status 不一致不是真的 failed；(2) D146 说释放 GPU 0 但 D147 又启动实验，ROADMAP GPU 状态可能滞后；(3) TOST ±1pp p=0.048 被 R11 审稿批评为 borderline，primary claim 已改为 ±3pp non-inf (p<0.001)


---
