# director / loop_7.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_7.md`
- **Structured JSON:** [`305ed235367609ccbfd1.json`](../../sessions/30/305ed235367609ccbfd1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_messages
updated: '2026-05-15T17:43:48+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-19828 的 cuda:0 和 cuda:1（`execution.gpu_ids`），严禁使用其他卡
- α=0.75 consensus (11/16) 与 α=1.0 consensus (6/16) **禁止直接对比**——标准不同（D038 #27）
- token_entropy→perplexity @ α=0.75 **不可引用为 robust evidence**（D017 确认 spurious，D038 #28）
- FNR=0 声明必须附 D017 独立证据，不能只说"框架在自己定义的 ground truth 上 FNR=0"（D041 循环论证风险）
- FPR/FNR 维度不对称：FPR 是 method-only（α=0.0 单 seed），FNR 是 method×seed（α=1.0 四 seed），不可放同一 ROC 曲线（D041）
- 投稿目标已确定为 **EMNLP 2026 main track**（D043，用户明确指定），不是 AAAI 2027

### 2. 🖥️ 基础设施快照
- 服务器：westd-19828 (connect.westd.seetacloud.com)，root 用户
- 工作目录：`/root/autodl-tmp/distrib_canary_collapse`
- Python：aml-train 镜像，`/root/miniconda3/bin/python`（conda base）
- 模型：Pythia-410M + GPT-2-medium（均在服务器本地）
- 数据：WikiText-103（服务器本地）
- 活跃进程（截至 handoff 时刻）：
  - cuda:0: gen_wiki_gpt2m_a100_s42_v3 (PID 117632, GPT-2-medium cross-arch, ETA ~22:20 UTC)
  - cuda:1: alpha_sweep_a050_s43 (PID 134860, D026 multi-seed #2, ETA ~22:10 UTC)
- Cron 监控两个进程，完成后自动回调

### 3. 📊 当前状态
**刚做完**：D037-D043 决策链（Claim 1 scope 扩展、论文结构、diagnostic→prescriptive 升级、EMNLP 2026 确定）；D040 filtering pipeline + FPR/FNR 校准表；consensus_workflow.pdf（Fig 5，Reviewer PASS）；regime_map_fdr.pdf v2（Fig 1，Reviewer PASS）；Paper Agent 已激活 Full Draft 模式，writing_plan.yaml 已审批，Step 2 图表生成中。

**正在等待**：
- F-value 审计 Worker（D017 undiff vs diff F 范围核实，fig_differencing_dmax Panel (a) 标注可能有误）
- a025_s43 刚完成（diversity 跨 seed 复现 <1.3pp 偏差，PASS）
- a050_s43 运行中（cuda:1，D026 multi-seed #2）
- gpt2m_v3 运行中（cuda:0，cross-arch 验证）
- Paper Agent 正在处理 venue 变更（AAAI→EMNLP）+ Step 2 图表

**D026 multi-seed 队列**：✅a025_s43 → 🔄a050_s43 → a025_s44 → a050_s44

### 4. 📋 待办（条件触发式）
- F-value audit Worker 回调 → 确认 F=612-2615 归属（undiff or diff），修正 fig_differencing_dmax Panel (a) 标注
- a050_s43 完成 → 分析 α=0.50 seed=43 drift + 与 s42 对比 → cuda:1 提交 a025_s44
- gpt2m_v3 完成 → 分析 GPT-2-medium cross-arch 结果 → cuda:0 提交 gen_wiki_gpt2m_a025_s42 → 这是 WA→Accept 的关键跳板
- Paper Agent 提交 writing_plan 更新（EMNLP 模板）→ 审批
- Paper Agent Step 2 图表完成 → 审查 Fig 2 (differencing_dmax) 和 Fig 4 (metric_trajectory)
- D026 全部 4 个 multi-seed 完成 → 补充低 α funnel 数据展示共识框架在模糊地带的过滤力 → 移除 C001 single-seed caveat
- multi-seed 确认 Phase 3 → Claim 3 Results 末尾加 observation window sensitivity 段落（~150 词）

### 5. 🎯 战略上下文
- **核心 narrative (D027 Option B)**：方法论陷阱 + 带量化校准的共识框架。Claim 3 领衔 → Claim 1 case study → Claim 2 regime map
- **D042 升级**：从 diagnostic 升级为 diagnostic + prescriptive。"empirically calibrated"（非"optimal"），限定"on reference extremes"
- **WA→Accept 路径**：(1) D026 multi-seed（运行中）= 首要条件；(2) GPT-2-medium cross-arch（运行中）= 泛化性
- **Strong Accept 路径**：workflow pipeline figure + FPR/FNR 校准表已完成（零 GPU），论文 actionable methodology 成色已质变
- **最容易判断错的事**：(1) Worker 池反复归零已被系统催促 6 次，Agent 架构限制无法持久驻留，靠 cron 回调接力；(2) fig_differencing_dmax 的 F 值列归属尚未确认，在审计结果回来前不要让 Paper Agent 引用该图的 F 值数字；(3) 用户对投稿目标敏感——EMNLP 2026 是用户明确指定的，不要自作主张改回 AAAI


---
