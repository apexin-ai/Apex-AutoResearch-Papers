# director / loop_3.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`64f047acb5b5052e1b56.json`](../../sessions/64/64f047acb5b5052e1b56.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-15T11:28:02+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：rtx5090-4x 的 cuda:0/1/2/3，不可越界
- SFT warmup 模型路径：`/root/autodl-tmp/sft_output`（已 merge，是所有下游实验的基座）
- RSFT 训练数据：`/root/autodl-tmp/rsft_filtered/rsft_train.jsonl`（2718 samples）和清洗版 `rsft_train_clean.jsonl`（2548 samples，去掉 170 截断 JSON）
- **TaskEvalCallback 的 rel_f1 数字不可信**（D038）：训练中间 eval 报的 ~0.05 是 50-doc vs 全量 gold 分母不匹配 bug。已修复但旧实验的中间 eval 数字全部作废，必须用独立的 `freige.eval.inference` 做全量 985-doc eval
- D037 已撤回——RSFT "灾难性失败" 是 eval bug，不是模型问题

### 2. 🖥️ 基础设施快照
- 服务器：rtx5090-4x (connect.bjb2.seetacloud.com)，account=root
- 工作目录：`/root/autodl-tmp/freige`
- 4× RTX 5090 32GB，bf16 only（不 quantize）
- 模型路径：SFT base `/root/autodl-tmp/sft_output`，RSFT 输出 `/root/autodl-tmp/rsft_output`(r1) / `rsft_output_s43` / `rsft_output_s44` / `rsft_output_r2a` / `rsft_output_r2b`
- 数据集：`/root/autodl-tmp/data/docred`
- W&B：project 内配置，run names rsft-ced-r1 / rsft-ced-r1-s43 / rsft-ced-r1-s44 / rsft-r2a / rsft-r2b
- 活跃进程（写 handoff 时）：
  - cuda:0: CED reranker PoC (PID 178050, ~37%)
  - cuda:1: r2a full eval (PID 189488)
  - cuda:2: s43 full eval (PID 194296, 刚启动)
  - cuda:3: r2b full eval (PID 189855)

### 3. 📊 当前状态
**MVP-2 已有 2/3 seed 通过**：
- r1 (seed=42): rel_f1=0.4449(+3.9pp), evi_f1=0.8187(+2.1pp), edcr=0.6565(-5.5pp) ✅
- s44 (seed=44): rel_f1=0.4655(+6.0pp), evi_f1=0.8087(+1.1pp), edcr=0.6350(-7.7pp) ✅
- SFT baseline: rel_f1=0.4057, evi_f1=0.7979, edcr=0.7118

**等待中**：
- s43 full eval (cuda:2) → 3 seed 齐全后 complete_mvp
- r2a eval (cuda:1) → ablation：1 epoch + clean data, original LoRA scaling
- r2b eval (cuda:3) → ablation：1 epoch + clean data + conservative LoRA (alpha=32, lr=1e-5)
- CED reranker PoC (cuda:0, ~37%) → 额外方案，dry run 显示 CED-F1 可能负相关（warning）

### 4. 📋 待办
- s43 eval 完成 → 汇总 3 seed 均值±std，确认全部 PASS → `complete_mvp("faith-evidence-ie")` → 进入 research 阶段
- complete_mvp 后立即执行 post-mvp-kickoff skill：写 paper_framing.md 定稿 → experiment_plan.yaml → dream_simulate(review_mode="full") → update_roadmap
- r2a/r2b eval 完成 → 对比 r1/s44 量化 epoch 数和 LoRA scaling 的效果（ablation 数据点）
- CED reranker PoC 完成 → 如果 CED > Random 且 evi_f1 提升，作为论文额外贡献；如果 CED-F1 负相关确认，记录为 negative result 但不影响 RSFT 主线
- ROADMAP 严重过时（7h+未更新）→ complete_mvp 后全量覆写

### 5. 🎯 战略上下文
- **核心结论**：CED rejection sampling 有效——SFT 模型生成 8 candidates → CED 打分 → top-1 筛选 → 再微调，三个维度全面改善。这是 CED 的首次端到端验证。
- **决策链**：MVP-1 PASS(CED 信号有效) → GRPO 全线 FAIL(D027/D031/D033, catastrophic forgetting) → RSFT "FAIL"(D037, 实为 eval bug) → D038 撤回 D037 → RSFT 实际 PASS
- **最容易判断错的事**：
  1. 不要相信任何 TaskEvalCallback 报的 rel_f1 ~0.05 数字，那是 bug 遗留。只看独立 full eval
  2. rel_f1 跨 seed 方差较大（0.4449 vs 0.4655, ~2pp），报均值时必须带 std
  3. paper_framing.md 里的 Claims 还是基于 GRPO 写的（"CED GRPO 的 Evi-F1 > DREEAM"），进 research 后需要全面改为 RSFT 框架
  4. CED reranker PoC dry run 显示 CED-F1 Spearman r=-0.39（负相关），全量结果可能确认 CED 选 evidence 好但不选 relation 好的 candidate——这不矛盾，但论文 framing 要小心处理
- **GRPO 失败是有价值的 negative result**：CED reward 在 GRPO 中是唯一不 collapse 的（flat-NLI 和 extract-only 都 20-30 步崩），但在线 RL 导致 catastrophic forgetting。论文可以讲"CED 有效但训练范式matters"


---
