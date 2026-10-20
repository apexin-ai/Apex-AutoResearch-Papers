# agent / loop_4.md

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_4.md`
- **Structured JSON:** [`85908424a3fe5275a068.json`](../../sessions/85/85908424a3fe5275a068.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: idle_timeout
updated: '2026-05-14T21:19:06+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 **仅 cuda:0**（`execution.gpu_ids: ["cuda:0"]`），autodl-rtx6000pro 上只有这一块卡
- vLLM serving 进程与 pipeline 共用 cuda:0，不要另起 vLLM 实例
- 禁止双进程写同一输出文件（2026-05-14 事故：tmux + nohup 同时启动导致数据损坏 + 静默退出）
- repair.py 已修复 repr_type 动态 prompt（之前硬编码 "Python script" 误导 FOL repair），**不要回滚此修复**
- v5 closed-world 2-way 方案已撤回（D007），保持 3-way 输出

### 2. 🖥️ 基础设施快照
- 服务器：**autodl-rtx6000pro**，工作目录 `/root/autodl-tmp/crdd`
- Python：`/root/miniconda3/bin/python`（conda base env，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 模型：Qwen3-32B-AWQ (awq_marlin)，vLLM serving 运行中（共用 cuda:0）
- 数据：FOLIO validation set（204 samples），结果在 `/root/autodl-tmp/crdd/results/mvp_v4_full.json`
- 日志：`pipeline_v4_full.log`（服务器上）+ `~/runs/cross_representation_disagreement_diagno/mvp_pipeline_004.log`
- 活跃进程：mvp_pipeline_004 PID 47964（或子进程 47959），tmux session
- Cron：当前无活跃 cron（reconcile 返回 0）
- HF cache：`/root/autodl-tmp/.hf_cache`（AutoDL 规范）
- AutoDL 注意：pip/git 前 `source /etc/network_turbo`；SSL 证书需 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt`

### 3. 📊 当前状态
- **mvp_pipeline_004** 状态 ANALYZING / conclusion=success，registry 记录进度 144/204（PID 47964 alive）。可能已完成或接近完成——需 SSH 确认实际进程状态和最终样本数
- 126 样本中间评估：**All-mode 5/5 PASS**（C1=35.9%, C2=88.1%, C3=3, C4=+7.4pp, C5=79.2%）
- Excl-Unknown 4/5（C4 FAIL +0.0pp），根因是 repair.py prompt bug，**已修复但未重跑**
- C4 趋势下滑：+22.6pp(@80) → +11.6pp(@109) → +7.4pp(@126)，风险：204 全量可能跌破 5pp
- 无等待中的 Worker 回调或 Cron
- 其他实验全部 DONE（001 negative, 002 negative, 003 killed, 003b killed）

### 4. 📋 待办（条件触发式）
- mvp_pipeline_004 进程结束 → SSH 确认 204/204 完成 → 运行 `evaluate_mvp.py` 最终评估 → 更新 registry metrics
- 204 全量评估完成 → 运行 `repair_only.py` 用修复后的 repair.py 重跑全量 repair+eval（关键：验证 C4 excl-unknown 修复效果）
- repair-only 结果出炉 → All-mode + Excl-Unknown 两组指标汇报 Director
- **如果 All-mode C4 ≥ 5pp + Excl-Unknown C4 修复后也 ≥ 5pp** → MVP 最终 PASS → 向 Director 汇报，申请进入 post-MVP 阶段（扩数据集/扩模型/写论文）
- **如果 C4 全量 < 5pp** → negative 结论 → 按 red-section 产出 Framing 调整提案，不默默跑下一个
- repair-only 完成且 MVP PASS → 准备 v5b 实验（anti-lazy Unknown prompt），减少 46% Code=Unknown 问题

### 5. 🎯 战略上下文
- **核心假设**：FOL vs Code 双表征分歧能诊断 LLM 推理错误。MVP 用 FOLIO + Qwen3-32B 验证 5 个 claims（C1-C5）
- **进展轨迹** v1(2/5) → v2(2/5) → v4@80(4/5) → v4@126(5/5 all-mode)，逐步修 bug 改善，非假设本身有问题
- **关键发现**：DISAGREE 方向高度不对称（FOL 正确:Code 错误 ≈ 9:1），FOL 在结构化逻辑推理上碾压 Code
- **最易判断错的事**：C4 的 +7.4pp 看起来 PASS 但趋势在跌——**不要以 126 样本中间结果作为最终结论**，必须等 204 全量 + repair-only 重跑后才能判定
- **第二个坑**：C4 excl-unknown 的 +0.0pp 是 repair.py prompt bug 导致的（已修复），但修复效果未经验证，repair-only 重跑是关键——如果重跑后仍 FAIL 则说明 Code 端 targeted repair 本身效果有限，需要重新评估 C4 claim
- **备案**：ProofWriter pivot 仅在 v4 全量 C1+C2 也 FAIL 时启动，当前数据不支持 pivot
- 决策链：D001(MVP 方案) → D002(增加 baseline 门控) → D005(v1 FAIL 是 prompt 问题非假设问题) → D006(v2 部分改善) → D007(撤回 v5 改 v5b) → D008(repair prompt bug) → D009(126 样本 5/5 PASS)


---
