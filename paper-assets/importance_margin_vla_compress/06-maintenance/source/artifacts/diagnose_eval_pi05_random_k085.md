# 诊断: eval_pi05_random_k085_object_seed42 失败

**服务器**: westd-41074  
**退出码**: 1  
**运行时间**: ~10 分钟  
**诊断时间**: 2026-05-21

## 具体错误

```
ValueError: Failed to instantiate processor step 'tokenizer_processor' with config:
  {'tokenizer_name': 'google/paligemma-3b-pt-224', ...}.
  Error: [Errno 101] Network is unreachable
```

完整调用链:
```
eval_pi05_pruning_libero.py:164 main()
  → factory.py:288 make_pre_post_processors()
    → pipeline.py:572 from_pretrained()
      → pipeline.py:908 _instantiate_step()
        → tokenizer_processor.py:111 AutoTokenizer.from_pretrained('google/paligemma-3b-pt-224')
          → huggingface_hub/hf_api.py:3218 model_info() via httpx
            → httpcore.ConnectError: [Errno 101] Network is unreachable
```

## 根因

**网络不可达**。`AutoTokenizer.from_pretrained('google/paligemma-3b-pt-224')` 尝试连接 HuggingFace Hub 下载/验证 tokenizer，但服务器网络不通。

与同服务器 `eval_pi05_random_k095_object_seed42` 失败原因完全相同。

## 环境状态

| 项目 | 状态 |
|------|------|
| GPU | 4× NVIDIA RTX PRO 6000 Black (98GB)，正常 |
| 磁盘 (/) | 23G/30G (75%)，正常 |
| 磁盘 (/root/autodl-tmp) | 185G/250G (74%)，正常 |
| 网络 | 不可达 |

## 建议

可以直接重跑，但需先解决网络问题：

1. **首选**：在启动脚本中加 `source /etc/network_turbo` 启用 AutoDL 代理加速
2. **备选**：将 `google/paligemma-3b-pt-224` tokenizer 预缓存到本地，eval 脚本中设 `TRANSFORMERS_OFFLINE=1` 或用本地路径替代 HF model ID
3. **备选**：在 `AutoTokenizer.from_pretrained` 调用处加 `local_files_only=True`（需确保 tokenizer 已缓存）
