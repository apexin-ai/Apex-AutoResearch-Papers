# ops d37g eval 19828 cuda0

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d37g_eval_19828_cuda0_20260521T080253_result.json`
- **Structured JSON:** [`1f9c881962a99e0d1131.json`](../../sessions/1f/1f9c881962a99e0d1131.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行正常。模型已加载，GPU 0 使用 6527 MiB / 71% 利用率，Generation 0 已开始。

## 结果

**D37-G Task Degradation Evaluation: 放弃**
- 原因: westd-17855 ↔ westd-19828 双向 SSH 不通（hostname 无法解析），且 19828 磁盘仅剩 24GB，不满足 C007 2x 空间要求（~14GB checkpoints 需要 28GB）

**Fallback a000_s48_fp32: 已启动**
- 服务器: westd-19828, cuda:0
- exp_id: `alpha_sweep_a000_s48_fp32`
- PID: 656188
- 配置: pythia-410m, α=0.00, seed=48, fp32, 10 generations × 5000 steps
- 状态: Generation 0 训练中，GPU 71% 利用率
- 预估完成: ~4 小时后（参考 a000_s46_fp32 速率 ~24 min/gen）

注意: 首次提交因 HF 网络请求阻塞（AutoDL 未配置 network_turbo），已用 `TRANSFORMERS_OFFLINE=1` + `python -u` 重启解决。

---
