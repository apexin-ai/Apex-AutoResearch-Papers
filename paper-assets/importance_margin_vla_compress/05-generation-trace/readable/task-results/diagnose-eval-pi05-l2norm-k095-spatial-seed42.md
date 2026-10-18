# diagnose eval pi05 l2norm k095 spatial seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_l2norm_k095_spatial_seed42_20260522T020202_result.json`
- **Structured JSON:** [`f3df1a17230941841a6a.json`](../../sessions/f3/f3df1a17230941841a6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 根因

**网络断连 + 缺少离线模式环境变量。** 模型权重加载成功（~90s），但 preprocessor 初始化时 `AutoTokenizer.from_pretrained('google/paligemma-3b-pt-224')` 内部的 `is_base_mistral()` 无条件调用 `model_info()` API → `[Errno 101] Network is unreachable`。

Tokenizer 缓存完整存在于 `/root/autodl-tmp/.hf_cache/hub/models--google--paligemma-3b-pt-224/`，但 transformers 库即使有本地缓存也会发网络请求（除非设置 `TRANSFORMERS_OFFLINE=1`）。

之前的 k=0.9（07:58 启动）成功是因为当时网络还可用；k=0.95（09:31 启动）时网络已断。

## 服务器状态

- 4× RTX PRO 6000 Blackwell 94GB，GPU 1/2/3 空闲
- 磁盘充足（根 22GB free，数据盘 52GB free）

## 重提交命令

```bash
source /etc/network_turbo && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.95 --suite libero_spatial --n_episodes 50 --seed 42 --gpu 1
```

报告已写入 `artifacts/diag_eval_pi05_l2norm_k095_spatial.md`。

---
