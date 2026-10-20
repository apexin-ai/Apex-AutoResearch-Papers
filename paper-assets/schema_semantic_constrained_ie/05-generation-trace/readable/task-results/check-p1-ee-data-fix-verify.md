# check p1 ee data fix verify

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_p1_ee_data_fix_verify_20260518T193606_result.json`
- **Structured JSON:** [`0b96884e249c4df67357.json`](../../sessions/0b/0b96884e249c4df67357.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
SFT splits: train=194, dev=20, test=20
文件修改时间：修复后（SFT文件 May 19 03:29 服务器时间 ≈ 19:29 UTC May 18，晚于修复时间）
重叠验证：train∩dev=0 OK, train∩test=0 OK, dev∩test=0 OK
total unique docs: 234
scenario_en_kairos_30: test.jsonl=1, all.jsonl=1, train/dev=0（正确排除）
训练状态：p1_ee_ft session 存在，但有报错
GPU 利用率：GPU1 85%, 18923MiB/97887MiB
```

**数据泄漏修复验证通过** — 三组 split 零重叠，scenario_en_kairos_30 仅在 test/all 中，未泄漏到 SFT 训练集。

**训练有问题** — tmux 捕获显示两个错误：
1. `RuntimeError: WandbCallback requires wandb` — 缺少 wandb
2. `[Errno 101] Network is unreachable` — 尝试从 HuggingFace 下载 `qwen3_8b_lora_wikievents_merged/config.json` 失败，正在重试 (Retry 1/5)

GPU1 有进程在跑（85% 利用率），但 tmux 最后输出停在网络重试。可能是训练脚本尝试从远程加载 merged checkpoint 而服务器无外网。需要确认模型路径是否应指向本地路径。

---
