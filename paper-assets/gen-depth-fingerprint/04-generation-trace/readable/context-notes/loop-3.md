# director / loop_3.md

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`aff3bc341b70883961fd.json`](../../sessions/af/aff3bc341b70883961fd.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-15T20:29:30+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0/1/2/3（4 张），禁止使用其他设备号
- plan_008 generate 完成后必须先跑 `python dedup_generations.py --dry-run` → 确认 → `python dedup_generations.py` 去重，再进 extract/evaluate。脏数据进 pipeline 会污染 multi-domain 结果
- 论文 primary metric 是 binary F1=0.723（排除 gen-0 leakage），不是 3-class 0.789。所有新实验结果入纸时以 binary 为主
- Qwen3-0.6B instruct partial ρ 数值已从 Discussion 移除（无 registry 溯源），不要重新加回。仅保留定性结论 "negligible after length control"
- .tex 文件有两份副本（docs/paper/ 和 artifacts/_project/paper/），改一处必须同步另一处

### 2. 🖥️ 基础设施快照
- 服务器：需从 `get_project_status` / `list_ssh_hosts` 确认（我这轮未直接 SSH）
- 本地 paper 路径：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/`
- artifacts 路径：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/`
- 活跃进程：plan-008 multi-domain generate（PID 234066，news 域，cuda:0）；plan-010 human_edit_robustness（cuda:1）
- dedup 脚本就绪：`/root/gen-depth-fingerprint/dedup_generations.py`（dry-run 确认 news 域 801 重复行）

### 3. 📊 当前状态
刚完成：Round 2 review_issues 全部 Agent 侧 action items 关闭（22 项：4 critical resolved, 17 warning/info resolved, 1 in_progress=Rd2-W4 Director action 由 plan_008 覆盖）。Qwen3-0.6B partial ρ 无溯源数值已移除。Sampling ablation 完成（low/default 稳健，high temp −6pp 退化）。

RUNNING：plan-008 multi-domain（cuda:0）、plan-010 human_edit_robustness（cuda:1）
刚派给 Agent：cuda:2/3 填满指令（plan_013 text_length_control / plan_015 ordinal_baseline_comparison 优先，已完成则挑 P1）+ sampling ablation 写入 Appendix

Round 3 审稿已提交（apr_20260515T190552_49mw，continue 模式），等用户审批卡确认。

### 4. 📋 待办
- Round 3 审稿报告回来 → Read `review-report-action.skill.md` → Holistic Pass + Per-Comment Action Matrix → 派 Agent 修复
- plan_008 generate 完成回调 → 确认 Agent 执行 dedup → extract → evaluate → 结果写入论文（Rd2-W4 provenance characterization 证据）
- plan_010 完成 → 评估 human edit robustness 结果对 Limitations 的影响
- plan_013/015 完成 → 如果 plan_015 发现单 detector 连续分数 ordinal F1 >0.70 → 必须 reframe contribution 为 "complementary to existing detectors"
- sampling ablation Appendix 写完 → 检查一致性

### 5. 🎯 战略上下文
- 项目核心：generative depth fingerprinting — 用分布特征（entropy/tail_decay/TTR/hapax）做 ordinal depth estimation（gen-0/gen-1/gen-2+）
- 论文已经过 2 轮审稿，Round 2 四个 critical 全部 resolved（CI misuse→per-gen std、gen-0 leakage→binary primary、instruct→scope to base、cross-scale→mid-scale scope）
- 叙事已从 "novel method" 收缩到 "systematic empirical characterization"，claim 强度适中
- 35 个成功实验，数据底子厚，但 experiment_plan 中大量 P0 实验显示 "planned"（无 registry_id 链接）——实际多数已在其他 registry 名下完成，需要 Agent 确认并补链接
- 易错：experiment_plan 的 "planned" 不等于 "未做"，很多是 registry_id 未绑定。下指令前先让 Agent 确认状态
- EMNLP 2026 DDL 6月15日，还有 1 个月，时间充裕但不能松懈


---
