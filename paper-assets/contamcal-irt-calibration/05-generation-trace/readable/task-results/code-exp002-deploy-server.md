# code exp002 deploy server

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp002-deploy-server_20260514T100325_result.json`
- **Structured JSON:** [`170316d34ef60ce5cc3a.json`](../../sessions/17/170316d34ef60ce5cc3a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

本地和服务器代码均已同步更新。

## 部署结果汇总

| 项目 | 状态 |
|------|------|
| 8 个代码文件写入服务器 `/root/contamcal-irt-calibration/exp002/` | ✅ |
| 依赖检查（faiss-cpu, sentence-transformers, scikit-learn, torch, transformers, peft） | ✅ 全部已装 |
| `compute_signals.py --help` dry-run | ✅ 通过 |
| 全模块 import 测试 | ✅ 通过 |
| 0.5B eval 数据（d000/d005/d100 s42） | ✅ 3 个目录均有 eval_results.json |
| SFT 数据（sft_dosage_000/005/025/050/100.jsonl） | ✅ |
| Checkpoint 路径 | ✅ 已修正 `merged` → `lora_adapter` |
| LoRA 加载（signal_minkpp + signal_selfcritique） | ✅ 已 patch 为 PEFT 自动检测 + merge_and_unload |

**发现并修正的问题**：
1. **faiss-gpu 不可用**，但 faiss-cpu 1.13.2 已装，代码已有 GPU→CPU fallback 逻辑
2. **Checkpoint 是 LoRA adapter 而非 merged model** — 修改了 `signal_minkpp.py`、`signal_selfcritique.py` 的模型加载函数，自动检测 adapter_config.json 并用 PEFT 加载+merge；同时修正 `run_exp002.sh` 路径

**注意**：部分 eval 目录（如 `Qwen2.5-0.5B_d000_s42_para`、`Qwen2.5-1.5B_d100_s42`）为空目录（size=6），ConStat signal 在缺少 paraphrase eval 时会自动跳过。

---
