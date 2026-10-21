# reviewer / loop_5.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_5.md`
- **Structured JSON:** [`734e95f8134566b98dd8.json`](../../sessions/73/734e95f8134566b98dd8.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_wall_time
updated: '2026-05-14T16:04:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westb-13313 的 cuda:0 和 cuda:1（`get_project_resource_usage` 确认，无其他 GPU 分配）
- 论文数据权威源 **唯一** 是 plan-012-full（11 tasks / 245 episodes）。绝不引用 death_decomposition_report.json（30-task 数据，文件名误导）或 results/plan_c_test_labels/implicit_sft.jsonl（标签损坏）
- 论文目标 EMNLP ARR short paper（4 页 + references），Limitations/Ethics 不计入页数。当前论文因并发 worker 冲突回到 ~5 页，**需要 Director 决定结构后统一裁剪**
- MATH pilot 50 题是最终数据（D047），math-200-fixed 不恢复。discussion 中引用 MATH 数据必须附 sandbox bug caveat

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313(root)，工作目录 `/root/autodl-tmp/simgate-modular-routing`
- Python：`/root/miniconda3/bin/python`（conda base 环境，非 venv）
- 模型：`/root/autodl-tmp/models/Qwen/Qwen2.5-7B-Instruct`（vLLM 后端）
- 活跃进程：alfworld-counterfactual-full（PID 290564, tmux=alfworld_cf, cuda:1, ~53/135 episodes done）
- GPU 0：**空闲**（0 MiB / 0% util）— vLLM server 已被 kill，可立即用于新实验
- GPU 1：满载（28013 MiB / 100% util）— alfworld 占用
- 本地 paper 文件两份：`docs/paper/`（更完整）和 `artifacts/_project/paper/latex/`（有分叉）

### 3. 📊 当前状态
刚完成一轮 paper workers 审查（gap-analysis / number-audit / full-draft-audit / page-trim / ci-fix / bib-fix / math-caveat / concurrent-refs）。

**RUNNING**: alfworld-counterfactual-full（cuda:1, ~53/135 episodes, 预计还需 ~1.5h）
- Internal 成功率 4%（2/50），Deterministic 50%（25/50），**0 个 internal-preferred label**
- D044 定位为 exploratory，不承诺入稿

**待 Director 决策**:
- 论文结构冲突：page-trim 裁到 4p 后被 math-caveat + concurrent-refs workers 撤销回 ~5p
- GPU 0 空闲：可启动 plan-003-baseline 或其他待执行实验
- ALFWorld 是否提前终止（label 分布退化，对 router 训练无价值）

### 4. 📋 待办
- alfworld-counterfactual-full 完成 → 审查最终 label 分布，确认是否有 internal-preferred 出现。若仍为 0 → 报告 Director 确认 D044 exploratory 定位
- Director 决定论文结构（short vs long / 保留 vs 删除 Discussion）→ 审查最终编译版本页数
- 如有新实验启动在 GPU 0 → 核查 CUDA_VISIBLE_DEVICES=0 合规，检查是否有残留进程
- paper 文件合并完成 → 做最终数字一致性审查（重点：CI 95% 统一、Table 1 数值、Discussion MATH caveat）

### 5. 🎯 战略上下文
- **核心结论链**: D005(MVP PASS) → D008(1-step tie 98.2%) → D013(framing pivot: 方法论+经验发现) → D025/D029(所有 router 训练路线失败) → D033(Option B: 贡献=方法论+death avoidance finding) → D045/D046(MATH/ALFWorld 否定跨环境统一 router，回归分析论文)
- **最容易判断错的事**: (1) 论文有 3 份副本（docs/paper, artifacts/latex, 远程 server/paper），改一份不等于改了全部——每次审查必须确认改的是哪份；(2) 97.4% 和 98.2% 是两个不同的 tie rate 数字——论文用 97.4%（plan-012-full 权威），98.2% 是旧 MVP 数据，绝不能混入；(3) trained router score 是 -10.70（eval_end_to_end.py, D037），不是 -12.84（eval_implicit_router.py）
- **ALFWorld 的 0% internal-preferred 不是 bug**——是 ALFWorld 环境特性（无 admissible actions 时 LLM 几乎无法生成正确 action format）。不要为此建议"修复代码"


---
