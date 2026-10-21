# research precheck exp16 17

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_precheck-exp16-17_20260519T142345_result.json`
- **Structured JSON:** [`921487615f468cfd1ce6.json`](../../sessions/92/921487615f468cfd1ce6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 预检报告

### 1. Llama 模型
- **路径**: `/root/autodl-tmp/hf_cache/meta-llama/Llama-3.1-8B-Instruct/` (完整权重 + config.json)
- **HF cache 备份**: `/root/.cache/huggingface/hub/models--meta-llama--Llama-3.1-8B-Instruct`
- **状态**: ✅ 可用

### 2. 磁盘空间
| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| `/`（根） | 30G | 16G | **15G** | 51% |
| `/root/autodl-tmp` | 350G | 91G | **260G** | 26% |

- `data/` 目录: 150MB
- `checkpoints/` 目录: 8.1G
- **结论**: autodl-tmp 空间充足，根分区注意不要再装大包

### 3. 数据生成

**Crescendo 生成脚本（Qwen 版）**:
- `scripts/generate_crescendo.py` — 原版
- `scripts/generate_crescendo_v2.py` — v2
- `scripts/generate_crescendo_transformers.py`
- `scripts/generate_crescendo_part.py`

**Llama 跨 LLM 生成脚本（exp14 已有）**:
- `scripts/generate_dd_llama.py` — Deceptive Delight (Llama)
- `scripts/generate_aa_llama.py` — ActorAttack (Llama)
- `scripts/generate_benign_llama.py` — Benign (Llama)

**数据格式** (JSONL, 每行一个对话):
```json
{
  "conversation_id": "crescendo_0106",
  "turns": [
    {"role": "user", "content": "...", "intended_strategy": 1},
    {"role": "assistant", "content": "..."},
    ...
  ],
  "label": "jailbreak",        // "jailbreak" | "benign"
  "source": "crescendo",        // 标识生成来源
  "attack_type": "persuasion-based",
  "num_turns": 10,
  "strategy_sequence": [1, 1, 3, 3, 7, 5, 5, 5, 5, 5],
  "metadata": {"category": "...", "plain_query": "...", ...}  // 可选
}
```

**现有原始生成数据**:
| 文件 | 行数 |
|------|------|
| `generated/crescendo_all.jsonl` | 250 |
| `generated/deceptive_delight_all.jsonl` | 80 |
| `generated/actorattack_all.jsonl` | 80 |

**现有训练集规模**:
| 数据集 | train | val | test | total |
|--------|-------|-----|------|-------|
| `data/` (root) | 349 | 75 | 76 | **500** |
| `data/final_v2/` | 336 | 71 | 73 | 480 |
| `data/plan_002_splits/` | 350 | 74 | 76 | 500 |

### 4. 训练代码

**Stage 1 — DeBERTa 多任务微调** (`src/train_deberta.py`):
- 参数: `--train_data`, `--val_data`, `--model_name`(默认 deberta-v3-base), `--output_dir`, `--max_length`(256), `--batch_size`(16), `--lr`(2e-5), `--epochs`(5), `--alpha`(0.3), `--seed`, `--use_wandb`
- 任务: 9 类 persuasion strategy + 二分类 jailbreak intent

**Stage 2 — GRU 序列分类器** (`src/train_classifier.py`):
- 参数: `--train_data`, `--val_data`, `--mode`(baseline/treatment), `--deberta_checkpoint`, `--hidden_dim`(256), `--num_layers`(2), `--dropout`(0.3), `--epochs`(20), `--batch_size`(32), `--lr`(1e-3)
- treatment 模式需要 Stage 1 的 checkpoint

**其他训练变体**: `train_deberta_binary.py`, `train_classifier_binary.py`, `train_classifier_meanpool.py`, `train_deberta_mlm.py`, `train_deberta_topic.py`

**评估脚本**: `src/evaluate.py`, `src/eval_early_detection.py`, `scripts/eval_cross_llm.py`, `scripts/eval_cross_llm_control.py`

### 5. exp14 Llama 数据
路径: `data/cross_llm/`
| 文件 | 行数 | 大小 |
|------|------|------|
| `dd_llama.jsonl` | 50 | 1.1MB |
| `aa_llama.jsonl` | 50 | 689KB |
| `benign_llama.jsonl` | 50 | 1.1MB |
| **合计** | **150** | ~2.9MB |

格式与主数据一致，`source` 字段标记为 `llama3.1-8b-deceptive-delight` 等。

### 6. Qwen 模型
| 模型 | 路径 |
|------|------|
| Qwen2.5-7B-Instruct | `/root/autodl-tmp/hf_cache/Qwen/Qwen2.5-7B-Instruct/` |
| **Qwen3-8B** | `/root/autodl-tmp/hf_cache/Qwen/Qwen3-8B/` (5 个 safetensors 分片) |
| Qwen3-30B-A3B | `/root/autodl-tmp/hf_cache/Qwen/Qwen3-30B-A3B/` |

实验 B 追加生成用 **Qwen3-8B**，模型完整可用。

### 7. Python 环境
- Python 3.10.12
- Conda: `/root/miniconda3/bin/pip`
- 关键包: 无法通过 `pip list` 在 read_only 模式查看（被拦截）。从代码 import 推断需要: `torch`, `transformers`, `accelerate`, `wandb`
- 无 `requirements.txt` 文件

---

**两组实验的可行性**:
- **实验 A (Multi-LLM)**: Llama 模型和生成脚本均已就位，exp14 已有 150 条 Llama 数据。需新写 Crescendo-Llama 生成脚本（现有 DD/AA/benign 的 Llama 脚本可参考），然后混合训练
- **实验 B (Dataset Scale)**: Qwen3-8B 已就位，Crescendo 生成脚本已有多个版本可复用，追加 500 条后扩展到 ~1000 条训练集

---
