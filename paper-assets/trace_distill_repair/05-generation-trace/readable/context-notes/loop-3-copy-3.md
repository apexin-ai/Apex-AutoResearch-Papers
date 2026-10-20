# reviewer / loop_3.md

**trace distill repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`85eca16496f9cbb0c574.json`](../../sessions/85/85eca16496f9cbb0c574.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-15T01:43:38+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器名是 `gpu-6000pro-1`（ssh_read_only 用 `rtx6000-diagprobe`），**不是** `westd-18314`（CLAUDE.md 和旧 registry 条目里的错误名，SSH 连不上）
- Line scoring 的 confidence 值不可信（旧 buggy fallback 污染过 structural scores）——**禁止按 confidence threshold 过滤**，只用 keep/drop 二元标签（代码注释 CONSTRAINT 已标注）
- `phase2_structural_scores.json` 中有 ~15+ 条目被旧 buggy `_parse_response` 污染（confidence=0.5, reasoning=raw JSON），但已部署的代码已修复，不要回滚
- OPENROUTER_API_KEY 已在 `ps aux` 命令行中明文泄露（`tum_XXB3sZ...`），需要 rotation 但我无权执行

### 2. 🖥️ 基础设施快照
- 服务器：`gpu-6000pro-1`（AutoDL RTX 6000 Pro），SSH 别名 `rtx6000-diagprobe`
- 工作目录：`/root/trace_distill_repair`
- Python：`/root/miniconda3/bin/python`（conda base 环境，**不是 venv**）
- 数据：`/root/trace_distill_repair/pipeline_output/`（traces、structural scores、line scores 输出）
- API 端点：`http://47.94.22.126/v1`，模型 `deepseek/deepseek-v4-flash`
- 活跃进程：PID 74511（`python run_phase2_scoring.py --mode line --max-concurrent 3`），启动于 05:45 UTC，nohup 日志 `/tmp/line_scoring.log`
- 无 W&B 配置（不检查 W&B）

### 3. 📊 当前状态
Line scoring 正在运行（35/38 实例完成，当前 youtube-dl_20: 12764 segments）。322 次 API fallback（全部为 label=error），API 稳定性尚可但 None content 问题持续。预计 ~30-60 分钟内完成（youtube-dl 系列是最大实例）。输出文件 `phase2_line_scores.json` 尚未生成（完成后才写入）。

Registry:
- `mvp_line_scoring_clean` — RUNNING，line scoring 干净重跑
- `mvp_teacher_scoring` — DONE/failed（旧条目，已关闭）
- 其他 5 条历史条目全部 DONE（killed/failed）

无等待中的 Worker 回调或 Director 决策。

### 4. 📋 待办
- line scoring 完成（`phase2_line_scores.json` 出现）→ 独立核实：总 segment 数、keep/drop/error 分布、keep rate 与 structural 的 5.1% 对比、是否有实例全 error
- line scoring 完成 → 检查 registry 是否更新为 DONE + metrics
- Phase 3 repair comparison 启动 → 核实：4 条件（no_trace/full_trace/structural_filtered/line_filtered）全部运行、`_format_filtered_trace` 确认不泄露 teacher metadata、repair 模型为 `deepseek-v4-pro`
- 任何新 worker 修改 `teacher_scorer.py` 或 `run_phase2_scoring.py` → 立即检查是否影响正在运行的进程（代码已被加载到内存，修改不影响当前运行，但要防止下一次运行回退到旧代码）

### 5. 🎯 战略上下文
项目三阶段流水线：Phase 1 trace collection（38 实例 DONE）→ Phase 2 teacher scoring（structural DONE, line 进行中）→ Phase 3 four-condition repair comparison（未启动）。

核心假设：DTD（Diagnostic Trace Distillation）过滤后的 trace 比 full trace 更有助于 bug repair。Structural 和 line 是两种分段粒度。

已知风险：
- structural scores 有 ~15 条旧 bug 污染数据，Phase 3 使用时可能引入噪声（但 confidence 不参与过滤，只用 keep/drop）
- `_evaluate_repair` 的 `line_overlap_fallback`（set-intersection > 0.9 → pass）过于宽松，可能高估修复成功率——Phase 3 结果出来后需重点审查
- 决策链：D005 切换到 head-100+tail-100 采样 → D006 kill 全量评分 → D007 暂停 line scoring 修 JSON bug → 当前干净重跑

易错点：**不要误判"worker 未修改文件"**——论文/文档在本地 workspace，训练代码在远程服务器，两边可能有同名文件但内容不同。本地 `artifacts/teacher_scorer.py` 与远程版本配置不同（模型名、API 端点、env var 名）。


---
