# 诊断报告: alpha_sweep_a050_postd093_s42_fp32

**日期**: 2026-05-20
**服务器**: westd-17855, cuda:4
**结论**: 实验成功完成，Cron 误报

## 诊断结果

### 实验状态: 成功 (EXIT_CODE=0)

- EXIT_CODE 文件内容为 `0`，正常退出
- Sentinel 文件已写入: `EXIT_CODE` (2 bytes, 11:02)
- 全部 11 个 generation (gen_0 ~ gen_10) 完成
- all_metrics.json 完整 (11 条记录)
- analysis_results.json 已生成 (13742 bytes)
- GPU 4 已释放 (0MiB / 0% util / P8 idle)

### Cron 误报原因

Cron 报告 "process dead 5x with no sentinel/W&B — auto-resolved as failed"。
实际情况：进程正常完成后退出，sentinel 文件 EXIT_CODE 已写入。
推测 cron 的 sentinel 检测逻辑与实际文件路径/格式不匹配，或检测窗口内 sentinel 写入尚未刷盘。

### Partial 结果

不适用——实验完整完成，无需抢救。

### 最终 metrics (gen_10)

| metric | value |
|--------|-------|
| perplexity | 32.62 |
| token_entropy | 2.62 |
| effective_rank | 59.74 |
| mauve | 0.0245 |
| distinct_1 | 0.064 |
| distinct_2 | 0.278 |
| distinct_3 | 0.442 |
| ece | 0.102 |

### 重试建议

无需重试。实验结果完整，应直接纳入分析流水线。建议排查 cron sentinel 检测逻辑，避免后续误报。
