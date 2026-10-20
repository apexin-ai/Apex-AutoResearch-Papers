# director / loop_1.md

**schema conform ie training** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`3493b08d589ff6a6dc68.json`](../../sessions/34/3493b08d589ff6a6dc68.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-12T19:36:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 只有 seetacloud-westb-2xpro6000 上的 cuda:0 和 cuda:1（RTX PRO 6000 96GB × 2），不可使用其他服务器的卡
- 模型路径必须用 `/root/autodl-tmp/models/Qwen/Qwen3.5-9B`（HF 网络不通，ModelScope 下载路径编码为 `Qwen3___5-9B`，已做 symlink）
- TRL v0.18 reward_fn 的 completions 参数是 `list[list[dict]]`（chat format），不是 `list[str]`，代码已适配
- 训练数据用 SciERC（非 ACE2005），ACE2005 需 LDC license，留研究阶段
- WANDB_MODE=offline（服务器无 wandb key）

### 2. 🖥️ 基础设施快照
- 服务器：seetacloud-westb-2xpro6000，SSH host westb-23072
- 工作目录：`/root/schema-conform-ie-training`
- Python：conda base `/root/miniconda3/bin/python`（aml-train 镜像）
- 模型：`/root/autodl-tmp/models/Qwen/Qwen3.5-9B`
- 数据：SciERC DyGIE++ 格式，在代码内 hardcoded schema
- 输出目录：`/root/autodl-tmp/output/eval_A/`, `eval_B/`, `eval_C/`
- 日志：`/root/autodl-tmp/logs/`
- 活跃进程（截至 handoff 时）：
  - exp_001 Group A 训练：PID 25842, cuda:0, 374/500 steps (~2h 剩余)
  - exp_002 Group B 评估：PID 44652, cuda:1, scierc_test 95/551 (~5h 总)
  - exp_003 Group C 推理：PID 29235, cuda:0 共存, crossner_science 进行中 (~2h)

### 3. 📊 当前状态
MVP 三组实验全部在跑，等结果收集后做 pass/fail 判定。

- **exp_002 (Group B, conformance+GDPO)**：训练 500/500 已完成。评估刚启动在 GPU 1 上，跑 scierc_test + crossner_politics + crossner_science。
- **exp_001 (Group A, F1-only baseline)**：训练 374/500，~2h 后完成。完成后需立即在 cuda:0 启动同样的三数据集评估。
- **exp_003 (Group C, base zero-shot)**：scierc_test 结果已出——**全零**（valid_json_rate=0, 所有 conformance=0）。base model 完全无法输出有效 JSON。crossner_politics 应已完成待读取，crossner_science 进行中。

已给 Agent 下达指令：A 训练完 → 立即启 A 评估；任何组出结果即汇报。

### 4. 📋 待办
- Agent 汇报 C 组 crossner_politics 结果 → 确认（预期也是全零）
- A 训练完成 → 确认 Agent 已在 cuda:0 启动 A 评估（scierc_test + crossner_politics + crossner_science）
- B 评估完成 → 读取 entity_f1, relation_f1, conformance 指标
- A 评估完成 → 读取同样指标
- **三组结果齐全 → MVP pass/fail 判定**：
  - CrossNER zero-shot: B ≥ A + 2 F1 → pass
  - In-domain (scierc): B 降幅 ≤ 3pp vs A → pass
  - Sanity: A, B ≥ C → 已确认必然满足（C 全零）
  - 灰区 1≤Δ<2: 允许 1 天调参
- MVP pass → `complete_mvp()` → 进入 research 阶段（写 paper_framing.md → experiment_plan.yaml → dream_simulate）

### 5. 🎯 战略上下文
- **核心假设**：分解式 schema-conformance rewards（type/relational/completeness/validity）+ GDPO normalization 能提升零样本 IE 迁移，相比 gold-label-only GRPO
- **C 组全零是重要发现**：base model 完全无法做结构化 IE 输出，GRPO 训练的价值在于教会模型输出结构化 JSON，conformance rewards 的增量价值体现在 B vs A 的 delta 上
- **MVP 的真正判定点是 B vs A 在 CrossNER 上的 F1 差**，C 组已退化为 trivial baseline
- 决策链：D001(MVP方案) → D002(加 base model baseline + RE 指标) → D003(SciERC 替代 ACE2005) → D004(LoRA 微调)
- **易错点**：
  - 不要因为 C 全零就认为 MVP 必然 pass——关键是 B vs A 的 delta 必须 ≥ 2 F1
  - grad_accumulation_steps=8 是否生效未确认（原计划 step 50 检查），如果没生效，实际 batch size 只有 2 而非 16，可能影响训练质量
  - DDL 是 EMNLP 2026 ARR May 25，剩 13 天，MVP 必须尽快收敛
  - ROADMAP.md 的"当前进展"section 过时（仍写"Agent 正在写代码"），结果出来后需更新


---
