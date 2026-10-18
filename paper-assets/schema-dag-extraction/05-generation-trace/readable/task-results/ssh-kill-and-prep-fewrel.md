# ssh kill and prep fewrel

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill-and-prep-fewrel_20260515T164746_result.json`
- **Structured JSON:** [`7f632e7bd326bbfca53b.json`](../../sessions/7f/7f632e7bd326bbfca53b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

干净状态，无残留结果。所有信息齐备。

## Kill 结果
- PID 297093: **KILLED** (SIGTERM, force_killed=false)
- nvidia-smi: **GPU 空闲** (0MiB / 97887MiB, RTX PRO 6000 Black)

## Fewrel 脚本
- 路径: `/root/schema-dag-extraction/src/run_fewrel_40rel.py`
- Shell wrapper: `/root/schema-dag-extraction/scripts/run_fewrel_40rel.sh`
- 增量保存: **已有** — 每个 batch 完成后 append 到 `results_incremental.jsonl`（JSONL 格式，非 atomic tmp+rename，但 JSONL append 足够安全）
- `preprocess_exp1.json` 已存在，exp1 可直接用 `--stage extract` 跳过数据加载

## 模型路径
- Qwen3-32B-FP8: `/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/`（脚本默认值，已验证存在）

## 启动命令

**exp1（用已有 preprocess，直接 extract）：**
```bash
bash -c "export CUDA_HOME=/root/miniconda3/lib/python3.12/site-packages/nvidia/cu13 && export CUDA_VISIBLE_DEVICES=0 && export FLASHINFER_DISABLE_VERSION_CHECK=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema-dag-extraction && python3 src/run_fewrel_40rel.py --stage extract --mode exp1 --output_dir artifacts/fewrel_40rel --preprocess_path artifacts/fewrel_40rel/preprocess_exp1.json 2>&1 | tee /tmp/fewrel_40rel_exp1.log && echo '=== exp1 DONE, starting exp2 ===' && python3 src/run_fewrel_40rel.py --stage all --mode exp2 --use_all --output_dir artifacts/fewrel_40rel 2>&1 | tee /tmp/fewrel_40rel_exp2.log && echo '=== ALL DONE ==='"
```

## Dry-run
- `--help`: **pass**（参数解析正确）
- `--dry_run`: 超时（数据加载 >30s），但 preprocess_exp1.json 已生成完整（274KB, 80 relations, counts=[1,4,8,16,32,40]），验证通过

需要我在 tmux 里启动吗？

---
