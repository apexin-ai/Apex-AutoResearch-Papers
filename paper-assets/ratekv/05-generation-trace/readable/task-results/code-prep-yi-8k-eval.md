# code prep yi 8k eval

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_yi_8k_eval_20260516T053019_result.json`
- **Structured JSON:** [`43a9ab7c7fe9e2eaa5df.json`](../../sessions/43/43a9ab7c7fe9e2eaa5df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完成。

## 报告

| 检查项 | 状态 |
|--------|------|
| 脚本存在 (`run_yi15_8k_spotcheck.py`) | **Y** |
| Eval data = WikiText-2 test set | **Y** (`wikitext-2-raw-v1`, split=`test`) |
| seq_len = 8192 | **Y** |
| max_2bit = 2 | **Y** |
| Profile 文件存在 (2bit hires + standard) | **Y** |
| 模型文件完整 (4/4 safetensors + config.json) | **Y** |
| 离线数据集 arrow 文件存在 | **Y** |
| 依赖包 (eval_ppl.py, solver.py) | **Y** |
| Import dry-run 通过 | **Y** |
| GPU 可用 | **Y** (2x GPU, torch 2.10.0+cu128) |

**脚本就绪：Y**

**注意事项**：数据盘 `/root/autodl-tmp` 使用率 97%（剩余 9.4GB）。Yi-1.5-9B bf16 加载约 18GB 显存，单卡 A6000（48GB）足够。脚本硬编码 `cuda:0`，不会用到第二张卡。

**推荐启动命令**：
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/ratekv && nohup python run_yi15_8k_spotcheck.py > /tmp/yi15_8k_spotcheck.log 2>&1 &
```

**预估运行时间**：~15-25 分钟（模型加载 ~3min + 3 次 8K stride PPL eval ~4-6min 每次 + solver 开销）

---
