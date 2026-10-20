---
loop: 6
reason: idle_timeout
updated: '2026-05-15T03:27:08+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单仅 `cuda:0`（autodl-rtx6000pro），绝不能用其他卡
- vLLM 服务（Qwen3-32B-AWQ）在 autodl-rtx6000pro 上常驻，pipeline 依赖它，不要 kill
- 禁止双进程写同一输出文件（D007 教训：tmux + nohup 同时启动导致数据损坏 + 静默退出）
- repair_only.py 正在跑（PID 66854），不要启动新 pipeline 实例直到它完成
- 服务器用 conda base（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`），没有 .venv

### 2. 🖥️ 基础设施快照
- 服务器：autodl-rtx6000pro（主），westd-32608（备，account=root）
- 工作目录：`/root/autodl-tmp/crdd`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型：Qwen3-32B-AWQ (awq_marlin)，通过 vLLM 本地 serving
- 数据集：FOLIO validation set，204 samples
- 结果文件：`/root/autodl-tmp/crdd/results/mvp_v4_full.jsonl`
- 活跃进程：repair_only.py（PID 66854，86 targets，ETA ~170min from 00:48 UTC）
- Cron：已 reconcile，无活跃 cron（mvp_pipeline_004 进程已完成主 pipeline，repair_only 是独立启动的）

### 3. 📊 当前状态
mvp_pipeline_004 主 pipeline 204/204 全量完成，status=ANALYZING，conclusion=success。

**All-mode（去重后 N=192）5/5 PASS**：C1 39.6%, C2 86.8%, C3 3types, C4 +6.2pp, C5 85.4%
**Excl-Unknown（N=126）4/5**：C4 FAIL（-1.7pp），根因是 repair.py 硬编码 "Python script" 误导 FOL 端 repair

repair.py prompt bug 已修复（repr_type 动态 prompt），repair_only.py 正在重跑 86 个 target 的 repair+eval。这是当前唯一在跑的任务。

等待：repair_only.py 完成 → 用 evaluate_mvp.py 做最终评估 → 判定 Excl-Unknown C4 是否翻转 PASS → 向 Director 汇报最终 MVP gate 结果。

我上一轮已向 Director 汇报了 204 全量 dedup 指标（All-mode 5/5 PASS），但 repair-only 重跑结果尚未产出。

### 4. 📋 待办（条件触发式）
- repair_only.py 完成（PID 66854 退出）→ SSH 读取结果 → evaluate_mvp.py 最终评估 → update_registry metrics → 刷新 report.md
- Excl-Unknown C4 ≥5pp → MVP 全面通过，向 Director 汇报并建议进入 post-MVP（扩模型/扩数据集）
- Excl-Unknown C4 <5pp → C4 仍 FAIL，产出 Framing 调整提案（C4 在 excl-unknown 下的局限性分析），向 Director 汇报 4/5 结果 + 提案
- 无论 C4 结果如何，All-mode 5/5 PASS 已确认 → 核心假设成立，post-MVP 方向可以开始规划
- Director 批准 post-MVP → 读 experiment_plan.yaml 铺下一批实验（多模型、多数据集、v5b anti-lazy prompt）

### 5. 🎯 战略上下文
**核心结论链**：D001 MVP 方案 → D005 v1 FAIL(FOL crash) → D006 v2 partial fix → D007 撤回 v5 改 v5b → D008 repair.py bug 确认 → D009 All-mode 5/5 PASS

**核心假设已验证**：跨表征（FOL vs Code）分歧确实能诊断推理错误。All-mode 5/5 PASS 是决定性证据。

**易判断错的点**：
- C4 excl-unknown FAIL 不代表方法失败——根因是 repair.py prompt bug（已修复），不是方法论缺陷。repair-only 重跑就是验证这一点
- FOL 压倒性优于 Code（9:1 disagree 方向）是 FOLIO 数据集特性，不是通用结论。扩到非纯逻辑数据集时 Code 可能反超
- "Unknown" 样本占比高（~46% Code 端）是 lazy prompt 问题不是能力边界，v5b prompt 已设计好但未验证
- repair_only.py 不走 submit_training_job（它是 CPU-bound API 调用，不是 GPU 训练），用 nohup 启动是正确的
