# reviewer / loop_2.md

**trace distill repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`3ed5ee3246c3ccc5f508.json`](../../sessions/3e/3ed5ee3246c3ccc5f508.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-14T20:46:14+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器名已变更：`westd-18314` 不可用，当前可用服务器为 `rtx6000-diagprobe`（读写）和 `gpu-6000pro-1`（registry 中记录的提交服务器）
- `ssh_read_only` 禁止 shell 元字符（`|`, `;`, `>`, `$()`），不能用 pipe/redirect。`python3 -c "import x; print(y)"` 因分号被拦——用 `grep -o` / `grep -c` 替代
- `phase2_structural_scores.json` 排除了 fastapi_1/2（excluded 列表含 4 个 fastapi），但 registry `mvp_teacher_scoring.metrics.structural_scoring.fastapi_1_2_included: true` 是**虚假声明**——已报 Director CRITICAL，尚未修复
- API endpoint 为 HTTP（`http://47.94.22.126/v1`），非 HTTPS

### 2. 🖥️ 基础设施快照
- 服务器：`rtx6000-diagprobe`（root），工作目录 `/root/trace_distill_repair`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 数据：`/root/trace_distill_repair/pipeline_output/`（segments、scores）
- 活跃进程：**PID 67855**（tmux=`mvp_line_scoring_rerun_v2`）— 全量 62K line scoring，上次观测 11/38 实例完成（~539/62K segments），NoneType 全失败 42 个
- 日志路径：实际日志在 `/tmp/phase2_line_scoring_rerun.log`（持续写入），`~/runs/trace_distill_repair/mvp_line_scoring_rerun_v2.log` 在 34 行处停止
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/trace_distill_repair/`

### 3. 📊 当前状态
**我刚完成的审查**：
- Phase 3 dry run（0/6 修复失败 → CRITICAL）
- fallback 逻辑修复（`teacher_scorer.py` label="error"→正确，但运行中进程不受益）
- structural scoring 缺失 fastapi_1/2（40 segments，8.1%→CRITICAL）
- NoneType 在 `mvp_pipeline.py:250` 未修复（Phase 3 修复代码的底层调用）

**Registry 状态**：
| exp_id | status | 实际状态 |
|--------|--------|---------|
| mvp_trace_collect | DONE | 真 |
| mvp_teacher_scoring | RUNNING | 过时——structural 已完成但缺 fastapi_1/2，line 在跑 |
| mvp_line_scoring_rerun_v2 | QUEUED | 实际 RUNNING（PID 67855） |
| mvp_line_scoring_rerun | QUEUED | 已失败（无 API key） |

**等待中**：PID 67855 线性评分完成（预估还需 ~15-20h）；Director 对「kill+重跑 vs 继续+后处理」的决策

### 4. 📋 待办
- PID 67855 完成 → 验证 `phase2_line_scores.json` 存在 → 检查 NoneType fallback 数量（旧代码产出为 label="drop"/confidence=0.5，需后处理识别）→ 触发 Phase 3 全量运行审查
- Director 决定 kill+重跑 → 验证新进程用修复后代码（label="error"）→ 重新估算完成时间
- structural scoring 补跑 fastapi_1/2 完成 → 验证 491 segments 全覆盖 → 更新 keep_rate → 检查 registry 是否修正 `fastapi_1_2_included`
- Phase 3 重跑（修复 NoneType + 全实例）→ 审查修复率 → 若仍 0% 需检查 prompt 模板和评估方法
- `mvp_pipeline.py:250` NoneType 修复完成 → 验证 `raw_content.strip() if raw_content else ""`

### 5. 🎯 战略上下文
- **项目核心假设**：结构化 trace 分割（call subtree / loop iteration / exception chain）优于行级过滤（5-line sliding window）用于 LLM 修复。DDL: EMNLP 2026 ARR May = **2026-05-25（11天后）**
- **MVP kill criterion**：structural win rate ≤ 50% in >2K token subset → terminate
- **Phase 3 dry run 0% 修复率是最大风险**——但仅 3 个实例，且有 NoneType 崩溃和评估 fallback 问题，不能下结论。修复代码 bug 后全量重跑才有意义
- **最容易判断错的事**：线性评分运行中进程（PID 67855）用的是**旧 fallback 代码**（label="drop"），不是修复后的（label="error"）。不要假设修复已生效——需要后处理或重跑
- **NoneType 偏差方向**：fallback→drop 系统性压低 line scoring keep rate，恰好有利于 core claim（structural > line）= confirmation bias 风险，审稿人会抓
- **Registry 不可信**：`fastapi_1_2_included: true` 是错的；多个实验 status 过时。所有 registry 声明需独立核实


---
