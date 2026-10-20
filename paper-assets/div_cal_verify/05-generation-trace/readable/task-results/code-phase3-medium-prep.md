# code phase3 medium prep

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase3_medium_prep_20260513T082438_result.json`
- **Structured JSON:** [`f597aa70fcf243aabfcf.json`](../../sessions/f5/f597aa70fcf243aabfcf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出汇总

| 项目 | 状态 |
|------|------|
| **run_mvp.py 修改** | **无需修改**。`--student_model` 参数已存在（line 40），`from_pretrained` 直接使用该参数（line 217-218），且已有 GPT2 的 float32 dtype 特殊处理（line 216） |
| **run_phase3_medium.sh** | `/root/div_cal_verify/run_phase3_medium.sh`，已创建，chmod +x，bash -n 语法检查通过 |
| **GPT2-medium 权重缓存** | 已缓存，`model.safetensors` 存在于 `/root/.cache/huggingface/hub/models--gpt2-medium/snapshots/` |
| **与 Phase 2 差异** | 仅 `--student_model gpt2-medium`、`output_dir results_phase3_medium`、默认 GPU 0（Phase 2 默认 GPU 1） |

**启动命令：**
```bash
nohup bash /root/div_cal_verify/run_phase3_medium.sh 0 > /root/autodl-tmp/phase3_medium.log 2>&1 &
```

---
