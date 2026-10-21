# ops check pruning method

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-pruning-method_20260520T113007_result.json`
- **Structured JSON:** [`da008a454a6e0285da56.json`](../../sessions/da/da008a454a6e0285da56.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已获取。

---

```
OpenVLA pruning 方法:
  脚本: eval_openvla_libero.py (westd-27271)
  方法: random_removal (true removal)
  具体实现: 在 projector 输出后注册 forward hook (RandomPruningHook)，
           对 N 个 vision token 用 torch.randperm 随机选 k=N*k_ratio 个，
           直接按 index 取子集返回 (output[:, indices, :])，
           即从序列中物理移除未选中的 token，不是置零。

X-VLA pruning 方法:
  脚本: eval_xvla_pruning_libero.py (westd-38929)
  方法: L2_norm_removal (importance-based true removal)
  具体实现: 替换 model.vlm._encode_image，在 Florence2 image encoder + 
           linear projection 输出后，按每个 token 的 L2 norm 排序，
           topk 保留 k=N*keep_ratio 个最大 norm 的 token，
           按位置排序后 gather 取子集返回，物理移除其余 token。

两者是否一致: 否
  - OpenVLA 用 random removal（随机选 token 移除）
  - X-VLA 用 L2 norm-based removal（按重要性保留 top-k norm token）
  - 两者都是 true removal（物理移除），不是 zero_out
```

补充：`eval_success_rate_libero.py`（SmolVLA/IMM 模型）支持三种 pruning method（`zero_mask` / `true_removal` / `merge`），且同时支持 `acis_prune`（ACIS importance scoring）和 `random_prune` 两种 mask 计算方式，默认 pruning method 是 `zero_mask`。这个脚本和 OpenVLA 的 6-point curve 脚本是不同的。

---
