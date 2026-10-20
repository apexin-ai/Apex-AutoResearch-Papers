# director / loop_1.md

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`628f55acfedd710b258d.json`](../../sessions/62/628f55acfedd710b258d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-15T15:43:19+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-32608 的 cuda:0（1× RTX PRO 6000 Blackwell 98GB），无其他 GPU 分配
- 模型固定 QwQ-32B FP16，不可替换（D003 硬约束）——换模型需要 Director 批准新决策
- May 19 UTC 前 MVP 未 pass → 放弃 EMNLP May 25，切 AAAI 2027（D003/ROADMAP 明确）
- 当前 AIME v2 用的是旧代码（修复前），Z3 Bool type bug 会导致部分题 crash——不要以为代码已修复就跳过验证

### 2. 🖥️ 基础设施快照
- 服务器：westd-32608 (connect.westd.seetacloud.com)，工作目录 /root/symb_invariant_consensus
- Python：aml-train 镜像，conda base 环境，`/root/miniconda3/bin/python`
- 模型：QwQ-32B FP16 via vLLM serving on cuda:0（ModelScope 下载，14 shards ~61GB）
- 数据集：/root/symb_invariant_consensus/data/（math500_subset.json 50题, aime2024_subset.json 30题, proofwriter_subset.json 10题）
- 活跃进程：sica_aime30_v2 (PID 121139)——**可能已完成或 crash，需要第一时间 SSH 检查**
- W&B / HF：未配置（本项目不使用）

### 3. 📊 当前状态
刚完成用户请求——向孙震详细解释了 SICA 完整 idea（motivation/背景/当前工作/问题/claims），已通过 director_reply_to_user 发送。

已向 Agent 派单检查 sica_aime30_v2 进度（Agent 空闲 81min），等待 Agent 回复。

Registry 状态：
- **sica_aime30_v2** — RUNNING：AIME 2024 30题，QwQ-32B，验证"SICA 在高难度场景下有信号"
- smoke-test-5q — PREPARING (failed)：旧实验，可忽略
- 其余 5 个实验全部 DONE（crd_folio_main=success, sica_smoke_5q=success, sica_temp_diversity=negative, mvp_math50_t07=killed, sica_aime30_t07=killed）

### 4. 📋 待办
- Agent 回复 AIME v2 进度 → 根据结果分叉：
  - 实验完成且有结果 → 分析 SICA vs SC 对比数据，按 D003 三档标准做 MVP 判定
  - 实验 crash（Z3 bug on old code） → 让 Agent 用修复后代码重跑
  - 仍在运行 → 等待完成，估算剩余时间
- AIME v2 结果出来后 → 如果矛盾检出 ≥5 题且 SICA>SC → 回跑修复后的 MATH-50 补充数据
- AIME + MATH 两组结果齐全 → MVP PASS/FAIL 最终判定（deadline May 19）
- MVP PASS → complete_mvp() + post-mvp-kickoff（paper_framing.md → experiment_plan.yaml → dream_simulate）
- MVP FAIL → 决策：换弱模型（Qwen2.5-7B）作为最后手段 or 止损

### 5. 🎯 战略上下文
- **决策链 D001→D006**：D001 定 MVP 方案 → D002 纠正 CRD 错误回归 SICA → D003 加固标准（三档判定）→ D004/D005 确认 QwQ-32B MATH-500 零分歧但继续 → D006 kill MATH MVP 优先跑 AIME
- **核心发现**：QwQ-32B 作为 reasoning model 在 MATH-500 上 trace 多样性极低（T=0.7/0.9/1.0 均零分歧），SICA 在"模型已经很准"的场景下无信号。AIME 2024（QwQ-32B ~79.5%）是寻找信号的最佳战场
- **AIME v2 早期信号**（旧代码，5/30）：Problem 1 有 5 个排除约束（正面），Problem 2 crash（Z3 bug），Problem 3 首次答案分歧 11/12，Problem 4 提取失败 8/12——信号有但提取质量是瓶颈
- **易错点**：不要把 AIME v2（旧代码）的 crash 当作方法论失败——那是实现 bug，修复后的代码已 ready；不要因为 MATH-500 零分歧就判 FAIL——AIME 才是正确的验证场景；Extraction-Verification Paradox（难题提取差）是已知风险，但不是 showstopper
- **ROADMAP 需更新**：当前 ROADMAP 停留在 D003 后的状态，D004-D006 的决策未反映，AIME v2 进展未写入


---
