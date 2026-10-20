# director / loop_3.md

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`c1500b499537464f2e2e.json`](../../sessions/c1/c1500b499537464f2e2e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-16T01:19:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:0（westd-32608 单卡服务器，无其他 GPU）
- QwQ-32B 模型不可替换（D002 锁定），弱模型只能作为 ablation
- vLLM max_model_len=16384（32768 会导致 engine core 初始化失败），因此 max_tokens 必须 ≤ 12288（留空间给 prompt）
- Z3 MaxSAT solver 必须有 60s 硬超时（v3 在 P23 被 Z3 hang 杀死过）
- 逻辑域实验用 LOGIC_EXTRACTION_PROMPT / FOLIO_PROMPT，不复用 MATH prompt

### 2. 🖥️ 基础设施快照
- 服务器：westd-32608，GPU: 1× NVIDIA RTX PRO 6000 Blackwell (98GB)
- 工作目录：/root/symb_invariant_consensus/sica/
- Python：/root/miniconda3/bin/python（conda base，不用 venv）
- 模型：/root/autodl-tmp/models/QwQ-32B/Qwen/QwQ-32B/（ModelScope 嵌套路径）
- vLLM：port 8000, bfloat16, max_model_len=16384, gpu_memory_utilization=0.90
- 数据：MATH-500 子集 /root/symb_invariant_consensus/data/math500_subset.json；ProofWriter-30 + FOLIO-30 子集已准备就绪（dry-run 通过）
- 活跃进程：sica_proofwriter30_v2 应在运行中（启动约 6h 前，预估 2.5h，可能已完成）；vLLM PID 需确认是否存活

### 3. 📊 当前状态
- **sica_proofwriter30_v2**：约 6h 前启动（max_tokens=12288 已修复），预估 2.5h。极可能已完成但 Agent 三次 idle 超时未处理回调。**第一优先级：检查这个实验的状态和结果。**
- **sica_folio30**：registry spec 已修复为 max_tokens=12288，等 ProofWriter 完成后串行启动
- **sica_aime30_v3**：已结束（22/30，进程自行退出），registry 可能仍为 RUNNING 需更新
- P1 早期信号（仅 1 题）：SC 12/12 unanimous（单候选），约束提取失败 8/12 traces — 令人担忧但样本太小

### 4. 📋 待办
- 启动后立即 SSH 检查 sica_proofwriter30_v2 状态 → 如已完成：读取结果 JSON，按 D012 标准评估（C0 多候选率、C1 提取率、C2 矛盾数、C3 SICA vs SC gap）
- ProofWriter 完成 → 立即启动 sica_folio30（命令用 --max-tokens 12288，已在 registry spec 中修正）
- FOLIO 完成 → 合并 60 题做 D012 MVP 判定
- D012 PASS → 通知用户 + 启动 post-MVP kickoff（paper_framing.md → experiment_plan.yaml → dream_simulate）
- D012 FAIL → 通知用户 MVP 失败，建议 May 19 checkpoint 终止 EMNLP，评估是否值得在 AAAI 时间线下换方向
- sica_aime30_v3 registry 如仍为 RUNNING → 更新为 killed/done + delete_cron

### 5. 🎯 战略上下文
- **核心发现**：SICA 在数学域（AIME + MATH）与 SC 完全等价（0pp gap），根因是 QwQ-32B 单候选主导——模型级特征，非任务特定（D010/D011，32 题 × 多温度零多候选）
- **决策链**：D002（锁定 QwQ-32B）→ D003（MVP 标准 v2）→ D007-D009（parser/scorer/truncation 修复）→ D010（0pp 结构性确认）→ D011（pivot 逻辑域）→ D012（逻辑域 MVP 标准，60 题合并判定）
- **最易判断错的事**：P1 早期信号显示逻辑域也可能是 12/12 unanimous 单候选。如果 C0（多候选率 ≥20%）FAIL，意味着 SICA 的 answer reranking 机制在 QwQ-32B 上系统性失效，不分域。这时不要试图再换 prompt/温度/数据集来挽救——32+ 题零多候选已是充分证据，应果断 FAIL
- **May 19 checkpoint**：距截止 ~3 天。逻辑域两个实验各 ~2.5h，时间充裕但不能再出第三次 idle 空转
- **容易踩的坑**：max_tokens 必须 ≤ 12288（不是 16384）；vLLM 如果挂了需要重启（检查 port 8000 是否响应）；ProofWriter 用 LOGIC_PROMPT，FOLIO 用 FOLIO_PROMPT（不同模板）


---
