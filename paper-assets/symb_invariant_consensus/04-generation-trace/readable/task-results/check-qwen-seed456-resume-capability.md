# check qwen seed456 resume capability

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_qwen-seed456-resume-capability_20260523T051215_result.json`
- **Structured JSON:** [`f12f7cffe3d0283beb04.json`](../../sessions/f1/f12f7cffe3d0283beb04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All clear. Here's the report:

---

## Resume 检查结果

### 1. results.json 状态
- 路径: `/root/symb_invariant_consensus/results/multi_seed/qwen25_pw_seed456/results.json`
- 结构: `{"summary": {...}, "results": [...]}`
- **已完成 478 / 600 条**（summary.n = 478，problem_id 出现 956 次 = 478×2）
- 文件完整（JSON 正常闭合，tail 显示 `}` 结尾）

### 2. 脚本 resume 支持
`run_full_mvp.py` **原生支持 `--resume`**（line 210）：
- 读取已有 output 文件中的 `results` 数组
- 提取 `completed_ids = {r["problem_id"] for r in completed_results}`
- 过滤 `remaining = [p for p in problems if p["id"] not in completed_ids]`
- 从第 479 条继续，不会重跑已完成的 478 条

### 3. 恢复命令

原始脚本 `multiseed_qwen25_pw_cuda0.sh` 使用 port 8005。恢复只需在原命令基础上加 `--resume`：

```bash
cd /root/symb_invariant_consensus
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

python run_full_mvp.py \
  --mode vllm --api-base "http://localhost:8005/v1" --k 12 --temperature 0.7 \
  --seed 456 \
  --math-data "data/empty.json" --pw-data "data/proofwriter_full.json" \
  --output "results/multi_seed/qwen25_pw_seed456/results.json" \
  --save-intermediates \
  --resume
```

前提：port 8005 上的 Qwen2.5-14B vLLM 服务需要在运行。剩余 122 条。

---
