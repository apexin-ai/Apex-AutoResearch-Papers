# director / loop_3.md

**trace distill repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`f0d2e56c625216035dec.json`](../../sessions/f0/f0d2e56c625216035dec.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-15T11:35:11+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 只能用 rtx6000-diagprobe 的 cuda:0 和 cuda:1
- MVP 阶段全程 API-only（scoring/repair 都调 DeepSeek API），GPU 为 Research 阶段 student training 预留，但不能释放
- API key 加载必须用 `source /root/trace_distill_repair/.env`，不能用 `source /root/.bashrc`（有 non-interactive guard 会 return）
- phase2_line_scores.json 可能被 rogue v5 进程（PID 112847）覆盖——使用前检查文件时间戳和实例数（应为 33 实例）
- Line scoring v3 是有效数据（v2 数据源，33 实例，4091 segments）——之前有过 "v3 是 v1 数据" 的误判，已被三条独立证据推翻，不要再重跑

### 2. 🖥️ 基础设施快照
- 服务器：rtx6000-diagprobe (connect.westd.seetacloud.com)，用户 root
- 工作目录：/root/trace_distill_repair
- Python：/root/miniconda3/envs/bugsinpy/bin/python（Python 3.8，BugsInPy 专用）
- conda env：bugsinpy（trace 收集用），base（其他用途）
- API key：/root/trace_distill_repair/.env（OPENROUTER_API_KEY / DEEPSEEK_API_KEY）
- Research 阶段模型：Qwen3-Reranker-0.6B 已下载（GPU 上），QLoRA 环境已验证
- 数据：pipeline_output/（v2 traces + segments），phase3_results.csv（132 条 repair 结果）
- 可能存活进程：PID 112847（rogue v5 line scoring，需 kill）；Phase 3 PID 116942 应已完成
- Cron：mvp_phase3_repair 监控可能还在

### 3. 📊 当前状态
Phase 3 repair comparison 全部完成（33 实例 × 4 条件 = 132 次评估），但评估不可信：0% test execution pass rate（BugsInPy 项目依赖未装）。

**D017 决策**：暂缓 MVP 判定，优先修复 test execution 后用客观指标重新评估。

Registry 状态：
- mvp_phase3_repair: DONE（需改 conclusion 为 negative_signal_pending_reeval）
- mvp_structural_scoring_v3: DONE(success) — 566 segments, keep=41 (7.2%), error 4.8%
- mvp_line_scoring_v3: DONE(success) — 4091 segments, keep=226 (5.5%), error 4.6%
- mvp_line_scoring_v4/v5: killed（冗余）

无等待中的 Worker 回调或 Cron。Agent 和 Reviewer 都刚 RESET。

### 4. 📋 待办
- 接手后立即 → kill PID 112847（rogue v5），确认 phase2_line_scores.json 未被覆盖
- 接手后 → 派 Agent 修复 test execution：从 4 个高 judge 实例开始（black_1, fastapi_1, fastapi_2, httpie_2），在 bugsinpy env 中安装项目依赖，验证 test_command 可执行
- Test execution 修复后 → 对 phase3_results.csv 已保存的 repair outputs 重新跑 test evaluation（不需要重调 API）
- Test-based 结果仍然 no_trace ≥ structural → MVP FAIL 确认，开始 pivot 方案（从 "method paper" 转 "analysis paper: when/why trace helps/hurts"）
- Test-based 结果 structural 有正面信号 → 按 D016 改 segment cap（MAX_SEGMENTS 从 20 提到 40-50 + 分层采样）后重跑一轮
- Reviewer 建议同时做两件事：(a) test-based re-eval (b) 改 cap 后重跑 scoring + Phase 3

### 5. 🎯 战略上下文
**核心问题**：LLM judge 数据显示 no_trace (1.06) > structural (0.76)——trace 不仅没帮助反而有害。但 0% test execution 意味着没有客观指标，这个结论不 definitive。

**决策链**：D013/D014（发现 Phase 1 trace bug）→ D015（Phase 1 v2 重跑 + Phase 2 scoring）→ D016（确认 segment cap 问题但先跑完 v3 做初步评估）→ D017（Phase 3 完成但评估不可信，暂缓 MVP 判定）

**最容易判断错的事**：
1. 不要因为 judge 数据负面就直接宣布 MVP FAIL——评估本身不可信（0% test exec + LLM 自评），需要 test-based 重新评估
2. 不要再重跑 line scoring——v3 已被三次独立证据确认为 v2 数据，Agent 之前的误判（"v3 是 v1 数据"）已纠正
3. Reviewer 指出 judge 相对排序仍有信息量（同框架下偏差对所有条件一致），方向性信号是真实的——不要完全忽视负面趋势
4. 55% 实例 structural keep=0，即使 test execution 修好，structural 在这些实例上 = no_trace。论文叙事需从 "structural > line" 转向 "token efficiency / precision-recall tradeoff"
5. DDL 5/25 还有 10 天，时间仍可控但不能再浪费在重复的数据源误判和 API key 问题上


---
