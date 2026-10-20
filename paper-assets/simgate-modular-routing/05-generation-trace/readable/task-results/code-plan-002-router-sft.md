# code plan 002 router sft

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-002-router-sft_20260514T042538_result.json`
- **Structured JSON:** [`0179058c4adfaa3012fa.json`](../../sessions/01/0179058c4adfaa3012fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有依赖就绪（transformers=4.57.6, peft=0.19.0, sklearn=1.8.0），均支持 Qwen3。

总结完成的工作：

**产出文件：**
- `src/training/data_loader.py` — 数据加载、prompt 构建、两种 split 策略（stratified / leave-one-out）、RouterDataset
- `src/training/router_sft.py` — 主训练脚本，LoRA + SeqCls head，class weighting + minority upsampling，支持 `--split_strategy {stratified, leave_one_out}`，自动解析本地模型路径
- `scripts/launch_plan002.sh` — 完整 pipeline（labeling → training → eval），支持 `SPLIT_STRATEGY` 环境变量切换

**数据统计：**
- 1710 条可用样本（11 个 task，过滤 no-preference 后）
- 类别分布：deterministic 1560 (91.2%) vs internal 150 (8.8%) — 严重不平衡，已通过 `--class_weights auto` + `--upsample_minority` 缓解

**验证：**
- Dry-run 在服务器上通过（数据加载、模型解析均正常）
- 依赖库版本兼容

**需 GPU dry-run：** 完整训练需要 GPU。启动命令：
```bash
bash scripts/launch_plan002.sh
```

---
