# agent / loop_1.md

**trace distill repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`537460f31143a77cf114.json`](../../sessions/53/537460f31143a77cf114.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-14T19:40:06+00:00'
---

### 1. 🔴 硬约束 / 红线
- API base_url: `http://47.94.22.126/v1`，key_id: `tum_XXB3sZILRCg8llb3NjxVbbRNzFpsYVFdiogFkavpGn8`，env var: `OPENROUTER_API_KEY`
- Teacher model: `deepseek/deepseek-v4-flash`，Repair model: `deepseek/deepseek-v4-pro` — 不要用其他 model ID
- EXCLUDED_INSTANCES 只排除 `fastapi_3` 和 `fastapi_5`（0 events）。fastapi_1/2 已恢复，必须包含在有效实例中。Reviewer 已提两次，第三次会 CRITICAL
- 有效实例应为 38 个（40 setup 成功 - 2 excluded），不是 36 个。当前运行的 Phase 2 用了旧排除列表（36 个），fastapi_1/2 需补跑
- DDL: EMNLP 2026 ARR May 2026-05-25

### 2. 🖥️ 基础设施快照
- 服务器: gpu-6000pro-1 (westd-18314)，RTX 6000 Pro × 2
- 工作目录: `/root/trace_distill_repair/`
- 数据目录: `/root/trace_distill_repair/pipeline_output/`（38 实例的 trace + structural segments + line segments JSON）
- Structural scores: `/root/trace_distill_repair/pipeline_output/structural_scores/`
- Line scores: 写入 `phase2_line_scores.json`（主进程完成后生成）
- 日志: `/tmp/phase2_structural_scoring.log`, `/tmp/phase2_line_scoring.log`
- 活跃进程: line scoring PID 60414/60524（预计还需 ~40-50 min），无 tmux/cron 监控（API-only 阶段）
- Python 环境: 未确认是 venv 还是 conda，Worker 连接时需 detect_image 先探测

### 3. 📊 当前状态
**刚做完：**
- Registry 更新了 structural scoring 结果（451/451, keep=23/5.1%, drop=428）
- teacher_scorer.py NoneType bug 已修复（retry + fallback）
- EXCLUDED_INSTANCES 已修复（移除 fastapi_1/2）
- Director 已收到进度汇报

**正在等：**
- Line scoring 主进程完成（12/36 done at ~19:05 UTC，预计 ~19:50-20:10 完成）
- 两个 Phase 2 原始 Worker 仍显示 running（`worker_exp_phase2_structural_v2_20260514T182529` 和 `worker_exp_phase2_line_v2_20260514T182543`），structural 那个可能已完成但未正式回调

**Registry:** mvp_teacher_scoring = RUNNING, mvp_trace_collect = DONE (success)

### 4. 📋 待办
- Line scoring 主进程完成 → 立即补跑 fastapi_1/2 的 line scoring + 检查 structural scoring 是否也缺 fastapi_1/2（如缺则一并补跑）
- 补跑完成 → 汇报 Director 完整对比：structural keep rate vs line keep rate（含 fastapi_1/2）
- Phase 2 全部完成 → update registry mvp_teacher_scoring → DONE，记录 line scoring metrics
- Phase 2 DONE → 立即启动 Phase 3: 4-condition repair comparison（no-trace / full-trace / structural-filtered / line-filtered），38 有效实例 × 4 条件 = 152 repair 调用，repair model = deepseek/deepseek-v4-pro
- Phase 3 分析要求：>2K token 子集按 structural segment 数量分层（≥5 vs <5），分别报告 win rate
- Phase 3 完成 → 运行 mvp_analysis.py 生成 MVP 判定报告
- annotations 标记（不排除但需标注）：httpie_1, tqdm_2, scrapy_4, scrapy_7 (too_small); luigi_5/10/14 (low_segment_count)

### 5. 🎯 战略上下文
- 核心假设：结构化 trace 分段 + teacher 打分产生的压缩 trace 在修复任务上优于行级过滤
- Structural keep rate 5.1% (23/451) 非常低 — 这本身是好信号（高压缩率），但 Phase 3 win rate 才是决定性指标
- Kill criteria: structural win rate ≤ 50% in >2K token subset → 终止项目
- 易错点 1: trace 序列化必须用 `dtd_types.serialize_event()`，不要手动构造 dict（已被 Reviewer catch 3 次）
- 易错点 2: 不要假设 .venv 存在，连接服务器先 detect_image
- 易错点 3: Phase 2 原始 Worker（structural_v2/line_v2）可能会回调 DONE，但实际 scoring 是由它们启动的后台进程完成的，需要看日志确认真正完成状态而非盲信 Worker 回调
- D001: MVP 用 teacher 直接打分验证，不训练 student model
- D002: 40 实例、50 segments 抽查、操作化 kill criteria
- D003: Claim 4（通用性）降级为 Discussion future direction
- D004: 启用 line event + sub-function 分段


---
