# sync pi05 model to cqa1 32758

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_sync_pi05-model-to-cqa1-32758_20260525T084010_result.json`
- **Structured JSON:** [`7ce994cc757900badc0a.json`](../../sessions/7c/7ce994cc757900badc0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有验证通过。

## Sync 汇报

**π0.5 模型权重**: ✅ 已就绪（无需传输）
- cqa1:/root/autodl-tmp/models/pi05_libero_finetuned/ 已存在，7.0G，所有 8 个文件齐全
- model.safetensors 大小完全匹配源端 (7,473,096,344 bytes)

**CRM checkpoint**: ✅ 同步成功
- cqa1:/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt
- 大小 2,484,379 bytes
- MD5: `25093621fd5158951b2297ca406472f4` ✓ 匹配预期

**cqa1 环境就绪**:
- torch 2.8.0+cu128, CUDA 可用, 6× RTX 4090 D (24GB each, 全空闲 0 MiB used)
- transformers 5.9.0
- 项目代码存在 (/root/acr-vla-conformal-refinement/src/evaluate.py)
- Python 在 `/root/miniconda3/bin/python`（启动 eval 时需使用此路径或先 `conda activate base`）

可立即部署 6 个 π0.5 eval 实验。

---
