# agent / loop_7.md

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_7.md`
- **Structured JSON:** [`4ec9b3858ae86759974a.json`](../../sessions/4e/4ec9b3858ae86759974a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: idle_timeout
updated: '2026-05-17T07:59:30+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-32608:cuda:0（gpu_ids=[0]，唯一分配）
- 多个 cross-family 实验（exp-010-mistral, exp-011-llama8b）反复因模型下载损坏失败，重跑前必须先验证模型完整性（checksum/shard size）
- vLLM 服务独占 GPU，启动新实验前必须确认无残留 vLLM 进程（之前 exp-011 因旧 vLLM 占显存 OOM）
- EXIT_CODE=129/143 在本项目常见：129=SIGHUP 伪失败（实际成功），143=SIGTERM 真 kill——必须看日志区分

### 2. 🖥️ 基础设施快照
- 服务器：westd-32608，GPU：1× RTX PRO 6000 Blackwell 98GB
- 工作目录：`/root/symb_invariant_consensus/`（远程）
- 运行日志：`~/runs/symb_invariant_consensus/`
- 模型缓存：HuggingFace cache（Qwen2.5-14B-Instruct 已验证可用；LLaMA-3.1-8B 权重 shard 2 损坏 3.7G vs 4.9G；Mistral-7B-v0.3 下载多次截断）
- vLLM 用于推理服务（单 GPU 部署）
- 活跃进程：无（GPU 当前空闲）
- Cron：reconcile 返回 0 active

### 3. 📊 当前状态
刚收到 exp-017-strategyqa 失败回调（EXIT_CODE=143 SIGTERM），已派 Worker `worker_diagnose_exp-017-strategyqa_20260517T034803` SSH 诊断日志，**尚未收到回调**。

Registry 状态：
- DONE: 21 个（success 8, negative 2, failed 5, killed 6）
- QUEUED: exp-010-mistral-v2, exp-018-arc（等 GPU）
- PREPARING: smoke-test-5q（遗留，无意义）
- RUNNING: 无

近期连续 3 个 failed：exp-017-strategyqa (SIGTERM)、exp-010-mistral (进程 5× dead)、exp-011-llama8b-v2 (权重损坏)。全是基础设施问题，非 negative result。

等待中：
- Worker 诊断回调 → 确认 exp-017 失败根因
- Director 决策：是否继续投入 GPU 跑 cross-family/cross-domain 验证

### 4. 📋 待办（条件触发式）
- 诊断 Worker 回调到达 → 根据根因决定：脚本 bug 则修复重跑；OOM 则调参重跑；外部 kill 则查明谁 kill 了
- exp-017 可重跑 → 用 submit_training_job 重新提交（确认无残留 vLLM）
- exp-010-mistral-v2 启动条件 → 先验证 Mistral-7B 模型完整性（ls -la shards + 对比预期 size）
- exp-018-arc 启动条件 → exp-017 成功或确认放弃后，切换到 ARC 数据集
- 所有 cross-validation 完成 → 汇总 C2 (operating regime) 证据，更新 paper_framing.md

### 5. 🎯 战略上下文
- **核心结论**：SICA ≈ SC（+0.25pp, n=804, n.s.）。项目已 pivot 到 "Capability Trap Analysis Paper"——论证为什么 symbolic consensus 不 work
- **三个 Claims**：C1(mechanism vacuous, 已有 exp-013+exp-016 支撑)、C2(operating regime boundary, exp-005 QwQ 支撑但缺 cross-family)、C3(C0 predictor, 需 multi-model 数据)
- **当前瓶颈**：cross-family 验证（Mistral/LLaMA）和 cross-domain 验证（StrategyQA/ARC）全部因基础设施问题失败，没有一个成功。C2 claim 缺乏 non-Qwen 模型数据点
- **易错点**：
  - 不要把 failed（基础设施崩溃）和 negative（hypothesis 被证伪）混淆——failed 应该重跑而非推导新 hypothesis
  - Qwen2.5-14B 的 sica_expanded_14b 是核心成功实验（N=804），所有 cross-validation 都是从它 derive 的
  - K-ablation 结果（SICA≤SC for all K）强化 C1 但也意味着方法本身无效——这是 feature not bug（分析论文视角）
  - vLLM 在 98GB 卡上跑 14B 模型没问题，但 LLaMA-8B 和 Mistral-7B 需要重新下载完整权重


---
