# reviewer / loop_4.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`0620ad227dc8f63da60c.json`](../../sessions/06/0620ad227dc8f63da60c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-14T11:00:19+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1（westd-39279 双卡）。历史上多次 GPU 越界事故（C002/C005）。
- 训练数据统一用 `data/train_500_seed42.jsonl`，禁止用 `proofwriter_fol_500.jsonl`（C001，s43 数据 confound 事故）。
- 跨 run ISR 对比必须用 eval_sta.py full STA 评估，禁止引用训练日志 ISR（C004，不同 run 用了不同 ISR 计算版本）。
- `save_total_limit=1`（C003，磁盘爆满事故）。plan009 train_sft.py 写了 3，已报 warning 但可能还没改。
- ISR β=0.1 三 seed 不可报 raw 3-seed mean ISR（被 H7 膨胀值污染），需按 hacking mode 分层报告。

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279 (root)，工作目录 `/root/solver-trace-ablation`
- Python：`/root/miniconda3/bin/python`（conda base 环境，非 venv）
- 模型：`/root/autodl-tmp/models/Qwen3-4B`
- 训练输出：`/root/autodl-tmp/outputs/plan*`
- 日志：`/root/runs/solver-trace-ablation/*.log`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/`
- Artifacts：`artifacts/` 目录下 table2_hacking_taxonomy.{csv,tex}、hacking_taxonomy.md 等
- W&B：未配置（no_wandb=true）
- 活跃进程（截至 handoff）：plan006-prolog-exec-s42 (PID 506020, tmux=plan006-prolog-exec-s42, cuda:0, step ~321/500)
- GPU 1 空闲（已多次报 Director，未获调度响应）

### 3. 📊 当前状态
**刚做完**：
- 审查 plan009-sft-prep worker（train_sft.py 创建，报了 C003 save_total_limit 违规）
- 审查 plan009-sft-fix worker（尚未读到修复内容，被 handoff 打断）
- 发了 5 份报告给 Director：(1) plan006 训练动态+GPU1 空闲 (2) evidence_audit.md 严重滞后 (3) paper_framing/ROADMAP 小修正 (4) experiment_plan.yaml 链接断裂导致覆盖率虚低 (5) plan009-sft-prep 审查

**RUNNING**：plan006-prolog-exec-s42 (cuda:0, step ~321/500, ETA ~25min from handoff time)
**QUEUED**：plan018-random-b01-s43, plan018-random-b01-s44
**PREPARING**：plan006-prolog-sta-s43/s44, plan006-prolog-exec-s43/s44

**等待中**：
- plan006-prolog-exec-s42 完成 cron 回调
- Director 对 GPU 1 调度的决策（plan018 s43/s44 vs plan006 后续 seeds vs plan009-sft）

### 4. 📋 待办（条件触发式）
- plan006-prolog-exec-s42 完成 → 审查完整训练轨迹，重点对比 exec-only vs exec+STA 饱和速度（exec+STA step~100 饱和 vs exec-only step~240+ 才出现信号）。检查 registry 是否更新（当前 notes 仍是旧的 FileNotFoundError）。
- plan006-prolog-exec-s42 eval 完成 → 核对 eval PR/ISR，与 FOL exec-only 对比，判断 Claim 3 cross-logic 证据强度。
- plan018-random-s43/s44 启动 → 验证 config 与 s42 一致（已审查过 config，OK）。
- plan009-sft 启动 → 确认 save_total_limit 已修为 1，确认 CUDA_VISIBLE_DEVICES 正确设置。
- 任何实验在 GPU 1 启动 → nvidia-smi 验证 GPU 隔离合规。
- Director 要求章节审查 → 走模式 B 流程（§5），先做合规检查（Agent 写作前是否看过 red-section skill）。

### 5. 🎯 战略上下文
**核心结论链**：
- D035：Framing 选 Goodhart 主线（非 STA-as-reward 成功故事）
- D041→D043：Claim 2 从 "β=0.1 sweet spot" pivot 到 "meta-level Goodhart"——ISR 作为 reward 在 2/3 seeds 诱导 ISR-specific gaming (H7 conclusion duplication)
- D044：Hacking taxonomy 统一用 strict 定义（classify_h7.py exact normalized match）

**最容易判断错的事**：
1. **ISR β=0.1 不是成功故事**。s42 单 seed 看起来好（PR=0.81, ISR=0.415, genuine~31%），但 s43/s44 几乎 100% H7 hacking。论文叙事是 "meta-level Goodhart"（诊断指标变优化目标后被 game），不是 "low-dose ISR works"。
2. **plan012 registry metrics 已过时**。plan012 的 genuine_rate 25.9%/17.7% 是旧分类（5-mode，无 H7）。Table 2 用的是 D044 strict 分类（genuine 30.9%/25.3%）。不要混用。
3. **evidence_audit.md 严重滞后**——Claim 3 写 "无证据" 但 plan006 已有数据；plan016 写 "待完成" 但已 DONE；H7 完全缺失。不要引用此文件的覆盖度判断。
4. **coverage matrix 报 16.7% 是假的**——experiment_plan registry_id 链接断裂 + negative conclusion 被计为 failed。实际 Claim 1/2 覆盖度 ~80-100%。
5. **Prolog exec-only (plan006) 饱和模式与 FOL 不同**：step 240+ 出现早期饱和信号但未完全锁定（到 step 321 仍有 non-perfect steps），而 exec+STA 在 step ~100 完全锁定。这个 2.4x 差异对论文有价值。


---
