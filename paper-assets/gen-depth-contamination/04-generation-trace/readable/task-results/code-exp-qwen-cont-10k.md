# code exp qwen cont 10k

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_qwen_cont_10k_20260522T092300_result.json`
- **Structured JSON:** [`b34c2c3b2a90c778fbc6.json`](../../sessions/b3/b34c2c3b2a90c778fbc6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已提交并运行中。汇总：

**1. 原始数据和模型路径**
- 原始实验: `exp_016_base_vs_instruct`，数据在 `data_exp016_qwen_base/`，5000 样本
- Base 模型: `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B`
- Instruct scorer: `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct`

**2. 策略: 全量重跑**
- Pipeline 不支持增量（无 append/resume 参数），从头生成 10k samples
- Pipeline 自动从 C4 validation 下载 depth_0（10k 行），无需手动扩展

**3. depth_0 样本数**
- Pipeline 的 `prepare_seed_data()` 根据 `--num_samples 10000` 自动从 C4 流式采样 10k 条，无瓶颈

**4. 执行信息**
- tmux session: `exp_qwen_cont_10k`
- GPU 1 已占用 3721 MiB，模型加载完成，正在下载 C4 种子数据
- 两阶段: Phase 1 base 生成 → 删 features.csv → Phase 2 Instruct 评分
- 日志: `/tmp/exp_qwen_cont_10k_phase1.log`, `/tmp/exp_qwen_cont_10k_phase2.log`
- Registry: `exp_qwen_cont_10k` → RUNNING

---
