# reviewer / loop_2.md

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`f435cf66eaaead33ed18.json`](../../sessions/f4/f435cf66eaaead33ed18.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-22T19:09:28+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 **cuda:0**（`gpu_ids: ["cuda:0"]`），cuda:1-3 属其他项目。我之前误报"3张卡空闲"被 Director 纠正过。
- 训练命令必须加 `WANDB_MODE=disabled`，否则 wandb auth 错误导致崩溃。已连续 3 次因此失败（15% s2、25% s2 两次）。
- Llama 5% 结果（|d|=5.53）已决定**不纳入**论文——anomalous non-monotonic（|d(5%)|>|d(15%)|），Director 确认排除。
- Finding 3 inverted-U 保持 **"exploratory"** 定位，即使 multi-seed 复现也不升级——瓶颈是 N=1 model family（仅 Qwen 有 4 levels），不是 seed variance。

### 2. 🖥️ 基础设施快照
- 服务器：**westd-35694(root)**
- Qwen 工作目录：`/root/autodl-tmp/ctrl_contam_pilot/`（注意不是 `ctrl_contam_qwen`）
  - checkpoints: `checkpoints/contam_{5,15,25,50}[_s2,_s3]/`
  - results: `results/contam_{level}[_s{n}]_results.json`
- Llama: `/root/autodl-tmp/ctrl_contam_llama/`
- Mistral: `/root/autodl-tmp/ctrl_contam_mistral/`
- 训练日志：`/root/runs/irt_personfit_contam/exp-ctrl-contam-*.log`
- Python：`/root/miniconda3/bin/python`（conda base）
- wandb：**禁用**（`WANDB_MODE=disabled`）
- 活跃进程：截至 handoff 时 GPU 空闲，无训练进程

### 3. 📊 当前状态
Multi-seed 管线进行中但未完成：

| 条件 | s1 | s2 | s3 | 状态 |
|------|----|----|-----|------|
| 15% | ✅ eval done | ✅ eval done | ❌ 未启动 | 2/3 |
| 25% | ✅ eval done | ✅ eval done | ✅ eval done | **3/3 完成** |
| 50% | ✅ eval done | ✅ eval done | ❌ 未启动 | 2/3 |

**剩余**：15% s3 训练+eval (~30min) + 50% s3 训练+eval (~50min) = ~80min 串行。GPU 当前空闲，管线在训练间隙反复停滞（已报 Director 3 次）。

已审查的 multi-seed 数据（15% 2-seed）：free-θ CV=18% ✓, fixed-θ CV=34% ⚠️（略超 30% 门槛）。25% 的 3-seed 数据已到但我还未审查 Cohen's d 计算。

### 4. 📋 待办
- 15% s3 + 50% s3 eval 完成 → 审查完整 3-seed Cohen's d（CV < 30%? peak 一致?）→ 按我之前给 Director 的升级门槛判断 claim (a)(b)(c)
- 全部 multi-seed 到手 → 审查 Appendix K 表格数值与 raw results 一致性
- Appendix K 纳入论文后 → 全文一致性审查（Method §3.3 引用、Limitations 更新）
- 如 fixed-θ CV 持续 >30% → 建议正文注明 "fixed-θ shows moderate training-run variance"（这是诚实 finding，不是缺陷）

### 5. 🎯 战略上下文
- **目标**：EMNLP 2026 ARR，score ≥ 3.0 Findings。DDL 2026-05-25。用户指示"能到 3.0 就投"。
- **核心 story**：IRT person-fit (lz*) 检测 LLM benchmark contamination，3 模型 × 2 benchmark × 2-4 levels，全部 CI exclude zero。θ-fixed 设计是方法创新，inverted-U dose-response 是 exploratory finding。
- **Mistral n 值**：free-θ 用 n=10（scalar lz* 全存活），θ-fixed 限 n=6（s4-s7 response vectors 丢失）。Table 2 脚注已披露。
- **易错点**：
  1. 不要把 Qwen 目录猜成 `ctrl_contam_qwen`，实际是 `ctrl_contam_pilot`
  2. 不要建议用 cuda:1-3，只有 cuda:0 归本项目
  3. Llama 5% |d|=5.53 是 anomaly 不是 strong signal，已排除，不要重新纳入
  4. 论文 Llama accuracy: 正文写 59.3%，scatter 用 59.4%（10-seed mean 0.5937 四舍五入差异），trivial 但未修
  5. Method.tex L45 "three conditions" 技术上正确但可能混淆（实际 Qwen 有 4 levels），INFO 级不阻塞


---
