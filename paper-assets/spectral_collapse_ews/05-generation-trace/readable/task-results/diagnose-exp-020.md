# diagnose exp 020

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_020_20260524T110010_result.json`
- **Structured JSON:** [`c4b263d549b9a2a060a7.json`](../../sessions/c4/c4b263d549b9a2a060a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。总结如下：

---

## 诊断结果

### 1. exp_020：**实际成功完成，不是崩溃**

日志最后输出了完整的 FINAL RESULTS SUMMARY（Gen 0-10），并保存了 summary JSON。进程正常退出。cron 报 "process dead" 是因为进程运行结束后自然退出，**不是崩溃**。

- Gen 0-10 全部 11 代数据完整
- 结果文件：
  - `/root/spectral_collapse_ews/results/phase1_gpt2m_pure_collapse_seed42_results.json`（6058 bytes, May 24 18:50）
  - `/root/spectral_collapse_ews/results/phase1_gpt2m_pure_collapse_seed42_summary.json`（6906 bytes, May 24 18:50）
- **可以将 registry 状态改为 success/DONE**

### 2. exp_022：**启动失败，路径错误**

日志显示 `cd: /root/spectral-collapse-ews: No such file or directory`（用了连字符而非下划线）。进程立即退出，从未运行。**可标记 DONE/failed**。

### 3. exp_022b：**启动失败，command not found**

日志显示 `python: command not found`（需要用 `python3` 或激活 venv）。进程立即退出。**可标记 DONE/failed**。

### 4. exp_022c：**正常运行中**（PID 868280, 已运行 3h20m）

- 这是 GPT-2-medium **fixed_mix r=0.3** 实验（3 代），不是 pure collapse
- 当前进度：Gen 2 生成合成数据中，已生成 ~9920/35000 samples
- Gen 0 eval 完成（eff_rank=23.09, ppl=15.45）
- Gen 1 完整完成（eff_rank=136.08, ppl=12.02, distinct4=0.9046, train_loss=2.4455）
- 结果在写入 `/root/spectral_collapse_ews/results/phase1_gpt2m_fixed_mix_r03_seed42_results.json`
- Checkpoints 存到 `/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1_gpt2m/fixed_mix_r03_seed42/`

---
