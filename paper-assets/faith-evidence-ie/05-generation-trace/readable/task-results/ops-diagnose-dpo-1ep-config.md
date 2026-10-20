# ops diagnose dpo 1ep config

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose-dpo-1ep-config_20260515T213021_result.json`
- **Structured JSON:** [`f908f1d05b4fcb06be08.json`](../../sessions/f9/f908f1d05b4fcb06be08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：**Bug — eval 缺少 SFT adapter 叠加**

### 根因

DPO 训练流程是 `base Qwen3-4B → merge SFT adapter → 新 LoRA → DPO 训练`（`dpo_trainer.py:171-185`）。DPO adapter 编码的是 **(base+SFT) → DPO** 的增量。

但 eval 时 `sft_adapter: null`（`metrics.json` 的 config 字段），意味着 eval 命令没传 `--sft_adapter`。实际加载路径变成了 `base Qwen3-4B + DPO adapter`，**缺失了 SFT 层**。

没有 SFT 基础，base Qwen3-4B 不认识 DocRED 的标准关系名（如 "headquarters location"、"country"），生成了自由文本关系（"based in"、"part of"、"relaunched"、"available on"），几乎全部无法与 gold 匹配。

### 各项检查具体发现

| 检查项 | 发现 |
|--------|------|
| **adapter 完整性** | 1ep adapter 存在（528MB safetensors），结构完整 |
| **1ep vs 3ep config** | 完全一致：base=Qwen3-4B, r=64, alpha=128, 相同 target_modules |
| **trainer state** | checkpoint-167 存在（最终 checkpoint），训练正常完成 |
| **metrics** | `field_compliance_rate=0.0`, `evidence_format_rate=0.0`，tp=34/18307 |
| **predictions 样本** | 输出 "based in"、"part of"、"relaunched" 等自由文本，非 DocRED 标准关系名 |
| **eval config** | `sft_adapter: null` — **未叠加 SFT adapter** |
| **训练代码** | `dpo_trainer.py` 明确 merge SFT 后再训 DPO LoRA |
| **eval 代码** | `inference.py:87-91` 支持 `--sft_adapter`，但此次未传 |

### 修复

重新跑 eval，加上 `--sft_adapter /root/autodl-tmp/sft_output`：

```bash
python -m freige.eval.inference \
    --model_path /root/autodl-tmp/dpo_output_1ep/ \
    --base_model /root/autodl-tmp/models/Qwen3-4B \
    --sft_adapter /root/autodl-tmp/sft_output \
    --data_path /root/autodl-tmp/data/docred \
    --output_dir /root/autodl-tmp/eval_results/dpo_ced_1ep_fixed \
    --batch_size 16 \
    --max_new_tokens 1024
```

---
