# code openvla spatial standardized v1

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_openvla_spatial_standardized_v1_20260522T013148_result.json`
- **Structured JSON:** [`9010161a489a2f2f804f.json`](../../sessions/90/9010161a489a2f2f804f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已提交并运行中，正在等待 checkpoint 下载完成。

**总结：**

| 项目 | 值 |
|------|------|
| exp_id | `openvla_spatial_standardized_v1` |
| PID | 594575 |
| GPU | cuda:0 @ westd-19183 |
| tmux session | `openvla_spatial_standardized_v1` |
| log | `~/runs/vla-ssd/openvla_spatial_standardized_v1.log` |
| 命令 | `bash /root/autodl-tmp/vla-ssd/scripts/run_spatial_pipeline.sh` |
| conditions | trained (openvla-7b-finetuned-libero-spatial) + untrained (openvla-7b) |
| 输出目录 | `results/libero_spatial/` + `results/libero_spatial_untrained/` |
| 预计耗时 | ~3-4h（参考 Goal pipeline），+ 下载等待时间（~14GB，取决于网速） |

当前状态：tmux 内 shell 正在 poll 等待 `openvla-7b-finetuned-libero-spatial` 的 4 个 safetensors 文件和 `modeling_prismatic.py` 下载完毕，然后自动执行 6-phase pipeline。

---
