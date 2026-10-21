# 诊断报告: exp_001_eval_llama32_3B_d000_s42_v3

## 结论：监控误报，实验实际已成功完成

## 根因

**监控 false positive**。进程经历多次重启后最终完成，但 `/tmp/agent-ml-exit/exp_001_eval_llama32_3B_d000_s42_v3.exit` 从未创建。监控系统 5 次检查 PID 807025 均发现已死亡且无 sentinel，遂自动标记 failed。

实际上输出目录 `Llama-3.2-3B_d000_s42_aligned/` 已包含全部结果和 `.done` 标记。

## 时间线重建

| 时间 | 事件 |
|------|------|
| v2 (May 16 15:28) | OOM killed，exit code **137** (`/tmp/agent-ml-exit/exp_001_eval_llama32_3B_d000_s42_v2.exit`) |
| v3 attempt 1 (May 16 22:37) | 启动，完成 MMLU (23:08)，GSM8K 跑到 ~33% 后进程死亡 (`/tmp/llama_eval_d000_s42.log`) |
| v3 attempt 2 (May 16 23:36) | 重启，从 HF cache 离线加载数据集，顺序完成 gsm8k (01:54)→arc (01:56)→humaneval (02:13) (`/tmp/eval_llama_d000_remaining.log`) |
| May 17 02:13 | `.done` 写入，全部 benchmark 完成 |

## 产出验证

输出目录 `/root/autodl-tmp/exp001/eval_results/Llama-3.2-3B_d000_s42_aligned/` 内容完整：

```
.done                   (May 17 02:13)
mmlu_results.json       (May 16 23:08, 1.3MB)
gsm8k_results.json      (May 17 01:54, 127KB)
arc_challenge_results.json (May 17 01:56, 110KB)
humaneval_results.json  (May 17 02:13, 100KB)
eval_results.json       (May 17 02:13, 401KB)
item_responses.json     (May 17 02:13, 457KB)
correctness_matrix.json (May 17 02:13, 18KB)
```

`eval_results.json` 确认 model_path 为 `/root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d000_s42/merged`。

## 关键日志摘录

**v2 OOM kill:**
```
137|2026-05-16T15:28:25Z  (exit code 137 = SIGKILL/OOM)
```

**v3 attempt 1 — HF 网络问题 + 进程中断:**
```
[WARNING] HTTPSConnectionPool(host='huggingface.co'): Max retries exceeded ... Connection refused
Evaluating GSM8K: 33%|███▎ | 434/1319 [42:57<...] (日志在此截断，进程死亡)
```

**v3 attempt 2 — 成功:**
```
Using the latest cached version of the dataset since openai/gsm8k couldn't be found on the Hugging Face Hub (offline mode is enabled).
```

## 进程死亡原因

1. **v2**: OOM killed (exit 137)，Llama-3.2-3B 生成任务（GSM8K 需 max_new_tokens）显存峰值超出单卡 24GB
2. **v3 attempt 1**: 可能同样 OOM（GSM8K 生成阶段 33% 时死亡），加上 HuggingFace 网络不通增加了加载开销
3. **v3 attempt 2**: 用 HF cache 离线模式避开网络问题，且可能跳过了已完成的部分样本，最终成功

## 修复建议

1. **无需重跑** — 结果已完整，应将实验状态更正为 completed
2. **监控改进** — 监控应同时检查 output-dir 中的 `.done` 文件，不应仅依赖 `/tmp/agent-ml-exit/` sentinel
3. **未来 Llama-3.2-3B eval**: 考虑 `--batch-size 2` 降低 GSM8K 生成阶段显存峰值，避免 OOM 重启
4. **网络**: `source /etc/network_turbo` 或设 `HF_HUB_OFFLINE=1`（如数据集已缓存），避免 HF 连接超时浪费时间
