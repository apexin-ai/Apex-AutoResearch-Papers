# urgent 70b constraint enforcement audit

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_70b_constraint_enforcement_audit_20260522T045512_result.json`
- **Structured JSON:** [`86e410aaead259e802fe.json`](../../sessions/86/86e410aaead259e802fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计基本完成。以下是完整审计报告。

---

## 审计结论：70B Grammar Enum 约束生效情况

### 1. ZS 70B（已完成）— 约束**真正生效**

**代码路径**：8B 和 70B 使用完全相同的 `run_constrained_extraction.py`，共享同一个约束应用路径：
- 服务器脚本 L546-548：`if mode in ("grammar_only", "full_s1") and compiled_grammar is not None: processors.append(xgr.contrib.hf.LogitsProcessor(compiled_grammar))`
- 服务器脚本 L976：`xgr.TokenizerInfo.from_huggingface(tokenizer, vocab_size=model.config.vocab_size)` → 基于模型实际 vocab_size 构建
- 服务器脚本 L987：`compiled_grammar = xgr_compiler.compile_grammar(grammar)` → JSON schema 中包含 `"type": {"enum": relation_types}`

**AWQ 量化不影响 XGrammar**：AWQ-INT4 只影响模型权重存储/计算，不改变 logits 接口。XGrammar 的 `LogitsProcessor` 在 logits 层面做 token masking，完全独立于模型量化方式。日志显示 `bfloat16 → float16` cast 是 AWQ CUDA kernel 限制，但 logits 仍然正常产出。

**实证数据**（`unified_eval/70b_con.json` vs `70b_unc.json`，DocRED ZS 998 samples）：

| 指标 | Unconstrained | Constrained (full_s1) | Delta |
|------|------|------|------|
| ET_pct | 0.02% | **0.0%** | -0.02 |
| RV_pct | 8.03% (1077) | **0.0%** | **-8.03** |
| DR_pct | 14.98% (2010) | **0.0%** | **-14.98** |
| CF_pct | 0.07% (12) | 5.15% (856) | +5.08 |
| R_F1 | 13.01 | **13.05** | +0.04 |
| E_F1 | 68.96 | 68.96 | 0.0 |

**RV=0% + DR=0%** 是 grammar enum 物理强制的直接证据——unconstrained 有 1077 个 RV violations（模型生成 "country" 而非 ontology 中的 "country"/"country of origin" 等精确映射名），constrained 全部消除。

### 2. LoRA 70B（r16 目录）— **constrained 从未运行**

| 目录 | 内容 |
|------|------|
| `r16_70b_lora_scierc/` | 只有 `scierc_unconstrained.jsonl` + `s1_run.log`（**0 字节**） |
| `r16_70b_lora_docred/` | 只有 `docred_unconstrained.jsonl` + `unconstrained_run.log` |

**s1_run.log 为空**说明 SciERC LoRA 70B constrained 实验从未启动。DocRED LoRA 70B 也只有 unconstrained 输出。当前论文中不应引用不存在的 "70B LoRA constrained" 数据。

### 3. 8B vs 70B 代码路径对比

| 方面 | 8B | 70B |
|------|-----|------|
| 加载方式 | `AutoModelForCausalLM.from_pretrained` (bf16) | 同上，但 AWQ → auto cast to fp16 |
| 约束挂载 | `xgr.contrib.hf.LogitsProcessor(compiled_grammar)` | **完全相同** |
| Schema 构建 | `build_full_schema(entity_types, relation_types)` 带 enum | **完全相同** |
| LoRA | `PeftModel.from_pretrained` (L958-961) | **同一代码路径** |
| VocabTrimProcessor | Qwen3 专用（L558）— 处理 `&lt;/think>` token 越界 | Llama 不需要但不影响（只 mask 超出 vocab_size 的 token） |
| Mode 分叉 | unconstrained=不加 processor, full_s1=加两层 | **完全相同** |

### 4. R-F1=13.05 的来源

- 来自 `unified_eval/70b_con.json`
- 模型：**Meta-Llama-3.1-70B-Instruct-AWQ-INT4**（ZS，非 LoRA）
- 数据集：DocRED dev 998 samples
- Mode：`full_s1`（grammar + semantic 双层约束）
- 评估脚本：`eval_d066_unified.py` 或同等评估器
- 计算方式：strict set matching（tp=1661, pred=13249, gold=12151）

### 5. 关键结论

1. **ZS 70B 的 grammar enum 约束 100% 通过 XGrammar logit masking 物理强制**，不是仅靠 prompt instruction。证据：RV=0%, DR=0%。
2. **AWQ-INT4 量化不影响约束执行**——XGrammar 作用于 logits 层，与权重量化正交。
3. **LoRA 70B constrained 实验尚未完成**——如果论文需要报告 LoRA 70B constrained 数据，需要先跑完实验。
4. **R-F1 几乎无提升（13.01→13.05）**的原因：grammar constraint 消除了 vocabulary 违规，但 ZS 模型的根本瓶颈是不知道该提取哪些关系对，修正 type 名称不解决配对错误。

---
