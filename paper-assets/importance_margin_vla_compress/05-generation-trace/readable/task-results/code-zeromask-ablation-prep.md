# code zeromask ablation prep

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_zeromask_ablation_prep_20260525T154421_result.json`
- **Structured JSON:** [`086c0615ac088a944cab.json`](../../sessions/08/086c0615ac088a944cab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**脚本**: `/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_zeromask_libero.py` (westd-38929, 439 行)

**核心改动**:
- 新增 `--ablation_mode {hard_prune, zero_mask}`，默认 `hard_prune`（保持原行为）
- 抽出 `_apply_selection(output, keep_indices, ablation_mode)` 共享逻辑：`hard_prune` 走 `torch.gather`（shape 缩减），`zero_mask` 走 `scatter_`+乘 mask（shape 保留，未选中位置置 0，position embedding 不变）
- `RandomPruningHook` / `L2NormPruningHook` / `AttentionPruningHook` 均接受 `ablation_mode` 参数，三种 importance 信号 × 两种 ablation 共 6 种组合可用
- 结果 JSON 增加 `ablation_mode` 字段；输出文件名加 `_zm`/`_hp` tag 避免覆盖

**验证**（不占 GPU）:
- `python3 -m py_compile` → 通过
- `_apply_selection` 单元测试（torch CPU tensor）→ `hard_prune` gather 正确，`zero_mask` 选中行原值保留 + 未选中行为 0
- argparse 4 个有效组合通过、`--ablation_mode bogus` 被正确拒绝

**artifact id**: `art_20260525_4ac92d`

未跑 GPU eval（westd-38929 4 卡满载 cliff zone 实验，按指令等 GPU 空出再跑）。

---
