# reviewer / loop_3.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`97830b4b24889c1b397a.json`](../../sessions/97/97830b4b24889c1b397a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-14T06:20:54+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1（westd-39279 仅 2 卡）。之前 plan013 因 CUDA_VISIBLE_DEVICES 未正确 export 越界两卡，plan014 也泄漏过 cuda:1。每次审查必 `nvidia-smi` 核对 PID 在哪张卡。
- 训练日志 ISR 是 binary approximation (_fast_fn)，**禁止用于论文或跨实验对比**。唯一可信 ISR 来源是 eval_sta.py (full STA) 的 held-out eval 结果。D013/D015 已明确。
- plan013 (0.9·r_exec+0.1·random) vs plan017 (r_exec·(1+0.3·random)) 公式结构不同，论文不可简化为"additive vs convex"对照。D027 已约束。
- s44 PR=98% 是 tautological fake（n_comp=2.04），不可与 s42 PR=93% 直接对比为"更好"。

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279 (root)，2× NVIDIA RTX PRO 6000 Blackwell 96GB
- 工作目录（远程）：`/root/solver-trace-ablation`
- 工作目录（本地）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不用 venv）
- 模型：`/root/autodl-tmp/models/Qwen3-4B`
- 训练数据：`/root/solver-trace-ablation/data/train_500_seed42.jsonl`（500 条 FOLIO）
- eval 数据：`data/proofwriter_fol_100.jsonl`（100 条 held-out）
- 磁盘：/root/autodl-tmp 44% (109G/250G)
- 活跃进程（截至 handoff）：
  - PID 262266 cuda:0 — plan002-additive-b01-s42 (step ~370/500, β=0.1)
  - PID 263273 cuda:1 — plan016-extended-1000-s42 (step ~269/1000)
- SWI-Prolog 已安装：`/usr/lib/swi-prolog/bin/x86_64-linux/swipl`
- eval_sta.py 已支持 `--logic_type prolog`

### 3. 📊 当前状态
**刚做完**：
- plan017 审查报告已发（WARNING：ISR worse than random，PR 18% vs 48%）
- GPU 1 僵尸进程 PID 261641 已确认被 kill
- 证据链全面审查 PASS，paper_framing.md 与 registry 一致
- plan006 Prolog readiness 审查已发（eval_sta.py Prolog 支持已补齐，但无 Prolog 训练数据 ground truth）

**RUNNING**：
- plan002-additive-b01-s42 (cuda:0, step ~370/500)：β=0.1 additive ISR bonus。若 negative → Kill Criteria #4 触发，additive 路线彻底关闭
- plan016-extended-1000-s42 (cuda:1, step ~269/1000)：1000-step exec-only。step 269 已 PR=1.0/ISR=0.117 — 已饱和，观察是否进一步退化

**未启动**：
- plan006 Prolog GRPO — 基础设施就绪，等 GPU 空出

### 4. 📋 待办
- plan002-b01 完成回调 → 审查 eval_sta 结果。PR 低+ISR 低 → 确认 Kill Criteria #4；PR>30%+ISR>0.2 → 意外正面，需仔细验证
- plan016 完成回调 → 审查 1000-step 行为。重点看 step 500 之后 ISR 轨迹——是继续崩塌还是稳定。若出现 tautological collapse（n_comp→2）则与 s44 同模式
- plan006 启动 → L1 #4 GPU 合规检查 + 验证 swipl + prolog_reward 端到端可用
- ROADMAP 更新通知 → 核对数据是否与 registry 一致（前三次更新都有错）
- 章节写作审查请求 → 按 §5.1-5.2 执行，先查 red-section skill 合规

### 5. 🎯 战略上下文
**核心结论**：ISR-as-reward 全面失败（D020），论文已 pivot 为诊断/分析贡献（D023/D028）。3 条 claims：(1) ISR 检测 hacking (2) GRPO saturation mechanism (3) cross-logic generality (conditional)。

**决策链关键节点**：D007 因果消歧 → D010 additive bonus → D018 推翻 D017（plan013 ISR=0.5 是 tautological 假象）→ D020 全面 pivot → D025/D026 ISR worse than random → D027 第 5 种 hacking mode

**易错点**：
1. **ISR 假高陷阱**：s44/plan013 的 ISR≈0.5 不代表好——是 2-component P⊢P 的机械值。必须看 ISR + n_components 联合诊断。ISR=0.5+comp=2 = 坏；ISR=0.5+comp=8 = 可能好
2. **plan002-b01 训练日志 ISR 看着像在学**（step 200 时 ISR=0.177），但这是 binary _fast_fn 近似——不可信，必须等 eval_sta
3. **plan016 step 269 已 PR=1.0+ISR=0.117**：这与 s42 500-step 的 ISR=0.1324 几乎一致，说明 hacking 在 ~200 步已完成，剩余 700 步可能只是更深退化
4. **ROADMAP 历史不可靠**：前三次 ROADMAP 更新都被我发现数据错误（s44 PR 写反、s42 ISR 引用旧值、plan012 状态标错）。每次 roadmap_updated 通知都要逐行核对 registry


---
