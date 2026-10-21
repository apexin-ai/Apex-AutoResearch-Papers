# analysis consolidate results

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_consolidate-results_20260513T225459_result.json`
- **Structured JSON:** [`2e872a669efbea9803b3.json`](../../sessions/2e/2e872a669efbea9803b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CLS v5 训练在 eval step 4600 之后中断（进程已死），但 best checkpoint 早已确认。现在编译完整报告。

---

## Part 1: CLS v5 完整 Checkpoint 列表与 Best 确认

**现有 checkpoint**: checkpoint-600, checkpoint-4000, checkpoint-4200, checkpoint-4400, checkpoint-4600（save_total_limit=5，早期 checkpoint 已被覆盖）

**Eval loss 趋势**（每 200 步评估一次）:

| Step | Eval Loss | Epoch |
|------|-----------|-------|
| 200 | 0.1258 | 0.09 |
| 400 | 0.0761 | 0.18 |
| **600** | **0.0642** ✓ best | **0.27** |
| ... | *(持续上升)* | |
| 4000 | 0.3216 | 1.81 |
| 4200 | 0.3045 | 1.90 |
| 4400 | 0.1824 | 1.99 |
| 4600 | 0.2906 | 2.08 |

**结论**: **Best checkpoint 确认为 step-600**（eval_loss=0.0642）。第一个 epoch 结束后严重过拟合，eval_loss 涨了 4-5 倍。训练进程已终止（PID 2947259 不存在），停在 step 4600 附近（总 6633 步），无需继续。

---

## Part 2: Repo-level 实验汇总表

### CLS 变体

| 实验 | 模型 | Seed | 服务器 | 状态 | Accuracy | F1_macro | 备注 |
|------|------|------|--------|------|----------|----------|------|
| cls-v1 | Qwen3-4B | 42 | — | failed | — | — | KeyError: sample_weight |
| cls-v2 | Qwen3-4B | 42 | — | failed | — | — | DataCollator bug |
| cls-v3 | Qwen3-4B | 42 | — | failed | — | — | 磁盘满 SIGKILL |
| **cls-v4** | Qwen3-4B | 42 | — | **success** | 66.11% | 56.61 | lr=2e-4 过高，低于 majority baseline |
| **cls-v5** | **Qwen3-4B** | **42** | **home** | **success** | **76.92%** | **73.9** | **anchor 结果，lr=5e-5，+10.8pp vs v4** |
| cls-v5-conda | — | — | — | PREPARING | — | — | conda 环境重跑 |
| cls-8b | Qwen3-8B | 42 | westd | killed | 71.37% | 69.05 | 环境差异（transformers 5.8 vs 4.57），低于4B |
| cls-8b-conda | Qwen3-8B | 42 | — | PREPARING | — | — | conda 环境重跑 |
| cls-seed123 | Qwen3-4B | 123 | westd | killed | — | — | 环境差异，结果无效 |
| cls-seed123-home | Qwen3-4B | 123 | home | RUNNING | — | — | home 服务器重跑，进行中 |

### CWM 变体

| 实验 | 模型 | Seed | 服务器 | 状态 | Accuracy | F1_macro | 备注 |
|------|------|------|--------|------|----------|----------|------|
| cwm-v1~v9 | Qwen3-4B | 42 | various | failed/killed | — | — | 连续失败（bug、OOM、磁盘、PID 冲突） |
| **cwm-v10** | Qwen3-4B | 42 | — | **success** | 69.91% | 46.71 | **eval 无效：93% unparseable（max_new_tokens=64 太短）** |
| cwm-v11 | — | — | — | ANALYZING | 66.6% | 52.99 | subset 500 样本，75.2% unparseable |
| cwm-v12 | Qwen3-4B | 42 | — | RUNNING | — | — | conda 环境重跑 |
| cwm-seed123 | Qwen3-4B | 123 | — | killed | — | — | 环境差异 |
| cwm-seed123-conda | Qwen3-4B | 123 | — | RUNNING | — | — | conda 环境重跑 |

### 有效结果小结

目前只有 **CLS v5** 有可靠的完整评估结果。CLS 8b 因环境差异（transformers 版本不同）结果可能不可信。CWM 尚无有效完整评估（unparseable 率过高）。

---

## Part 3: Planned 实验可行性分析

| 实验 | 优先级 | 依赖 | 状态 | 现在能否开始 |
|------|--------|------|------|-------------|
| oracle-total-validated | P0 | p2p-regression-rate | **DONE** | ✅ 已完成 |
| oracle-f2p-stratified | P0 | mvp-a-oracle-sim | planned | ⚠️ 纯计算，无GPU需求，可立即开始（如果 oracle sim 数据已有） |
| per-test-precision-recall | P0 | mvp-b-train | planned | ⚠️ 需要已训练好的模型做 per-test 预测，CLS v5 checkpoint 可用 |
| cwm-baseline | P0 | mvp-b-train | PREPARING | 🔄 正在准备 |
| multi-seed-core | P0 | cwm-baseline | planned | ❌ 等 cwm-baseline 完成 |
| trace-then-judge | P0 | cwm-baseline | planned | ❌ 等 cwm-baseline，但**代码/数据可以提前准备** |
| traj-level-finetuned | P0 | mvp-b-data-prep | planned | ⚠️ 数据构造可以提前做（按 problem_id 聚合） |
| model-size-scaling | P1 | cwm-baseline | planned | ⚠️ CLS 8b 已在重跑（8b-conda），CWM 8b 等 cwm-baseline |
| **diagnostic-rerepair** | **P1** | cwm-baseline + traj-level | planned | ❌ 需要 repair agent 框架 + 上游结果 |
| swebench-pertest-data | P1 | 无 | planned | ✅ 无依赖，CPU/Docker，可立即开始 |
| llm-judge-baseline | P1 | 无 | planned | ✅ 无依赖，可立即在 westd 上跑 |
| per-test-majority-voting | P2 | mvp-b-train | planned | ⚠️ 需要模型，CLS v5 可用 |
| block-corr-empirical | P2 | mvp-b-train | planned | ⚠️ 需要模型预测数据 |

### 可立即推进的工作

1. **swebench-pertest-data** (P1) — 无依赖，纯 CPU/Docker，应尽早启动（预计 16-24h）
2. **llm-judge-baseline** (P1) — 无依赖，可在 westd 上用 Qwen3-8B/32B 零样本评估
3. **oracle-f2p-stratified** (P0) — 纯计算分析，无 GPU 需求
4. **per-test-precision-recall** (P0) — CLS v5 checkpoint-600 可用于推理
5. **trace-then-judge** — 可提前准备数据格式和训练代码
6. **traj-level-finetuned** — 可提前构造 trajectory-level 数据集

### diagnostic-rerepair (P1) 特别说明

依赖 cwm-baseline + traj-level-finetuned 两个上游实验，且需要集成 SWE-agent 或类似 repair agent 框架。这是工程量最大的实验，建议在 cwm 和 traj-level 结果确认后再正式投入，但可以提前调研 repair agent 接口和 200 个测试实例的选取标准。

---
