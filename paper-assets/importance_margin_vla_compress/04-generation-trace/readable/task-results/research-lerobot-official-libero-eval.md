# research lerobot official libero eval

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_lerobot_official_libero_eval_20260516T163536_result.json`
- **Structured JSON:** [`a6b5c42f89d6a48e2b01.json`](../../sessions/a6/a6b5c42f89d6a48e2b01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：**B. 有官方通用 eval pipeline 支持 LIBERO，且服务器已安装**

### 官方方案

lerobot 已内置 LIBERO eval 支持，服务器上已安装：
- **eval 脚本**: `/root/miniconda3/lib/python3.12/site-packages/lerobot/scripts/lerobot_eval.py`
- **LIBERO env wrapper**: `/root/miniconda3/lib/python3.12/site-packages/lerobot/envs/libero.py`（内含 `check_success()` → `is_success` metric）

### 官方 eval 命令

```bash
lerobot-eval \
  --policy.path=&lt;checkpoint_path_or_hub_id> \
  --env.type=libero \
  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=10 \
  --policy.device=cuda
```

`--policy.path` 接受 Hub model ID 或本地目录（需包含 `config.json` + `model.safetensors`）。

### 与项目 checkpoint 的兼容性

项目已有自写的 `eval_success_rate.py`（基于 gym_aloha 环境，非 LIBERO）。要用官方 `lerobot-eval` 跑 LIBERO，checkpoint 需为 lerobot 标准格式（`config.json` + `model.safetensors`）。项目当前 checkpoint 是 `checkpoint.pt` 格式，**需要格式转换**才能使用官方 pipeline。

### 两个可选路径

| 方案 | 优点 | 缺点 |
|------|------|------|
| 用官方 `lerobot-eval --env.type=libero` | 零代码、multi-suite 一键跑、metric 标准化 | 需将 checkpoint 转为 lerobot pretrained_model 格式 |
| 自写 eval（参考已有 `eval_success_rate.py`，把 env 从 gym_aloha 换成 libero） | 直接读 `.pt` checkpoint、灵活控制 ACIS pruning 逻辑 | 需自己集成 libero env + rollout 逻辑 |

Sources:
- [lerobot LIBERO 官方文档](https://huggingface.co/docs/lerobot/en/libero)
- [lerobot_eval.py 源码](https://github.com/huggingface/lerobot/blob/main/src/lerobot/scripts/lerobot_eval.py)
- [SmolVLA LIBERO eval issue #1316](https://github.com/huggingface/lerobot/issues/1316)
- [lerobot-libero fork](https://github.com/huggingface/lerobot-libero)
- [SmolVLA 文档](https://huggingface.co/docs/lerobot/en/smolvla)

---
