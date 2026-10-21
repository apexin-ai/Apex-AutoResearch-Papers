# code counterfactual batch template

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_counterfactual_batch_template_20260521T164440_result.json`
- **Structured JSON:** [`153608363a1d34a59611.json`](../../sessions/15/153608363a1d34a59611.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建: `/root/autodl-tmp/vla-ssd/scripts/counterfactual_batch.py` (884 行)

功能:
- 支持 `--arch openvla/tracvla/nora`, `--suite goal/spatial/object/long`, `--condition trained/untrained`
- `--method auto` 自动选择: trained openvla/tracvla → action_mse, nora 和所有 untrained → cosine_dist
- 内置全部 checkpoint/data/results 路径映射，匹配现有 pipeline 脚本的 task 顺序
- OFT checkpoint 自动合并 dataset_statistics.json 到 norm_stats
- `--dry-run` 快速验证, `--results-dir` 可覆盖输出目录
- `--gpu`, `--n-demos`, `--n-timesteps` 可调

用法:
```bash
python counterfactual_batch.py --arch tracvla --suite spatial --condition untrained
python counterfactual_batch.py --arch openvla --suite long --condition trained
python counterfactual_batch.py --arch openvla --suite object --condition untrained
```

---
