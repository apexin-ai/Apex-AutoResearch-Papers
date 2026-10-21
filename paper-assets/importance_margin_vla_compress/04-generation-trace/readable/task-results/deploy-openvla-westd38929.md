# deploy openvla westd38929

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_openvla_westd38929_20260524T143729_result.json`
- **Structured JSON:** [`a9cad91e5b59490456a3.json`](../../sessions/a9/a9cad91e5b59490456a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇报

### diag_openvla_unnorm_key (GPU 3) → DONE ✓

诊断完成，关键发现：
- `CHECKPOINT_PATH` 和 `UNNORM_KEY` 在脚本中**硬编码**为 `openvla-libero-object` / `libero_object`
- **不存在** `--model_path`、`--unnorm_key`、`--gpu` 这三个 CLI 参数
- 原始命令传了这些不存在的参数，即使 python 能找到也会报 `unrecognized arguments`

### eval_openvla_l2norm_k05_goal_seed42 (GPU 1) → 无法提交，3 个 blocker

1. **模型缺失**：`openvla-7b-finetuned-libero-goal` 在 westd-38929 上不存在。服务器上有 `openvla-oft-libero-goal`（OFT 微调版本，不是同一个模型）
2. **脚本不支持 CLI 覆盖**：需要给 `eval_openvla_l2norm_libero.py` 添加 `--model_path` 和 `--unnorm_key` 参数（当前硬编码 libero_object）
3. **python 不在 PATH**：需要 conda 激活（`/root/miniconda3/bin/python` 存在）— 这个问题通过提交命令模板中的 `source conda.sh && conda activate base` 可以解决

**需要 Director 决定**：
- 模型来源：是从 westd-27271 复制 `openvla-7b-finetuned-libero-goal`，还是改用 westd-38929 上已有的 `openvla-oft-libero-goal`？
- 脚本修改：是否要我添加 `--model_path` 和 `--unnorm_key` 参数到 eval 脚本？

---
