# train openvla vtc only westd27271

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_openvla_vtc_only_westd27271_20260519T182443_result.json`
- **Structured JSON:** [`ae56bb0fe9263e83ca54.json`](../../sessions/ae/ae56bb0fe9263e83ca54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练稳定运行。step=50 loss 从 16.6 降到 3.99，梯度从 883 降到 30，sps=0.5。

总结：

**已完成：**
1. 文件检查 - OpenVLA 适配文件已存在于 westd-27271（由其他 worker 同步）
2. 修复 `preprocessor_config.json` auto_map（去掉 `openvla/openvla-7b--` 前缀以支持离线加载）
3. 修复 `openvla_vtc_adapter.py` dtype 不匹配（添加 `pixel_values.to(dtype=model_dtype)` 转换）
4. 使用 `HF_HOME=/root/autodl-tmp/.hf_cache` 解决数据集缓存路径问题
5. 旧实验 `train_openvla_sc_m128_seed42` 状态更新为 DONE(failed)
6. 新实验 `train_openvla_sc_m128_seed42_v2` 注册并启动

**训练状态：**
- 服务器：westd-27271，tmux 会话 `train_openvla_sc_m128_v2`，PID=841334
- step=50/100000，loss=3.99，sps=0.5（约 ~55 小时完成 100k steps）
- 可训练参数：411M（VTC 403M + LoRA 8.4M），总参数 7.95B
- 数据集：273465 samples，batch_size=8

---
