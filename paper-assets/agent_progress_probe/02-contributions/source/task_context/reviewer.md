---
loop: 8
reason: max_wall_time
updated: '2026-05-16T02:45:13+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 bjb2-23165 只有 cuda:0, cuda:1 两张卡，且当前状态为空闲——任何实验不得使用超出这两个设备
- 本项目无 wandb 配置，审查时不检查 wandb 指标
- 论文数据源双边核对：论文/文档在本地 workspace (`projects/agent_progress_probe/`)，训练代码/数据/checkpoint 在远程 `/root/autodl-tmp/agent_progress_probe/`——断言"未修改"前必须两边都读
- early_termination_sim 产出在远程 `artifacts/d072/`（不是 d073），路径不一致但数据正确

### 2. 🖥️ 基础设施快照
- 服务器：bjb2-23165，远程工作目录 `/root/autodl-tmp/agent_progress_probe`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/`
- 数据：SWE 轨迹 `data/swe_agent_trajectories_5000.jsonl`，OH 数据 `/root/autodl-tmp/openhands_data/`
- Gold set：`artifacts/gold_set/gold_2plus_agreed_B.csv` (N=505, Set B)
- 活跃进程：无（GPU 空闲）
- 无 wandb、无 cron、无 tmux session

### 3. 📊 当前状态
**已审查完成：**
1. **d073-conf1-decomposition** → PASS。GB 在 conf=1 上净纠正 MV 13 个错误 (15 vs 2)，N=172，数字自洽。
2. **d073-early-termination-sim** → WARNING。GB k=3 precision=1.0/recall=0.451/saved=16.3%。两个 warning：(a) GB 多 seed 是伪多 seed（sklearn GB 默认确定性）；(b) false_termination_rate 90%+ 需要上下文解释（stag-tail 基线率仅 4.7%）。

**Registry PREPARING 状态（尚未收到 worker_done）：**
- d073-figures
- d073-statistical-robustness
- d073-llm-on-oh
- d073-probe-e5-large
- d073-probe-bge-m3
- e3-conf-stratified-gold
- e4-gb-swe-gold
- e2-gb-matched-scope

### 4. 📋 待办
- d073-statistical-robustness worker 完成 → 重点核实 bootstrap CI 覆盖率和 p-value 计算方法
- d073-llm-on-oh worker 完成 → 核实 LLM 调用成本、parse failure rate、与论文 Table 已有数字一致性
- d073-probe-e5-large / d073-probe-bge-m3 完成 → 与 appendix Table encoder_ablation 数字交叉验证
- d073-figures 完成 → 用 paper-visual-review skill 检查图表质量
- e3-conf-stratified-gold 完成 → 核心审查：per-conf gold agreement 是否支撑论文"conf≥2 可信"的 claim
- 任何 worker 报 DONE 但 registry 未更新 → 提醒 Agent 补更状态

### 5. 🎯 战略上下文
- **项目核心论点**：结构化特征（30 维手工特征 + GB/RF）在零样本跨 agent 迁移上大幅优于 embedding probe（0.967 vs 0.598），但 probe 微调后反超（0.976）——deployment trade-off framing
- **circular evaluation caveat 是全文命脉**：in-domain 0.995 是 LF 重构而非真检测。三个非循环证据：(1) 跨 agent 0.967；(2) instance isolation <0.1pp；(3) gold set GB 0.839 vs MV 0.798
- **最容易判断错的事**：
  - GB 多 seed std=0 不是稳定性证据——sklearn GB 默认无随机性，已发 warning 给 Director
  - 论文 headline "16.8pp" 是跨 agent GB (0.967) vs LLM best (0.799)，注意比较的是不同 setting（cross-agent vs in-domain），论文已声明这一点但审稿人仍可能攻击
  - false_termination_rate 90%+ 是 base rate 问题不是模型问题——stag-tail 仅 4.7%
  - Gold set 的 Fleiss κ=0.39（fair agreement），说明 stagnation 边界本身就有主观性，这支撑了弱监督方法的动机但也限制了 gold evaluation 的 claim 强度
