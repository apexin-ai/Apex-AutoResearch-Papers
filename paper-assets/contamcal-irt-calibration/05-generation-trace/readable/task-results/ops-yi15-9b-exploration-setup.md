# ops yi15 9b exploration setup

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_yi15-9b-exploration-setup_20260522T122453_result.json`
- **Structured JSON:** [`25240b1506aa3d0ca24f.json`](../../sessions/25/25240b1506aa3d0ca24f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

磁盘仅剩2.3GB，较紧张但LoRA checkpoint较小（~300-400MB/个），暂时够用。

---

## Yi-1.5-9B 探路实验报告

### 1. 模型信息
| 项目 | 值 |
|------|-----|
| 模型路径 | `/root/autodl-tmp/.hf_cache/Yi-1.5-9B` |
| 架构 | `LlamaForCausalLM` (model_type=llama) |
| 参数 | 48层, hidden=4096, GQA (32 heads, 4 KV heads), vocab=64000 |
| 大小 | ~16.4GB (4 safetensor shards) |
| 来源 | hf-mirror.com (aria2c 16连接, ~10-16 MB/s) |

### 2. Tokenizer & Chat Template
| 项目 | 值 |
|------|-----|
| Tokenizer类 | LlamaTokenizerFast |
| Chat template | 原始无 → 自动设置 **ChatML** (`<|im_start|>`/`<|im_end|>`) |
| 特殊token | `<|im_start|>`=6, `<|im_end|>`=7 (已在词表中) |
| 兼容性 | ✅ train_sft.py fallback 逻辑正确匹配 ChatML |

### 3. SFT 数据确认
| 项目 | 值 |
|------|-----|
| 路径 | `/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl` |
| 样本数 | 50,000 |
| 格式 | messages (system/user/assistant) ✅ |

### 4. Dry-run 结果
| 项目 | 值 |
|------|-----|
| 状态 | ✅ 成功（跑了18步无报错） |
| Tokenization | 50k样本, ~30s, ~1675 examples/s |
| 步速 | ~3.5-4.5 s/step |
| 已知warnings | vocab holes [3,4,5,9-13] (Yi tokenizer正常); 部分序列>4096 tokens (被max_length截断) |

### 5. 正式训练 (d000)
| 项目 | 值 |
|------|-----|
| tmux session | `yi15_d000` |
| PID | **636899** |
| GPU | 0 (CUDA_VISIBLE_DEVICES=0), 46651 MiB |
| 日志 | `/root/autodl-tmp/exp001/checkpoints/yi15_9b_d000_s42.log` |
| 输出目录 | `/root/autodl-tmp/exp001/checkpoints/Yi-1.5-9B_d000_s42` |
| LoRA | r=16, alpha=32, targets=q/k/v/o/gate/up/down_proj |
| 训练参数 | bs=4, grad_accum=4 (effective 16), lr=5e-5, 1 epoch, gradient-checkpointing |
| 总步数 | 3125 |
| 步速 | ~4.3 s/step |
| 预估时间 | **~3.7 小时** (~24:45 完成) |

### ⚠️ 风险提示
- 数据盘仅剩 **2.3GB**，LoRA checkpoint ~300-400MB/个，如果 Trainer 默认保存多个 checkpoint 可能爆盘。建议关注 `save_total_limit` 设置或在训练中清理旧 checkpoint。

---
