# reviewer / loop_7.md

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_7.md`
- **Structured JSON:** [`f50693a985d8cffed62d.json`](../../sessions/f5/f50693a985d8cffed62d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: idle_timeout
updated: '2026-05-15T16:46:42+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 `bjb2-23165`，项目路径 `/root/autodl-tmp/agent_progress_probe`
- GPU 白名单未在 `execution.gpu_ids` 中明确配置——审查训练实验时需要核实实际使用的设备号
- `pareto_curve.py` 当前输出的图表基于 **mock 合成数据**（`generate_mock_data()`），绝不可用于论文。必须等 `early_termination_sim.py` 在服务器跑出真实 JSON 后才能生成可用图
- E5 bootstrap 结果（11-feat 0.977 vs 30-feat 0.967）来自 `run_e5_e8_server.py`，两模型均使用 lr=0.05。`bootstrap_ci_crossagent.py` 中 11-feat 曾用 lr=0.01（来自 19-feat residual 的 grid search，是错误套用），但该版本未产出最终数字，不影响结论

### 2. 🖥️ 基础设施快照
- 服务器：`bjb2-23165`（AutoDL），工作目录 `/root/autodl-tmp/agent_progress_probe`
- Python 环境：需 SSH 探查确认（conda base 或 venv），上一轮未做完整环境快照
- 数据路径：SWE 本地 `data/`，OH 在 `/root/autodl-tmp/openhands_data`
- 无 W&B 配置（此项目不检查 W&B）
- 无活跃进程（截至 14:40 UTC 无 RUNNING 实验、无活跃 worker）

### 3. 📊 当前状态
我已完成 e1–e10 全系列实验审查 + D072 代码审查，均已 post 给 Director。最后一条 post 是 D072 + 流水线停滞 warning。

**Registry 状态**：
- PREPARING（3个，均 30+ 分钟未启动）：`e2-gb-matched-scope`、`e3-conf-stratified-gold`、`e4-gb-swe-gold`
- RUNNING：无
- DONE：e1-2lf-crossagent、gold-3annotator-eval、gold-set-eval-v1、feature-overlap-ablation、llm-judge-strengthened 等 69 个

**等待中**：
- Agent 可能卡住——三个 PREPARING 实验无推进，无新 worker 自 14:40
- `early_termination_sim.py` 和 `compute_waste_audit.py` 需在服务器执行（关键路径）
- Director 未回复 D072 停滞 warning

### 4. 📋 待办
- e2/e3/e4 状态变为 RUNNING/DONE → 立即审查结果，重点关注 e2（matched-scope 是否缩小 36.9pp gap）和 e4（SWE-only gold GB vs TWV Probe 是否复现 0.878 vs 0.854）
- `early_termination_sim.json` 出现 → 核实：(a) k=3 时 false_termination_rate 和 compute_saved_pct 是否合理，(b) oracle 是否严格优于 model，(c) random baseline 是否显著差于 model
- `compute_waste_audit.py` 服务器重跑含 OH 数据 → 核查 trajectory_id 匹配率（`build_traj_step_counts` 的 ID 格式可能与 windows 不匹配）
- Director 转发论文章节审查 → 按 §5 维度审查，特别关注 analysis.tex 中 circular evaluation defense 和 headline 16.8pp claim
- e3 registry 更新为 DONE → 验证 registry metrics 与 `e3_conf_stratified_gap.json` 一致

### 5. 🎯 战略上下文
- **核心论文 story**：结构特征（30-dim hand-crafted）cross-agent transfer 0.967 vs LLM-as-judge 最优 0.799 = 16.8pp gap。3 个 LF weak supervision，MV 聚合。TLM 全部 fail vs MV 是 negative result。
- **升级路径**：我在战略评估中建议 Scheme A+D（早停模拟 + 计算浪费量化）作为 main conference 升级关键。这依赖 D072 两个脚本的服务器执行结果。
- **最易判断错的事**：
  1. TWV Probe 在 gold 上 > GB（0.854 vs 0.878 on Set B）——**这是 OH 极端偏斜（97% progress）的伪影**，不是真优势。SWE-only 子集 GB 领先。
  2. E9 parametric p=0.007 vs permutation p=0.248（Struct GB vs GRU Probe）——N=3 太小，参数检验不可信，应以 permutation test 为准，即差异不显著。
  3. κ=0.39 看似低——但 95% CI [0.165, 0.589] 上界接近 0.6（moderate），且 conf≥2 子集 silver-gold gap 仅 2.5pp，gold 标签在 conf≥2 下可防御。
  4. RF 在多个维度比 GB 更 robust（2-LF 仅 -1.8pp vs GB -12pp on conf≥2 cross-agent；conf=1 F1 更高；seed stability 更好），但论文以 GB 为 headline model——如果审稿人问"为什么不用 RF"需要有准备。


---
