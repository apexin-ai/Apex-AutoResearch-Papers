# debug fp32 accuracy investigation

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_fp32_accuracy_investigation_20260520T190333_result.json`
- **Structured JSON:** [`a45ece5ffdef2a406e5e.json`](../../sessions/a4/a45ece5ffdef2a406e5e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整报告。

---

## FP32 准确率异常调查报告

### 1. BF16 vs FP32 逐 item 对比（5 个样本）

| Item | BF16 pred | FP32 pred | Gold | BF16✓ | FP32✓ |
|------|-----------|-----------|------|-------|-------|
| abstract_algebra_14 | D | D | C | ✗ | ✗ |
| abstract_algebra_3 | D | D | B | ✗ | ✗ |
| abstract_algebra_35 | B | B | B | ✓ | ✓ |
| abstract_algebra_81 | A | A | D | ✗ | ✗ |
| abstract_algebra_94 | A | D | D | ✗ | ✓ |

两种精度的生成文本在答案字母后立即分叉（不同的续写内容），说明 logit 分布确实不同。

### 2. FP32 错误 pattern

**整体统计：**
- bfloat16: 1232/1800 correct (68.4%), 0 extraction failures
- float16: 1230/1800 correct (68.3%), 0 extraction failures
- float32: 1079/1800 correct (59.9%), 0 extraction failures

**Extraction failure 不是原因** — 三种精度都为零。差异来自模型本身给出不同答案。

**Pairwise 对比（1800 对完全匹配的条件）：**
- Both correct: 1005 (55.8%)
- Both wrong: 494 (27.4%)
- BF16✓ FP32✗: **227 (12.6%)**
- FP32✓ BF16✗: 74 (4.1%)

净差：FP32 比 BF16 多错 153 个 = 8.5pp gap。

**Subject 分解：**

| Subject | BF16 | FP32 | Gap |
|---------|------|------|-----|
| abstract_algebra | 30.6% | 30.3% | +0.3pp |
| college_physics | 51.1% | 48.9% | +2.2pp |
| world_religions | 88.9% | 81.1% | +7.8pp |
| us_foreign_policy | 97.5% | 85.3% | **+12.2pp** |
| professional_medicine | 74.2% | 54.2% | **+20.0pp** |

差距高度不均匀 — 集中在 professional_medicine 和 us_foreign_policy。

**答案分布偏移：**

| Answer | BF16 | FP32 | Δ |
|--------|------|------|---|
| A | 444 | 482 | +38 |
| B | 400 | **488** | **+88** |
| C | 481 | 442 | -39 |
| D | 475 | **388** | **-87** |

FP32 系统性地 **D→B 偏移**。Gold 中 D=504 是最常见答案，FP32 严重 under-predict D。

当 BF16✓ FP32✗ 时，FP32 的预测分布：A=105, B=50, C=37, D=35 — 偏向 A。

该 pattern 在所有实验条件（seed/template/ordering/temperature）下都稳定复现。

### 3. vllm_runner.py 处理方式

```python
# vllm_runner.py:66-74
self.llm = LLM(
    model=model_name,
    dtype=dtype,           # "float32" 直接传入
    seed=seed,
    tensor_parallel_size=1,
    gpu_memory_utilization=0.90,
    trust_remote_code=True,
    max_model_len=4096,
    enforce_eager=(dtype == "float32"),  # ← 仅 FP32 为 True
)
```

- `dtype="float32"` 直接传给 vLLM，无误转
- `enforce_eager=True` **仅对 float32 开启**，BF16/FP16 为 False

### 4. V0 vs V1 引擎证据

**vLLM 版本：0.9.2**

在 0.9.x 中，V1 是默认引擎。但 FP32 被强制使用不同路径：

1. **`enforce_eager=True`** → 禁用 CUDA graphs，使用 eager 模式
2. **FlashAttention 不支持 float32** → fallback 到 PyTorch SDPA 或 xformers eager attention
3. Step 4 的报错堆栈显示 float32 走的是 `vllm/engine/llm_engine.py`（V0 引擎路径），而非 V1 的 async engine

**两个因素交织：**
- 精度差异（float32 vs bfloat16）
- 引擎差异（V0/eager attention vs V1/FlashAttention + CUDA graphs）

### 5. 结论

**不是 pipeline bug。** 这是 `enforce_eager=True` + float32 attention 后端差异导致的真实效应。

证据链：
- 0 extraction failures，答案解析逻辑没有问题
- 系统性的 D→B 答案偏移，在所有条件下稳定复现
- 差距高度 subject-dependent（abstract_algebra 几乎无差，professional_medicine 差 20pp），符合"不同 logit 分布"而非"随机噪声"
- BF16 和 FP16 结果几乎一致（68.4% vs 68.3%），说明 16-bit 精度不是问题，差异来自 FP32 的特殊代码路径

**核心问题：precision 和 engine 的混淆（confound）。** 当前设计中 float32 同时改变了两个因素：
1. 数值精度（float32 vs bfloat16）
2. 推理引擎（enforce_eager/V0/no-FlashAttention vs V1/FlashAttention）

**建议**：跑一组 `bfloat16 + enforce_eager=True` 来解耦这两个因素。如果 BF16+eager 也出现类似下降，则确认 engine 是主因；如果不下降，则是 float32 + eager attention 的交互效应。

---
