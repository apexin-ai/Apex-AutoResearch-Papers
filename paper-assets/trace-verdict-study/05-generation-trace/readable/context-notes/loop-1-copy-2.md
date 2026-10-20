# agent / loop_1.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`6fe22ab1a6dd134be900.json`](../../sessions/6f/6fe22ab1a6dd134be900.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-14T22:14:46+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-11235 的 cuda:0 和 cuda:1，**不可用其他卡**
- VOTA trace 输出中**禁止包含 match/assert_match 字段**——这是 Round 1 作废的直接原因（信息泄漏）
- 训练数据格式化必须保证 label（pass/fail）不被截断——用 `_truncate_trace` 智能截断，不能依赖 tokenizer 粗暴截断
- `[No trace available - execution failed]` 类文本是隐性泄漏，已改为 `[No trace available]`，不可回退
- submit_training_job 的 command 必须用 `bash -c "..."` 包裹（tmux 用 sh 不是 bash，不包会 EXIT_CODE=127）

### 2. 🖥️ 基础设施快照
- 服务器：westd-11235，工作目录 `/root/trace-verdict-study/`
- Python：`/root/miniconda3/bin/python`，conda base 环境（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 模型缓存：`HF_HOME=/root/autodl-tmp/.hf_cache`（Qwen2.5-Coder-7B-Instruct 通过 ModelScope 下载）
- 数据目录：`/root/autodl-tmp/trace-verdict-study-data/`（raw_traces.jsonl 5910 样本 + 3 组 train/test jsonl）
- Checkpoint 目录：`/root/autodl-tmp/trace-verdict-study-checkpoints/{condition}/final/`
- GPU：2x RTX PRO 6000 Blackwell 94GB, CUDA 12.8
- 活跃进程：
  - no_trace_seed42_v4: PID 835084, tmux=no_trace_seed42_v4, cuda:0（预计 ~1.3h，约 23:30 UTC 完成）
  - vota_seed42_v4: PID 835161, tmux=vota_seed42_v4, cuda:1（预计 ~3.7h，约 01:50 UTC 完成）
- W&B：无 API key，训练 fallback 到 tensorboard

### 3. 📊 当前状态
**MVP Round 2 训练中**（Round 1 因 match 泄漏 + label 截断全部作废）。

刚完成：
- Bug 1（match 泄漏）和 Bug 2（label 截断）修复 + 数据重新生成
- 文献调研：12 篇论文写入 literature_map.yaml，确认 VOTA 有文献空白

Registry 活跃实验：
- `no_trace_seed42_v4`: RUNNING, cuda:0（baseline）
- `vota_seed42_v4`: RUNNING, cuda:1（核心实验）
- `full_trace_seed42_v2`: PREPARING，排队等 cuda:0 空闲

等待中：
- cron 回调：no_trace_seed42_v4 完成 → 需立即提交 full_trace_seed42_v2
- cron 回调：vota_seed42_v4 完成 → 评估
- cron 回调：full_trace_seed42_v2 完成 → 评估
- 三组全部完成后 → 向 Director 汇报完整对比结果

### 4. 📋 待办（条件触发式）
- no_trace_seed42_v4 cron 完成 → 立即 `submit_training_job` full_trace_seed42_v2 到 cuda:0，command: `bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --gpu 0 --wandb_project trace-verdict-study --wandb_run_name full_trace_seed42_v2"`
- 任一实验完成 → spawn worker 运行 `python eval/evaluate.py --condition {cond} --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/{cond}/final/ --data_dir /root/autodl-tmp/trace-verdict-study-data/`
- 三组评估全部完成 → 向 Director 汇报三组完整对比（accuracy / lift / fail_F1 / bootstrap CI），Director 判定 MVP pass/fail
- 若 VOTA lift ≥ no_trace + 2pp 且 CI 不含 0 → MVP PASS，进入 research 阶段
- 若 VOTA lift < 2pp 或 CI 含 0 → WEAK PASS，需在 CRUXEval 上追加验证

### 5. 🎯 战略上下文
- **核心假设**：VOTA（assertion snapshots + exception summaries + loop compression）在 verdict 二分类上显著优于 no-trace baseline（≥2pp + CI 不含 0）
- Round 1 的 99.2% VOTA accuracy 是假的（match 字段泄漏），Round 2 才是真实测试
- **最容易判断错的事**：Round 2 的 VOTA accuracy 预期会**大幅低于** 99.2%（泄漏已移除）。不要因为数字下降就认为实验失败——关注的是 VOTA vs no_trace 的 **lift**，不是绝对值
- 截断率：vota 88.7% / full_trace 94.9%。两者截断后 avg tokens 接近（1922 vs 1957），**差异在 trace 内容质量不是长度**——VOTA 把 assertion snapshots 放前面，截断丢的是次要信息
- 文献空白已确认：无现有工作做 compressed trace + SFT for verdict → VOTA 有 novelty
- MVP 截止 May 17（还剩 ~2.5 天），时间充足
- 7 个旧实验（v1/v2/v3）全部标记 killed，不要理会


---
