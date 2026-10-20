# agent / loop_2.md

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`57e5730d0714343060dd.json`](../../sessions/57/57e5730d0714343060dd.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-12T22:35:00+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**只能用 cqa1-21977 的 cuda:2 和 cuda:3**，其他 GPU 一律 push back Director
- vLLM 端口分配：**8001 = hgate-dpo002（cuda:3），8002 = hgate-dpo003（cuda:2）**，不要混用或覆盖
- **不要删除** `/root/autodl-tmp/models/Qwen/`（dpo-002/003 基础模型）、`Qwen2.5-7B-Instruct-DPO-merged/`、`structfuse/`（其他项目）
- llama-bcp-001 数据**已降级为辅助证据**：不能 claim "BCP 失败机制跨模型复现"，最多支持"低能力模型在 BCP 下展现行为偏移"（Reviewer 修正）
- dpo-001/dpo-002 均有 TRL tokenizer mismatch bug（D006 确认），**不作为决策依据**，仅为对比数据点

### 2. 🖥️ 基础设施快照
- 服务器：**cqa1-21977**，账户 root，工作目录 `/root/democalib`
- Python：aml-train 镜像，`/root/miniconda3/bin/python`，conda base 环境
- 模型路径：`/root/autodl-tmp/models/Qwen/Qwen2.5-7B-Instruct`（基础模型）
- DPO checkpoints：`dpo_output/`(v1) / `dpo_output_v2/`(v2) / `dpo_output_v3/`(v3 Fix B)，各有 `final_adapter/`
- Mistral hedge：`/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3/`（14GB，已验证 tokenizer）
- 磁盘：`/root/autodl-tmp/` 约 33GB 可用（清理后）
- 活跃进程：
  - **hgate-dpo003**: tmux=hgate-dpo003, cuda:2, port 8002, cron 监控中（决策节点）
  - **hgate-dpo002**: PID 311654, tmux=hgate-dpo002, cuda:3, port 8001, cron 监控中（对比数据点）
- W&B：project=democalib，dpo-003 训练时 WANDB_MODE=disabled

### 3. 📊 当前状态
刚完成：dpo-003 registry 更新为 DONE/success + 派 Worker 启动 hgate-dpo003 eval on cuda:2。

Registry RUNNING/PREPARING：
- **hgate-dpo003** (RUNNING) — 决策节点 eval，cuda:2，4 runs × 20 tasks × 6 variants，~80min
- **hgate-dpo002** (RUNNING) — 对比数据点 eval，cuda:3，同 protocol，~80min

等待中：
- 两个 eval 的 cron 回调（完成后自动触发 `[CRON]` 消息）
- Director 无待决策项（等 eval 结果后分叉）

### 4. 📋 待办
- **hgate-dpo003 cron 回调** → 读日志聚合 4 runs 结果 → 判 H2（politeness ≤45.1%）+ H3（completion ≥29.6%）→ update_registry → 按 on-experiment-done skill 分叉处理 → 汇报 Director（这是 Plan A/B/KILL 的唯一判据）
- **hgate-dpo002 cron 回调** → 同上流程 → 作为对比数据点记录，与 hgate-dpo001/hgate-dpo003 横向对比
- **hgate-dpo003 H2+H3 双 PASS** → Plan A：DPO 校准方法论文，Mistral 非必须
- **hgate-dpo003 FAIL** → Plan B：empirical analysis paper，需在 Mistral-7B 上复现 BCP（模型已就绪）
- **磁盘告警**：如有额外 checkpoint 写入需求，可删 `Qwen2.5-7B-Instruct-DPO-merged`（15GB）释放空间

### 5. 🎯 战略上下文
- 核心方向：DemoCalib — 用小样本校准 LLM 用户模拟器的方言行为分布，使 agent 评估对 AAVE/印度英语更公平
- 投稿目标：**EMNLP 2026 Findings，ARR deadline 2026-05-25（剩余 13 天）**
- 决策链：D001(MVP)→D002(H-gate重构)→D003(BCP FAIL)→D004(三失败机制)→D005(决策树)→D006(TRL mismatch根因+Fix B)→D007(Llama无效)→D008(hedge Mistral)
- **dpo-003 是唯一决策节点**：dpo-001/002 都有 mismatch bug，只有 dpo-003 (Fix B, 0% mismatch) 的 H-gate 结果决定方向
- 易错点：**不要用 dpo-001/002 的 H-gate 结果做任何方向判断**——它们的 mismatch 使学习信号极弱（acc 0.5→0.667），eval 结果只有对比价值
- 易错点：dpo-003 训练指标看起来很好（acc 0.75-1.0），但训练 accuracy ≠ eval completion。H-gate eval 才是真正考验
- BCP 路线已判 FAIL（D003/D004），三个失败机制（global suppression, cross-dim interference, overcorrection）是可发表 negative result，但 Llama 复现数据不支持"跨模型复现"claim


---
