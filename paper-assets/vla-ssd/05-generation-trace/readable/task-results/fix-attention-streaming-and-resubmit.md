# fix attention streaming and resubmit

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_attention_streaming_and_resubmit_20260521T052618_result.json`
- **Structured JSON:** [`e06db5e9d126fc13f47c.json`](../../sessions/e0/e06db5e9d126fc13f47c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都启动成功：
- **libero_object**: 模型 shards 加载完毕（6.25 it/s），正在加载 processor
- **nora_goal**: 已进入 Phase 1 提取，100/5000 samples 已处理

## 完成总结

### 修改内容
6 个 pipeline 脚本全部修改（`tracvla_spatial_probing_only.py` 不涉及 attention，未改）：

| 文件 | 修改点 |
|------|--------|
| `libero_object_full_pipeline.py` | 7 处 |
| `libero_long_full_pipeline.py` | 7 处 |
| `nora_goal_full_pipeline.py` | 7 处 |
| `nora_spatial_full_pipeline.py` | 7 处 |
| `tracvla_object_full_pipeline.py` | 7 处 |
| `tracvla_spatial_full_pipeline.py` | 7 处 |

每个文件的 7 处修改：
1. **init**: `l1_attns=[]` → `head_instr_ratio_sum/sq_sum` 累加器
2. **attn_block**: `.append(l1)` → 在 GPU 上 streaming 计算 per-head instruction ratio 并累加
3. **return**: 返回统计量而非原始矩阵
4. **analyze_fn**: `analyze_attention` 改为从累加统计量计算 mean/std
5. **unpack**: 调用侧解包变量名更新
6. **analyze_call**: Phase 3 调用参数更新
7. **del**: 清理变量名更新

### 额外修复
- `openvla-7b-finetuned-libero-object/preprocessor_config.json` 的 `auto_map` 指向 HF repo 导致离线时加载失败，改为本地路径

### 内存节省
- 旧方案: 5000 × attention_matrix (每个 ~10MB for OpenVLA) ≈ **50GB RAM**
- 新方案: 仅 2 个 float64 数组 (N_HEADS,) + 1 个计数器 ≈ **< 1KB**

### 实验状态
- cuda:0 `libero_object_full_pipeline.py` — PID 536977, 正在加载
- cuda:1 `nora_goal_full_pipeline.py --conditions trained untrained` — PID 537115, Phase 1 进行中

---
