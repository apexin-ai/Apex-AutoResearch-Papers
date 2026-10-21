# setup 5090b 32b inference prep

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_5090b_32b_inference_prep_20260520T210456_result.json`
- **Structured JSON:** [`cb7e5941d21faae459ce.json`](../../sessions/cb/cb7e5941d21faae459ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部检查和部署完成。汇报：

---

## 汇报

### 1. 5090-b 环境就绪状态

| 项目 | 状态 |
|------|------|
| GPU | 4× RTX 5090 (32GB) ✓ |
| RAM | 754G (689G 可用) ✓ |
| 磁盘 | 350G 总量, 95G 可用 |
| torch | 2.10.0+cu128, CUDA ✓ |
| vLLM | 0.18.1 ✓ |
| peft | 0.17.1 ✓ |
| transformers | 4.57.1 ✓ |
| accelerate | 1.11.0 ✓ |
| `run_mvp_pilot.py` | 已存在 ✓ |

**环境完全就绪，无需额外安装。**

### 2. 32B base model

5090-b 上**没有** Qwen2.5-32B-Instruct（cache 里只有 7B、72B-AWQ、Qwen3-8B）。如需在 5090-b 做 merge/inference，需下载 ~60GB base model。

### 3. 5090 磁盘能否做 merge

- 5090 磁盘：250G 总量，154G 已用，**97G 可用**
- Merge 产出 ~60G → 剩余 ~37G
- base model 已在 HF cache 中，无需额外下载
- **够用。**

### 4. 建议：在 5090 上做 merge + inference

理由：
- 5090 已有 32B base model 缓存，97G 磁盘够 merge
- 训练完成后 4 卡释放，可直接跑 vLLM inference
- 省去跨机器传输 ~60G merged model 的时间
- 5090-b 作为备选：如果 5090 磁盘不够或出问题，5090-b 环境已就绪，只需下载 base model

### 5. 部署的脚本路径

- **5090**: `/root/autodl-tmp/struct_self_consist_ie/scripts/merge_32b_lora.py` ✓
- **5090-b**: `/root/autodl-tmp/struct_self_consist_ie/scripts/merge_32b_lora.py` ✓

用法：
```bash
cd /root/autodl-tmp/struct_self_consist_ie
python scripts/merge_32b_lora.py checkpoints/qwen25-32b-fewnerd-qlora-s42 checkpoints/qwen25-32b-fewnerd-merged
```

### 训练进度

38000/41180 steps (92.28%)，预计剩余 ~3h，约 08:00 UTC 完成。

---
