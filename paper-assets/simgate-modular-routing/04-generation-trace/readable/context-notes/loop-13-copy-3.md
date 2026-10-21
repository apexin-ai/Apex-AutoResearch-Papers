# reviewer / loop_13.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_13.md`
- **Structured JSON:** [`006ce96fe3544681b14f.json`](../../sessions/00/006ce96fe3544681b14f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: max_wall_time
updated: '2026-05-16T18:45:30+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**仅 cuda:0, cuda:1**（westb-13313）。任何脚本 `--gpu_id` / `device_map` 只能是 0 或 1
- 1.7B reference (47.1%) 使用旧训练配置，**不能与 plan-008-v4 训练的 0.6B/4B 做"同配置 monotonic"三点对比**——混淆变量未消除
- **DAF 定义不一致未修正**：论文报 90.4%（全 episodes 公式）vs framework_draft.md 形式定义算出 63.5%（仅 det-preferred）。Direction A 形式化前必须统一公式，否则审稿人会复现出矛盾
- guided-router LOTO "learned" variant 传入了 task_type 字符串 = 泄漏 task identity，不是真正 blind。不能报 "LOTO=62.92%"——只有 blind prior_majority=50% 是真 LOTO

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313 (root)，工作目录 `/root/autodl-tmp/simgate-modular-routing`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/`
- 模型路径：`/root/autodl-tmp/models/Qwen/Qwen3-{0.6B,1.7B,4B}`，Llama `/root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct`
- Checkpoints：`/root/autodl-tmp/simgate-modular-routing/checkpoints/plan-008-v4-{0_6b,4b}-seed{42-45}/final_adapter`
- 论文：`/root/autodl-tmp/simgate-modular-routing/paper/main.tex`（编译干净，PDF 406KB @ 22:29）
- guided_router 代码+结果：`/root/autodl-tmp/simgate-modular-routing/guided_router/`
- 活跃进程：**无**（全部实验 DONE，GPU 空闲）
- W&B：未配置

### 3. 📊 当前状态
90 个实验全 DONE（含新增 loto/cross-model guided router）。进入 Direction A 框架形式化 + 论文修改阶段。

**本轮完成的审查**：
1. guided-router-framework: CRITICAL（数据泄漏 + oracle=learned identical + find-non-living-thing 逻辑错误）
2. paper compilation: 从全面 broken → 干净编译（0 undefined warnings）
3. LOTO eval: blind=50%=always-det，learned=62.92% 但 task identity 泄漏
4. cross-model guided router: degenerate（Llama 0 int-preferred → trivially 100%）
5. SCI computation: Gini=0.21，death signal 均匀分布（加强 C1）
6. DAF bootstrap: **CRITICAL 不一致** 63.5% vs 论文 90.4%（公式定义域不同）
7. 战略评估：推荐 Direction A（框架形式化 targeting Main，Findings 作 fallback）

**等待 Director 决策**：
- Direction A 是否正式启动
- DAF 公式统一方案（推荐改 framework 定义匹配论文的 all-episodes 公式）
- Llama 数据是否升级到正文（已推荐）

### 4. 📋 待办
- Director 确认 Direction A → 审查 framework_draft.md → LaTeX method section 写作质量审查
- Paper Agent 提交 method section 草稿 → 按 5.1 维度审（特别关注 DAF 定义是否与 90.4% 一致、SCI 是否有实验支撑）
- 如 Paper Agent 更新 abstract/experiments 引用 LOTO 数据 → 验证 claim 措辞不误导（不能把 learned 62.92% 当泛化性能）
- registry 中 loto-guided-router-eval / cross-model-guided-router-eval 仍为 PREPARING → 确认 Agent 更新为 DONE + 正确 metrics
- 如有新 paper section 提交审查 → 检查 Llama N=70 是否从 Limitations hedge 升级到正文 result

### 5. 🎯 战略上下文
- **论文核心 story**：C1 death avoidance dominates (DAF 90.4%, r=0.97) + C2 router negative (cross-split 47.1%, data scaling 无效, capacity 4B=59% but disproportionate) + C3 cross-model/cross-env
- **Direction A 的关键**：把 episode-level counterfactual labeling + DAF 分解包装为通用诊断框架（"pre-training diagnostic"），定位 vs ITP-R/learned routing。不需新实验，纯 reframe + formalization。
- **DDL**：EMNLP ARR May 25（~8 天）
- **最容易判断错的事**：
  1. DAF 63.5% vs 90.4% 不是 bug——是两个合法但不同的定义。论文用 all-episodes（更直觉），framework 用 det-preferred-only（更 rigorous）。必须选一个统一。推荐 all-episodes 因为数字更大且更好解释。
  2. LOTO=50% 不是 negative result——是 positive evidence："DAF correctly predicts router failure, always-det is provably optimal without foreknowledge"
  3. Cross-model guided router 100% 是 degenerate（0 opposing class），不是 transfer 成功
  4. 论文 abstract/conclusion 已更新（Llama 70eps, capacity 4B, penalty-independent 78.9%），但这些更新在 21:38 AFTER 最后编译 22:29——PDF 应已包含


---
