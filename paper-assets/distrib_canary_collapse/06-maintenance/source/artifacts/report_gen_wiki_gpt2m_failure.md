# 实验失败诊断: gen_wiki_gpt2m_a100_s42_v2

## 根因

**符号链接路径错误，缺少 `hub/` 层级。**

`/root/autodl-tmp/models/gpt2-medium/` 下所有文件都是指向 HF cache 的符号链接，但链接目标路径错误：

- 错误路径: `/root/autodl-tmp/.hf_cache/models--gpt2-medium/snapshots/6dcaa7a.../`
- 正确路径: `/root/autodl-tmp/.hf_cache/hub/models--gpt2-medium/snapshots/6dcaa7a.../`

创建符号链接时漏掉了 `hub/` 目录层级，导致所有链接悬空（dangling symlinks）。

## 关键日志

```
Loading model: /root/autodl-tmp/models/gpt2-medium
Traceback (most recent call last):
  File "/root/autodl-tmp/distrib_canary_collapse/iterative_train.py", line 284, in <module>
    main()
  File "/root/autodl-tmp/distrib_canary_collapse/iterative_train.py", line 182, in main
    tokenizer = AutoTokenizer.from_pretrained(args.model_name)
  ...
  File ".../tokenization_gpt2.py", line 153, in __init__
    with open(vocab_file, encoding="utf-8") as vocab_handle:
TypeError: expected str, bytes or os.PathLike object, not NoneType
EXIT_CODE=1
```

GPT2Tokenizer 初始化时找不到 `vocab.json`（因为符号链接指向不存在的路径），`vocab_file` 解析为 None，触发 TypeError。

## 修复操作（已执行）

重建了全部 7 个符号链接，指向正确的 HF cache 路径：

```bash
cd /root/autodl-tmp/models/gpt2-medium
SNAP=/root/autodl-tmp/.hf_cache/hub/models--gpt2-medium/snapshots/6dcaa7a952f72f9298047fd5137cd6e4f05f41da
for f in config.json generation_config.json merges.txt model.safetensors tokenizer.json tokenizer_config.json vocab.json; do
    ln -sf "$SNAP/$f" "$f"
done
```

验证通过：`AutoTokenizer.from_pretrained` 成功加载，vocab_size=50257。

## 是否可自动重试

**是。** 根因已修复，可以直接重跑原始命令。
