# director / loop_1.md

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`b16dd9f1c1bb241f0eca.json`](../../sessions/b1/b16dd9f1c1bb241f0eca.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-15T13:59:32+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：autodl-5090 上 cuda:0/1/2/3（4× RTX 5090），无跨项目 GPU 约束但不能用其他服务器的卡
- **gen-0 数据泄露已确认**：所有 6 generator 共享同一批 Wikipedia seeds。3-class F1=0.789 中 gen-0 被人为放大。primary metric 已改为 binary (gen-1 vs gen-2+) F1=0.723（D017）
- **论文中禁止用 bootstrap CI width 作为跨生成器一致性论据**（Round 2 C1 critical）——用 per-generator F1 std/range 替代
- method.tex 超参声明必须区分：ensemble 200/6，baselines 100/3（不再声称 "unified"）
- EMNLP 2026 ARR DDL = 2026-05-25（~10 天），不允许换会议

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090，项目目录 /root/gen-depth-fingerprint/
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/
- 论文真源：artifacts/_project/paper/（docs/paper/ 是同步副本）
- 参考模型：Pythia-410M（用于 NLL 特征提取）
- 生成器：Pythia-1B/2.8B, OLMo-2-1B, Qwen3-0.6B/1.7B/8B-Base（全 base model）
- P1-C instruct 实验用 Qwen3-1.7B（注意：Qwen3 系列无独立 base 版本，所有 Qwen3 出厂即 instruction-tuned，只是论文中用 raw continuation 模式）
- 数据集：/root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl（共享 seed 池）

### 3. 📊 当前状态
**Round 2 审稿修复进行中**（D016, D017）。已完成 + 运行中：

已完成实验：
- P0-A gen-0 泄露修复：binary F1=0.723 (7-feat), 0.724 (4-base+surf), 0.712 (4-base)
- P0-B volume-matched：Qwen3-8B +1.1pp 中 94% 来自 diversity 非 volume
- P1-D Table 3 统一 6-gen LOGO：AvgLP=0.737, LD=0.655, FDG=0.688, Bino=0.417; M6 关闭（100/3 vs 200/6 差异 <0.002pp）
- P1-E ordinal regression：CORAL 0.771, Frank-Hall 0.793, XGBoost 0.789——CI 重叠，M5 关闭
- P2-F cross-ref bias：Pythia-1B 在所有 ref model 下均 #1，same-family bias 不成立

运行中：
- P1-C instruct 模型验证（cuda:1, Qwen3-1.7B-Instruct）——Reviewer 预审 PASS on methodology
- Agent 正在处理紧急重写指令（Table 3 替换 + binary eval 段落 + 全文数字更新）

**写作修改**：大部分 minor fixes 已完成（C1 CI→per-gen std, C2 gen-0 disclosure, C3/C4 scope narrowing, M1/M2 claim calibration, m1-m9）。**但 Reviewer 审查发现 3 个 critical 遗漏**：Table 3 仍是旧 5-gen 数字、binary eval 段落缺失、text-table CI 矛盾。已通过 urgent_agent_message 派发修复指令。

### 4. 📋 待办（条件触发式）
- Agent 完成 Table 3 + binary eval 重写 → post_to_reviewer 验证数字一致性 → 如 PASS 则这批 critical 关闭
- P1-C instruct 结果出来 → 如 drift pattern 存在 → 追加 1-2 个 instruct 模型（OLMo-2-1B-Instruct, Qwen3-0.6B-Instruct）；如不存在 → 仅报告为 limitation（scope narrowing 已就位）
- 全部修改完成 → submit_paper_to_review(recommended_review_mode="continue") Round 3
- Round 3 如升至 Weak Accept → 准备 EMNLP ARR 提交材料；如仍 Borderline → 评估是否 main conference 或转 Findings track（不换会议）
- review_issues.yaml 需要添加 Round 2 的新 issues（C1-C4, M1-M6, m1-m9）并标记状态

### 5. 🎯 战略上下文
- **D017 是本轮最重要决策**：primary metric 改为 binary F1=0.723。关键发现——D015 的"4-baseline 反超 7-feature"结论在排除 gen-0 后反转（7-feat 0.723 > 4-base 0.712）。baseline ensemble 优势完全来自 gen-0 分类（detectors 天然擅长 human-vs-machine）。这对论文叙事是好消息。
- **最容易判断错的事**：(1) 6-gen baseline 数字与旧 5-gen 差异巨大（Binoculars 从 0.579 崩到 0.417，FDG 从 0.627 升到 0.688），不是 bug 是协议统一的正常结果；(2) Qwen3 系列没有真正的 base model，所有 Qwen3 都是 instruction-tuned，论文中需要加注释说明用 raw continuation mode
- **paper_framing.md 需要全面更新**——当前仍写着旧的 F1=0.79 和 CI width 叙事，与 D017 决策不一致。下一轮应优先更新 framing 文档
- 决策链：D012(EMNLP 主投) → D013(alt-classifier) → D014(R1修复) → D015(baseline ensemble framing) → D016(R2修复计划) → D017(binary primary metric)


---
