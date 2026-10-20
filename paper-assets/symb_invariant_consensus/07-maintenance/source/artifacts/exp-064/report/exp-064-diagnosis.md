# exp-064-deepseek-r1-qwen3-8b-folio204 诊断报告

## 结论：实验已正常完成，Cron 误报

### 实际状态

实验 **204/204 全部完成**，日志末尾输出 `FULL_MVP_DONE`。

- 开始时间：2026-05-19 16:56:40
- 结束时间：2026-05-20 02:01:51
- 总耗时：355.6 min（约 5.9 小时）

### Cron 误报原因

Cron 检测到 "process dead 5× with no sentinel/W&B"，原因是：
1. **无 sentinel 文件**：`find /root -name "*sentinel*" -name "*064*"` 返回空——脚本没有写 sentinel 文件
2. **无 W&B 集成**：run_exp064.sh 中没有 `--wandb` 参数，Cron 无法通过 W&B 确认进程存活
3. **进程正常退出**：脚本跑完后 Python 进程自然退出，Cron 检测到进程不存在，误判为异常退出

实验在 05-20 02:01 完成后进程退出，Cron 随后多次探测不到进程，累计 5 次后自动标记为 failed。

### 实验结果

| 指标 | 值 |
|------|-----|
| SICA 准确率 | **83.8% (171/204)** |
| SC 准确率 | **83.8% (171/204)** |
| 总约束提取 | 4839 (去重后 3755) |
| 提取率 | 38.2% |
| 矛盾率 | 1.7% (40/204 题存在矛盾约束) |
| K (采样数) | 12 |
| 温度 | 0.7 |
| 模型 | DeepSeek-R1-0528-Qwen3-8B (vLLM, GPU2) |

SICA 与 SC 准确率完全一致，说明约束聚合在此模型上未带来额外增益。

### 结果文件

- 主结果：`/root/symb_invariant_consensus/results/exp064_deepseek_r1_qwen3_8b_folio204/results.json` (7888行, 204条)
- 中间文件：`intermediates/folio_0.json` ~ `folio_203.json` (204个文件，完整)
- 日志：`exp064.log` (880KB)
- 运行脚本：`scripts/run_exp064.sh`

### 服务器当前状态

- GPU0/GPU1 被 vLLM 占用（其他实验），GPU2/GPU3 空闲
- 磁盘：/root/autodl-tmp 40% 使用 (137G/350G)

### 建议

**无需重跑。** 204/204 已全部完成，结果完整可用。将 Cron 状态从 failed 更正为 completed。

备注：SC 数据可直接用于 Table 1（不受 legacy 代码版本影响）；SICA/delta 如 notes 所述不入 Table 1。
