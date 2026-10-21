# reviewer / loop_5.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_5.md`
- **Structured JSON:** [`e68dd82b0f7dfd265fb6.json`](../../sessions/e6/e68dd82b0f7dfd265fb6.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_wall_time
updated: '2026-05-14T15:38:59+00:00'
---

### 1. 🔴 硬约束 / 红线
- AutoDL 服务器 `cqa1-21977` 是共享 6×4090D，项目约束 C001：提交前必须 `nvidia-smi` 查目标 GPU 上有无同类进程，有则不提交
- `submit_training_job` 的 `bash -c` wrapper 里裸 `python` 会 EXIT_CODE=127——必须用 `/root/miniconda3/bin/python` 绝对路径
- HuggingFace 在 AutoDL 上连不通——eval 类任务必须加 `HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1`（数据已全缓存）
- D018 决策：3B GSM8K 排除出 dose-response 分析（LoRA SFT 导致 CoT 灾难性遗忘，d000 仅 11.98%）
- auto-relay shell 脚本（`run_eval_*_auto.sh`）不写 sentinel 文件，cron 会误报 "process dead 5×"——审查这类实验必须独立检查日志和 PID，不信 cron 结论

### 2. 🖥️ 基础设施快照
- 服务器：`cqa1-21977`，代码目录 `/root/contamcal-irt-calibration`
- Python：`/root/miniconda3/bin/python`（conda base env，不用 venv）
- 模型缓存：`/root/autodl-tmp/.hf_cache/`（Qwen2.5-0.5B / 1.5B / 3B）
- Checkpoint：`/root/autodl-tmp/exp001/checkpoints/`
- Eval 结果：`/root/autodl-tmp/exp001/eval_results/`
- Exp006 代码：`/root/contamcal-irt-calibration/exp006/`（已修复 regex + 三参数过滤，dry run 通过）
- Exp002 signals：`/root/autodl-tmp/exp002/signals/`（0.5B 9/9 完成）
- Exp003 exposure：`/root/autodl-tmp/exp003/exposure_scores.json`
- 本地 exp004 sweep：PID 411032，`/tmp/exp004_sweep_20260514_071141.log`（48/120 runs）
- 本地 exp005 noise prop v3：PID 426335/426336，`artifacts/exp005_noise_propagation/exp005_v3.log`（14/25 fits）

### 3. 📊 当前状态
**我刚做完的审查**：
- exp_001_eval_05B_d100_aligned_v2 (failed, python not found) → v3 (failed, HF timeout) → v4 已提交（加了 HF_DATASETS_OFFLINE=1），在 GPU 2 运行中
- exp_001_eval_3B_d100_aligned：cron 误报，实际成功，已修正为 success（MMLU 64.17%, GSM8K 69.67%, ARC 83.96%, HumanEval 12.20%）
- worker_code_exp_006_fix_and_dryrun：代码修复正确，dry run PASS
- worker_diag_gpu3_gpu5_output_check：**Worker 误诊 d025_aligned 为 failed**（实际 PID 374947 仍在运行），已报 Director

**Registry RUNNING/PREPARING**：
- `exp_001_eval_05B_d100_aligned_v4` — GPU 2，0.5B d100 aligned eval（第 4 次尝试）
- `exp_001_eval_05B_d025_aligned` — GPU 5, PID 374947（2h21m+），conclusion 被误标 failed，实际在跑
- `exp_001_eval_3B_d005_aligned` — GPU 4, PID 373931（2h26m+），正常运行，输出待写
- `exp_001_sft_d025_15B` — GPU 0，1.5B d025 SFT 训练，ETA ~02:00 UTC May 15
- `exp_001_eval_15B_aligned_batch` — GPU 1，1.5B aligned eval batch
- `exp_004_sim_sweep_v2` — 本地，48/120 runs
- `exp_005_noise_prop_v3` — 本地，14/25 fits

### 4. 📋 待办（条件触发式）
- d025_aligned (PID 374947) 完成 → 验证结果完整性 + 要求 Agent 修正 registry conclusion
- d100_aligned_v4 完成/失败 → 审查；若又失败要求 Agent 在命令中显式 `source /etc/network_turbo`
- 3B d005 aligned (PID 373931) 完成 → 审查 metrics，对比 3B d000 baseline
- 0.5B d100 + d025 aligned 都完成 → exp_006 IRT 可正式重跑（命令：`python run_exp006.py --model-scale 0.5B --data-seed 42 --aligned-only`）
- 1.5B d025 SFT 完成 → 检查 final_loss 是否与 d005/d100 一致
- exp_004 sweep 到 120/120 → 审查 parameter recovery 是否稳定
- exp_005 noise prop 到 25/25 → 审查 CI width 差异是否 statistically significant

### 5. 🎯 战略上下文
- **核心 story**：4PL+γ IRT 模型通过 exposure scores 校准被污染 benchmark 分数，给出带 CI 的 calibrated scores
- **关键决策链**：D017（aligned MC format 替换 legacy）→ D018（3B GSM8K 排除）→ exp_006 代码修复（scale/seed/aligned 过滤）
- **最易判断错的事**：
  1. `evaluate.py` 只在**全部 benchmark 完成后**才写 `eval_results.json`——"输出目录为空"≠"进程失败"，必须查 PID + GPU util
  2. Cron "process dead 5×" 对 auto-relay 脚本是系统性误报——永远独立查日志
  3. Registry 的 `exp_id` filter 经常返回 0 条——用 `limit=N` 无 filter 拉最近 N 条再人工找
- **0.5B 指标参考**：d000 MMLU=39.79%, d005 MMLU=32.55%（d005 < d000 是因为 LoRA SFT capacity 损耗，非 bug）
- **3B 污染效应弱**：d100 vs d000 MMLU 仅 +0.77pp, ARC +1.20pp——大模型抗污染，这是预期结果


---
