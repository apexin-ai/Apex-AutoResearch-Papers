# exp mvp phase a

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_mvp_phase_a_20260520T183626_result.json`
- **Structured JSON:** [`8b8eae8760407a1f32c3.json`](../../sessions/8b/8b8eae8760407a1f32c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## MVP Phase A 完整结果

### 1. 推理统计
| 指标 | 值 |
|------|-----|
| 总记录数 | **5,400** (108 条件 × 50 items) |
| 条件数 | **108** |
| 总体准确率 | **0.6557** |
| bfloat16 | 0.6844 (1,800 records) |
| float16 | 0.6833 (1,800 records) |
| float32 | 0.5994 (1,800 records) |

**注意**: float32 准确率显著低于 bf16/fp16（~8.5pp 差距）。float32 使用了 V0 引擎（`enforce_eager`，无 CUDA graph）因为 V1 引擎的 torch.compile 对 float32 触发 `InductorError: PassManager::run failed`。这个引擎差异本身可能引入方差。

### 2. 方差分量排名（占总方差 %）

| 排名 | 分量 | 估计值 | % 总方差 | 95% CI |
|------|------|--------|----------|--------|
| 1 | **item_id** | 0.1343 | **58.44%** | [0.0885, 0.1736] |
| 2 | **residual** | 0.0404 | **17.59%** | [0.0279, 0.0527] |
| 3 | **precision:item_id** | 0.0166 | **7.24%** | [0.0097, 0.0247] |
| 4 | **temperature:item_id** | 0.0157 | **6.85%** | [0.0042, 0.0294] |
| 5 | **prompt_template:item_id** | 0.0132 | **5.73%** | [0.0061, 0.0225] |
| 6 | **seed:item_id** | 0.0062 | **2.70%** | [0.0020, 0.0108] |
| 7 | **precision** | 0.0020 | **0.87%** | [0.0, 0.0069] |
| 8 | ordering:item_id | 0.0010 | 0.44% | [0.0001, 0.0022] |
| 其他 | (所有交互项) | < 0.0001 | < 0.04% | — |

### 3. 关键交互项

| 交互项 | 估计值 | % 总方差 | CI 含零? |
|--------|--------|----------|---------|
| precision × prompt_template | 4.50e-5 | 0.020% | CI 含零 |
| precision × seed | 0.0 | 0.0% | CI 含零 |
| precision × temperature | 3.84e-6 | 0.002% | CI 含零 |
| precision × item_id | **0.0166** | **7.24%** | **CI 不含零** |

**方法论层面的 precision × methodology 交互极小**。但 **precision × item_id 交互占 7.24%**——说明不同精度对不同题目的影响不同（某些题目对精度更敏感）。

### 4. D-study

| 指标 | 值 |
|------|-----|
| 当前 G 系数 | **0.357** |
| 达到 G≥0.90 | **不可达**（所有 facet sweep 到 n=20 仍远低于 0.90） |
| 达到 G≥0.95 | 不可达 |
| 达到 G≥0.99 | 不可达 |

G 系数极低的原因：**item_id 方差占 58.4%**，它是实验的对象（object of measurement），代表的是不同测试题目的内在难度差异。这导致条件间的方差信号很弱（σ²_τ = 0.002），相对于误差（σ²_δ = 0.004）。

关键发现：**增加 item 数量是提升 G 系数的唯一有效途径**（从 n=50 到 n=200 时 G ≈ 0.184，仍远不够）。这说明当前实验设计中，方法论变量（prompt template, seed, ordering）引入的方差极小，绝大部分方差来自 item 难度差异和残差。

### 5. Pass/Fail 判定

| 标准 | 结果 |
|------|------|
| (a) Pipeline 完整运行 | **PASS** — 108 条件全部完成，5400 条记录 |
| (b) ≥2 分量占总方差 ≥5% 或 CI 不含零 | **PASS** — item_id (58.4%), residual (17.6%), precision:item_id (7.2%), temperature:item_id (6.9%), prompt_template:item_id (5.7%) |
| (c) ≥1 precision×methodology 交互显著 | **PARTIAL** — precision×methodology 直接交互极小（<0.02%），但 precision×item_id (7.24%, CI 不含零) 显著 |

### 产出文件
- `results/all_results.jsonl` (5,400 行)
- `results/variance_components.json`
- `results/d_study_results.json`
- `results/figures/variance_components.png`
- `results/figures/interaction_heatmap.png`
- `results/figures/d_study_curves.png`

### 技术问题记录
- float32 + vLLM V1 引擎触发 `InductorError: PassManager::run failed`，回退到 V0 引擎 (`VLLM_USE_V1=0`) 解决
- float32 推理速度约为 bf16/fp16 的 1/30（每 batch 10s vs 0.3s）
- float32 准确率显著偏低（0.60 vs 0.68），可能与 V0/V1 引擎差异或精度本身有关

---
