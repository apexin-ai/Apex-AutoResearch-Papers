# code mvp 001 validation

**When Does KV Redundancy Predict MLP Sparsity? Architecture Dependence of Cross-Axis Signals in Reasoning Inference** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-001-validation_20260511T224510_result.json`
- **Structured JSON:** [`f0d1d2e7a71157be1796.json`](../../sessions/f0/f0d1d2e7a71157be1796.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已成功提交并运行中。

**状态总结：**

- **实验 ID**: mvp-001
- **服务器**: seetacloud-bjb2-structtts (RTX 5090, 31GB)
- **进程 PID**: 6503
- **GPU 占用**: 15.2GB / 32.6GB, 利用率 56%（正在生成 CoT）
- **数据源**: HF 网络超时，自动 fallback 到 20 道硬编码 MATH 题（Level 3-5）
- **日志**: `/home/sonny/redundancy-compound-sparsity/results/mvp/mvp_run.log`
- **结果输出**: `/home/sonny/redundancy-compound-sparsity/results/mvp/mvp_results.json`

**脚本实现要点：**
1. 对每道题先 `model.generate()` 生成 CoT（max 4096 tokens），再做完整前向传播收集指标
2. Forward hooks 挂在 `k_proj`/`v_proj`（KV cosine similarity）和 `down_proj`（MLP L1 norm + 40%/55% sparsity perturbation）
3. Surprisal 用 logsumexp 高效计算，避免具现化完整 log_softmax 矩阵
4. 每层独立计算 EMA (α=0.3)，全局 EMA 取跨层均值
5. 聚合后输出 Pearson r、K-S test、Δpert 及 pass/fail 判定

**注意**: Python stdout 重定向到文件有缓冲延迟，日志更新可能不及时。查看进度可用 `nvidia-smi` 确认 GPU 活跃，或等结果 JSON 生成。

---
