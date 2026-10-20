# westd-11672 宕机恢复 Checklist

**创建时间**: 2026-05-18
**背景**: westd-11672 SSH 端口关闭，4 个 MATH-500 eval + 1 个 GSM8K eval 状态未知。恢复后按本文档顺序执行。

## 宕机前实验状态快照

| 实验 | GPU | 进度 | 最后已知 acc | 状态 |
|------|-----|------|-------------|------|
| eval_math500_grpo_unpruned | cuda:2 | 500/500 | 69.0% | **已完成** |
| eval_math500_grpo_standard_20 | cuda:1 | 438/500 | 28.3%@300 | 接近完成 |
| eval_math500_grpo_rasp_20_v3 | cuda:3 | 422/500 | 25.0%@400 | 接近完成 |
| eval_math500_sft_cka_only_20_v2 | cuda:0 | 101/500 | 39.0%@100 | 早期阶段 |
| eval_gsm8k_grpo_cka_only_20 | cuda:2 | 未知 | 未知 | 刚启动即宕机 |

---

## Step 1: 检查服务器状态

```bash
# 确认 SSH 恢复
ssh westd-11672 "hostname && nvidia-smi --query-gpu=index,memory.used,memory.total,utilization.gpu --format=csv,noheader"

# 检查是否有残留进程
ssh westd-11672 "ps aux | grep -E 'python|eval_math|eval_gsm' | grep -v grep"
```

---

## Step 2: 检查结果文件（可能宕机前已完成）

```bash
# === eval_math500_grpo_unpruned (已确认完成，验证结果文件存在) ===
cat /root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_unpruned.json 2>/dev/null && echo "COMPLETE" || echo "NO RESULT FILE"

# === eval_math500_grpo_standard_20 (438/500, 可能已完成) ===
cat /root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_standard_20.json 2>/dev/null && echo "COMPLETE" || echo "NO RESULT FILE"
tail -20 ~/runs/recovery_aware_struct_prune/eval_math500_grpo_standard_20.log

# === eval_math500_grpo_rasp_20_v3 (422/500, 可能已完成) ===
cat /root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_rasp_20_v3.json 2>/dev/null && echo "COMPLETE" || echo "NO RESULT FILE"
tail -20 ~/runs/recovery_aware_struct_prune/eval_math500_grpo_rasp_20_v3.log

# === eval_math500_sft_cka_only_20_v2 (101/500, 大概率中断) ===
cat /root/autodl-tmp/recovery_aware_struct_prune/results/math500_sft_cka_only_20_v2.json 2>/dev/null && echo "COMPLETE" || echo "NO RESULT FILE"
tail -20 ~/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_20_v2.log

# === eval_gsm8k_grpo_cka_only_20 (刚启动，大概率中断) ===
cat /root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_cka_only_20.json 2>/dev/null && echo "COMPLETE" || echo "NO RESULT FILE"
tail -20 /tmp/eval_gsm8k_grpo_cka_only_20.log
```

---

## Step 3: 读取已完成实验的结果

```python
import json, glob

result_dir = "/root/autodl-tmp/recovery_aware_struct_prune/results"
targets = [
    "math500_grpo_unpruned",
    "math500_grpo_standard_20",
    "math500_grpo_rasp_20_v3",
    "math500_sft_cka_only_20_v2",
    "gsm8k_grpo_cka_only_20",
]

for name in targets:
    path = f"{result_dir}/{name}.json"
    try:
        with open(path) as f:
            data = json.load(f)
        # 尝试常见 key
        acc = data.get("accuracy") or data.get("acc") or data.get("score") or data.get("exact_match")
        total = data.get("total") or data.get("num_samples") or data.get("n")
        print(f"[DONE] {name}: accuracy={acc}, total={total}")
    except FileNotFoundError:
        print(f"[MISS] {name}: no result file")
    except Exception as e:
        print(f"[ERR]  {name}: {e}")
```

---

## Step 4: 重提交中断的实验

**优先级**: standard_20 > rasp_20_v3 > sft_cka_only_20_v2 > gsm8k_grpo_cka_only_20

