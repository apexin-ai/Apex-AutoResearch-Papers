# agent / loop_20.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_20.md`
- **Structured JSON:** [`0b1cf32fdc0b5958594e.json`](../../sessions/0b/0b1cf32fdc0b5958594e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 20
reason: idle_timeout
updated: '2026-05-22T18:35:37+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：rtx5090-4x cuda:0/1/2/3，共 4 张。不得用其他服务器或卡号
- test_eval 系列是 Re-DocRED test_revised (500 docs) 评估，split 必须是 `test_revised`，不是 `test` 或 `dev`
- 4B RSFT s42 adapter 已丢失（/root/autodl-tmp/rsft_output/checkpoint-510 被删），不可直接重跑 4B RSFT eval，需要先用 retrain_4b_rsft_ced_s42_v2 的 checkpoint
- no-evidence eval 必须与 with-evidence eval 配对使用同一 max_new_tokens=2048，否则截断不对称导致 tax 计算不可信（D139/D140 教训）
- Framing: threshold claim 仅限 observational + Qwen family specific；cross-arch 仅放 Discussion（D147）

### 2. 🖥️ 基础设施快照
- **服务器**: rtx5090-4x (4× RTX PRO 6000, 96GB/卡)
- **工作目录**: `/root/autodl-tmp/freige`（代码），`/root/autodl-tmp/eval_results/`（eval 输出）
- **Python**: `/root/miniconda3/bin/python`，激活: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型路径**:
  - Qwen3-1.7B: `/root/autodl-tmp/models/Qwen/Qwen3-1.7B`
  - Qwen3-4B: `/root/autodl-tmp/models/Qwen3-4B`（注意不是 `/models/Qwen/Qwen3-4B`）
  - Qwen3-8B: `/root/autodl-tmp/models/Qwen/Qwen3-8B`
  - Qwen3-14B: `/root/autodl-tmp/models/Qwen/Qwen3-14B`
  - LLaMA-3.1-8B: `/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B`
- **SFT adapters**: `sft_output_qwen3_1_7b_bf16`, `sft_output`(4B), `sft_output_qwen3_8b_bf16`, `sft_output_qwen3_14b_bf16`, `sft_output_llama_3_1_8b` (均在 `/root/autodl-tmp/` 下)
- **数据**: `/root/autodl-tmp/data/re-docred-repo/data`（test_revised, 500 docs）
- **活跃进程**（reconcile_crons 确认）:
  - test_eval_14b_sft_s42_no_evi: PID 143166, cuda:3
  - test_eval_1_7b_sft_s42_no_evi: PID 147596, cuda:1
  - test_eval_8b_sft_s42_no_evi: PID 152873, cuda:2
- **空闲**: cuda:0（test_eval_1_7b_sft_s42 失败后释放）

### 3. 📊 当前状态
**刚做完**: 收到 `test_eval_1_7b_sft_s42` 失败 cron 回调（failure_reason: "process dead 5× with no sentinel/W&B — auto-resolved as failed"）。已 spawn 诊断 Worker (`worker_diagnose_test_eval_1_7b_sft_s42_20260522T022529`)，**尚未收到回调**。

**RUNNING (3)**:
| exp_id | GPU | 用途 |
|--------|-----|------|
| test_eval_14b_sft_s42_no_evi | cuda:3 | D147 no-evi test spot-check: 14B |
| test_eval_1_7b_sft_s42_no_evi | cuda:1 | D147 no-evi test spot-check: 1.7B |
| test_eval_8b_sft_s42_no_evi | cuda:2 | D147 no-evi test spot-check: 8B |

**cuda:0 空闲 = 失职状态**。test_eval_1_7b_sft_s42 是 test table 最后一个 SFT 缺口（1.7B SFT test eval），必须诊断完立即重跑。

**等待中**:
- Worker 回调: `worker_diagnose_test_eval_1_7b_sft_s42_20260522T022529`（诊断 1.7B SFT test eval 失败原因）
- 尚未向 Director 汇报（等诊断结果后一并汇报）

### 4. 📋 待办
- 诊断 Worker 回调到达 → 读根因 → update_registry failure_reason → 修复后立即在 cuda:0 重跑 test_eval_1_7b_sft_s42（命令需要加 conda activate，参考其他成功实验的格式）
- test_eval_14b_sft_s42_no_evi / test_eval_1_7b_sft_s42_no_evi / test_eval_8b_sft_s42_no_evi 任一完成 → on-experiment-done 流程（更新 registry、report.md、汇报 Director evidence tax test-set 结果）
- 全部 test eval 完成 → 编译 test table → 派 Paper Worker patch 论文表格
- 4B RSFT retrain 需要 Director 审批（在近期任务列表中）

### 5. 🎯 战略上下文
- **核心结论**: FREIGE 系统在 DocRE 上验证了 (1) RSFT+NLI 有效性 (2) evidence tax 随 scale 变化的 landscape：1.7B evidence helps (-5.63pp tax)，4B+ neutral (~0)，LLaMA unstable。Variance compression 是核心贡献
- **当前阶段**: test set eval 收尾 + D147 reviewer framing 预审的 no-evidence spot-check。距 EMNLP 2026 ARR July ~55 天
- **决策链关键**: D140 截断审计 → D143 @2048 confirmed → D144 3-scale tax → D145 paper_framing C3 修正 → D146 4B 3-seed neutral → D147 reviewer 预审采纳
- **易错点**:
  1. submit_on_allocated 的命令必须自带 conda 激活（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`），裸 python 可能找不到依赖
  2. 4B 模型路径是 `/root/autodl-tmp/models/Qwen3-4B` 不是 `/root/autodl-tmp/models/Qwen/Qwen3-4B`（历次失败教训）
  3. test_eval 用 `--split test_revised` 不是 `--split test`
  4. 1.7B 截断率很高（test RSFT trunc 73.8%），test SFT 也会类似，这是已知行为不是 bug


---
