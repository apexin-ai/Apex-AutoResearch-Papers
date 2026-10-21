# agent / loop_8.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_8.md`
- **Structured JSON:** [`e2522b2c8a24bcc7262a.json`](../../sessions/e2/e2522b2c8a24bcc7262a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: idle_timeout
updated: '2026-05-15T22:11:53+00:00'
---

### 1. 🔴 硬约束 / 红线
- 只能用 **westd-11235:cuda:0** 和 **westd-11235:cuda:1**，无其他 GPU 配额
- DeepSeek 系列实验必须用**旧代码**（`load_best_model_at_end` 已注释为 `# TEMP_DISABLED`），保持 DeepSeek 组内一致。Qwen seed 实验可用新代码
- **"0pp gap" 叙事已死**（D028）——不得在论文或汇报中声称 exception_only 跨模型 gap = 0pp
- DeepSeek full_trace v3 的 `--model_path` 必须用 `/root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6.7b-instruct`（注意最后一层不带下划线）
- 同 GPU 上禁止并行 eval+training（之前 cuda:1 上并行导致 7s/step→49s/step）

### 2. 🖥️ 基础设施快照
- **服务器**: westd-11235，2x RTX PRO 6000 Blackwell 94GB，CUDA 12.8
- **工作目录**: `/root/trace-verdict-study`
- **Python**: `/root/miniconda3/bin/python`，conda base 环境（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- **模型**: Qwen = 默认 HF cache; DeepSeek = `/root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct`（路径含 `___`）
- **数据**: `/root/autodl-tmp/trace-verdict-study-data/`（5910 samples, 4720 train / 1190 test）
- **Checkpoints**: `/root/autodl-tmp/trace-verdict-study-checkpoints/`
- **W&B**: project=`trace-verdict-study`
- **HF cache**: `HF_HOME=/root/autodl-tmp/.hf_cache`
- **活跃进程**:
  - `deepseek_full_trace_seed42_v3`: PID 163109, cron 监控中, cuda:0
  - `deepseek_exception_only_seed456`: 训练已完成（22:08 UTC），状态 ANALYZING
- **活跃 Worker**: `worker_analysis_deepseek_eo_seed456_eval`（running，正在做 seed456 评估）

### 3. 📊 当前状态
我这个 session 一直在处理 DeepSeek 跨模型验证 + seed robustness 实验。关键时间线：

- **刚完成**: `deepseek_exception_only_seed456` 训练结束（22:08 UTC），Worker 正在跑 eval。这是**最高优先级数据点**——第三个 seed，决定 Claim 1 最终 framing（seed42=99.83%, seed123=91.09%, seed456=?）
- **正在跑**: `deepseek_full_trace_seed42_v3`（cuda:0, PID 163109）——用 label-preserving truncation fix 重训 DeepSeek full_trace。预计还需 ~1h
- **Registry**: 33 个实验，RUNNING 1, ANALYZING 1, DONE 30（success 16, negative 4, failed 2, killed 8）
- **等待中**: `worker_analysis_deepseek_eo_seed456_eval` Worker 回调 → 需要立即处理 seed456 结果

### 4. 📋 待办（条件触发式）
- **seed456 eval Worker 回调到达** → 读 metrics → update_registry → 计算 3-seed 统计（mean/std/CI） → 确定 Claim 1 最终 framing → 汇报 Director → 更新 paper_framing.md → 通知 Paper Agent 恢复 Claim 1 相关章节
- **seed456 ≥ 97%** → Claim 1 可以说 "2 out of 3 seeds ≥99%, 1 seed outlier due to LoRA init"，故事更强
- **seed456 ≈ 91%** → seed42 是 outlier，Claim 1 必须说 "effective but high-variance on DeepSeek"，framing 更保守
- **deepseek_full_trace_v3 cron 回调** → spawn Worker 跑 eval → 结果填入跨模型对比表第 4 格（目前缺 full_trace DeepSeek 有效数据）
- **full_trace v3 success** → 跨模型 4 条件对比表完整 → 可以写 Table 2 终稿
- **full_trace v3 collapse again** → DeepSeek full_trace 可能需要 2-epoch early stopping 或更激进截断策略，向 Director 汇报

### 5. 🎯 战略上下文
- **投稿 DDL**: ARR May 25 = 10 天后。Paper Agent 已在写初稿（Claim 2/3 章节继续，Claim 1 暂停等 seed456）
- **核心叙事转变**（D028）: 从 "exception signal is model-agnostic universal (0pp gap)" 转向 "exception is consistently the best component, but absolute cross-model performance is seed/model dependent"。paper_framing.md 已更新到 v2.8
- **Qwen 数据非常强**: exception_only 99.83% ± 0.00 across 3 seeds，irreducible error 已确认（2 样本来自 GeneratorExit 误标记）
- **DeepSeek 是薄弱环节**: VOTA 84.45% (vs Qwen 99.41%), exception_only seed-dependent。文献解释准备了 3 个 hypothesis（CRUXEval gap / pretraining scale / inductive bias ceiling），将放 Discussion
- **易踩的坑**:
  1. 不要把 DeepSeek epoch1 checkpoint 的 accuracy 当最终结果报——除非论文明确说用 epoch1（目前 paper 用 final epoch3）
  2. Bootstrap CI 方法不一致：Qwen 用 paired，DeepSeek 部分用 unpaired。论文同一表格必须统一方法
  3. `vota_ae_only_seed42` (99.92%) 不是 headline claim——D020 裁定 ae_only 进 Claim 3 层级表但 headline 仍是 exception_only
  4. calibration_analysis 用的 token ID 查询已修复（P0），DeepSeek calibration 必须用 v2 代码


---
