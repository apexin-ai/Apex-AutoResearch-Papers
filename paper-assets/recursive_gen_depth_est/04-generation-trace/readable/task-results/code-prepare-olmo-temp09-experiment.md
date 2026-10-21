# code prepare olmo temp09 experiment

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare_olmo_temp09_experiment_20260514T203351_result.json`
- **Structured JSON:** [`b48b61da6e4ad21c6a19.json`](../../sessions/b4/b48b61da6e4ad21c6a19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

### 结果汇总

| 检查项 | 状态 |
|--------|------|
| Registry 条目 `cross_model_olmo_temp09_001` | PENDING, hypothesis/parent 已设置 |
| 模型文件 `/root/autodl-tmp/models/olmo-1b-hf/` | 存在，model.safetensors 4.7GB |
| 数据文件 `data/depth_0.jsonl` | 存在，10.5MB |
| 脚本语法检查 `bash -n` | SYNTAX_OK |

### 提交命令

cuda:1 空出后可直接执行：

```bash
cd /root/autodl-tmp/recursive_gen_depth_est && GPU=1 AML_EXP_ID=cross_model_olmo_temp09_001 nohup bash scripts/run_pipeline_olmo_temp09.sh > logs/pipeline_olmo_temp09.log 2>&1 &
```

脚本配置确认：
- 模型：`/root/autodl-tmp/models/olmo-1b-hf`
- target_modules：`q_proj,k_proj,v_proj`
- 解码：`temp_only`, temperature=0.9
- 递归深度：0→1→2→3（3轮 finetune + 3轮 generate）

---
