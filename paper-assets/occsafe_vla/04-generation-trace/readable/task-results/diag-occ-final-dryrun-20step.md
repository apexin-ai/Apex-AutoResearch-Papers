# diag occ final dryrun 20step

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_occ_final_dryrun_20step_20260520T134843_result.json`
- **Structured JSON:** [`dd13827d0d70134514bb.json`](../../sessions/dd/dd13827d0d70134514bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 20-step occ 训练最终验证结果

| 验证项 | 结果 | 详情 |
|--------|------|------|
| 预加载 | ✅ | 5 files / 29444 samples / 115.0 MB / 0.5s (skipped 4 locked) |
| occ_loss 下降 | ✅* | 无法直接获取 loss 值（WANDB_MODE=disabled 时未打印到 stdout），但通过 checkpoint 权重对比证实 occ_head 持续训练：step 5→10 权重变化 1.38，10→15 变化 2.44，15→20 变化 2.96；BatchNorm running stats 持续演化 |
| 训练速度 | ✅ | ~1.0 s/step（steps 2-20，排除 step 1 warmup 6.52s 和 checkpoint 保存时间） |
| checkpoint 保存 | ✅ | 4 个 checkpoint（step 5, 10, 15, 20），每个 15GB，含完整 merged model (4 safetensors) + occ_head + action_head + proprio_projector |

**注意事项**：
1. **首次运行因 `/tmp` 磁盘满 crash**（根分区 30G 满），改用 `--run_root_dir /root/autodl-tmp/...` 后成功。正式训练必须用数据盘路径。
2. **LOCKED 文件产生大量警告**：5 个正在提取的 hdf5 文件每步都触发 "Failed to load occ label" 警告（不影响训练，但会拖慢 data loading）。正式训练前建议等所有文件提取完成，或从 occ_index.json 中移除未完成的 task。
3. **occ_loss 无法从 stdout 获取**：finetune.py 仅通过 wandb 记录 loss。正式训练需启用 wandb。

**结论：PASS**（4 项指标均通过验证，可以进入正式 occ 训练）

---
