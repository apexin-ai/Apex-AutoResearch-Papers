# code verify d112 step4 and plan 14b

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify_d112_step4_and_plan_14b_20260519T060322_result.json`
- **Structured JSON:** [`fbb74cbf645c78ed678c.json`](../../sessions/fb/fbb74cbf645c78ed678c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 任务 1: D112 step4_eval.sh 验证结果

**脚本完全正确，无需修复。** 逐项检查：

| 检查项 | 状态 | 值 |
|--------|------|----|
| 文件存在 | ✅ | `/root/autodl-tmp/scripts/d112/step4_eval.sh` |
| `HF_HUB_OFFLINE=1` | ✅ | 已设置 |
| `TRANSFORMERS_OFFLINE=1` | ✅ | 已设置 |
| `HF_HOME=/root/autodl-tmp/.hf_cache` | ✅ | 已设置 |
| 推理命令 | ✅ | `python -m freige.eval.inference` |
| `--model_path` | ✅ | `/root/autodl-tmp/rsft_output_4b_sft_s44` (= step3 的 OUTPUT_DIR) |
| `--sft_adapter` | ✅ | `/root/autodl-tmp/sft_output_seed44` (SFT s44) |
| `--base_model` | ✅ | `/root/autodl-tmp/models/Qwen3-4B` |
| `--data_path` | ✅ | `/root/autodl-tmp/data/docred` (目录，非文件) |
| CUDA_VISIBLE_DEVICES | ✅ | `${GPU:-${CUDA_VISIBLE_DEVICES:-0}}` |

Step3 `output_dir = /root/autodl-tmp/rsft_output_4b_sft_s44`，已有 checkpoint-150 到 checkpoint-350。Step4 的 `--model_path` 指向同一路径，匹配正确。

---

## 任务 2: 14B post-SFT 调研

### 现有资源

| 资源 | 路径/状态 |
|------|-----------|
| 14B base model | `/root/autodl-tmp/models/Qwen/Qwen3-14B` (28GB on disk) |
| 14B SFT output | `/root/autodl-tmp/sft_output_14b/` (checkpoint-48, 训练中) |
| RSFT pipeline 模板 | `/root/autodl-tmp/scripts/d112/step1~step4` (4B 完整流程，直接改路径即可) |

### GPU 当前状态 (全部 RTX 5090, 32GB)

| GPU | 已用 | 备注 |
|-----|------|------|
| 0 | 29.6 GB | 几乎满 |
| 1 | 16.2 GB | 14B SFT 训练中 |
| 2 | 25.2 GB | 14B SFT 训练中 |
| 3 | 27.5 GB | 几乎满 |

### 14B 显存估算

Qwen3-14B bf16 权重 ~28GB，运行时 ~30GB+，**单卡 32GB 放不下 bf16 推理**。

| 步骤 | bf16 | 4-bit 量化 | 建议 |
|------|------|-----------|------|
| Step 1: candidates gen (inference) | 2卡 | 单卡 ~9GB + LoRA ~10-12GB | **单卡 4-bit** |
| Step 2: CED scoring (NLI model) | 单卡 ~1GB | — | **单卡** |
| Step 3: RSFT training (QLoRA) | 2卡 | 单卡 ~14-16GB | **单卡 QLoRA (`--quantize`)** |
| Step 4: D076 eval (inference) | 2卡 | 单卡 ~10-12GB | **单卡 4-bit** |
| Step 5: no-evidence eval | 同上 | 同上 | **单卡 4-bit + `--no_evidence`** |

### 14B Pipeline 准备清单

1. **等 14B SFT 完成** — 目前 cuda:1+2 训练中，完成后释放 2 卡
2. **创建 D112-14B 脚本目录** — 复制 `scripts/d112/` 为 `scripts/d112_14b/`，修改：
   - `BASE_MODEL` → `/root/autodl-tmp/models/Qwen/Qwen3-14B`
   - `SFT_ADAPTER` → `/root/autodl-tmp/sft_output_14b`
   - 所有 output 路径加 `_14b` 后缀
   - Step 1/3/4/5 确保带 `--quantize`（4-bit QLoRA）
   - Step 5 加 `--no_evidence`（C005 约束）
3. **Step 1 candidates gen** — 14B 4-bit 推理 + 8 generations，单卡可跑但比 4B 慢很多。考虑 4 GPU 并行 sharding（SFT 完成后 4 卡全空）
4. **Step 2 CED scoring** — 与模型规模无关（只用 NLI deberta），脚本几乎不用改
5. **Step 3 RSFT training** — QLoRA 单卡可行，LoRA rank 可能需要调整（14B 可考虑 rank 128）
6. **Step 4+5 eval** — 单卡 4-bit，注意 C001（eval 前 nvidia-smi 确认显存空闲）

**最大瓶颈**: Step 1 candidates generation，14B 推理速度比 4B 慢 ~3-4x，4 卡并行 sharding 可大幅缩短时间。

---
