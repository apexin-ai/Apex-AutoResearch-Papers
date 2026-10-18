# research exp 005 alternatives

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_exp-005-alternatives_20260522T142547_result.json`
- **Structured JSON:** [`7458a3e9aa0333fc31a7.json`](../../sessions/74/7458a3e9aa0333fc31a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。下面写可行性报告。

---

## 可行性报告

### 数据总览

| 目录 | 内容 | 大小 |
|------|------|------|
| `lm_eval_clean/` | 主评估数据（per-example samples） | 4.1GB |
| `results/` | 分析结果 + e4/exp005 数据 | 119MB |
| `models/` | 模型权重（18个模型） | 23GB |

磁盘：16GB/30GB (53%)，剩余空间充足。

### 活跃进程

- **exp005 zoo expansion** 在 tmux session `exp-005` 中运行：正在下载 DeltaNet-h3-1 模型（当前 ModelScope 下载阶段），之后会评估 5 个新架构的 lambada+arc_easy
- GPU 空闲（0% util, 0 MiB mem）

---

### A. BoolQ + WinoGrande Benchmark 扩展

**BoolQ per-example 数据：✅ 已存在**
- 路径：`lm_eval_clean/boolq/{arch}/samples/boolq.jsonl`
- 覆盖：3 架构 (GDN/RetNet/HGRN2) × 5 ratio (pure/h24-1/h12-1/h6-1/h3-1) = **15 个配置全部有**
- 规模：1.3B scale，每文件 3270 样本
- 格式：含 `doc_id`, `resps`（per-choice loglikelihood）, `acc`（per-example correctness）

**WinoGrande per-example 数据：✅ 已存在**
- 路径：`lm_eval_clean/winogrande/{arch}/samples/winogrande.jsonl`
- 覆盖：同上 15 个配置
- 规模：1.3B scale，每文件 1267 样本

**所需工作**：改编现有 `compute_trajectories.py` 脚本（A1 分析），增加 BoolQ/WinoGrande 读取路径。纯计算，**预计 5-10 分钟**完成 Jaccard trajectory 分析。

**补充说明**：HellaSwag (10042样本)、PIQA (1838样本) 的 per-example 数据同样完整（15配置全有），虽已在 A1 中做了 aggregate Jaccard trajectory，但**尚未做 per-example 的 detailed Jaccard 分析**（A1 只产出了 trajectory JSON，未做 per-sample 级分析）。

---

### B. Transformer Baseline Jaccard 对比

**Transformer 模型：✅ 存在** (`models/transformer_340M_baseline/`, 1.3GB)

**Transformer per-example 数据：⚠️ 仅 LAMBADA**
- `exp007/340m/Transformer/samples/lambada_openai.jsonl` — 有
- BoolQ/HellaSwag/WinoGrande/PIQA/ARC-Easy — **无 per-example 数据**
- 仅有 aggregate JSON 结果（`340m/transformer_340M_baseline.json`）

**mvp_logprob 数据**：`results/mvp_logprob/` 中有 `transformer_340M_baseline_depth{1-5}_details.json`，但这是 functional composition 任务的 logprob 数据，不是标准 benchmark 评估。

**所需工作**：
- LAMBADA Jaccard：可直接计算（hybrid vs transformer），**5 分钟**
- 其他 benchmark：需重新跑 `lm_eval --log_samples` for transformer 340M on 5 benchmarks。340M 模型小，估计每 benchmark ~2-5 分钟，**总计 15-25 分钟**
- 注：当前 exp005 占用 tmux 但 GPU 空闲（在下载阶段），需等 exp005 完成或另开评估

---

### C. 已有数据深入分析

**样本字段**（以 BoolQ 为例）：

| 字段 | 说明 |
|------|------|
| `doc_id` | 样本唯一 ID |
| `doc` | 完整题目文本 |
| `target` | 正确答案标签 |
| `resps` | 每个选项的 `[loglikelihood, is_greedy]` |
| `filtered_resps` | 过滤后的 loglikelihood |
| `acc` | 0/1 per-example correctness |
| `doc_hash`, `prompt_hash` | 可做跨模型 matching |

**可做的分析**：

1. **Confidence distribution 分析：✅ 可行**
   - `resps` 含 per-choice loglikelihood → 可算 confidence margin = max_logprob - second_max_logprob
   - 已有 A2 分析的框架代码可复用

2. **Error type 分类：✅ 可行**
   - `acc` 字段 + `doc` 内容 → 可做 helped/hurt/stayed 分类
   - A3 complementarity 已做 UC/MC/mC/UW 四分类，可细化到 per-example 级

3. **跨 benchmark consistency：✅ 可行**
   - 6 个 benchmark 的 per-example 数据全在，doc_id 可跨配置 match
   - 已有 A1 做了 4 benchmark 的 trajectory，加入 BoolQ/WinoGrande 扩展到 6 个

**已完成的分析**（仅限 LAMBADA/HellaSwag/PIQA/ARC-Easy）：
- A1: Cross-benchmark Jaccard trajectory
- A2: Confidence margin prediction (AUC 0.54-0.76)
- A3: Complementarity decomposition (UC/MC/mC/UW)
- E1-E3: Confidence selection, continuous Jaccard, calibration

---

### 可行性排序

| 排名 | 方案 | 已有数据 | 新评估需求 | 预计时间 |
|------|------|----------|------------|----------|
| **1** | **A. BoolQ+WinoGrande Jaccard** | ✅ 15×2 benchmark 完整 per-example 数据 | 零 | **5-10 分钟**（纯脚本） |
| **2** | **C. 已有数据深入分析** | ✅ 6 benchmark × 15 config 全覆盖 | 零 | **20-30 分钟**（新分析脚本） |
| **3** | **B. Transformer baseline Jaccard** | ⚠️ 仅 LAMBADA 有 per-example | 需跑 5 benchmark eval | **30-40 分钟**（含等 GPU+eval+分析） |

**建议优先级**：A → C → B。A 和 C 完全不需要 GPU，可立即执行。B 需要等 exp005 释放 GPU 或在下载间隙插入评估。

---
