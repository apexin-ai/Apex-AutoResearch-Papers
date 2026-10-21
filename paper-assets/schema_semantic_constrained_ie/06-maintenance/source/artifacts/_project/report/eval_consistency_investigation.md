# Eval 一致性调查报告

## 问题

Table 2 (tab:composability) Llama DocRED Full S1 行的数字与 eval_d064.py 结果不一致：

| 来源 | DR% | CF% | R-F1 | E-F1 |
|------|-----|-----|------|------|
| Table 2 (registry) | 0.20 | 0.26 | 44.23 | 85.23 |
| eval_d064.py (d064_w5 file) | 0.00 | 0.16 | 44.83 | 83.40 |
| eval_d064.py (w5 原始 file) | 0.21 | 0.21 | 43.78 | 83.94 |

## 根因：两个独立问题叠加

### 问题 1：不同 JSONL 文件（不同推理运行）

| 文件 | 位置 | 创建日期 | 大小 | Parse Failures | 服务器 |
|------|------|----------|------|----------------|--------|
| `w5_llama_docred_lora_constrained_eval.jsonl` | `outputs/` on 16980 | May 16 | 9.72MB | 25 (2.5%) | westd-16980 |
| `d064_llama_docred_greedy_constrained_w5.jsonl` | `/root/autodl-tmp/schema_outputs/` on 16980 | May 20 | 9.36MB | 50 (5.0%) | westd-16980 |
| `d064_llama_docred_greedy_constrained.jsonl` | `/root/autodl-tmp/schema_outputs/` on 21461 | May 19 | N/A | 51 (5.1%) | westd-21461 |

三个文件使用 **同一 checkpoint**（w5 LoRA merged on 16980，前两个确定；第三个 registry 注明 "d064 checkpoint kept as internal reference only" 但 eval 结果接近前两个）。

w5 原始运行（25 parse failures）和 d064 重跑（50 parse failures）的差异来源：**d064 使用了不同版本的 run_constrained_extraction.py**（增加了 `decoding_strategy`, `num_beams` 字段），code 版本变化可能改变了 xgrammar 编译、tokenizer padding 或 prompt 格式，导致 greedy decoding 在部分文档上产生不同输出。

### 问题 2：不同 F1 计算方法（Parse Failure 处理不一致）

至少存在三套不同的 eval 逻辑：

| 方法 | Parse Failure 处理 | w5 文件上的 E-F1 | 使用场景 |
|------|-------------------|-----------------|---------|
| **Registry (Table 2)** | **跳过 parse failures（不计入 FN）** | 85.23 (P=85.04, R=85.41) | w5 registry 入库 |
| **analysis_v2.json** | 计入 FN | 84.01 (P=85.04, R=83.0) | violation_checker_docred.py 配套分析 |
| **eval_d064.py** | 计入 FN | 83.94 (P=85.00, R=82.90) | d064 统一评估 |

验证：在 w5 文件上，跳过 parse failures 的方法得到 E-F1=85.15 (P=85.00, R=85.31)，接近 registry 的 85.23（0.08pp 差距来自 registry 脚本的细微差异，不影响结论）。

**关键：Precision 几乎相同（85.00 vs 85.04），Recall 差异来自 parse failure 的 gold entities 是否计入 FN。**

### 跨模型不一致（更严重的问题）

| 模型 | Table 2 E-F1 | Registry 字段名 | 含 parse failures? | Parse Fail Rate |
|------|-------------|----------------|--------------------|----|
| Qwen DocRED | 81.43 | `E_F1` (另有 `E_F1_excl_fail: 85.69`) | **是** | 8.52% |
| Llama DocRED | 85.23 | `entity_f1` (无 `_excl_fail` 版本) | **否**（≈excl_fail） | 2.51% |

**Table 2 在不同模型上使用了不同的 parse failure 处理方式**。Qwen 的 E_F1=81.43 包含了 parse failures 的惩罚，Llama 的 85.23 排除了 parse failures。这导致模型间比较不公平。

## DR% 差异分析

