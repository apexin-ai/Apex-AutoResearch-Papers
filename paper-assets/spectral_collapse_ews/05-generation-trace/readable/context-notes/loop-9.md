# agent / loop_9.md

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_9.md`
- **Structured JSON:** [`555d9e86fed326ead357.json`](../../sessions/55/555d9e86fed326ead357.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: idle_timeout
updated: '2026-05-25T09:29:45+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：rtx6000-diagprobe 的 cuda:0 和 cuda:1，不可用其他设备
- exp_023 和 exp_022c 是 3-gen pilot（非 10-gen 完整实验），DDL 约束下的缩短版，分析时不要按 10-gen 标准判断
- 跨架构验证的 trajectory type 判定必须与 Pythia-410M 同条件结果做定性对比，不能孤立判断
- r_crit bound 维持 (0.25, 0.3]（D031 撤回了 D030 的下修），r=0.25 仍为 Type II

### 2. 🖥️ 基础设施快照
- 服务器：rtx6000-diagprobe，工作目录 /root/spectral_collapse_ews
- Python：/root/miniconda3/bin/python（conda base 环境，不用 venv）
- 模型：gpt2-medium (HuggingFace cached, HF_HUB_OFFLINE=1)
- 数据：OpenWebText cached，50000 samples per gen
- 训练脚本：/root/spectral_collapse_ews/run_gpt2m_phase1.py
- 日志目录：~/runs/spectral_collapse_ews/
- 磁盘：充裕（根分区 96% 可用，数据盘 76% 可用）
- 活跃进程：exp_022c (PID 868280, cuda:1, tmux session, RUNNING)
- exp_023 刚完成 (PID 881061, cuda:0, 已退出)

### 3. 📊 当前状态
- **刚做完**：收到 exp_023 CRON 完成回调，已派 Worker (worker_analysis_exp_023_20260524T172011) 去 SSH 分析结果（读日志、收集 SLV metrics、查 W&B、判定 trajectory type）。Worker 尚未返回。
- **exp_023** (ANALYZING)：GPT-2-medium r=0.25, 3-gen pilot，测试 Type II trajectory。等 Worker 分析报告。
- **exp_022c** (RUNNING)：GPT-2-medium r=0.3, 3-gen pilot，测试 Type III trajectory，cuda:1。等 cron 完成回调。
- **等待中**：
  - Worker worker_analysis_exp_023_20260524T172011 回调 → 读分析报告 → update_registry → 汇报 Director
  - exp_022c cron 完成回调 → 派 Worker 分析 → 同上流程
  - 两个实验都完成后 → 跨架构数据集成论文

### 4. 📋 待办
- Worker analysis_exp_023 完成 → 读 artifacts/exp_023/analysis_report.md → 判定 conclusion → update_registry(status=DONE, conclusion=success/negative, metrics=..., checkpoint_path=..., log_path=...) → 刷新 report.md → 按 on-experiment-done 流程汇报 Director（带 [资源] 行）
- exp_022c cron 回调到达 → 派 Worker 分析（同 exp_023 流程）→ update_registry → 汇报 Director
- exp_023 + exp_022c 都 DONE 且 success → 跨架构相图完整（r=0 Type I ✅ / r=0.25 Type II / r=0.3 Type III / r=1.0 Control ✅）→ 派 Worker 集成数据写论文新 Table/Section
- 任一实验 negative → 按 on-experiment-done negative 流程，从 hypothesis 推导下一步，汇报 Director 等决策，不默默跑下一个
- 全部跨架构数据就绪 → final pass + 编译检查 + Round 2 提交（May 25 目标）

### 5. 🎯 战略上下文
- **核心结论**：递归合成训练导致三阶段谱坍缩（decompression→onset→acceleration），SLV 是廉价监测器，r_crit ∈ (0.25, 0.3] 划分 Type I/II/III trajectory
- **当前阶段**：Round 1 得分 3.0，目标 3.5+。审稿剩 3 条未解决：R1-N2(r=0.5 缺 seed, best-effort) + R1-W1(r_crit coarseness, rebuttal 处理) + R2-C2(跨架构验证，就是当前这批实验)
- **关键决策链**：D039 确认 exp_020 (r=0) 三阶段复现 → D038 设计 4 条件跨架构矩阵 → 当前 exp_022c + exp_023 是矩阵最后两格
- **易错点**：
  - 3-gen pilot 只需判定 trajectory type 的定性 pattern，不要用 3 代数据做定量 claim（如加速率）
  - Type II 的判定标准是 EMA SLV 在 Gen 1-2 出现 transient dip 然后 recovery，Pythia r=0.25 在 Gen 1-2 即出现此 pattern，3-gen 足够
  - exp_020 的 conclusion 标注为 success 但 report.md 里有一条 "auto-resolved as failed" 的异常标注——实际 exp_020 是 success（D039 确认），那个标注是 cron 系统的 false alarm
  - 论文 Round 2 提交的 DDL 紧迫（May 25），跨架构数据集成 + final pass 必须当天完成


---
