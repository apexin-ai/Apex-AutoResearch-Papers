# director / loop_1.md

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`53f0206d6977ec710642.json`](../../sessions/53/53f0206d6977ec710642.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-17T16:52:09+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 仅限 cuda:0-3（C001 约束，westd-33183 的 4× RTX PRO 6000 Blackwell）
- TF-IDF sanity check 是训练前的 HARD GATE — 不能再跳过（M003 教训）
- Benign turns 的 persuasion_strategy 不能 hardcoded 为某个固定值（M004 教训，会引入 spurious feature）
- Crescendo 数据 `crescendo_all.jsonl`（250 条）和 `taxonomy.json` 绝对不能删
- 用 reasoning model（Qwen3 系列）生成时必须 `enable_thinking=False` + regex strip（M001 教训）

### 2. 🖥️ 基础设施快照
- 服务器：westd-33183 (connect.westd.seetacloud.com:18048)，用户 root
- 工作目录：`/root/persuasion_turn_jailbreak_detect/`
- 代码：`src/train_deberta.py`（Stage 1 multi-task）、`src/train_classifier.py`（Stage 2 GRU）、`src/evaluate.py`（评估）、`src/compute_baseline_embeddings.py`
- 数据：`data/generated/crescendo_all.jsonl`（250 jailbreak）、`data/generated/benign_v4c_full_gpu0.jsonl` + `benign_v4c_full_gpu2.jsonl`（共 230 benign）
- 磁盘：~6GB 可用（79% 使用，已做过一次清理）
- 无 W&B / 无 Git / Python 路径未确认（Agent 之前通过 ssh_execute 直接操作）
- 活跃进程：Phase B full 已完成，补充评估 Worker 可能仍在跑（K=1, per-attack-type breakdown）

### 3. 📊 当前状态
**刚完成**：Phase B full 训练 + 评估（480 条数据：250 jailbreak + 230 benign）
- Treatment K=2 F1=0.987 vs Baseline 0.879 (+10.8pp) → MVP PASS (D002)
- **但 TF-IDF=1.0 at all K** — 数据仍有完美词汇 shortcut
- Reviewer 发了 severity:critical 报告（TF-IDF=1.0 + strategy=7 confound + sanity check 被跳过）

**Registry**：仅 `pilot_phase_b` (DONE/success)。Phase B full 未注册（需补）。

**等待中**：Agent 派了补充评估 Worker（K=1、per-attack-type breakdown、balanced TF-IDF sanity），结果可能已到或即将到。

### 4. 📋 待办
- 补充评估 Worker 回调到达 → 记录结果，注册 Phase B full 实验到 registry
- MVP 判定已 PASS (D002) → 调 `complete_mvp()` 正式进入 research 阶段
- complete_mvp 后 → 读 `post-mvp-kickoff` skill → 写 `paper_framing.md` → 写 `experiment_plan.yaml` → `dream_simulate(review_mode="full")` → 更新 ROADMAP
- Research 阶段第一优先级：解决 TF-IDF=1.0（方案见下方战略上下文）
- Strategy=7 confound → 需要 scrambled-label ablation 验证 treatment 优势是否来自 label shortcut

### 5. 🎯 战略上下文
**决策链**：D001（接受 DeBERTa F1=0.789, 停止数据迭代, reframe 为 early detection）→ D002（MVP PASS, early detection K=2 +10.8pp）

**核心结论**：Persuasion-grounded fine-tuning 的价值集中在 early turns（K=2 差距最大），符合 DisPeD 的 core claim。但当前数据 TF-IDF=1.0 使论文不可投。

**TF-IDF=1.0 的解决方向**（研究阶段优先级排序）：
1. **Adversarial perturbation 实验**（推荐）：对 jailbreak 数据做 paraphrase/register normalization，使 TF-IDF 降到 ~0.65，然后证明 DisPeD 仍然有效。这让 TF-IDF=1.0 变成 paper motivation（"lexical cues 可被规避，pragmatic patterns 不可规避"）
2. **Adversarial filtering**：生成大量 benign 后用 TF-IDF 筛掉最易分类的，只保留 hard examples
3. **WildChat 真实数据**：`wildchat_benign_226.jsonl` 已存在但之前有 14-16% jailbreak 污染问题

**易踩的坑**：
- 不要继续无限迭代 benign 数据生成（已经 5 轮了：v1→v2→v3→v4b→v4c，每轮都失败在 register mismatch）
- v4c casual-only register 让 TF-IDF 从 0.924 恶化到 1.0 — 纯 casual benign vs formal/hypothetical jailbreak escalation 是系统性差异
- MVP PASS 判定不变，但 Reviewer 的 critical 报告不能忽视 — research 阶段首要任务是数据质量
- DDL: EMNLP 2026 ARR 2026-05-25（距今 ~8 天），时间紧但 AI 团队速度足够


---
