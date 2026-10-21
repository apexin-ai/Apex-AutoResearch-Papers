# code accumulation v3 script only

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_accumulation_v3_script_only_20260519T075454_result.json`
- **Structured JSON:** [`fc8353fe58600af50f30.json`](../../sessions/fc/fc8353fe58600af50f30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**脚本**: `/root/autodl-tmp/recursive_gen_depth_est/scripts/run_accumulation.py` (320行, 已写入远程服务器)

**报告**: `artifacts/accumulation_v3/script_review.md`

核心逻辑:
- 每个 depth: 混合 human text + 前一 depth 生成文本 → LoRA 微调 base GPT-2 XL (GPU) → BOS 无条件生成 (GPU) → 更新 synthetic 源
- d1 的 synthetic 来源: 现有 full-replacement `depth_1.jsonl`; d2 用 d1 accumulation 生成文本; d3 用 d2 的
- 所有 LoRA 训练和生成通过 subprocess 调用现有 `lora_finetune.py` / `generate_next_depth.py`
- 参数完全复用现有 pipeline: r=16, alpha=32, lr=2e-4, epochs=3, nucleus p=0.95

**运行命令** (未执行):
```bash
python scripts/run_accumulation.py --mix_ratio 0.5 --gpu_id 0 --seed 42   # ~6h
python scripts/run_accumulation.py --mix_ratio 0.25 --gpu_id 1 --seed 42  # 可并行
```

---
