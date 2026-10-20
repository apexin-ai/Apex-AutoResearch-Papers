# director / loop_3.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`6776a1c568544c515a28.json`](../../sessions/67/6776a1c568544c515a28.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-15T10:12:55+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 cuda:0 和 cuda:1（westd-11235 分配给本项目的两张 RTX PRO 6000 Blackwell 98GB）
- 所有训练必须加 `--gradient_checkpointing`（两次 OOM 教训：plan_002 首次、exception_only 首次）
- vota_v5 registry accuracy 以 eval_results.json (0.9916) 为准，不是旧 registry 值 (0.9941)
- ae_only 数据 88% 是 fallback locals dump，不能在论文主表中将 ae_only 结果归因于 "actual/expected comparison values"（D007）
- cuda:0 曾有 49GB 孤儿显存问题（无法软件清除），服务器重启后已解决但可能复发

### 2. 🖥️ 基础设施快照
- 服务器：westd-11235 (connect.westd.seetacloud.com)，账号 root
- 工作目录：/root/trace-verdict-study
- Checkpoints：/root/autodl-tmp/trace-verdict-study-checkpoints/{condition}/final/
- 模型：Qwen2.5-7B（主模型）；DeepSeek-Coder-6.7B（plan_004 需下载）
- 数据：/root/trace-verdict-study/data/ 下各 condition 的 train/test jsonl
- 活跃进程：ae_only 在 cuda:1 训练中（~2h15m 总时长，启动约 1h 前）；plan_004 刚指令 Agent 启动 cuda:0
- Dream：dream_20260515T084908 running（full mode），完成后会注入 Director session

### 3. 📊 当前状态
plan_001/002/003(exception_only+loop_only) 全部完成，三个 Core Claims 均有实验支撑。我刚完成：
- D011 记录完整 component hierarchy（two-tier architecture）
- paper_framing.md 三个 Claims 全部更新到最新实验结果
- 指令 Agent 启动 plan_004（DeepSeek-Coder 三条件复现）on cuda:0

Registry RUNNING/PREPARING：
- `vota_ae_only_seed42` — cuda:1 训练中（plan_003 最后一个 sub-condition，结果入 Appendix）
- plan_004 尚未注册 registry（Agent 刚收到指令）

等待中：
- ae_only 训练完成 cron 回调
- plan_004 Agent 启动确认
- Dream dream_20260515T084908 完成回调
- Reviewer 审查报告（Related Work 有两个 WARNING：遗漏 TRACED/TracePile、全部引用为 placeholder）

### 4. 📋 待办
- ae_only 完成 → eval + registry，结果仅入 Appendix 附 caveat（D007）
- plan_004 DeepSeek-Coder 三条件完成 → 与 Qwen 结果对比，确认 VOTA 跨模型泛化
- Dream 完成 → Read `skills/global/dream-report-action.skill.md`，按协议处理三档审稿报告
- plan_003 + plan_004 全部完成 → 决定是否启动 Paper Agent（写 Related Work/Method/Setup），或先跑 plan_005（第二 verdict task）
- Related Work Reviewer WARNING → Agent 需补 TRACED (ICSE 2024) + TracePile (NeurIPS 2025)，但写作暂缓到 Dream 之后
- EMNLP ARR deadline May 25（还剩 10 天）→ plan_003+004 完成后评估是否够 Main 还是走 Findings

### 5. 🎯 战略上下文
**决策链**：D003 MVP PASS → D006 collapse=bug → D008 ae冗余 → D009 gradient dilution 26% → D010 exception 是核心机制 → D011 two-tier architecture

**核心结论**：verdict prediction 本质是 fault detection。VOTA 有效因为它保留了 exception signals（Tier 1 fault indicators，99.83% 单独即近完美）。loop 是 Tier 2（85.6%，有信息但被 Tier 1 覆盖）。非 exception 组件组合反而引入噪声（exception_only > VOTA full, p=0.01）。

**易错点**：
- Claim 1 不能说 "behavioral understanding"——已精确化为 "fault indicator preservation"（D010）
- exception_only > VOTA full 是 positive finding 不是 limitation——定位为 "identifying minimal sufficient diagnostic signal"
- plan_002 的 4.5pp 提升已通过 paired bootstrap 确认显著（p<0.001, CI [2.4, 6.6]），不要因 individual CI 重叠而质疑
- Reviewer 建议过在 Discussion 做 failure-type 分组分析（AssertionError vs RuntimeError），不需额外实验用现有数据即可，值得做
- ROADMAP 需要更新（当前版本未反映 D009-D011 和 plan_003 完成），新 session 启动后先 update_roadmap


---
