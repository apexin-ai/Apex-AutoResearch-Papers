# ops llama70b check and infer

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama70b_check_and_infer_20260523T144433_result.json`
- **Structured JSON:** [`810b822154abfd0b8348.json`](../../sessions/81/810b822154abfd0b8348.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. 下载状态：**IN_PROGRESS** (28/30)

| 分片 | 状态 | 进度 | 速度 | ETA |
|------|------|------|------|-----|
| 00020 | 下载中 | ~65% (2.81G/4.34G) | 410 kB/s | ~60 min |
| 00027 | 下载中 | 51% (2.23G/4.34G) | 732 kB/s | ~52 min |
| 其余 28 个 | 完成 | 100% | - | - |

**预计完成时间**：约 50-60 分钟（受限于 model-00020 的慢速连接）

### 2. 磁盘空间
- 数据盘：350G 总量，283G 已用（81%），68G 可用
- pth 原始文件占用 116G（下载完成后可删除释放空间）

### 3. 推理脚本已就绪
- 脚本路径：`/root/nlp_variance_gtheory/scripts/exp_llama70b/run_llama70b_inference.py`
- 输出目录：`/root/nlp_variance_gtheory/data/exp_llama70b/`
- 设计：5 benchmarks × 288 conditions × 200 items = 288,000 evals
- 每 benchmark：2 temps × 6 prompts × 6 seeds × 4 orderings = 288 条件
- MMLU 优先运行
- TP=4（全部 4 张 RTX PRO 6000）
- Dry-run 验证通过

### 4. 下载完成后需执行的步骤

a) 删除 pth 文件释放 116G：
```bash
rm -rf /root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-70B-Instruct/original/
rm -rf /root/autodl-tmp/.hf_cache/._____temp/
```

b) 创建软链接：
```bash
ln -sfn /root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-70B-Instruct /root/autodl-tmp/models/Llama-3.1-70B-Instruct
```

c) 验证模型完整性

d) 启动推理命令：
```
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/nlp_variance_gtheory && python scripts/exp_llama70b/run_llama70b_inference.py
```

---
