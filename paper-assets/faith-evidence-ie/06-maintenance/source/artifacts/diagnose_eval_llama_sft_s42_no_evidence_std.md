# 诊断: eval_llama_sft_s42_no_evidence_std 失败

## 错误信息

```
ValueError: Couldn't instantiate the backend tokenizer from one of:
(1) a `tokenizers` library serialization file,
(2) a slow tokenizer instance to convert or
(3) an equivalent slow tokenizer class to instantiate and convert.
```

发生在 `inference.py:62`，`AutoTokenizer.from_pretrained("/root/autodl-tmp/sft_output_llama_3_1_8b")` 调用。

## 根因分类: 文件路径错误（迁移导致目录嵌套）

迁移时 SFT adapter 被放入了同名包裹目录，导致双层嵌套：

```
/root/autodl-tmp/sft_output_llama_3_1_8b/           ← eval 传入的路径（空目录）
└── sft_output_llama_3_1_8b/                         ← 实际内容在这里
    ├── adapter_config.json
    ├── adapter_model.safetensors (671MB)
    ├── tokenizer.json
    ├── tokenizer_config.json
    ├── checkpoint-190/
    └── checkpoint-570/
```

`inference.py` main() 的自动检测逻辑检查 `Path(model_path) / "adapter_config.json"` 是否存在（L408）。因为外层目录没有该文件，代码将路径当作 full model 加载（而非 adapter），随后从该空目录加载 tokenizer 失败。

## 连锁影响

- adapter 未被检测到 → 代码走 "Full model" 分支 → tokenizer 在空目录找不到文件 → 崩溃
- 即使 tokenizer 问题被绕过，model 加载也会失败（空目录无 model weights）

## 其他环境确认

- 基座模型存在: `/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B/config.json` ✓
- adapter_config 中 `base_model_name_or_path` 指向正确基座 ✓

## 修复建议

**方案 A（推荐）: 解除目录嵌套**

```bash
mv /root/autodl-tmp/sft_output_llama_3_1_8b/sft_output_llama_3_1_8b/* /root/autodl-tmp/sft_output_llama_3_1_8b/
rmdir /root/autodl-tmp/sft_output_llama_3_1_8b/sft_output_llama_3_1_8b
```

然后直接重跑 eval。

**方案 B: 修改 eval 调用路径**

将 `--model_path` 改为 `/root/autodl-tmp/sft_output_llama_3_1_8b/sft_output_llama_3_1_8b`。

方案 A 更好，因为一次修复所有后续引用。

## 重跑前检查

重跑前需按 C001 约束 `nvidia-smi` 确认目标 GPU 显存占用 < 2GB。
