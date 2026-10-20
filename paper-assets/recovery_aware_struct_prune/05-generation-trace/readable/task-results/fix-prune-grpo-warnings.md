# fix prune grpo warnings

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_prune-grpo-warnings_20260514T031253_result.json`
- **Structured JSON:** [`e5f0961af0fdead51bf8.json`](../../sessions/e5/e5f0961af0fdead51bf8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有修改已确认正确。汇报如下：

---

## 修复汇报

### Fix 1: prune.py — config 更新 + forward pass 验证

**修改位置**：`main()` 函数，剪枝执行后、保存前（L334-387）

**新增逻辑**：
1. 遍历每层 `self_attn.num_heads` / `num_key_value_heads`，检测是否均匀剪枝
2. **均匀**：直接更新 `model.config.num_attention_heads` 和 `num_key_value_heads`
3. **非均匀**：config 设为 min 值，同时存 `per_layer_num_attention_heads` / `per_layer_num_key_value_heads` 列表到 config
4. 同样处理 `intermediate_size`（MLP 剪枝）
5. forward pass 验证：`dummy_input (1,32)` → 成功则 log shape，失败则 `raise RuntimeError`

**注**：`prune_attention_heads` 函数中已有 per-layer `attn.num_heads`/`attn.num_key_value_heads`/`attn.head_dim` 更新（原代码已正确），本次补的是 **config 级别** 和 **forward pass 验证**。

### Fix 2: train_grpo.py — max_completion_length 2048

**修改位置**：L147
- `--max_new_tokens` default: `512` → `2048`
- 该值通过 `max_completion_length=args.max_new_tokens` 传入 GRPOConfig
- batch_size=2 保持不变（96GB 显存 + 剪枝后 ~4.5B 参数足够）

### Fix 3: train_grpo.py — W&B 日志

**修改**：
- L24-26: 添加 `import wandb`（try/except 容错）
- L160: `os.environ.setdefault("WANDB_PROJECT", "recovery_aware_struct_prune")`
- L191: 添加 `run_name=f"grpo_{os.path.basename(args.model_path)}"`
- L199: `report_to="none"` → `report_to="wandb"`

### W&B 登录状态

**未登录**。训练前需执行 `wandb login &lt;API_KEY>` 或设置 `WANDB_API_KEY` 环境变量。

### Dry-run

未执行。服务器上只有 `cka_scores_dryrun.pt`，缺少 importance scores `.pt` 文件，无法运行 prune.py。forward pass 验证逻辑已集成到 prune.py 中，首次实际剪枝时会自动验证。

---
