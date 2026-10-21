# ssh exp012 llama preflight

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp012-llama-preflight_20260515T130030_result.json`
- **Structured JSON:** [`ece450467a46c075466e.json`](../../sessions/ec/ece450467a46c075466e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

预检完成，汇报如下：

---

## exp-012 预检结果

### ✅ 就绪项

| 项目 | 状态 | 详情 |
|------|------|------|
| 启动脚本 | ✅ | `scripts/run_exp012_llama.sh` (784B) + `scripts/submit_exp012.sh` |
| run_experiment.py | ✅ | `src/run_experiment.py` (10.5KB)，所有依赖模块均在 `src/` 下 |
| LLaMA 模型 | ✅ | 15 safetensor shards, config.json + tokenizer 齐全, 68GB |
| vllm | ✅ | import 成功 |
| GPU | ✅ | NVIDIA RTX PRO 6000 Blackwell, 96GB VRAM — 跑 70B FP8 绰绰有余 |
| 配置文件 | ✅ | `configs/few_nerd_types.json`, `artifacts/type_embeddings.pt`, `artifacts/sim_matrix.pt` 均存在 |
| 磁盘 | ✅ | 数据盘 53GB 可用 |
| logs 目录 | ✅ | 已存在，submit 脚本可直接写入 |

### ⚠️ 需确认/修复项

1. **数据集不匹配** — 脚本使用 `--dataset fewnerd`，但任务描述说的是 "FewRel confusability study"。脚本参数全部指向 FewNERD（`few_nerd_types.json`、`type_embeddings.pt`、`sim_matrix.pt`）。如果 exp-012 确实是用 LLaMA 重复 **FewNERD** 实验，则没问题；如果要跑 FewRel，脚本需要改。

2. **`--use_all` 参数不存在** — `run_experiment.py` 的 argparse 中没有 `--use_all` 参数。脚本中也未使用。如果不需要此参数则无影响。

3. **Dry-run 未完成** — `ssh_read_only` 无法执行 Python 脚本（需 `ssh_execute`）。`import vllm` 已验证通过，但完整的 `--help` / dry-run 测试需要用 `ssh_execute` 跑一次。

### 脚本关键参数一览

```
MODEL=/root/autodl-tmp/.hf_cache/llama-3.3-70b-instruct-fp8/
--dataset fewnerd
--prompt_version v2
--types_file configs/few_nerd_types.json
--max_samples 1000
--max_model_len 4096
--output_dir artifacts/exp012
--mode exp1 → exp2 (顺序执行)
```

**结论**：环境和依赖均就绪。主要风险是第 1 点数据集不匹配——请确认 exp-012 目标数据集是 FewNERD 还是 FewRel。

---
