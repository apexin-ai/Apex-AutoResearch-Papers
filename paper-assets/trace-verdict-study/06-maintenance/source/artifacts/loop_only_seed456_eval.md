# loop_only_seed456 评估结果

## eval_results.json

```json
{
  "condition": "loop_only",
  "checkpoint_dir": "/root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed456/final",
  "metrics": {
    "accuracy": 0.8663865546218488,
    "majority_baseline": 0.7151260504201681,
    "lift": 0.1512605042016807,
    "majority_class": "pass",
    "n": 1190,
    "pass_precision": 0.9178743961352657,
    "pass_recall": 0.8930669800235017,
    "pass_f1": 0.905300774270399,
    "fail_precision": 0.7486187845303868,
    "fail_recall": 0.799410029498525,
    "fail_f1": 0.7731811697574893
  },
  "confidence_intervals": {
    "accuracy_ci_lower": 0.8470378151260504,
    "accuracy_ci_upper": 0.8840336134453781,
    "majority_baseline_ci_lower": 0.6915966386554622,
    "majority_baseline_ci_upper": 0.738655462184874,
    "lift_ci_lower": 0.12268907563025211,
    "lift_ci_upper": 0.18067226890756305,
    "pass_precision_ci_lower": 0.9004681680331177,
    "pass_precision_ci_upper": 0.9353749943575383,
    "pass_recall_ci_lower": 0.8714256198347108,
    "pass_recall_ci_upper": 0.9140845811049194,
    "pass_f1_ci_lower": 0.8897009655310747,
    "pass_f1_ci_upper": 0.9187609585037989,
    "fail_precision_ci_lower": 0.7054011242647606,
    "fail_precision_ci_upper": 0.7930153268029049,
    "fail_recall_ci_lower": 0.7596410887858194,
    "fail_recall_ci_upper": 0.8395299145299144,
    "fail_f1_ci_lower": 0.7396449704142012,
    "fail_f1_ci_upper": 0.8047833058011855
  }
}
```

## GPU 使用状态

| GPU | 型号 | 显存使用 | 显存总量 | 利用率 |
|-----|------|----------|----------|--------|
| 0 | NVIDIA RTX PRO 6000 Blackwell Server Edition | 88263 MiB | 97887 MiB | 97% |
| 1 | NVIDIA RTX PRO 6000 Blackwell Server Edition | 32851 MiB | 97887 MiB | 100% |

## 活跃训练进程

| PID | 命令 | GPU | 说明 |
|-----|------|-----|------|
| 277054 | `python train/train_sft.py --condition no_trace --seed 42 --output_dir .../codellama13b_no_trace_seed42` | CUDA_VISIBLE_DEVICES=1 | codellama13b_no_trace_seed42 训练中 |

另有多个 CodeLlama-13b 模型下载进程在运行（huggingface-cli download + aria2c）。
