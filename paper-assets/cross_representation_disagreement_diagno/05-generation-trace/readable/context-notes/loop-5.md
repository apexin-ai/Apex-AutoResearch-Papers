# agent / loop_5.md

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_5.md`
- **Structured JSON:** [`f24c3618348d16db1d62.json`](../../sessions/f2/f24c3618348d16db1d62.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: idle_timeout
updated: '2026-05-15T00:23:24+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单仅 `cuda:0`（autodl-rtx6000pro），禁止使用任何其他 GPU
- 禁止双进程启动 pipeline——曾因 submit_on_allocated + nohup 同时写同一输出文件导致数据损坏（D007 教训）。启动前必须确认前一进程已终止
- v5 closed-world 2-way 方案已被 Reviewer 撤回（D007），不要再尝试。正确方向是 v5b：保持 3-way + anti-lazy Unknown 约束
- conda 环境，非 venv：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不要创建或假设 .venv 存在

### 2. 🖥️ 基础设施快照
- 服务器：autodl-rtx6000pro（主力），westd-32608（备用，未使用）
- 工作目录：`/root/autodl-tmp/crdd`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型：Qwen3-32B-AWQ (awq_marlin)，vLLM serving 在 autodl-rtx6000pro 上运行
- 数据集：FOLIO validation set，204 samples
- 产出目录：`/root/autodl-tmp/crdd/results/`，主文件 `mvp_v4_full.jsonl`
- 活跃进程：mvp_pipeline_004 PID 57877（tmux session），状态 ANALYZING / conclusion=success
- Cron：reconcile 返回 0 个活跃 cron（可能已清理或过期）
- HF cache / W&B：未配置（纯 API pipeline，无训练 loop）

### 3. 📊 当前状态
mvp_pipeline_004 处于 **ANALYZING** 状态，conclusion=success，registry 显示 177/204 样本已完成。PID 57877 可能已跑完或接近完成（report.md 上次更新时在 127/204，已过时）。

**148 样本 MVP 指标（registry 中最新评估）**：
- All-mode 5/5 PASS：C1 disagree 35.9%, C2 diagnostic 88.1%, C3 3 types, C4 +7.4pp, C5 79.2%
- Excl-Unknown 4/5（C4 FAIL -2.5pp）——根因是 repair.py prompt 硬编码 "Python script" 导致 FOL repair 方向错误，**已修复**

**关键修复已完成但未重跑**：
- repair.py: repr_type 动态 prompt（不再硬编码 "Python script"）
- repair_only.py: 跳过生成阶段仅重跑 repair+eval 的脚本已就绪

**没有等待中的 Worker / Cron 回调。** 上一个 session 可能在 pipeline 运行期间被 reset。

### 4. 📋 待办（条件触发式）
- SSH 检查 PID 57877 存活 → 若已完成：运行 `evaluate_mvp.py` 对 204 全量做最终 MVP gate 评估
- 204 全量 MVP gate 评估完成 → 运行 `repair_only.py` 用修复后的 repair.py 重跑 repair+eval
- repair-only 结果出来 → 汇报 Director 两组指标（All-mode + Excl-Unknown），重点看 C4 excl-unknown 是否翻 PASS
- MVP gate 最终 5/5 PASS（含 excl-unknown）→ 向 Director 提议进入 post-MVP kickoff（多数据集/多模型扩展）
- MVP gate 仍有 FAIL → 分析失败指标，决定是继续修 prompt 还是 pivot（ProofWriter 备案仅在 C1+C2 都 FAIL 时启动）

### 5. 🎯 战略上下文
**核心假设**：跨表征（FOL vs Code）分歧可诊断 LLM 推理错误。MVP 在 FOLIO 上验证 5 个 claim（C1-C5）。

**关键发现链**：
- D001: FOLIO + Qwen3-32B 双表征验证
- D005: v1 失败(2/5)是 Z3 prompt 质量问题，非假设失败
- D008: C4 下降根因是 repair.py prompt bug，非方法论缺陷
- D009: All-mode 5/5 PASS @126 样本

**易错点**：
- DISAGREE 样本中 FOL 压倒性正确（9:1），不要把这个方法框架为"双向诊断"——实际上是"Code 错 FOL 对"的单向模式。论文 framing 需要正面承认这个不对称性
- C4 趋势持续下滑（+22.6→+11.6→+7.4pp），repair.py bug 修复应能改善，但如果全量仍然边缘 PASS，post-MVP 需要更强的 repair 策略
- Excl-Unknown 模式下 C4 一直 FAIL（根因已修复但未验证），这是 repair-only 重跑的核心验证目标
- 不要混淆 report.md 中的旧数据（127/204, PID 47964）和 registry 中的新数据（177/204, PID 57877）——pipeline 被 resume 过，PID 变了


---
