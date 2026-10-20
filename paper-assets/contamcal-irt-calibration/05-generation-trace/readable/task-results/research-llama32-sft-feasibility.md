# research llama32 sft feasibility

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_llama32_sft_feasibility_20260517T115107_result.json`
- **Structured JSON:** [`34e719b6cf293da2fb7a.json`](../../sessions/34/34e719b6cf293da2fb7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I have all the data needed. Here's the complete assessment:

## Q1: 模型可用性

**Llama-3.2-3B 已在服务器上，且 SFT 已完成。**

- HF 缓存: `/root/.cache/huggingface/hub/models--meta-llama--Llama-3.2-3B`
- 训练用路径: `/root/autodl-tmp/models/LLM-Research/Llama-3___2-3B`
- 另有 3 个副本（Meta-Llama-3___2-3B、Llama-3.2-3B、unsloth/Llama-3___2-3B）
- **已有全部 4 个 dosage 的 SFT checkpoint**（seed=42, alpha=32, lr=5e-5）:
  - `Llama-3.2-3B_d000_s42` (50K samples)
  - `Llama-3.2-3B_d005_s42`
  - `Llama-3.2-3B_d025_s42` (54K samples)
  - `Llama-3.2-3B_d100_s42` (66K samples)
- 每个 checkpoint 包含 `lora_adapter/` + `merged/`（6.1GB）
- eval 结果和 signals 也已全部跑完

## Q2: SFT 脚本适配

**零改动，已原生支持 Llama。**

`train_sft.py` 关键设计：
- 文件头已声明支持 `Llama-3.2-3B`
- 使用 `AutoModelForCausalLM` / `AutoTokenizer`（模型无关）
- 内置 `LLAMA3_CHAT_TEMPLATE` 作为 fallback（当 tokenizer 无 chat_template 时自动应用）
- LoRA target modules = `[q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj]` — Qwen 和 Llama 的 attention/MLP 层命名一致
- `formatting_func` 用 `tokenizer.apply_chat_template()` 而非硬编码模板
- 已实际成功训练过 Llama（现有 checkpoint 即为证据）

## Q3: 训练时间估计

从现有 Llama 训练的文件时间戳推算：

| Dosage | Samples | Steps (bs=2, accum=8) | 完成时间 |
|--------|---------|----------------------|---------|
| d000 | 50,000 | 3,125 | May 16 20:49 |
| d025 | 54,133 | ~3,383 | May 17 01:28 |
| d100 | 66,533 | ~4,158 | May 17 02:17 |

- d000→d100（含中间 d005, d025）总耗时约 5.5h
- 单 dosage 平均 ~1.5-2h
- 3 dosages (d000+d025+d100) 估计 **5-6h 单卡**
- A6000 48GB 单卡 LoRA SFT 3B 模型完全够用（batch_size=2 + gradient_checkpointing）
- 如果并行在 2 张 GPU 上跑，~3h 可完成

## Q4: Paraphrase 数据

**模型无关，可直接复用。**

- 位置: `/root/autodl-tmp/exp001/paraphrases/`（arc_challenge, gsm8k, humaneval, mmlu）
- 本质是 benchmark 题目的改写（question paraphrasing），不涉及任何模型输出
- `prepare_sft_data.py` 将 paraphrase 转为通用 chat format（`user`/`assistant` 消息对），不含任何 tokenizer/模型依赖
- `data_meta.json` 确认："D010: ALL paraphrases used (no QC filtering)"
- 现有 `sft_dosage_XXX.jsonl` 已同时被 Qwen 和 Llama 共用

## Q5: Signal Pipeline

**已完成适配，无需任何修改。**

- `compute_signals.py` 通过 `--model-path` / `--adapter-path` 接受任意模型
- S1 (embedding): 用 sentence-transformers/all-MiniLM-L6-v2 做 embedding 相似度，与 target 模型无关
- S2 (Min-K++): 用 target 模型和 ref 模型的 token log-prob，通过 AutoModelForCausalLM 加载，模型无关
- S4 (self-critique): 同样用 AutoModelForCausalLM，模型无关
- **已跑完全部 Llama signals**：4 dosages × 3 benchmarks × 3 signals (S1/S2/S4) 全部存在于 `/root/autodl-tmp/exp002/signals/Llama-3.2-3B_d{000,005,025,100}_s42/`

## 总结

- **可行性: 高 — 实际上已经完成了**
- 现有 Llama-3.2-3B 的 d000/d005/d025/d100 (seed=42, alpha=32, lr=5e-5) SFT、eval、signals 全部已完成
- 如果需要的是 **新 seed 的训练**（如 s123），预计准备时间: **0h 代码改动 + 5-6h 训练时间**
- 主要风险: **无** — 基础设施已验证，脚本原生支持，数据可直接复用

---
