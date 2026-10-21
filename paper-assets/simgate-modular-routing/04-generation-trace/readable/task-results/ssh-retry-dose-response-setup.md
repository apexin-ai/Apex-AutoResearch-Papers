# ssh retry dose response setup

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_retry-dose-response-setup_20260518T030600_result.json`
- **Structured JSON:** [`4f037fe1b44e772d2a32.json`](../../sessions/4f/4f037fe1b44e772d2a32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### 1. Wrapper 脚本
已写入 `/root/autodl-tmp/simgate-modular-routing/run_dose_response_full.sh`，权限 `-rwxr-xr-x`。注意：原始任务模板缺少 `source /root/miniconda3/bin/activate`，已补上。

### 2. 验证检查结果

| 检查项 | 结果 |
|--------|------|
| vllm 可导入 | vllm 0.21.0 |
| port 8000 | 空闲 |
| GPU 占用 | 4× RTX PRO 6000 Blackwell 96GB，全部 0 MiB / 0% 利用率 |
| run_retry_dose_response.py 语法 | syntax OK |

### 3. `run_retry_dose_response.py` 实际参数接口

```
--n-values          str, default="1,5,10"     逗号分隔的 retry N 值
--episodes-per-task int, default=20
--max-steps         int, default=30
--model             str, default="Qwen2.5-7B-Instruct"
--api-base          str, default="http://localhost:8000/v1"
--output-dir        str                        (有默认值，未完整显示)
--seed              int, default=42
--dry-run           flag
```

wrapper 脚本中的 `--n-values 1,5,10 --episodes-per-task 20` 完全匹配。

### 4. 启动命令

```bash
cd /root/autodl-tmp/simgate-modular-routing && bash run_dose_response_full.sh
```

或用 nohup / submit_training_job：
```bash
nohup bash /root/autodl-tmp/simgate-modular-routing/run_dose_response_full.sh > /root/autodl-tmp/simgate-modular-routing/logs/wrapper.log 2>&1 &
```

---
