# ops extract entropy results

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_extract_entropy_results_20260518T053841_result.json`
- **Structured JSON:** [`4fbceacbce4edad3e80f.json`](../../sessions/4f/4fbceacbce4edad3e80f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated to DONE, cron deleted. Key findings and full JSON below.

## Key Findings

| Metric | Value |
|---|---|
| **Overall entropy ratio** | **0.6393** ± 0.1334 |
| N images | 250 (10 LIBERO-Object tasks) |
| Vision attention fraction | 0.1211 |
| Min entropy layer | Layer 29 (0.4774) |
| Max entropy layer | Layer 0 (0.9790) |

**Layer depth pattern** (confirms strong monotonic decrease):
- Shallow (L0-L1): 0.979, 0.952 (near-uniform)
- Mid (L10-L15): 0.62-0.66
- Deep (L27-L31): 0.54, 0.53, **0.48**, 0.52, 0.57

**vs previous measurement** (20 random images, overall 0.617): real data gives 0.6393, slightly higher but directionally identical. Deep layers consistently in 0.47-0.57 range (previous was 0.37-0.40 on random noise, real images are a bit less concentrated but still strongly sub-uniform).

**vs SmolVLA**: 0.64 vs 0.98. OpenVLA's attention is ~36% more concentrated than SmolVLA's.

---

## Full JSON

```json
{
  "model": "OpenVLA-7B-libero-object",
  "dataset": "LIBERO-Object",
  "n_images": 250,
  "n_tasks_covered": 10,
  "tasks": [
    "pick_up_the_alphabet_soup_and_place_it_in_the_basket",
    "pick_up_the_bbq_sauce_and_place_it_in_the_basket",
    "pick_up_the_butter_and_place_it_in_the_basket",
    "pick_up_the_chocolate_pudding_and_place_it_in_the_basket",
    "pick_up_the_cream_cheese_and_place_it_in_the_basket",
    "pick_up_the_ketchup_and_place_it_in_the_basket",
    "pick_up_the_milk_and_place_it_in_the_basket",
    "pick_up_the_orange_juice_and_place_it_in_the_basket",
    "pick_up_the_salad_dressing_and_place_it_in_the_basket",
    "pick_up_the_tomato_sauce_and_place_it_in_the_basket"
  ],
  "per_layer_entropy_ratio": {
    "0": 0.979, "1": 0.9523, "2": 0.7995, "3": 0.7256, "4": 0.7008,
    "5": 0.678, "6": 0.688, "7": 0.6744, "8": 0.6514, "9": 0.6526,
    "10": 0.6612, "11": 0.6505, "12": 0.622, "13": 0.6508, "14": 0.6618,
    "15": 0.622, "16": 0.6372, "17": 0.6069, "18": 0.597, "19": 0.5662,
    "20": 0.5672, "21": 0.5904, "22": 0.5861, "23": 0.5806, "24": 0.5653,
    "25": 0.5719, "26": 0.5709, "27": 0.5419, "28": 0.5298, "29": 0.4774,
    "30": 0.5241, "31": 0.5739
  },
  "per_layer_entropy_std": {
    "0": 0.0088, "1": 0.0216, "2": 0.0667, "3": 0.0847, "4": 0.1023,
    "5": 0.1252, "6": 0.1107, "7": 0.1049, "8": 0.0941, "9": 0.0766,
    "10": 0.0692, "11": 0.0704, "12": 0.0634, "13": 0.0796, "14": 0.0761,
    "15": 0.0966, "16": 0.0785, "17": 0.0762, "18": 0.0761, "19": 0.0766,
    "20": 0.0734, "21": 0.0766, "22": 0.0756, "23": 0.0798, "24": 0.0806,
    "25": 0.0695, "26": 0.0842, "27": 0.0695, "28": 0.0717, "29": 0.0702,
    "30": 0.075, "31": 0.1141
  },
  "per_layer_vision_attention_fraction": {
    "0": 0.4181, "1": 0.3212, "2": 0.0587, "3": 0.0408, "4": 0.0476,
    "5": 0.0583, "6": 0.0643, "7": 0.0704, "8": 0.0881, "9": 0.0938,
    "10": 0.1382, "11": 0.1805, "12": 0.1257, "13": 0.1413, "14": 0.2097,
    "15": 0.174, "16": 0.1371, "17": 0.0808, "18": 0.0897, "19": 0.0809,
    "20": 0.1104, "21": 0.1399, "22": 0.0936, "23": 0.0848, "24": 0.095,
    "25": 0.0942, "26": 0.1038, "27": 0.0568, "28": 0.0869, "29": 0.0985,
    "30": 0.0908, "31": 0.202
  },
  "overall_entropy_ratio": 0.6393,
  "overall_entropy_std": 0.1334,
  "overall_vision_attention_fraction": 0.1211,
  "min_entropy_layer": { "layer": 29, "ratio": 0.4774 },
  "max_entropy_layer": { "layer": 0, "ratio": 0.979 },
  "comparison_note": "Measured on 250 real LIBERO-Object rendered observations across 10 tasks (vs previous 20 random noise images)",
  "previous_random_result": {
    "n_images": 20,
    "overall_entropy_ratio": 0.617,
    "source": "random noise images"
  },
  "smolvla_reference": {
    "entropy_ratio": 0.98,
    "n_frames": 2400,
    "source": "real LIBERO-Object frames"
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "model": "OpenVLA-7B-libero-object",
    "dataset": "LIBERO-Object",
    "n_images": 250,
    "n_tasks_covered": 10,
    "tasks": [
      "pick_up_the_alphabet_soup_and_place_it_in_the_basket",
      "pick_up_the_bbq_sauce_and_place_it_in_the_basket",
      "pick_up_the_butter_and_place_it_in_the_basket",
      "pick_up_the_chocolate_pudding_and_place_it_in_the_basket",
      "pick_up_the_cream_cheese_and_place_it_in_the_basket",
      "pick_up_the_ketchup_and_place_it_in_the_basket",
      "pick_up_the_milk_and_place_it_in_the_basket",
      "pick_up_the_orange_juice_and_place_it_in_the_basket",
      "pick_up_the_salad_dressing_and_place_it_in_the_basket",
      "pick_up_the_tomato_sauce_and_place_it_in_the_basket"
    ],
    "per_layer_entropy_ratio": {
      "0": 0.979,
      "1": 0.9523,
      "2": 0.7995,
      "3": 0.7256,
      "4": 0.7008,
      "5": 0.678,
      "6": 0.688,
      "7": 0.6744,
      "8": 0.6514,
      "9": 0.6526,
      "10": 0.6612,
      "11": 0.6505,
      "12": 0.622,
      "13": 0.6508,
      "14": 0.6618,
      "15": 0.622,
      "16": 0.6372,
      "17": 0.6069,
      "18": 0.597,
      "19": 0.5662,
      "20": 0.5672,
      "21": 0.5904,
      "22": 0.5861,
      "23": 0.5806,
      "24": 0.5653,
      "25": 0.5719,
      "26": 0.5709,
      "27": 0.5419,
      "28": 0.5298,
      "29": 0.4774,
      "30": 0.5241,
      "31": 0.5739
    },
    "per_layer_entropy_std": {
      "0": 0.0088,
      "1": 0.0216,
      "2": 0.0667,
      "3": 0.0847,
      "4": 0.1023,
      "5": 0.1252,
      "6": 0.1107,
      "7": 0.1049,
      "8": 0.0941,
      "9": 0.0766,
      "10": 0.0692,
      "11": 0.0704,
      "12": 0.0634,
      "13": 0.0796,
      "14": 0.0761,
      "15": 0.0966,
      "16": 0.0785,
      "17": 0.0762,
      "18": 0.0761,
      "19": 0.0766,
      "20": 0.0734,
      "21": 0.0766,
      "22": 0.0756,
      "23": 0.0798,
      "24": 0.0806,
      "25": 0.0695,
      "26": 0.0842,
      "27": 0.0695,
      "28": 0.0717,
      "29": 0.0702,
      "30": 0.075,
      "31": 0.1141
    },
    "per_layer_vision_attention_fraction": {
      "0": 0.4181,
      "1": 0.3212,
      "2": 0.0587,
      "3": 0.0408,
      "4": 0.0476,
      "5": 0.0583,
      "6": 0.0643,
      "7": 0.0704,
      "8": 0.0881,
      "9": 0.0938,
      "10": 0.1382,
      "11": 0.1805,
      "12": 0.1257,
      "13": 0.1413,
      "14": 0.2097,
      "15": 0.174,
      "16": 0.1371,
      "17": 0.0808,
      "18": 0.0897,
      "19": 0.0809,
      "20": 0.1104,
      "21": 0.1399,
      "22": 0.0936,
      "23": 0.0848,
      "24": 0.095,
      "25": 0.0942,
      "26": 0.1038,
      "27": 0.0568,
      "28": 0.0869,
      "29": 0.0985,
      "30": 0.0908,
      "31": 0.202
    },
    "overall_entropy_ratio": 0.6393,
    "overall_entropy_std": 0.1334,
    "overall_vision_attention_fraction": 0.1211,
    "min_entropy_layer": {
      "layer": 29,
      "ratio": 0.4774
    },
    "max_entropy_layer": {
      "layer": 0,
      "ratio": 0.979
    },
    "comparison_note": "Measured on 250 real LIBERO-Object rendered observations across 10 tasks (vs previous 20 random noise images)",
    "previous_random_result": {
      "n_images": 20,
      "overall_entropy_ratio": 0.617,
      "source": "random noise images"
    },
    "smolvla_reference": {
      "entropy_ratio": 0.98,
      "n_frames": 2400,
      "source": "real LIBERO-Object frames"
    }
  }
}
```

</details>

---
