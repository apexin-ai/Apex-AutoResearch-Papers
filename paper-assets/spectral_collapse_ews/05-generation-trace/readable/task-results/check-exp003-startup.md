# check exp003 startup

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp003_startup_20260517T040517_result.json`
- **Structured JSON:** [`cc2786999542215f1329.json`](../../sessions/cc/cc2786999542215f1329.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

| 检查项 | 状态 |
|--------|------|
| PID 77663 存活 | ✓ 存在 |
| tmux session exp_003 | ✓ 存在 |
| Checkpoint 路径指向 autodl-tmp | ✓ `/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/adaptive_seed42/` |
| GPU cuda:1 使用 | **✗ cuda:1 空闲（0% util, 3MiB）** |

### 问题：网络不可达导致模型下载失败

日志显示 HuggingFace 连接失败（`Network is unreachable`），正在重试下载 `EleutherAI/pythia-410m-deduped` tokenizer。进程卡在模型加载阶段，尚未开始训练。

重试 5 次后大概率会 crash。需要确认：
1. 服务器是否有外网访问权限，或需要配置代理
2. 模型是否已有本地缓存（如有可设置 `HF_HUB_OFFLINE=1` 跳过网络请求）

要我检查本地是否已有 pythia-410m-deduped 缓存？

---