先检查 eval 脚本是否支持 resume：
```bash
grep -n "resume\|skip\|exist\|already" /root/recovery_aware_struct_prune/scripts/eval_math500.py | head -20
```

### 4a. eval_math500_grpo_standard_20 (如未完成)

```python
# submit_training_job 格式
# GPU: cuda:1 | 预计时间: ~10 min (仅剩 62/500 samples)
# 如果支持 resume，脚本会自动跳过已完成 samples
submit_training_job(
    server="westd-11672",
    account="root",
    job_name="eval_math500_grpo_standard_20",
    gpu_id=1,
    command="cd /root/recovery_aware_struct_prune && python scripts/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/checkpoints/grpo_standard_20 --output /root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_standard_20.json",
    log_file="~/runs/recovery_aware_struct_prune/eval_math500_grpo_standard_20.log"
)
```

### 4b. eval_math500_grpo_rasp_20_v3 (如未完成)

```python
# GPU: cuda:3 | 预计时间: ~12 min (仅剩 78/500 samples)
submit_training_job(
    server="westd-11672",
    account="root",
    job_name="eval_math500_grpo_rasp_20_v3",
    gpu_id=3,
    command="cd /root/recovery_aware_struct_prune && python scripts/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/checkpoints/grpo_rasp_20_v3 --output /root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_rasp_20_v3.json",
    log_file="~/runs/recovery_aware_struct_prune/eval_math500_grpo_rasp_20_v3.log"
)
```

### 4c. eval_math500_sft_cka_only_20_v2 (大概率需要重跑)

```python
# GPU: cuda:0 | 预计时间: ~35-40 min (399/500 samples 需要跑，或全部 500 如不支持 resume)
submit_training_job(
    server="westd-11672",
    account="root",
    job_name="eval_math500_sft_cka_only_20_v2",
    gpu_id=0,
    command="cd /root/recovery_aware_struct_prune && python scripts/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/checkpoints/sft_cka_only_20_v2 --output /root/autodl-tmp/recovery_aware_struct_prune/results/math500_sft_cka_only_20_v2.json",
    log_file="~/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_20_v2.log"
)
```

### 4d. eval_gsm8k_grpo_cka_only_20 (最低优先级)

```python
# GPU: cuda:2 | 预计时间: ~50-60 min (GSM8K 1319 samples, 需从头跑)
# 注意: 这个实验 log 在 /tmp，宕机后可能丢失
submit_training_job(
    server="westd-11672",
    account="root",
    job_name="eval_gsm8k_grpo_cka_only_20",
    gpu_id=2,
    command="cd /root/recovery_aware_struct_prune && python scripts/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/checkpoints/grpo_cka_only_20 --output /root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_cka_only_20.json",
    log_file="~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_cka_only_20.log"
)
```

---

## Step 5: GPU 分配方案

| GPU | 实验 | 优先级 | 备注 |
|-----|------|--------|------|
| cuda:0 | eval_math500_sft_cka_only_20_v2 | P3 | 重跑，耗时最长 |
| cuda:1 | eval_math500_grpo_standard_20 | P1 | 可能已完成，检查后决定 |
| cuda:2 | eval_gsm8k_grpo_cka_only_20 | P4 | 从头跑，unpruned 已完成释放此 GPU |
| cuda:3 | eval_math500_grpo_rasp_20_v3 | P2 | 可能已完成，检查后决定 |

**GPU 释放后的复用**:
- cuda:1 完成 standard_20 后 → 空闲，可接新任务
- cuda:3 完成 rasp_20_v3 后 → 空闲，可接新任务
- cuda:0 和 cuda:2 预计耗时较长

---

## 注意事项

1. **先检查后提交**: Step 2 中 standard_20 和 rasp_20_v3 宕机前已接近完成，有可能在宕机前写入了结果文件
2. **/tmp 日志丢失**: eval_gsm8k_grpo_cka_only_20 的 log 写在 /tmp，宕机重启后可能被清理。重提交时改用 ~/runs/ 路径
3. **磁盘空间**: 提交前检查数据盘空间 `df -h /root/autodl-tmp`
4. **结果汇总**: 所有 eval 完成后，汇总到 analysis_recent_results 更新实验对比表
