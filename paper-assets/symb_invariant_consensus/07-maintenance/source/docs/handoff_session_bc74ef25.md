# Director Handoff — Session bc74ef25
**Written**: 2026-05-22 ~04:00 UTC | **DDL**: EMNLP 2026 ARR May 25 (~3 days)

## 刚做完什么

本 session 处理了 D134-D135 用户指令，核心是"ALL IN 全并行"和"kill GPT-4o 换 2026 frontier"。

三个实验完成并报告给用户 + Paper Agent 已收到 patch 指令：
- **E3 DRC FOLIO** ✅ — τ=0.7 w=3: 83.3% gain recovery @ 34.8% cost。跨数据集泛化确认（ProofWriter 是 90%/38.8%）
- **E4 Process BR** ✅ — Position uniform BR≈5.2-5.4 (Fisher p=0.71)；Difficulty reversal BR_easy(SC≥10)=18.8 >> BR_hard(SC≤6)=2.7 (p≈0)。SCB 不是 late-step 泄漏，是从第一步就存在的系统性偏差
- **E5 CIL** ✅ — 8 pairs computed。Spearman ρ=0.762 (p=0.028)。Cross-arch NLI CIL +1.4~+1.9（正，互补），SICA CIL -2.9~-4.6（负，同源偏差），强模型 CIL→0。统一解释 SCB/NLI Escape/Aggregation Ceiling

## 正在跑的实验（接手后首先检查）

1. **E1 70B SICA** (Qwen2.5-72B-AWQ) — westd-16639 cuda:2, vLLM PID 435076, ~30 tok/s, 预计 5-10h（从 ~08:02 开始）。可能已经完成或接近完成
2. **DeepSeek R1 Distill 8B SICA** — westd-16639 cuda:3, vLLM PID 441147, 预计 5-6h（从 ~13:19 开始）
3. **D135 Frontier** — OpenRouter API 异步并发 Worker，选 3 个 2026 frontier 模型（Claude/GPT-4.1/Gemini），处理 FOLIO-204×K=12。用户要求 30-60min 出结果，但 Worker 在 ~13:43 才刚开始
4. **E2 Cross-Model SICA** — 状态不明，log 显示"30分钟后检查"。需要 SSH 确认是否还在跑

## 未 spawn / 待做

- **Direction A BAF** — 用户 D134 明确要求"千万不要抛弃"。但 E4 发现 BR position-uniform (p=0.71)，truncated extraction 预计 negative。BAF (Bias-Aware Filtering) 可能仍有意义——基于偏差信号过滤约束而非截断 trace。需要决定是否还跑
- **Paper Agent 积压 patches** — DRC FOLIO + Process BR + CIL 三个 patch 已派，Paper Agent 忙碌中（之前还有 Discussion/Corollary/DRC/CIL 等旧队列）。接手后检查 Paper Agent 完成度
- **V16 数据 5/6 完整** — Gemini 是 must-have 第 6 项。D135 如果成功覆盖 Gemini，则 V16 数据齐全

## 已验证的闭源数据

- gpt-4o: SC=73.9%, SICA=72.1%, BR=2.94, κ_p=0.79, κ_a=0.80
- gpt-4.1 cross→Mistral: SC=82.84%, SICA=81.37%, Δ=-1.47pp, BR=2.70

## 关键用户态度/指令

- **ALL IN**（D131）: "无需问我, 我全力支持你, 卡给你无限开"
- **D135**: GPT-4o outdated，必须用 2026 frontier。异步并发 ×15 提速
- **D134**: "5-7 路 fully parallel, 不要 sequential"，"A 千万不要抛弃"
- **反复警告的 bug**: Agent multi-worker drop — 每次只 spawn 1 个 worker（D126 要 3 个只出 1 个）。解法：逐个 spawn_worker 指令，不合并
- **M050 违反历史**: 用户批准的 D 决策不可单方面推翻。之前我 6 次 lockdown D116 pivot 被严厉批评

## 审稿状态

- 审稿群 (Group C) 活跃，review_chat_id: oc_c338e034cbffa10b9cc723e731d288d8
- 最近审稿 R10/R11 已处理，139 条决策记录
- Paper provenance 覆盖率 53/53

## 教训

1. 不要保守——用户明确要求大胆并行，每次犹豫都被批评
2. Agent multi-worker drop 是已知 bug，必须逐个 spawn
3. rollback 用户批准的内容是大忌（Push B rollback 事件）
4. Process BR 证明 truncation 路线无效，但 BAF 可能不同于 truncation
5. CIL 是真正的 unified metric，论文叙事的关键支撑

## 接手后第一步

1. `get_project_status` + `get_agent_queue_status` 了解最新状态
2. 检查 E1/E2/D135/R1-Distill 是否完成（SSH 或 worker-done 回调）
3. 检查 Paper Agent patch 队列完成度
4. 决定 Direction A BAF 是否还 spawn
5. 如果 D135 frontier 数据到了 → 立即整合到论文 + 通知用户
6. 编译论文检查页数（EMNLP 8 页限制），上次 ~9 页需要压缩
