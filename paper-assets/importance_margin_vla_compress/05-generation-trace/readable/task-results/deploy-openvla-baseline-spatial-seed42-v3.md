# deploy openvla baseline spatial seed42 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_openvla-baseline-spatial-seed42-v3_20260521T222500_result.json`
- **Structured JSON:** [`3f58f5654fb71d7287cc.json`](../../sessions/3f/3f58f5654fb71d7287cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。三阶段任务总结：

**Phase 1 - 脚本修改** ✅
- 添加了 `--model_path`、`--unnorm_key`、`--gpu` 三个 CLI 参数
- `CHECKPOINT_PATH` 和 `UNNORM_KEY` 在 main() 中从 args 覆盖
- L282 model 名改为 `os.path.basename(args.model_path)` 动态生成

**Phase 2 - Checkpoint 下载** ✅
- `openvla/openvla-7b-finetuned-libero-spatial` 下载到 `/root/autodl-tmp/openvla-7b-finetuned-libero-spatial/`
- 4/4 safetensors 分片完整，共 15GB

**Phase 3 - 实验部署** ✅
- `eval_openvla_baseline_spatial_seed42_v3` 已在 GPU0 上运行（PID 369092）
- 模型加载成功（15.1GB），正在执行 libero_spatial 10 tasks × 50 episodes
- GPU1 M32 VTC 训练未受影响
- Registry 状态: RUNNING

---
