# LLaMA-8B SC 实验准备摘要

## 1. 模型位置

| 服务器 | 模型路径 | 状态 |
|--------|----------|------|
| westd-16639 | `/root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct` | ✅ 完整（4 shards） |
| westd-25068 | 无 LLaMA-3.1-8B-Instruct | ❌ 需下载或从 16639 使用 |

## 2. exp-063 已有结果（westd-16639）

- 路径: `/root/symb_invariant_consensus/results/exp-063-llama8b-folio204-16639/`
- SC 准确率: **66.18%** (135/204)，SICA: 61.76% (126/204)
- K=12, vLLM 模式, 总耗时 9336s

### Per-trace 数据可复用性

**results.json**: 每题有 `sc_vote_distribution`（聚合计数，如 `{"True": 4, "Unknown": 7, "False": 1}`），无逐 trace 答案。

**intermediates/ (204 files)**: 每题有完整的 12 条 traces，每条含 `answer` 和 `trace_idx` 字段。
- 示例: `intermediates/folio_0.json` → `sica_result.traces[i].answer`
- **可直接用于 κ 计算，无需重新跑 SC。**

## 3. 草拟启动命令（如需重跑）

### vLLM 服务端（选端口需确认）
```bash
cd /root/symb_invariant_consensus
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
VLLM_USE_FLASHINFER_SAMPLER=0 python -m vllm.entrypoints.openai.api_server \
  --model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct \
  --port 80XX --enforce-eager --gpu-memory-utilization 0.9
```

### SC 实验
```bash
cd /root/symb_invariant_consensus
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
python run_full_mvp.py \
  --mode vllm --k 12 --temperature 0.7 --seed 42 \
  --api-base http://localhost:80XX/v1 --model auto \
  --folio-data data/folio_full.json \
  --math-data data/empty.json --pw-data data/empty.json \
  --output results/exp_llama8b_folio204_sc/results.json \
  --save-intermediates
```

### run_full_mvp.py 可用参数
| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--mode` | vllm | mock/vllm/api |
| `--k` | 12 | trace 数量 |
| `--model` | auto | 模型名 |
| `--api-base` | http://localhost:8000/v1 | vLLM endpoint |
| `--temperature` | 0.7 | 采样温度 |
| `--seed` | None | 随机种子 |
| `--folio-data` | None | FOLIO 数据路径 |
| `--math-data` | data/math500_subset.json | MATH 数据 |
| `--pw-data` | data/proofwriter_subset.json | ProofWriter 数据 |
| `--output` | results/mvp_full_results.json | 输出路径 |
| `--save-intermediates` | false | 保存中间结果 |
| `--resume` | false | 断点续跑 |
| `--max-tokens` | 4096 | 最大 token 数 |

## 4. 待 Director 确认事项

1. **是否需要重跑 SC？** exp-063 intermediates 已有 per-trace 答案，可直接提取用于 κ 计算。仅当需要不同 seed 或参数时才需重跑。
2. **端口分配**: westd-16639 上 vLLM 使用哪个端口（80XX）？需检查是否有其他 vLLM 进程占用。
3. **服务器选择**: 模型仅在 westd-16639 上，如需在 westd-25068 运行需先下载（ModelScope: `LLM-Research/Meta-Llama-3.1-8B-Instruct`）。
4. **exp-063 的 seed**: 需确认 exp-063 使用的 seed 值（日志中可查），以判断是否与目标实验参数一致。

## 5. 其他 LLaMA-8B 实验记录

| 实验 | 服务器 | 路径 | 说明 |
|------|--------|------|------|
| exp-063 | westd-16639 | results/exp-063-llama8b-folio204-16639/ | FOLIO-204, SC=66.18% |
| exp048 | westd-16639 | results/exp048_llama8b_pw600/ | ProofWriter-600 |
| exp069 | westd-16639 | results/exp069_llama8b_logiqa200/ | LogiQA-200 |
| exp072/072b | westd-16639 | results/exp072_llama8b_logiqa200/ | LogiQA-200 |
| exp034 | westd-25068 | results/exp034_llama31_8b_folio204/ | FOLIO-204（仅日志） |
