# code d022 alpha code diff

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d022-alpha-code-diff_20260515T084504_result.json`
- **Structured JSON:** [`aed771eb132e9dab0f8e.json`](../../sessions/ae/aed771eb132e9dab0f8e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/alpha_ablation_diff_report.md`。以下是核心结论：

---

## 排查结论

### 代码差异：无
prune.py、model_utils.py、eval_gsm8k.py 两台服务器完全一致（0 行 diff）。

### 真正的差异源

**1. Importance scores 不同：westb 用 512 calibration samples，westd 用 256。** 这导致 ~5% 的 MLP group 选择不同（6 层各 1-2 groups 交换），但 layer 级别的保留数量完全一致。

**2. α ablation 在 N=100 下无统计显著差异：**
- α=0.0: 30% ± 4.6pp
- α=0.5: 25% ± 4.3pp  
- α=1.0: 27% ± 4.4pp
- 三者在 95% 置信区间内重叠，**不支持 "CKA 反而伤性能"** 的结论

**3. westb Standard (1%) 是真实退化，不是 eval bug。** 同一服务器、同一 eval 脚本、间隔 45 分钟：Standard 输出 "10 years, 10 years..." 重复循环（文件 316KB），RASP 输出连贯推理（文件 91KB）。

**4. 29pp 差距的根因：**
- RASP vs Standard 的 layer 分布完全不同：RASP 用 layer 6/27 的容量换取 layer 16-18/22/25/26 的保护
- α=0.0 vs Standard 的 layer 分布相同，但具体 group 选择因 calibration 差异略有不同
- 最可能解释：512-sample importance 恰好把某个 critical group 排到 "safe to prune"，256-sample 没有 → 模型在 20% sparsity 下处于 fragile threshold

### 建议行动
1. **等 GPU 空闲后在 westb 重跑 `pruned_standard_20` eval**（用当前代码），确认 1% 可复现
2. **在 westd 上用 n_samples=512 重算 importance scores 再跑 α=0.0**，消除 calibration 混淆
3. **α ablation 需要 N=全集** 才能判断 α 效应是否显著

---
