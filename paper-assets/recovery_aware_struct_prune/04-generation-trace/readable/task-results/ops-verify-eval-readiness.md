# ops verify eval readiness

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_eval_readiness_20260514T200247_result.json`
- **Structured JSON:** [`529c3801c2494c15bd61.json`](../../sessions/52/529c3801c2494c15bd61.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证报告

### eval_full_gsm8k.sh — **不存在，需创建**

服务器上没有 `eval_full_gsm8k.sh`。最接近的是：
- `run_full_eval_d008_parallel.sh` — 2 GPU 并行 eval 4 个模型（pruned + recovered），full 1319 samples，max_new_tokens=4096。**缺 baseline**。
- `run_full_eval_d008.sh` — 串行版本，同样 4 个模型，**缺 baseline**。

**差距**：现有脚本覆盖 4/5 模型，缺少 baseline (`/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B`)。

### eval_gsm8k.py — **OK，就绪**

- `--max_samples` 默认 `None`（全量 1319 samples）
- `--max_new_tokens` 默认 4096（满足 ≥2048）
- 无硬编码限制
- 答案提取支持 `\boxed{}`、`####`、纯数字回退

### 训练进度快照

| 训练任务 | 进度 | 速度 | 预计剩余 |
|---------|------|------|---------|
| grpo_rasp_20_fast (cuda:0) | 294/500 (58.8%) | ~24.8s/step | ~85 min |
| grpo_standard_20_fast (cuda:1) | 293/500 (58.6%) | ~24.9s/step | ~86 min |

两个训练进度基本同步，reward 趋势暂不可见（日志显示的是 TRL 训练表格 UI）。

### 结论

**需创建 `eval_full_gsm8k.sh`**。建议基于现有 `run_full_eval_d008_parallel.sh` 改造：
1. 在 GPU0 任务队列开头加 baseline eval（`/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B`）
2. 保持其余 4 个模型不变
3. 输出路径统一到 `results/eval_*_full.json`

是否需要我现在创建这个脚本？

---
