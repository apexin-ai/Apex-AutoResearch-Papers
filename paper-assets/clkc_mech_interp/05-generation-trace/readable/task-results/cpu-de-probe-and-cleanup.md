# cpu de probe and cleanup

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_de-probe-and-cleanup_20260522T150155_result.json`
- **Structured JSON:** [`8788bbec29413622ebba.json`](../../sessions/87/8788bbec29413622ebba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**磁盘清理**: pip cache purge 清理 376 个文件，当前 30G 用了 21G（68%）。

**DE probe training 已启动**:
- **PID**: 496671（bash wrapper: 496666）
- **服务器**: westd-41302
- **命令**: `--langs en,zh,de --bootstrap_seeds 2000`
- **方向**: 9 个（EN→EN, ZH→ZH, DE→DE, EN→ZH, ZH→EN, EN→DE, DE→EN, ZH→DE, DE→ZH）
- **输出**: `data/llama31/de_probe_results_bootstrap_n2000.json`
- **日志**: `/tmp/de_probe_n2000.log`
- **注册**: exp_id=`de_probe_n2000_112`，状态 RUNNING

**脚本修改**: `train_probe.py` 新增 `--langs` 参数（默认 `en,zh` 向后兼容），动态生成所有单语+跨语言方向。

**预计时间**: 2000 bootstrap × 9 directions × 32 layers，预计 3-5 小时（CPU-only 多核并行中，CPU 2104%）。

**无冲突**: PID 465851（EN/ZH bootstrap）已完成；Gemma probe（PID 476339）在不同数据集上运行，输出文件不同。

---
