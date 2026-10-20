# research finetuned feasibility

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_finetuned_feasibility_20260515T140316_result.json`
- **Structured JSON:** [`432667a90a70d83b0ba5.json`](../../sessions/43/432667a90a70d83b0ba5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个调研全部完成。汇总报告如下。

---

## Fine-tuned Model 实验可行性调研报告

### 方案 A: GoLLIE (ICLR 2024)

**架构**: Code-LLaMA 2 + LoRA, 7B/13B/34B

**核心问题 — 输出格式不兼容**:
GoLLIE 输出是 **Python dataclass 实例化代码**，不是 JSON：
```python
result = [
    Mission(mention='Ares 3', date='2032', destination='Mars'),
]
```
Schema 定义用 Python `@dataclass` + docstring，解析靠 `exec()` 执行。

**与 OntoCoDec 的兼容性**:
- XGrammar 的 EBNF 专为 JSON 设计，无法约束 Python 代码输出
- 要适配需要：(a) 改 GoLLIE 输出为 JSON（需重训），或 (b) 写 Python 代码 EBNF（极复杂），或 (c) 放弃 constrained decoding 只做 post-hoc 对比（失去论文核心贡献的验证意义）

**SciERC 支持**: GoLLIE 原论文**不含 SciERC 评估**，也没有 zero-shot RE 结果。需自行写 SciERC schema 定义并跑实验。

**结论**: ❌ 不推荐。改造成本极高，且无法直接验证 OntoCoDec 的 composability。

---

### 方案 B: LoRA 微调 Qwen3-8B

**数据量**:
- SciERC training set: **350 docs, ~1750 sentences, 5598 entities, 3219 relations**
- 每条训练样本 = 一个 sentence → 用现有 `SCIERC_SYSTEM` + `SCIERC_USER_TEMPLATE` prompt，gold answer 为 JSON `{"entities": [...], "relations": [...]}`
- 数据格式转换：直接复用 `load_scierc_data()` 函数逻辑，~50 行脚本

**GPU 成本**:
- 模型：Qwen3-8B（已下载 `/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B`）
- GPU：2× RTX PRO 6000 Blackwell (94GB)
- bf16 全精度 + LoRA rank=16 → 模型 ~16GB + LoRA ~50MB，94GB 绰绰有余
- QLoRA 不必要（VRAM 充足），但可选用以加速
- **预估训练时间：~30-60 分钟**（1750 samples × 2 epochs, batch size 4, gradient accumulation 4）

**实施复杂度**:
1. **数据转换脚本** (~50 行): SciERC JSONL → chat format `[{"role":"system",...}, {"role":"user",...}, {"role":"assistant", "content": gold_json}]`
2. **训练脚本** (~80 行): TRL `SFTTrainer` + LoRA config, 标准流程
3. **推理**: 加载 base model + LoRA adapter → 直接用现有 `run_constrained_extraction.py`，**零代码修改**（OntoCoDec 通过 `AutoModelForCausalLM` + `LogitsProcessorList` 对接，与是否有 LoRA adapter 无关）

**论文价值**:
- **直接回应审稿**: "OntoCoDec works with fine-tuned models, not just zero-shot"
- **预期效果**: R-F1 从 ~8% (zero-shot) → ~25-35% (fine-tuned), violation rate 下降但非零 → OntoCoDec 仍有额外约束价值
- 可展示：fine-tuned unconstrained vs fine-tuned + OntoCoDec → 增量改进仍显著
- **最强论点**: 同一模型(Qwen3-8B) zero-shot vs fine-tuned 对比，变量控制最干净

---

### 方案 C: 现有 Supervised IE Baselines

**SciERC RE SOTA**:

| 方法 | 年份 | Rel F1 | Rel+ F1 | Checkpoint? |
|------|------|--------|---------|-------------|
| **HGERE** | EMNLP 2023 | 55.72 | **43.60** | ❌ 需重训 |
| **PL-Marker** | ACL 2022 | 53.25 | 41.62 | ✅ Google Drive |
| **PURE** | NAACL 2021 | 48.65 | 35.68 | ✅ 直接下载 |
| **ITER** | EMNLP 2024 | — | 39.36 | ✅ HuggingFace |
| **DyGIE++** | EMNLP 2019 | ~48 | — | ✅ 脚本下载 |

**核心问题**: 这些全是 **encoder-only / task-specific 模型**（SciBERT/DeBERTa based），不是 autoregressive LLM：
- XGrammar 和 TypeConstraintProcessor 只能用于 autoregressive decoding
- 无法对这些模型施加 OntoCoDec 约束
- **只能作为 F1 baseline 参考**，不能验证 "OntoCoDec composability with fine-tuned models"

**可行用途**: 在论文 Table 中加一行 "Supervised SOTA (PL-Marker)" 作为 F1 上界参考，展示 fine-tuned LLM + OntoCoDec 与传统 supervised 方法的差距正在缩小。

---

### 决策矩阵

| 维度 | GoLLIE (A) | LoRA Qwen3-8B (B) | Supervised (C) |
|------|-----------|-------------------|---------------|
| **可行性** (1-5) | 2 | **5** | 3 |
| **GPU 成本** (hours) | ~2-3h (推理) | **~1h** (训练+推理) | ~0.5h (推理) |
| **实施时间** (天) | 3-5 天 | **1-1.5 天** | 1-2 天 |
| **代码修改量** | 大量（grammar改写） | **最小**（新增2个脚本） | 中等（环境适配） |
| **论文提升力度** | 中（不同模型） | **强**（同模型对比） | 弱（不验证OntoCoDec） |
| **风险** | 高（格式不兼容） | **低** | 中（checkpoint兼容性） |
| **推荐** | ❌ | ✅ **首选** | ⚠️ 可选补充 |

---

### 推荐：方案 B (LoRA 微调 Qwen3-8B)

**理由**:
1. 唯一能直接验证 "OntoCoDec works with fine-tuned models" 的方案
2. 实施最快（~1天），风险最低（复用全部现有代码）
3. 实验设计最干净：同模型 zero-shot vs fine-tuned，唯一变量是 SFT
4. 论文新增一行表格即可展示

**可选追加**: 同时在论文 Table 中引用 PL-Marker (Rel+ F1 41.62) 作为 supervised SOTA 参考线（不需跑实验，直接引用论文数字）。

---

### 方案 B 实施计划 (Step-by-Step)

**Day 1 上午 (~3h)**:

1. **数据准备脚本** `prepare_sft_data.py`:
   - 读取 `data/processed_data/train.json`（350 docs）
   - 用 `load_scierc_data()` 拆分为 ~1750 sentence-level 样本
   - 每条转为 chat 格式: system prompt + user prompt + assistant gold JSON
   - 输出 `data/sft_train.jsonl` + `data/sft_val.jsonl`（从 dev split）

2. **训练脚本** `train_lora.py`:
   ```
   - Base model: /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B
   - LoRA: rank=16, alpha=32, target_modules=["q_proj","v_proj","k_proj","o_proj"]
   - Training: 2 epochs, lr=2e-4, bf16, batch_size=4, grad_accum=4
   - Save: /root/autodl-tmp/models/qwen3-8b-scierc-lora/
   ```

3. **启动训练** (~30-60 min)

**Day 1 下午 (~2h)**:

4. **推理**: 修改 `run_constrained_extraction.py` 的 model path 参数，加载 base + LoRA adapter
   - 跑 4 个 mode: unconstrained, grammar_only, full_s1, full_s2
   - 测试集: 100 docs (test split)

5. **评估**:
   - 用现有 `violation_checker.py` + `unified_f1_eval.py` 计算 violation rate + F1
   - 用现有 `compute_bootstrap_ci.py` 算置信区间

6. **结果整理**: 更新论文 Table，新增 "Fine-tuned Qwen3-8B" 行

---
