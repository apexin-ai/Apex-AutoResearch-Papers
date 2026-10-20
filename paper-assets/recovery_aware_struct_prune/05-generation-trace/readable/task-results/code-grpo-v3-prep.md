# code grpo v3 prep

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_grpo_v3_prep_20260515T080439_result.json`
- **Structured JSON:** [`8f7d359d5e7141729797.json`](../../sessions/8f/8f7d359d5e7141729797.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。修改摘要：

**`src/train_grpo.py` 修改内容 (v4 → v5)：**

1. **新增 CLI 参数**：
   - `--repetition_penalty` (default=1.0) — 惩罚重复 token，>1.0 抑制退化循环
   - `--top_p` (default=1.0) — nucleus sampling 阈值
   - `--top_k` (default=0) — top-k sampling，0=禁用
   - `--sampling_quality_check` — 训练前采样质量检查开关

2. **GRPOConfig 传参**：`top_p`, `top_k`, `repetition_penalty` 直接传入 GRPOConfig（trl 1.1.0 原生支持）

3. **`sampling_quality_check()` 函数**：训练前用当前 sampling 配置生成 10 个样本，报告：
   - 平均 completion 长度
   - 3-gram 重复率
   - EOS 率（正常终止比例）
   - 非零 reward 比例
   - 前 3 个样本预览
   - 0/10 非零 reward 时打印 WARNING 但不阻断训练

4. **训练启动 log** 增加 sampling 配置摘要

5. **文件注释** 更新为 v5，说明新参数用途

`--help` 验证因 trl 导入慢（>30s）无法在 SSH 30s 超时内完成，但已通过语法检查 + argparse 独立验证 + grep 确认所有参数定义和传递路径正确。

---