| 文件 | DR% | DR violations | Total relations |
|------|-----|---------------|-----------------|
| w5 原始 | 0.21% | 33 | 16074 |
| d064_w5 | 0.00% | 0 | 14733 |
| d064_21461 | 0.00% | 0 | 14554 |

w5 原始有 33 个 DR violations，d064 重跑 0 个。原因：d064 代码版本的推理输出不同（更多 parse failures → 更少的 relations extracted → 部分 DR-violating 的 relation 未被生成）。

## CF% 差异分析

eval_d064.py 的 CF 计算方式与 registry 不同：
- **eval_d064.py**: CF 基于 **relation 的 head/tail entity**，按 entity text（lowercased）聚合 type，CF violations / total_entities_pred
- **Registry**: CF 基于 **entities + relation 的 head/tail**，CF_rate 分母可能不同

CF 值 (0.26% vs 0.16% vs 0.21%) 差异来自数据差异 + CF 分母/聚合方式差异。

## 建议

### 1. 统一 eval 方法
**推荐方案：parse failures 计入 FN**（eval_d064.py 的方式）。

理由：
- 这是 NLP 文献的标准做法（模型如果无法产生有效输出，应受惩罚）
- 排除 parse failures 会系统性地高估 F1，尤其当不同模型/条件的 parse failure rate 差异大时
- Qwen (8.52%) 和 Llama (2.51%) 的 parse failure rate 差异大，统一方法后更公平

### 2. 统一数据文件
**用 w5 原始文件**（`w5_llama_docred_lora_constrained_eval.jsonl`），不用 d064 重跑文件。

理由：
- w5 原始文件是 Table 2 数据的实际来源
- 25 个 parse failures 更低，说明代码版本更稳定
- d064 重跑文件是不同代码版本的产物，不应作为 w5 的替代

### 3. 需要重新评估的行

用 eval_d064.py（含 parse fail FN）重新评估所有 w5 文件：

| Table 2 行 | JSONL 文件 | 预期变化 |
|------------|-----------|---------|
| Llama DocRED FT Unc | `w5_llama_docred_lora_unconstrained_eval.jsonl` | E-F1 ↓ |
| Llama DocRED FT S1 | `w5_llama_docred_lora_constrained_eval.jsonl` | E-F1: 85.23 → ~83.94 |
| Qwen DocRED FT Unc | `w5_qwen_docred_lora_unconstrained_eval.jsonl` | 可能无变化（已用含 FN） |
| Qwen DocRED FT S1 | `w5_qwen_docred_lora_constrained_eval.jsonl` | 可能无变化（已用含 FN） |

### 4. 更新 eval_d064.py 后用作统一脚本

eval_d064.py 当前逻辑合理，但需确认：
- Entity type normalization 在 F1 matching 中是否需要（当前不 normalize for F1，只 normalize for violations）
- CF 分母是否应该统一（当前用 `total_entities_pred`，与 registry 可能不同）

## 文件路径汇总

| 文件 | 路径 |
|------|------|
| w5 Llama DocRED FT constrained | `westd-16980:/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_constrained_eval.jsonl` |
| w5 Llama DocRED FT unconstrained | `westd-16980:/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_unconstrained_eval.jsonl` |
| d064 Llama greedy constrained (w5 ckpt) | `westd-16980:/root/autodl-tmp/schema_outputs/d064_llama_docred_greedy_constrained_w5.jsonl` |
| d064 Llama greedy constrained (d064 ckpt) | `westd-21461:/root/autodl-tmp/schema_outputs/d064_llama_docred_greedy_constrained.jsonl` |
| eval_d064.py | `westd-16980:/root/schema_semantic_constrained_ie/scripts/eval_d064.py` |
| analysis_v2.json | `westd-16980:/root/schema_semantic_constrained_ie/outputs/analysis_w5_llama_docred_lora_constrained_v2.json` |
| violation_checker_docred.py | `westd-16980:/root/schema_semantic_constrained_ie/violation_checker_docred.py` |
