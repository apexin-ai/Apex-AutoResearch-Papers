# fix d003 restart v2

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_d003_restart_v2_20260512T132632_result.json`
- **Structured JSON:** [`fb418bb308fe516a43ba.json`](../../sessions/fb/fb418bb308fe516a43ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都在正常运行：

- **d003_reasoning_traces (GPU 0)**: 29GB 显存，93% 利用率，正在生成 reasoning traces（0/20）
- **d003_wikitext_32k (GPU 1)**: 35GB 显存，95% 利用率，"full" strategy eval 阶段 61%（~4000/6554）

修复总结：
1. **carc_kv_eviction.py**: 添加了 transformers 4.57+ 的 DynamicCache 新路径（`layers[i].keys/values` 替代 `key_cache/value_cache`），解决 tuple→DynamicCache 类型错误
2. **d003_reasoning_traces.py**: 用内嵌的 60 道数学题替代了不可访问的 `hendrycks/competition_math` HF 数据集，移除了 `load_math_data` 依赖
3. 两个命令都加了 `source /etc/network_turbo` 确保网络可用
4. d003_wikitext_32k 的 `--gpu` 改为 0（因 CUDA_VISIBLE_DEVICES 重映射）

---
