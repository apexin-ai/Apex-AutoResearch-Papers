# eval llama3b adaptive lm eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_llama3b_adaptive_lm_eval_20260517T144557_result.json`
- **Structured JSON:** [`de7ce2aef3650f7fac72.json`](../../sessions/de/de7ce2aef3650f7fac72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

MMLU 数据准备阶段较慢（可能在下载 57 个子任务数据），进程正常运行（2m22s, 27.5% CPU）。MMLU 评估预计总共 1-2 小时。

当前状态总结：
- **HellaSwag (10-shot) 已完成**: acc_norm = **0.7249**
- **MMLU (5-shot) 正在运行**: PID 110816, 预计 1-2 小时

要我继续等 MMLU 结果，还是你稍后手动检查？检查命令：

```bash
# 检查是否完成
ps -p 110816 -o etime --no-headers

# 查看结果
cat /tmp/llama3b_adaptive_mmlu.log | tail -50

# 查看 JSON 结果
source /root/miniconda3/bin/activate && python -c "
import json, glob
files = glob.glob('/root/autodl-tmp/provenance_weight_training/output/eval/llama3b_adaptive_lm_eval/*/results_*.json')
for f in sorted(files):
    d = json.load(open(f))
    for k,v in d['results'].items():
        print(f'{k}: {v}')
"
```

---
