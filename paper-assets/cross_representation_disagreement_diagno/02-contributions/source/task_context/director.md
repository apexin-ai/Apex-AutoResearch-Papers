---
loop: 4
reason: max_messages
updated: '2026-05-15T03:26:48+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 `cuda:0`@autodl-rtx6000pro（项目白名单唯一 GPU）
- Registry conclusion 不要提前标 success——之前在 148/204 时错标过，被 Reviewer WARNING
- JSONL 多次 resume 会产生重复记录（已发生 211 vs 204），任何评估前必须按 sample_id 去重
- repair_only.py 必须在去重后的数据上运行，输入是 `mvp_v4_deduped_for_repair.json`，不是原始 JSON

### 2. 🖥️ 基础设施快照
- 服务器：autodl-rtx6000pro (connect.westd.seetacloud.com)，用户 root
- 第二台：westd-32608（root），用途不明确
- 工作目录：`/root/autodl-tmp/crdd`
- Python：服务器上的默认 python3（非 conda，非 venv）
- 模型：Qwen3-32B，通过 vLLM serving（PID 19633 或后续重启的进程，localhost:8000）
- 数据：FOLIO 验证集 204 样本，结果在 `results/mvp_v4_full.jsonl`（已去重为 204 行）
- 原始 211 行备份：`results/mvp_v4_full_original_211.jsonl`
- 活跃进程：repair_only.py（PID 66854，86 targets，启动于 ~01:00 UTC，ETA ~170min，应已完成）
- tmux session：`mvp_pipeline_004`

### 3. 📊 当前状态
Pipeline 204/204 完成。去重后评估 All-mode 5/5 PASS（C4 +6.2pp，margin 仅 1.2pp）。Excl-Unknown C4 FAIL（-1.7pp），原因是 repair.py prompt bug（已修复）。

repair_only.py（PID 66854）用修复后的 prompt 对 86 个 target 重跑 repair，**预计已完成**（ETA 早已过），但结果尚未回收。这是 MVP gate 的最终判定步骤。

Registry: mvp_pipeline_004 ANALYZING/success，progress 需更新。其余 5 个实验全 DONE。

**最重要的待办**：确认 repair_only.py 是否完成 → 用修复后数据跑 evaluate_mvp.py → 汇报最终 C1-C5 → MVP gate 判定。

### 4. 📋 待办
- repair_only.py 完成 → 对 `results/mvp_v4_repair_fixed.json` 运行 evaluate_mvp.py → 汇报两组 C1-C5（原始 vs repair-fixed），重点看 C4
- C4 All-mode >5pp + Excl-Unknown PASS → `complete_mvp()` 进入 research 阶段 → post-mvp-kickoff skill（paper_framing.md → experiment_plan.yaml → dream_simulate）
- C4 All-mode >5pp 但 Excl-Unknown 仍 FAIL → 与 Reviewer 讨论是否仍可 complete_mvp（Reviewer 之前的预案建议：不降标准，但可讨论）
- C4 All-mode ≤5pp → 需要进一步诊断，可能需改进 repair strategy
- MVP 通过后 → 更新 ROADMAP，开始写 paper_framing.md

### 5. 🎯 战略上下文
- 决策链：D001(FOLIO+Qwen3-32B) → D002(加 C4≥5pp/C5≥60%) → D005(v1 FAIL, Z3 crash) → D006(v2 改善) → D007(撤回 v5 closed-world) → D008(repair.py prompt bug 定位) → D009(126 样本 5/5 PASS)
- 核心发现：分歧不对称性 9:1（FOL 几乎总是对的，Code 几乎总是错的）；C4 趋势持续下滑但部分归因于已修复的 prompt bug
- executor.py 的 SystemExit 静默退出 bug 已修复（L76 新增 `except SystemExit`）
- **最容易判断错的事**：C4 +6.2pp 是 bug 污染数据上的值，repair_only.py 的结果才是真实 C4。不要在 repair 结果出来前做 MVP gate 判定
- **容易踩的坑**：(1) Agent 已被 reset 两次因为空闲超时——派任务后要确认 Agent 确实在执行；(2) cron 回调有时没触发，需要手动催问结果；(3) 用户（孙震）刚问过进展，repair 结果出来后需要 director_reply_to_user 汇报
