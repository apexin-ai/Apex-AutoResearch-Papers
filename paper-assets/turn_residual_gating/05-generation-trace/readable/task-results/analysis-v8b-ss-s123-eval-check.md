# analysis v8b ss s123 eval check

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v8b_ss_s123_eval_check_20260521T151951_result.json`
- **Structured JSON:** [`264f19c2b36541514b84.json`](../../sessions/26/264f19c2b36541514b84.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

### v8b SS s123

- **训练已完成**（3 epoch，耗时 38773s ≈ 10.8h），checkpoint 已保存到 `epoch_0/1/2` + `gate_params.pt` + `lora/`
- **没有 eval 输出**。训练脚本不自带 eval，checkpoint 目录和服务器上均无 eval 相关文件。s123 需要单独跑 eval。

### s42 参考

- s42 的目录名是 `tg_v8b_ss_fixed_s42`（不是 `tg_v8b_ss`），同样**服务器上没有 eval 文件**
- s42 的 eval 结果存在**本地** `artifacts/eval_v8b_ss/data/v8b_ss_eval_results.json`，是独立 eval 脚本产出的，不是训练自带
- s42 eval 关键指标：model_gen GAR_ours mid_turns=0.3177, iid GAR_ours mid_turns=0.4983, ppl=2.78/1.38

### v7 训练状态

- **PID 245628 仍在运行**，已运行 4h29m，命令为 `launch_v7_tg_s123.sh`，正常。

**结论：s123 训练完成但还没跑 eval，需要参照 s42 的方式单独执行 eval 脚本。**

---
