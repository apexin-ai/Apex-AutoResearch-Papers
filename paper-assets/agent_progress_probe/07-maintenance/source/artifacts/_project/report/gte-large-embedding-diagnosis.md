# gte-large Embedding 异常诊断

## 现象
- 文件大小：402K（正常 e5-large/bge-m3 应为数百 MB）
- windows 数量：10（应为 54809）
- 格式正确（dict, 含 embeddings/labels/instance_ids 等 keys），但数据极不完整

## 详情
- embed_dim: 1024
- encoder: gte-large
- model_id: /root/autodl-tmp/.hf_cache/modelscope_models/gte-large/damo/nlp_gte_sentence-embedding_english-large
- 仅处理了约 0.02% 的数据即终止

## 可能原因
1. embedding 生成脚本中途报错退出，但已保存了前 10 条结果
2. 模型加载或推理过程中出现异常（OOM / 模型兼容性问题）
3. 需检查生成日志确认具体错误

## 结论
gte-large embedding 不可用于 ablation，需重新生成。