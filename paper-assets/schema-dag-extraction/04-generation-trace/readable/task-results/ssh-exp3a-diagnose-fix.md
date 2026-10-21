# ssh exp3a diagnose fix

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp3a-diagnose-fix_20260515T024903_result.json`
- **Structured JSON:** [`2bcc9cf70050030d9832.json`](../../sessions/2b/2bcc9cf70050030d9832.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本正常启动，参数解析通过，embeddings 加载成功，开始 extraction。

---

## 诊断结果

**1. 失败根因**
`python3 run_experiment.py` — 文件不在项目根目录，实际路径是 `src/run_experiment.py`。Python 报 `can't open file: No such file or directory`，EXIT_CODE=2。

**2. 修复内容**
- 脚本路径：`run_experiment.py` → `src/run_experiment.py`
- 缺少必需参数：`--types_file configs/few_nerd_types.json`
- 前置依赖：`artifacts/type_embeddings.pt` 不存在，已用 `compute_type_embeddings.py` 生成

**3. 验证结果**
脚本能正常启动，参数解析通过，embeddings 加载成功，开始 extraction 阶段。

**4. 正确的提交命令**

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/schema-dag-extraction && python3 src/run_experiment.py --mode exp1 --prompt_version v2 --eval_mode text_match --model_path /root/autodl-tmp/.hf_cache/qwen3-32b-fp8/ --types_file configs/few_nerd_types.json --max_samples 1000 && python3 src/run_experiment.py --mode exp2 --prompt_version v2 --eval_mode text_match --model_path /root/autodl-tmp/.hf_cache/qwen3-32b-fp8/ --types_file configs/few_nerd_types.json --max_samples 1000"
```

---
