# infra model prep gemma qwen w17

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_model_prep_gemma_qwen_w17_20260518T173632_result.json`
- **Structured JSON:** [`28d3ab9ba5dd96c43b72.json`](../../sessions/28/28d3ab9ba5dd96c43b72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个模型都已下载完成。现在汇总报告。

## 报告

### 1. 下载状态

| 模型 | 状态 | 大小 | Token 需求 |
|------|------|------|-----------|
| google/gemma-4-E2B | **成功** | 9.6GB (model.safetensors) | 不需要（无 gated 限制） |
| Qwen/Qwen3.5-0.8B-Base | **成功** | 1.7GB (model.safetensors) | 不需要 |

### 2. 磁盘空间
- 下载前：325GB 可用
- 下载后：306GB 可用（使用 19GB，含 .cache）

### 3. 脚本兼容性 - **两个模型都有严重兼容性问题**

**核心问题：两个模型都是多模态模型，不是纯文本 CausalLM。**

**Gemma 4 E2B:**
- 架构：`Gemma4ForConditionalGeneration`（vision + audio + text）
- `model_type: "gemma4"` → `AutoModelForCausalLM` 映射到 `Gemma4ForConditionalGeneration`（不是 CausalLM）
- 包含 vision encoder（16 层）、audio encoder（12 层）、text backbone（35 层）
- vocab_size: 262,144（vs Pythia 50,304）
- 实际参数量远超 2B（9.6GB in bf16 ≈ ~4.8B params）
- **不兼容 iterative_train.py**：AutoModelForCausalLM 会加载整个多模态模型，forward/generate 调用方式不匹配

**Qwen3.5-0.8B-Base:**
- 架构：`Qwen3_5ForConditionalGeneration`（vision + text）
- `model_type: "qwen3_5"` → `AutoModelForCausalLM` 映射到 `Qwen3_5ForCausalLM`
- **这个可能部分兼容**：mapping 直接指向 CausalLM 类，但权重文件包含 vision encoder，加载时会有 unexpected keys 警告
- vocab_size: 248,320
- 使用 linear_attention + full_attention 混合层（非标准 transformer）

**训练脚本本身（iterative_train.py）没有硬编码参数：**
- 使用 `AutoModelForCausalLM` + `AutoTokenizer`（通用加载）
- pad_token 处理：`tokenizer.pad_token = tokenizer.eos_token`（通用兼容）
- `--bf16` 支持已就绪
- 无模型特定条件分支
- transformers 5.8.1 已安装（满足版本要求）

### 4. 需要的修改列表

1. **Gemma 4 E2B 不可直接用**：
   - 方案 A：用 `Gemma4ForCausalLM` + `Gemma4TextConfig` 只加载 text backbone（需要从多模态权重中提取 text 部分）
   - 方案 B：换用纯文本版本 `google/gemma-3-1b-pt` 或 `google/gemma-2-2b`
   
2. **Qwen3.5-0.8B-Base 可能可以用但需验证**：
   - `AutoModelForCausalLM` mapping 指向 `Qwen3_5ForCausalLM`，有可能只加载 text 部分
   - 需要实测 `AutoModelForCausalLM.from_pretrained` 是否能正常加载并 generate
   - linear_attention 层可能影响训练行为（非标准 transformer）

3. **如果要用这两个模型**，建议先在服务器上做快速加载测试确认能否 `model.generate()` 正常工作

---
