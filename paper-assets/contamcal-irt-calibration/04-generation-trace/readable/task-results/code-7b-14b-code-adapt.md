# code 7b 14b code adapt

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_7b-14b-code-adapt_20260518T061857_result.json`
- **Structured JSON:** [`d15ed650b1196203481d.json`](../../sessions/d1/d15ed650b1196203481d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 总结

### 代码兼容性：全部通过，无需修改 Python 代码

| 文件 | 状态 | 说明 |
|------|------|------|
| `prepare_sft_data.py` | ✅ 兼容 | 无模型依赖，输出通用 chat JSONL |
| `train_sft.py` | ✅ 兼容 | model-name/LoRA/batch/GC 全部参数化，target_modules 通用 |
| `evaluate.py` | ✅ 兼容 | `device_map="auto"`，chat template 有 Llama fallback |
| `exp002/signal_*.py` | ✅ 兼容 | `device_map="auto"`，无模型特定逻辑 |
| `train_and_eval.sh` | ✅ 兼容 | 透传所有参数 |

### 新增文件（4 个配置文件）

- `configs/qwen25_14b.yaml` — bs=1, accum=16, GC=true (~50GB VRAM)
- `configs/llama31_8b.yaml` — bs=2, accum=8, GC=true (~30GB VRAM)
- `configs/run_14b_example.sh` — 14B 训练命令示例
- `configs/run_llama31_8b_example.sh` — Llama-3.1-8B 训练命令示例

### 推荐配置

所有模型统一：**LoRA r=16, alpha=32, lr=5e-5, effective_bs=16, GC=true, seq=2048, 1 epoch**。与现有 ≤3B 实验保持一致（C006 要求 alpha=32）。

### 注意事项

- **14B 是最紧的**：~50GB on 80GB，留 30GB headroom。若 OOM 可降 max_seq_length 到 1024
- **Llama-3.1-8B** base 模型无内置 chat template，代码已有 fallback 处理
- **4× A100 策略**：4 个独立单卡 job 并行（每卡跑不同 model/dosage/seed），无需多卡数据并行

---
