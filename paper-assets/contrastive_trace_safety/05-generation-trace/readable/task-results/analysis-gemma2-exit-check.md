# analysis gemma2 exit check

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gemma2_exit_check_20260522T172105_result.json`
- **Structured JSON:** [`eac404bd6c1105bdc5f3.json`](../../sessions/ea/eac404bd6c1105bdc5f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. Gemma-2 实验状态：**SUCCESS**（修复后）
- Phase 1 首次运行即成功（520 traces，2874s）
- Phase 2 首次运行崩溃：随机 split 将所有 6 个 JB trace 分到 train+val，test 里 0 个 JB → `evaluate_layer` 全部返回 None → `best_key` 为 None → TypeError
- **修复**：改为 stratified split，确保 test 有 1 个 JB trace；加 None guard
- Phase 2 重跑成功（213s）

### 2. Trace 数量 + JB/safe 分布
- **520 traces**：6 jailbreak / 514 safe（JB rate = 1.15%）
- JB trace indices: 26, 123, 185, 256, 289, 428
- Gemma-2-9B-it 对 AdvBench 的对齐非常强，只有 6/520 被判定为 jailbreak

### 3. Phase 2 Layer Selection 关键 Metrics

| Metric | Best Layer | Depth | Value |
|--------|-----------|-------|-------|
| CR-composite | **L0** | 0.0% | 0.029 |
| Precision | **L9** | 22.0% | 1.000 |
| Bal. accuracy | **L9** | 22.0% | 1.000 |
| Inv. FPR | **L9** | 22.0% | 0.000 |
| AUROC | **L3** | 7.3% | 1.000 |

**Layer selection bias: REPLICATED** — 22.0pp divergence (CR-composite → L0 vs precision → L9)

⚠️ 注意：test 集只有 1 个 JB trace，metrics 容易 ceiling 到完美值，statistical power 有限。

### 4. Cosine Compression 结果

| 指标 | 值 |
|------|-----|
| Shallow (L0-L5) mean | 0.2373 |
| Deep (L30-L41) mean | 0.3055 |
| **Ratio (shallow/deep)** | **0.7766** |
| **Compression magnitude** | **22.3%** |

**Shallow compression CONFIRMED** — 浅层 step-to-step cosine 变化比深层少 22.3%，与 Qwen 模型的 compression 模式一致。

---
