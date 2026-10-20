# code mvp seed0 replication v2

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp_seed0_replication_v2_20260514T004040_result.json`
- **Structured JSON:** [`afa75e26782f3f54c17a.json`](../../sessions/af/afa75e26782f3f54c17a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功启动。

**完成摘要：**

1. **磁盘清理** — 删除 G0/G1/G2 共 15 个中间 checkpoints（各 ~5.7G），释放 ~85G。磁盘从 98%（7.1G 可用）降到 64%（92G 可用）。final_model/ 和 metrics.jsonl 均保留。

2. **KL bug** — 已修复（`effective_vocab = max(arr_a.max()+1, arr_b.max()+1, vocab_size)`），服务器上的 metrics.py 已包含该补丁。

3. **launch_seed0.sh** — 服务器上已存在且配置正确（seed=0, output_dir=output_seed0）。

4. **Dry-run** — 验证通过（数据加载正常、tokenize 正常、无导入错误）。

5. **实验已提交** — `mvp_seed0_replication`, PID=122711, tmux session=`mvp_seed0_replication`, 正在 tokenize 阶段。日志：`/root/autodl-tmp/pilot_seed0.log`。

---
