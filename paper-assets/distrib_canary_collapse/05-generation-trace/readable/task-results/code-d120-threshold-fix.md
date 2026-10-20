# code d120 threshold fix

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d120_threshold_fix_20260520T050549_result.json`
- **Structured JSON:** [`bd437421a140f0bf7dd3.json`](../../sessions/bd/bd437421a140f0bf7dd3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D120 修复完成。总结：

**修改内容**：`run_5method_analysis_d102.py` 中 `_onset_gen` 函数从 `3x_sigma_drift`（std(前3点)，双向检测）改为 D105 true 3σ（std(全序列)，单向检测）。三处标签同步更新。

**验证结果**：在 `alpha_sweep_a050_s42_fp32` 上运行，threshold_onset = 0/8，与 `recompute_3sigma_d105.py` 参考实现逐对完全一致。

**关于预期值差异**：任务描述中 "threshold 3σ 后应为 8/8" 不准确。8/8 是旧 `3x_sigma_drift` 的结果（前3点 std 极小导致阈值极低）。D105 true 3σ 用全序列 std，阈值更高，α=0.50 的 downstream 指标 drift 不够越过 → 0/8。这与 M037 审计中所有实验的 thr3s=0-2/8 一致。

**服务器同步**：westd-19828（原地修改+备份）、westd-17855（base64 传输）均已更新。

**状态**：D120 fix validated，等 Agent 协调启动全量重算。

---
