# agent / loop_4.md

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_4.md`
- **Structured JSON:** [`a6700ba3fb39c4a9d179.json`](../../sessions/a6/a6700ba3fb39c4a9d179.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: idle_timeout
updated: '2026-05-15T00:56:20+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 `autodl-5090:cuda:0` / `cuda:1` / `cuda:2` / `cuda:3`，无例外
- `submit_training_job` 的 command 必须用 `bash -c '...'` 包装（tmux 用 sh，否则 EXIT_CODE=127）
- command 中必须显式 `export CUDA_VISIBLE_DEVICES=N &&`，仅靠 gpu 参数传递不可靠（2026-05-14 inject25 r1 OOM 事故教训）
- eval 参数是 `--device cuda:0`（不是 `--gpu 0`）
- Dose-response 所有实验 seed=42，baseline 对比 vanilla seed=42 (61.7%)，**不是** 3-seed 均值 (65.3%)
- `multiseed_stats.py` permutation test 已修复（`np.mean(diffs)` + Phipson-Smyth correction），paper_framing 中旧 p 值需已更正

### 2. 🖥️ 基础设施快照
- 服务器：`autodl-5090`，工作目录 `/root/autodl-tmp/tax_error_inject_agent`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 模型：`/root/autodl-tmp/models/Qwen/Qwen3-8B`
- ms-swift 版本：4.2.0
- Dose-response 预生成数据：`data/mini_pipeline_v4/ablation_fixed/`（inject10/25/50 已就绪）
- Checkpoint 查找：`ls -dt .../v0-*/ | head -1` 选最新 run，`ls -d checkpoint-* | sort -V | tail -1` 选最大 step
- W&B config：项目级配置在 `load_project_config` 中
- 活跃进程（4 个训练）：
  - `v4-taxei-fixed-inject50`：cuda:0，SFT 训练
  - `v4-random-fixed-inject25`：cuda:1，SFT 训练
  - `v4-random-fixed-inject10`：cuda:2，SFT 训练
  - `v4-random-fixed-inject50`：cuda:3，SFT 训练
- Cron：reconcile 返回 0（可能训练刚启动、cron 尚未注册，或上一轮 session 未来得及注册——**优先检查这 4 个实验是否有 cron 监控**）

### 3. 📊 当前状态
**刚完成**：Random 3-seed eval 全部完成（63.1%±7.0pp），D015/D016 决策更新，paper_framing.md 修正（p 值更正、narrative 从 "significant degradation" → "directional but NS"），dose-response baseline 修正（same-seed comparison）。

**正在跑**：4 个 dose-response 训练占满全部 4 张 GPU（TaxEI-50% + Random-10%/25%/50%），这是 dose-response 对照实验的最后一批。

**3 个 Worker 运行中**（可能已完成但未回调）：
1. `worker_analysis_comprehensive-results` — 汇总全维度结果 artifact
2. `worker_code_fix-multiseed-add-seed123` — 修复 multiseed_stats.py + 加入 seed=123 数据
3. `worker_eval_check-training-and-eval` — 检查训练进度和 eval 状态

**等待中**：无活跃 cron。这 3 个 Worker 的回调随时可能到达。4 个训练完成后需要 eval。

### 4. 📋 待办（条件触发式）
- 3 个 Worker 回调到达 → 按 on-worker-done skill 处理各自产出，更新 registry + report.md
- **v4-taxei-fixed-inject50 训练完成** → spawn Worker eval（`--device cuda:0`），结果填 dose-response 50% 格（预期比 25% 的 48.9% 更低）
- **v4-random-fixed-inject10/25/50 训练完成** → 各自 spawn Worker eval，结果与 TaxEI 同比例对比（消歧：数据稀释 vs 注入毒性）
- Random inject25 eval 结果判断：若 Random-25% ≈ TaxEI-25% (48.9%) → 纯稀释效应，taxonomy 标签无害也无益；若 Random-25% > TaxEI-25% → taxonomy 标签额外有害
- 所有 dose-response 完成 → 汇总 dose-response 曲线（TaxEI vs Random 两条线），更新 paper_framing.md，向 Director 汇报完整结果
- comprehensive-results artifact 完成 → 注册 artifact，用于论文 Results section
- **确认 4 个训练是否有 cron 监控**——reconcile 返回 0 是异常信号，可能需要手动注册 cron

### 5. 🎯 战略上下文
**项目结论链**：D008 Gate FAIL → D009 Option C 补充验证 → D010/D013/D014 全维度否定 → 转 negative result paper → D015/D016 修正统计（所有比较 NS）。

**论文方向**：Target EMNLP 2026 Insights from Negative Results。核心 narrative = "Error injection helps tool-use (PALADIN) but hurts/no-effect on embodied planning (TaxEI)"。三个 pillars：(1) 主效应 NS + 高方差，(2) dose-response 非线性阈值，(3) TaxEI vs Random 无差异（taxonomy 标签无附加价值）。

**易错点**：
- 不要把 dose-response 结果和 3-seed 均值混用——dose-response 全是 seed=42，baseline=61.7%
- PALADIN +57pp 中 ~30pp 来自 retrieval augmentation，不是纯 SFT 效果——对比时必须说明
- Detection rate 全 0% 是 eval 框架局限（只看最终成功），不是模型能力结论——写论文时注意措辞
- 26 个 PREPARING 实验大部分是历史遗留（v1-v3 迭代、retry 版本），不需要跑，不要被数量误导
- permutation test 已修复但 paper_framing.md 中的 p 值可能仍是旧值——写论文前再核实一遍


---
