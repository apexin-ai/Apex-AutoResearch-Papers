# research qwen3 14b feasibility

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_qwen3_14b_feasibility_20260518T100058_result.json`
- **Structured JSON:** [`59331ea9334e2cf6b528.json`](../../sessions/59/59331ea9334e2cf6b528.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== Qwen3-14B 可行性报告 ===

模型: Qwen/Qwen3-14B / 14.8B params (13.2B non-embedding) / bf16 ~29.5GB

架构:
  hidden_size: 5120
  num_layers: 40
  num_attention_heads: 40 (Q), 8 (KV, GQA)
  intermediate_size: 17408
  vocab_size: 151936
  head_dim: 128

─────────────────────────────────────────────

LoRA 参数量估算 (rank=64, 7 target modules per layer):
  q_proj:    (5120+5120)×64  = 655K
  k_proj:    (5120+1024)×64  = 393K
  v_proj:    (5120+1024)×64  = 393K
  o_proj:    (5120+5120)×64  = 655K
  gate_proj: (5120+17408)×64 = 1442K
  up_proj:   (5120+17408)×64 = 1442K
  down_proj: (17408+5120)×64 = 1442K
  ──────────────────────────────
  Per layer: 6.42M → 40 layers → ~257M LoRA params

─────────────────────────────────────────────

显存估算 1: bf16 LoRA (不量化)
  Base model (bf16):     14.8B × 2B = 29.6 GB
  LoRA adapters (bf16):  257M × 2B  = 0.5 GB
  Optimizer (fp32, AdamW): 257M × 12B = 3.1 GB
  Gradients (bf16):      257M × 2B  = 0.5 GB
  Activations (GC, bs=1, seq=4096): ~3-5 GB
  CUDA overhead:         ~1 GB
  ──────────────────────────────
  总计: ~38-40 GB
  32GB 单卡: ❌ 不可行 (模型权重本身已 29.6GB，几乎填满显存)

─────────────────────────────────────────────

显存估算 2: QLoRA 4-bit (NF4)
  Base model (4-bit):    14.8B × 0.5B = 7.4 GB
  量化 overhead:         ~0.5 GB
  LoRA adapters (bf16):  257M × 2B   = 0.5 GB
  Optimizer (fp32, AdamW): 257M × 12B = 3.1 GB
  Gradients (bf16):      257M × 2B   = 0.5 GB
  Activations (GC, bs=1, seq=4096): ~3-5 GB
  CUDA overhead:         ~1 GB
  ──────────────────────────────
  总计: ~16-18 GB
  32GB 单卡: ✅ 可行，余量充足 (~14GB headroom)

  可尝试 bs=2: 额外 ~3-4 GB activations → ~20-22 GB，仍可行

─────────────────────────────────────────────

Gradient Checkpointing 影响:
  关闭: activations 可达 10-15 GB (bs=1, seq=4096, 40 layers)
  开启: 降至 ~3-5 GB (只存层边界 activations，重算中间值)
  代价: 训练速度慢 ~30%
  QLoRA 场景下必须开启（已是项目默认配置）

─────────────────────────────────────────────

推荐配置:
  量化: QLoRA 4-bit (NF4, double_quant=True)
  batch_size: 1-2 (per_device)
  gradient_accumulation: 8 (有效 bs=8-16)
  gradient_checkpointing: True
  LoRA: rank=64, alpha=128 (与现有配置一致)
  precision: bf16 compute dtype
  flash_attention: 开启 (attn_implementation="flash_attention_2")

─────────────────────────────────────────────

预估训练时间:
  参考: Qwen3-8B bf16 LoRA, 3018 samples, 3 epochs, 1134 steps
  14B vs 8B: ~1.8x FLOPs (层数 40 vs 36, hidden 5120 vs 4096)
  QLoRA 额外开销: dequant ~10-15%, GC recompute ~30%
  综合: 每 step 约 2-2.5x 慢于 8B bf16 LoRA

  SFT (3000 samples, 3 epochs, ~1125 steps):  ~3-5h
  RSFT (3000 samples, 3 epochs, ~1125 steps): ~3-5h
  (实际取决于 seq_len 分布，DocRED 样本较短则更快)

─────────────────────────────────────────────

与现有 pipeline 兼容性:
  ✅ TRL SFTTrainer + PEFT LoRA: 完全兼容，同架构家族
  ✅ target_modules 名称一致: q/k/v/o_proj, gate/up/down_proj
  ✅ BitsAndBytesConfig 4-bit: 直接可用
  ✅ tokenizer/chat_template: Qwen3 系列通用
  ✅ 单卡训练: QLoRA 无需 model parallelism
  ✅ 代码改动: 只需改 model_name 路径
  ⚠️ 建议加 attn_implementation="flash_attention_2" 省显存+加速

─────────────────────────────────────────────

风险/注意事项:
  1. bf16 LoRA 不可行，必须用 QLoRA 4-bit
  2. 4-bit 量化会引入精度损失，可能影响 IE 任务细粒度输出质量
     → 需要实验验证 14B-QLoRA vs 8B-bf16 的质量权衡
  3. 推理/eval 同样需要 QLoRA 加载，单卡 ~8-9GB
     → eval 不会有显存压力 (C001 约束仍应遵守)
  4. 模型下载: bf16 safetensors ~29.5GB，需确认服务器磁盘空间
  5. Qwen3-14B 的 thinking mode (&lt;/think> tokens) 需在训练数据中处理
     → 建议用 chat_template 的 enable_thinking=False
```

---
