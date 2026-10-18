# agent / loop_2.md

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`9c3981b0b98b67d02594.json`](../../sessions/9c/9c3981b0b98b67d02594.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-14T06:03:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-37397 cuda:0 + cuda:1，只有这两张卡，不可用其他设备
- 所有 eval 必须 bf16（fp16 在 Qwen L27 / Llama 上 overflow 产生无效 PPL，已踩坑两次）
- Mistral hires negative 已定论（MCKP=7.323 vs Uniform=7.131），不要重跑 4x Mistral
- max_2bit 缩放：Qwen 112 heads 用 max_2bit=8；Llama/Mistral 256 heads 需要按比例放大（Llama aggressive 用了 144/248）
- submit_training_job 不在 ssh/registry tool_group 里，必须 tools=["submit_training_job"] 显式传；否则 Worker 会 fallback tmux 导致 orphan 进程
- conda 环境：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不要假设 .venv 存在

### 2. 🖥️ 基础设施快照
- 服务器：westd-37397（2× RTX PRO 6000 96GB）
- 工作目录：`/root/ratekv/`
- Python：`/root/miniconda3/bin/python`（conda base）
- HF cache：需要确认，AutoDL 规则不适用（westd 非 AutoDL）
- Profiling 数据：
  - Qwen hires: `/root/ratekv/hires_profiling_results.json`（64×2048）
  - Llama hires: `/root/ratekv/llama_hires_profiling_results.json`
  - Mistral hires: `/root/ratekv/mistral_hires_profiling_results.json`
- 图表产出：`/root/ratekv/figures/`（3 张 PDF/PNG 已生成）
- 结果汇总：`/root/ratekv/results_summary.csv`（20 行，缺 Llama hires / Mistral hires / Llama aggressive 数据）
- 活跃进程：handoff 时无 GPU 进程在跑（nvidia-smi 0%/0 MiB），3 个 Worker 在代码准备阶段

### 3. 📊 当前状态
刚完成 session 恢复初始化，处理 Director 紧急指令（双卡空闲）。

**Registry PREPARING（3 个）：**
- `downstream_eval_qwen` — Worker turn 18，卡在 HF 下载超时（lm-evaluation-harness），尝试镜像站
- `mistral_aggressive_compression` — Worker turn 12，读取现有脚本中，即将写 run_mistral_aggressive.py 提交 cuda:0
- `kv_separation` (plan_014) — Worker 刚派发，需写 K/V 分离 profiling 代码后提交 cuda:1

**已完成本轮：**
- `head_sensitivity_viz` — conclusion=success，3 张图（heatmap/compounding/allocation），artifacts 已注册

**等待中：**
- 3 个 Worker 的 WORKER DONE 回调
- Director 对 plan_015/016（P0 未启动）的优先级决策

### 4. 📋 待办
- mistral_aggressive Worker 完成 → 更新 registry metrics，与 Llama aggressive 对比汇报；如果 5.3x MCKP 显著优于 uniform → 支撑"compression severity 放大 MCKP 优势"跨架构
- downstream_eval Worker 完成 → 更新 registry，检查 ARC-C/HellaSwag/PIQA/WinoGrande accuracy gap（MCKP vs uniform vs baseline）
- kv_separation Worker 完成 → 如果 K/V 独立分配 PPL < 当前 K=V MCKP (9.569) → 新 claim 维度；如果无差异 → 说明 K/V 对称性好，简化方法描述
- Director 批准 plan_015/016 → 立即派 Worker；两个都是 P0 且 GPU-h 极少（1h + 2h），应在当前实验间隙插队
- results_summary.csv 缺 3 组数据（Llama hires/Mistral hires/Llama aggressive）→ 下次有 CPU Worker 空档时补全
- Mistral heterogeneity 第 6 个数据点未补到 heterogeneity_analysis.txt → 用 Mistral hires profiling 数据补

### 5. 🎯 战略上下文
**核心结论**：MCKP 有效性 ∝ per-head sensitivity heterogeneity ∝ GQA ratio + compression severity。
- Qwen (GQA 7:1, 112 heads): Top-5% concentration 0.59-0.66 → MCKP 显著（4x: -15.7% PPL degradation reduction）
- Llama (GQA 4:1, 256 heads): Top-5% 0.34-0.59 → marginal（4x: thin margin 8.4498 vs 8.469）
- Mistral (GQA 4:1, 256 heads): Top-5% 0.42 → negative at 4x, 待验 aggressive
- 激进压缩放大优势：Llama 5.3x MCKP=57.6 vs Uniform=2644（45×）

**Framing**：A+C hybrid — "analysis paper + conditional method"。Claim 2 conditional on heterogeneity。D015 决策。paper_framing.md 已更新。

**最易判断错的事**：
- 不要以为 lowres profiling 够用 — 256 heads 模型必须 hires（64×2048），lowres 产生 false negative（Llama/Mistral 都踩过）
- plan_015 (L0-only heuristic) 是 Dream review 标记的 critical gap — 如果 L0-only 8bit + rest 4bit 匹配 MCKP，则整个优化框架冗余。这是论文最大风险，优先级应极高
- plan_016 (greedy + cardinality) 同理 — 如果 greedy+constraint 匹配 MCKP，贡献是 constraint 不是 solver
- downstream eval 标 8 GPU-h 但实际可能更快（4 tasks on 7B），也可能因 HF 网络问题拖很久

**决策链**：D007(放弃eviction) → D009(constrained MCKP) → D010(MVP pass) → D014(scope to ≥4x) → D015(Plan B analysis framing) → D016(跨架构定论)

**ARR May 25 deadline，剩余 11 天。** Timeline: May 14-15 完成 P1 实验 → May 15-16 Full Draft → May 16-19 写作迭代 → May 22-24 提交。


---
