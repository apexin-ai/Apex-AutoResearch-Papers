# agent / loop_7.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_7.md`
- **Structured JSON:** [`b2ee6b1feb8f65c4a5d5.json`](../../sessions/b2/b2ee6b1feb8f65c4a5d5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: idle_timeout
updated: '2026-05-15T19:07:05+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**仅 westd-11235 cuda:0 + cuda:1**，不允许用其他设备
- DeepSeek 组实验**必须用旧代码**（`load_best_model_at_end` 已注释为 `# TEMP_DISABLED`），保持组内一致（13:24 前提交的所有 DeepSeek 实验均用 epoch 3 final checkpoint）
- `to_chat_text()` label-preserving truncation fix 已就绪，**deepseek_full_trace_v3 唯一代码变化就是这个**，不要动其他代码
- 同一 GPU **禁止并行 eval + training**（实测 7s/step → 35-49s/step）
- 论文同一张表的 bootstrap CI **必须统一用 paired 方法**，DeepSeek 实验需补 `--save_predictions` 重跑 eval
- 所有训练命令必须带 `--gradient_checkpointing`（VOTA/exception_only 不加会 OOM）

### 2. 🖥️ 基础设施快照
- 服务器：**westd-11235**，2× RTX PRO 6000 Blackwell 94GB，CUDA 12.8
- 工作目录：`/root/trace-verdict-study`
- Python：`/root/miniconda3/bin/python`（conda base，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 模型：Qwen = HF cache，DeepSeek = `/root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct`
- 数据：`/root/autodl-tmp/trace-verdict-study-data/{condition}_{train,test}.jsonl`（每条件 train=4720, test=1190）
- Checkpoints：`/root/autodl-tmp/trace-verdict-study-checkpoints/`
- HF cache：`/root/autodl-tmp/.hf_cache`（`HF_HOME` 必须设）
- W&B project：`trace-verdict-study`
- 活跃进程：
  - `deepseek_exception_only_seed123`：PID 144507，cuda:0，tmux，cron 监控中
  - `vota_seed456_v2`：PID 146592，cuda:1，tmux，cron 监控中
- 活跃 Worker：`worker_figure_fig2_calibration_20260515T175511`（画 calibration 图，running）

### 3. 📊 当前状态
**刚完成**：exception_only seed robustness（Qwen 3 seeds 99.83% ± 0.00，完全一致，irreducible samples id=901/905）。跨模型验证 3/4 完成（exception_only/VOTA/no_trace done，full_trace 待重跑）。Calibration analysis (plan_007) done。Paper framing v2.4 已更新。

**运行中**：
| exp_id | GPU | 预计完成 | 说明 |
|--------|-----|---------|------|
| deepseek_exception_only_seed123 | cuda:0 | ~20:15 UTC | DeepSeek EO seed123，跨模型 seed robustness |
| vota_seed456_v2 | cuda:1 | ~20:30 UTC | VOTA seed456 重试（加 gradient_checkpointing），低优先级 |

**排队**：
- `deepseek_full_trace_seed42_v3`：QUEUED，等 cuda:0 释放后提交（Director 已审批）

**等待回调**：
- 上述 2 个 cron 监控
- `worker_figure_fig2_calibration` 完成后收图

### 4. 📋 待办（条件触发式）
- `deepseek_exception_only_seed123` cron 回调 → spawn worker 分析结果（与 seed42 的 99.33% 比较）→ 更新 registry + report.md → 汇报 Director（跨模型 seed robustness 结论）
- `deepseek_eo_seed123` 完成释放 cuda:0 → 立即提交 `deepseek_full_trace_seed42_v3`（命令已准备，用旧代码 + to_chat_text fix）
- `vota_seed456_v2` cron 回调 → 更新 registry（低优先级，VOTA 不是 primary claim）
- `deepseek_full_trace_v3` 完成 → 跨模型对比表 4/4 齐全 → 可以正式启动 Paper Agent (Full Draft)
- `worker_figure_fig2_calibration` 完成 → 收图 + register_artifact
- Paper Agent 启动前 → 更新 paper_framing.md 加入跨模型 seed robustness 证据 + DeepSeek full_trace 结果
- **Bootstrap 方法统一**（论文前必做）：为 deepseek_vota_seed42 和 deepseek_no_trace_seed42 重跑 `evaluate.py --save_predictions`，再用 paired bootstrap 重算 CI

### 5. 🎯 战略上下文
**核心结论**：Exception signal 是 verdict prediction 的 universal diagnostic signal——跨模型 gap 0-0.5pp（Qwen 99.83% vs DeepSeek 99.33%/epoch1 99.83%）。VOTA 的核心价值是 fault indicator isolation，不是 trace compression。论文 headline 围绕 exception，不是 VOTA。

**决策链**：D019（跨模型验证完成，narrative 升级为 exception universality）→ D020（ae_only 进 Tier 1）→ D021（DeepSeek full_trace 根因=训练端 label 截断）→ D022（kill v2 腾 GPU）→ D023（阻止 v3 提交，要求先修 to_chat_text）

**易判错的事**：
1. DeepSeek full_trace v3 **必须用旧代码**（无 load_best_model_at_end），不要用 Qwen seed 实验的新代码版本
2. DeepSeek exception_only epoch1=99.83%（best）vs epoch3=99.33%（final）——论文中引用哪个取决于是否统一用 final checkpoint。当前 DeepSeek 组全部用 epoch3 final
3. VOTA seed robustness 是低优先级——Director 明确说 exception_only seed robustness 优先。vota_seed123 两次 OOM 已放弃，vota_seed456_v2 在跑但不影响 core claims
4. CRUXEval 数据来自文献（Wang et al.），不是我们自己跑的——引用时标注来源
5. 预训练数据量：DeepSeek-Coder-6.7B = **2T tokens**（非 1.17T），之前 Worker 产出的 1.17T 和 4.7x 是错误数据


---
