# director / loop_6.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_6.md`
- **Structured JSON:** [`77a8c974cfaf2ce7e968.json`](../../sessions/77/77a8c974cfaf2ce7e968.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-15T08:47:38+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-19828 的 cuda:0 和 cuda:1（2× RTX PRO 6000 Blackwell 96GB）
- D026 multi-seed 实验**必须 bs=4**（与 seed=42 保持可比性），C4/GPT-2 generalization 用 bs=32
- Registry 中所有 Granger p-value 必须标注 `_p_raw` 或 `_p_fdr` 后缀——Agent 被纠正过三次仍会犯，每次 Worker 回来都要检查
- "regime switch"（ECE 替代 entropy 作为 canary）仅是假说（raw p-value 对比，FDR 后不显著），**禁止**写入 framing 或 decisions 作为 confirmed finding
- α-sweep 所有结论（非单调 dose-response、regime switch）目前 single seed (seed=42)，论文中必须标注此限制

### 2. 🖥️ 基础设施快照
- 服务器：westd-19828 (connect.westd.seetacloud.com)，root 用户
- 工作目录：/root/autodl-tmp/distrib_canary_collapse
- Python：aml-train 镜像，conda base（/root/miniconda3/bin/python）
- 模型：Pythia-410M（HF cache 在服务器上已有）
- 数据：WikiText-103 子集 5000 条（已部署）；C4 和 GPT-2-medium 正在由 Worker 下载/准备中
- 活跃进程：plan_006_s42 PID=68368 cuda:0（~gen15/20）；alpha_sweep_a075_s42 PID=89753 cuda:1（~gen3/10）
- W&B / Git：未配置（可选）

### 3. 📊 当前状态
**刚完成的重大决策**：
- D025: Claim 1 收窄至 α=1.0 only（α=0.50 strict 全归零）
- D026: GPU 优先级重排——multi-seed > finer α grid
- D027: 论文叙事切换 Option B（方法论陷阱 + 多方法共识框架为主线）

**RUNNING**：
- plan_006_s42 (α=1.0, 20gen, cuda:0) — ~gen15/20, ~2h 剩余, supplementary evidence
- alpha_sweep_a075_s42 (α=0.75, cuda:1) — ~gen3/10, ~2-3h 剩余, pivotal boundary

**QUEUED (D026 multi-seed)**：a025_s43 → a050_s43 → a025_s44 → a050_s44（cuda:1 串行，a075 完成后启动）

**等待中的 Worker**：
- consensus_framework_formalization — 零 GPU，共识规则 + sensitivity analysis + FPR/FNR 表
- generalization_c4_gpt2_prep — C4 数据 + GPT-2 weights 下载/脚本准备
- multiseed_batch_optimization — 已完成（结论：保持 bs=4）

**等待用户确认**：无（D027 reframe 已自行批准执行）

### 4. 📋 待办
- a075 cron 回调 → 更新 registry → 立即提交 a025_s43 到 cuda:1 → 派分析 Worker 跑 5-α-point cross-alpha（含双向 Granger + FDR）
- a075 Granger FDR-sig → Claim 1 scope 扩展为 "α ≥ 0.75"，更新 paper_framing.md 约束 #21
- a075 Granger null → Claim 1 确定为 "α=1.0 only"，paper_framing.md 约束 #22 practical utility 退回纯 boundary mapping
- plan_006 完成 → cuda:0 释放 → 立即启动 C4 cross-domain（α=0.25+1.0, bs=32）→ 然后 GPT-2 cross-arch
- consensus_framework Worker 完成 → 审查产出（classify_robust() + sensitivity heatmap + FPR/FNR 表）→ post_to_reviewer 验证
- multi-seed 首批完成（a025_s43）→ 对比 seed=42 的非单调性和 Claim 3 方法敏感性是否跨 seed 稳定
- Reviewer 评估 cuda:0 释放后可接管 multi-seed tail（a050_s44），双卡并行省 ~4h

### 5. 🎯 战略上下文
**决策链**：D013(MVP pass) → D017(perplexity 伪回归) → D020(Granger-causal 升级) → D022(Claim 2 reframe: detectability) → D024(dose-response 非单调) → D025(Claim 1 收窄 α=1.0) → D026(multi-seed 优先) → D027(Option B reframe: 方法论主线)

**论文水平**：Reviewer 评估 Weak Accept 4-5/10。WA→Accept 路径：multi-seed（error bars）+ C4/GPT-2（泛化）+ 共识框架 formalization（正面贡献）。预期总计 ~26h GPU + 零 GPU 分析即可到 6-7/10。

**最容易判断错的事**：
1. Agent 会反复用 raw p-value 做结论（已纠正 3 次），每次分析 Worker 回来都要检查是否标注 raw vs FDR
2. "regime switch" 假说（ECE 替代 entropy at high α）听起来诱人但 FDR 后不显著——不要被 Agent 的热情带偏，等 α=0.75 数据再判断
3. plan_006 在 D027 下已降为 supplementary（P0-），不需要追加 seed 或扩展，让它跑完即可
4. Worker 池容易归零——Agent 完成回调后不保持待命 Worker，需要定期检查并催促（已被 system 催促过 3 次）
5. 证据强度排序是 Claim 3 > Claim 2 > Claim 1，论文叙事必须让 Claim 3 领衔，不要退回 Claim 1 领衔的 Option A


---
