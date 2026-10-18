# code smart token compression

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_smart_token_compression_20260517T170928_result.json`
- **Structured JSON:** [`8e4d02905bc62762fc25.json`](../../sessions/8e/8e4d02905bc62762fc25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出文件和 dry-run 结果汇总：

**产出文件（cqa1-33015:/root/autodl-tmp/importance_margin_vla_compress/）**

| 文件 | 行数 | 说明 |
|------|------|------|
| `smart_compress_module.py` | 389 | VisionTokenCompressor + SmartCompressWrapper |
| `train_smart_compress.py` | 595 | 训练脚本（含 `--dry-run`） |
| `eval_smart_compress.py` | 201 | 离线 eval（含 `--compare-baseline`） |
| `configs/smart_compress.yaml` | 42 | M=32 配置（默认） |
| `configs/smart_compress_m64.yaml` | 7 | M=64 ablation |
| `configs/smart_compress_m96.yaml` | 7 | M=96 ablation |

**Dry-Run 验证结果**

| 检查项 | 结果 |
|--------|------|
| Forward shape | `[4, 50, 32]` ✓ |
| Loss 正常 | 1.0367 ✓ |
| Compressor 收到梯度 | ✓ (queries grad=0.28) |
| Expert 收到梯度 | ✓ |
| VLM+SigLIP 冻结 | ✓ |
| Compressor 参数量 | 22.2M |
| 总可训练参数 | 122.1M / 472.2M (25.85%) |
| 压缩率 (M=32) | 128→32, 75% reduction |
| Inference 输出 | `[B, 50, 32]` ✓ |

训练命令（准备好后执行）：
```bash
HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 python train_smart_compress.py --config configs/smart_compress.yaml
```

---
