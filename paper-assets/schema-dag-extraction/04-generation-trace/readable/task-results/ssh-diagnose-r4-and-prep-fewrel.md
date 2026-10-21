# ssh diagnose r4 and prep fewrel

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose-r4-and-prep-fewrel_20260515T164612_result.json`
- **Structured JSON:** [`7856a51446e18ea2ed0f.json`](../../sessions/78/7856a51446e18ea2ed0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。

---

## R4 诊断结果
- **conclusion**: failed (功能性失败)
- **metrics**: 所有条件下 precision=0, recall=0, f1=0, total_pred=0
- **failure_reason**: llama-3.1-8b-instruct 对每个样本仅生成 2 token（空预测 `[]`），完全没有提取出任何实体。模型太弱无法遵循 NER 提取 prompt。
- **结果文件路径**:
  - `artifacts/exp012/eval_fewnerd_exp1_llama-3.1-8b-instruct.json`
  - `artifacts/exp012/eval_fewnerd_exp2_llama-3.1-8b-instruct.json`
  - `artifacts/exp012/predictions_fewnerd_exp1_llama-3.1-8b-instruct.json` (49MB)
  - `artifacts/exp012/predictions_fewnerd_exp2_llama-3.1-8b-instruct.json` (29MB)
- **退出码**: 0（进程正常完成，但结果无效）
- **日志关键信息**: 无专用 r4 log 文件；r3 log (`/tmp/exp012_r3.log`) 显示 70b-fp8 因 flashinfer CUDA 头文件不兼容崩溃
- **tmux**: 无活跃 session

## GPU 状态
- **空闲**
- NVIDIA RTX PRO 6000 Black, 98GB VRAM, 0% 利用率, 0MiB 已用
- Driver 590.44.01, CUDA 13.1

## Fewrel 40rel 准备
- **脚本路径**: `/root/schema-dag-extraction/src/run_fewrel_40rel.py`
- **增量保存**: **已有** — 每个 batch 完成后 append 到 `results_incremental.jsonl`（JSONL 格式）
- **模型路径**: `/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/`（脚本默认值，已确认存在 7 个 safetensors 分片）
- **dry-run 结果**: 成功 — 960 samples, 105 batches, 6960 inferences, 预估 ~174 min
- **启动命令**:

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema-dag-extraction && export CUDA_HOME=/root/miniconda3/lib/python3.12/site-packages/nvidia/cu13 && export FLASHINFER_DISABLE_VERSION_CHECK=1 && export CUDA_VISIBLE_DEVICES=0 && python3 src/run_fewrel_40rel.py --stage all --mode exp1 --use_all --output_dir artifacts/fewrel_40rel 2>&1 | tee /tmp/fewrel_40rel.log"
```

exp2 同理，`--mode exp1` 改为 `--mode exp2`。建议先跑 exp1，完成后再跑 exp2（shell 脚本 `scripts/run_fewrel_40rel.sh` 串联两者，但没有设 CUDA_HOME 和 CUDA_VISIBLE_DEVICES）。

---
