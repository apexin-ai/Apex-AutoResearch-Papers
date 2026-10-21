# infra pythia variant scripts launch

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_pythia-variant-scripts-launch_20260514T145010_result.json`
- **Structured JSON:** [`7b0f495b950ff123b4c7.json`](../../sessions/7b/7b0f495b950ff123b4c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline 已成功启动，模型正在加载。

### 产出报告

1. **脚本路径**
   - `/root/autodl-tmp/recursive_gen_depth_est/scripts/run_pipeline_pythia_temp09.sh` (temp_only, t=0.9)
   - `/root/autodl-tmp/recursive_gen_depth_est/scripts/run_pipeline_pythia_topk50.sh` (topk, k=50)

2. **Temperature 变体启动状态**
   - PID: 125067，tmux session: `pythia_temp09_001`
   - cuda:0 上运行，Step 1 (LoRA finetune depth-0) 正在加载模型权重
   - 日志输出正常：`logs/pipeline_pythia_temp09.log`

3. **预估完成时间**
   - 参考 MVP pipeline ~1.8h，本变体结构相同（3 轮 finetune + 3 轮 generate），预计 ~1.8-2h，约 2026-05-15 00:50 CST 完成

4. **注意事项**
   - 服务器名实际为 `autodl-rtx6000`（非 `westb-52439`）
   - topk50 变体脚本已就绪，待 cuda:0 空闲后可启动

---
