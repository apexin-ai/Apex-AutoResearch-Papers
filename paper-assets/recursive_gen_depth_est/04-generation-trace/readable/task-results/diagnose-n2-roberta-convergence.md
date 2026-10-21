# diagnose n2 roberta convergence

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_n2_roberta_convergence_20260515T124221_result.json`
- **Structured JSON:** [`5eef72a083b1bd51cace.json`](../../sessions/5e/5eef72a083b1bd51cace.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。以下是结论。

核心证据链：

1. **`pytorch_model.bin` 文件损坏** — `torch.load` 报 `storage has wrong byte size`，无论 `weights_only=True/False` 都失败
2. **下载缓存中有 `.incomplete` 文件** — `.cache/huggingface/download/` 下有两个 `.incomplete` 文件（10MB、20MB），说明下载被中断
3. **训练日志 `n2_roberta_finetune_broken.log` 显示 `loss=nan` 从 step 0 开始**，不是用户描述的 ~1.39
4. **Tokenizer 完全正常** — pad/cls/sep token 全部正确
5. **脚本代码无 bug** — `AutoTokenizer.from_pretrained(args.model_name)` 正确从 model_name 推断；`num_labels=4` 正确；lr/loss/数据加载全部正常
6. **模型加载报告正常** — pooler UNEXPECTED + classifier MISSING 是预期行为（base → classification head）

```json
{
  "root_cause": "pytorch_model.bin 文件损坏（下载中断）。torch.load 报 'storage has wrong byte size'，.cache/huggingface/download/ 下存在 .incomplete 文件。损坏的权重导致 forward pass 从 step 0 起就产出 NaN。",
  "error_type": "data",
  "fix_steps": [
    "删除 /root/autodl-tmp/models/roberta-base/ 整个目录",
    "source /etc/network_turbo 启用 AutoDL 网络加速",
    "重新下载: python -c \"from huggingface_hub import snapshot_download; snapshot_download('FacebookAI/roberta-base', local_dir='/root/autodl-tmp/models/roberta-base')\"",
    "验证: python -c \"import torch; sd=torch.load('/root/autodl-tmp/models/roberta-base/pytorch_model.bin', map_location='cpu'); print(f'keys={len(sd)}, any_nan={any(torch.isnan(v).any() for v in sd.values())}')\"",
    "重新运行实验: python src/n2_deberta_finetune.py --model_name /root/autodl-tmp/models/roberta-base --output_dir results/n2_roberta_finetune --gpu 1"
  ],
  "can_auto_fix": true,
  "code_diff": "脚本代码无需修改。唯一需要的操作是重新下载完整的 roberta-base 模型权重。注意：用户描述的 'loss=1.39' 与实际日志 'loss=nan' 不符，实际情况更严重——模型从第一步起就输出 NaN。"
}
```

补充说明：`tokenizer_config.json` 只有 `{"model_max_length": 512}`，`special_tokens_map.json` 缺失，但这不影响功能——`tokenizer.json` (fast tokenizer) 内嵌了完整的 RobertaProcessing 配置和所有 special tokens。重新下载后这些文件也会补齐。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "pytorch_model.bin 文件损坏（下载中断）。torch.load 报 'storage has wrong byte size'，.cache/huggingface/download/ 下存在 .incomplete 文件。损坏的权重导致 forward pass 从 step 0 起就产出 NaN。",
    "error_type": "data",
    "fix_steps": [
      "删除 /root/autodl-tmp/models/roberta-base/ 整个目录",
      "source /etc/network_turbo 启用 AutoDL 网络加速",
      "重新下载: python -c \"from huggingface_hub import snapshot_download; snapshot_download('FacebookAI/roberta-base', local_dir='/root/autodl-tmp/models/roberta-base')\"",
      "验证: python -c \"import torch; sd=torch.load('/root/autodl-tmp/models/roberta-base/pytorch_model.bin', map_location='cpu'); print(f'keys={len(sd)}, any_nan={any(torch.isnan(v).any() for v in sd.values())}')\"",
      "重新运行实验: python src/n2_deberta_finetune.py --model_name /root/autodl-tmp/models/roberta-base --output_dir results/n2_roberta_finetune --gpu 1"
    ],
    "can_auto_fix": true,
    "code_diff": "脚本代码无需修改。唯一需要的操作是重新下载完整的 roberta-base 模型权重。注意：用户描述的 'loss=1.39' 与实际日志 'loss=nan' 不符，实际情况更严重——模型从第一步起就输出 NaN。"
  }
}
```

</details>

---
