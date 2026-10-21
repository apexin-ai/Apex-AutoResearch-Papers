# reviewer / loop_7.md

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_7.md`
- **Structured JSON:** [`8e78d3b5b3ea78bdf5b2.json`](../../sessions/8e/8e78d3b5b3ea78bdf5b2.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_wall_time
updated: '2026-05-17T17:10:15+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 `westd-32608:cuda:0`（RTX PRO 6000 98GB）。任何进程跑在其他设备上立即 CRITICAL
- exp-011 (n=30, +10pp) 是噪声（SE≈9pp），禁止作为正面证据引用。exp-020 同任务 n=204 显示 -2.4pp
- n=60 条件只能说"suggestive/consistent with"，n≥200 才能说"confirms null"
- 论文标题和 claims 必须限定在"self-extracted constraints / SICA"范围内，不能泛化到"symbolic consensus"整体（DyLoS/Aristotle/FoVer/LogicAgent 在相同 benchmark 上有正面结果）

### 2. 🖥️ 基础设施快照
- 服务器：westd-32608(root)，工作目录 `/root/symb_invariant_consensus`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/`
- 模型路径：`/root/autodl-tmp/models/Qwen2.5-14B-Instruct`
- 数据：`data/folio_full.json`(204题), `data/gsm8k_200.json`(1601行), `data/D012_60.json`(60题)
- vLLM：exp-012 完成后已自动停止（`EXP012_DONE` in log）。当前 GPU 应已释放
- 无 wandb 配置。无活跃 tmux/cron

### 3. 📊 当前状态
**刚完成的审查（已提交 Director）：**
- Method section (method.tex)：3 WARNING（σ函数未定义、FOL名实不符、缺prompt示例）
- Fig 1 pipeline 图：1 WARNING（figsize=16×7 缩放后字号<7pt）
- exp-012 GSM8K：PASS（SICA=SC=96.67%, C0=13.3%, 约束提取率仅14.7%）

**Registry 状态：**
- exp-012-gsm8k-pilot：服务器上已完成（`GSM8K_PILOT_DONE`），但 registry 仍标 RUNNING——Agent 还没处理结果
- 所有其他实验 DONE（共38条）

**等待中：**
- Agent 处理 exp-012 完成并更新 registry
- ROADMAP 排队：exp-004 Qwen-7B scaling → Mistral StrategyQA（各~1.5h GPU）
- Paper Agent 可能继续写其他章节（Introduction/Experiments/Related Work）

### 4. 📋 待办
- exp-012 registry 更新为 DONE → 核实 metrics 是否包含 C0=13.3% 和 extraction_rate=14.7%
- exp-004 Qwen-7B 启动 → 检查 GPU 合规（必须 cuda:0）、检查模型路径是否存在
- 新论文章节 worker 完成 → 按 §5 协议审查（Claim可信度 + 叙事逻辑 + 审稿人攻击面）
- Paper Agent 提交 `paper_agent_request_review` → 必须用 §5.3 评分模板（5维度+Overall）
- Fig 1 修复版完成 → 验证字号≥7pt at print scale

### 5. 🎯 战略上下文
**核心结论链：** SICA ≈ SC everywhere（5 models, 3 domains, N>1300）。原因是 capability trap：instruction-scale 模型有 diversity（C0=38-62%）但约束无判别力；reasoning 模型（QwQ-32B）无 diversity（C0<5%）。Oracle exp-021 是杀手锏：gold FOL → +8.82pp (p<0.001)，证明聚合机制有效、瓶颈在提取。

**易错点：**
1. GSM8K 的失败模式与 FOLIO 不同——GSM8K 是"约束提取不出来"（85%空），FOLIO 是"提取出来但无判别力"。论文不能用同一个 framing 解释两个 domain
2. exp-021 用的是 Qwen-14B traces（sica_expanded_14b.json），不是设计文档说的 LLaMA-8B traces。已标 WARNING 但未 CRITICAL（实际选择对论文更好）
3. Temperature ablation C0 range 只到 43%（T=1.0），没到预期的 60%+。Agent notes 里写"高于 T=0.7 的 53% 预期但合理"有矛盾——T=0.7 的 C0 是 53% 但 T=1.0 只有 43%？需要核实 T=0.7 的 C0 是来自 D012(60题) 还是 sica_expanded_14b(804题) 不同数据集
4. paper_provenance.yaml 和 constraints.yaml 未创建（标⚠️），论文写作推进后需要 Agent 补建


---
