# infra comet diagnose restart

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_comet_diagnose_restart_20260521T230831_result.json`
- **Structured JSON:** [`bc38a5e5beb908eb7b78.json`](../../sessions/bc/bc38a5e5beb908eb7b78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 COMET 进程运行正常：

- **Qwen** (PID 59407, GPU 0): COMET 模型已加载，正在 back-translate 798 条，GPU 利用率 28%
- **Llama** (PID 59566, GPU 2): COMET 模型已加载，正在 back-translate 1096 条，GPU 利用率 39%

## 诊断总结

| 项目 | 结论 |
|------|------|
| **死因** | `EXIT_CODE=124` — 被 `submit_training_job` 的 timeout 命令杀死，非 OOM |
| **首次启动失败** | 忘加 `source /etc/network_turbo` 或 `TRANSFORMERS_OFFLINE=1`，COMET 内部 xlm-roberta-large 加载时尝试连 HuggingFace 失败 |
| **解决** | 用 `TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1` + nohup 直接启动，绕过 timeout 限制和网络依赖 |
| **重复 bootstrap** | PID 57240 已 kill（与 57514 重复的 llama bootstrap） |
| **无 resume** | validate_translation.py 无断点续传，必须从头跑 |

## 预计耗时

- Qwen: 798 train + 168 test ≈ 966 条 × ~10s/条 ≈ **2.7 小时** + COMET 评分
- Llama: 1096 train + 272 test ≈ 1368 条 × ~10s/条 ≈ **3.8 小时** + COMET 评分

## 监控命令

```bash
tail -5 /root/clkc_mech_interp/logs/comet_qwen_restart.log
tail -5 /root/clkc_mech_interp/logs/comet_llama_restart.log
```

---
