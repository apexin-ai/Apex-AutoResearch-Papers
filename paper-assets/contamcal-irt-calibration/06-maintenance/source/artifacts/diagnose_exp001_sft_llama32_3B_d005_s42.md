# 诊断: exp_001_sft_llama32_3B_d005_s42

## 失败原因

**磁盘空间不足 (No space left on device, os error 28)**

训练 3177/3177 steps 全部完成（epoch=1.0, loss=1.52），LoRA adapter 已成功保存。失败发生在 merge 阶段——将 LoRA adapter 合并回 base model 并保存 merged weights 时，`/root/autodl-tmp` 分区已满（169G/169G, 剩余 2.4MB）。

具体错误：
```
safetensors_rust.SafetensorError: Error while serializing: I/O error: No space left on device (os error 28)
```

写入 `merged/model-00001-of-00002.safetensors`（4.2GB）后，第二个 shard 无法写入。

## 可恢复性

**完全可恢复。** LoRA adapter 完整保存在：
```
/root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d005_s42/lora_adapter/
  - adapter_model.safetensors (93MB)
  - adapter_config.json
```

无需重新训练。

## 修复方案

1. 清理 `/root/autodl-tmp` 腾出 ~6GB 空间（删除旧 checkpoint、不需要的模型缓存等）
2. 删除不完整的 merged 目录：`rm -rf /root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d005_s42/merged/`
3. 单独重跑 merge 步骤（加载 base model + LoRA adapter → save_pretrained）

或者将 merged output 写到有空间的路径（如根分区 /root/ 下临时目录，前提是根分区有足够空间）。
