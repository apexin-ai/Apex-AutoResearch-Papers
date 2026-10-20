# code exp wnut17 qwen25 7b v3

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_wnut17_qwen25_7b_v3_20260519T080426_result.json`
- **Structured JSON:** [`6e10b15d46a89b7f528e.json`](../../sessions/6e/6e10b15d46a89b7f528e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

一切正常。总结当前状态：

**exp_wnut17_qwen25_7b 已启动 (RUNNING)**

- **Server**: autodl-5090-c, screen session `exp_wnut17_7b`
- **GPU**: cuda:2,3 (不干扰 cuda:0,1 上的 14B 实验)
- **当前阶段**: 等待 Qwen2.5-7B-Instruct 下载完成（~3GB/14.2GB，预计 ~70min）
- **Pipeline 5 阶段自动执行**:
  1. QLoRA 训练（rank=32, alpha=64, 4-bit NF4, 5 epochs, WNUT-17 train）
  2. LoRA 导出/合并
  3. 3-seed N=8 推理（seed 42/123/456, T=1.0）
  4. 5-signal 分析（SJ/FK/VC/EM/LP）
  5. Entity construction（θ=2/N, LP-weighted）

**文件清单**:
- 训练配置: `train_config_qwen25_7b_wnut17_s42.yaml`
- 导出配置: `export_config_qwen25_7b_wnut17.yaml`
- Pipeline 脚本: `run_wnut17_qwen25_7b_pipeline.sh`
- Entity construction: `code/wnut17_entity_construction.py`
- 日志: `logs/exp_wnut17_7b_pipeline.log`
- 输出目录: `output/wnut17/qwen25_7b_n8_seed{42,123,456}/`

---
