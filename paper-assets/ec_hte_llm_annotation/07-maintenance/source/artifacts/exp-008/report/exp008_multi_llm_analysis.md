# exp-008: Multi-LLM Misclassification Comparison

## Available Models

118 models on proxy:

- babbage-002
- chat-latest
- chatgpt-image-latest
- davinci-002
- gpt-3.5-turbo
- gpt-3.5-turbo-0125
- gpt-3.5-turbo-1106
- gpt-3.5-turbo-16k
- gpt-3.5-turbo-instruct
- gpt-3.5-turbo-instruct-0914
- gpt-4
- gpt-4-0613
- gpt-4-turbo
- gpt-4-turbo-2024-04-09
- gpt-4.1
- gpt-4.1-2025-04-14
- gpt-4.1-mini
- gpt-4.1-mini-2025-04-14
- gpt-4.1-nano
- gpt-4.1-nano-2025-04-14
- gpt-4o
- gpt-4o-2024-05-13
- gpt-4o-2024-08-06
- gpt-4o-2024-11-20
- gpt-4o-mini
- gpt-4o-mini-2024-07-18
- gpt-4o-mini-search-preview
- gpt-4o-mini-search-preview-2025-03-11
- gpt-4o-mini-transcribe
- gpt-4o-mini-transcribe-2025-03-20
- gpt-4o-mini-transcribe-2025-12-15
- gpt-4o-mini-tts
- gpt-4o-mini-tts-2025-03-20
- gpt-4o-mini-tts-2025-12-15
- gpt-4o-search-preview
- gpt-4o-search-preview-2025-03-11
- gpt-4o-transcribe
- gpt-4o-transcribe-diarize
- gpt-5
- gpt-5-2025-08-07
- gpt-5-chat-latest
- gpt-5-codex
- gpt-5-mini
- gpt-5-mini-2025-08-07
- gpt-5-nano
- gpt-5-nano-2025-08-07
- gpt-5-pro
- gpt-5-pro-2025-10-06
- gpt-5-search-api
- gpt-5-search-api-2025-10-14
- gpt-5.1
- gpt-5.1-2025-11-13
- gpt-5.1-chat-latest
- gpt-5.1-codex
- gpt-5.1-codex-max
- gpt-5.1-codex-mini
- gpt-5.2
- gpt-5.2-2025-12-11
- gpt-5.2-chat-latest
- gpt-5.2-codex
- gpt-5.2-pro
- gpt-5.2-pro-2025-12-11
- gpt-5.3-chat-latest
- gpt-5.3-codex
- gpt-5.4
- gpt-5.4-2026-03-05
- gpt-5.4-mini
- gpt-5.4-mini-2026-03-17
- gpt-5.4-nano
- gpt-5.4-nano-2026-03-17
- gpt-5.4-pro
- gpt-5.4-pro-2026-03-05
- gpt-5.5
- gpt-5.5-2026-04-23
- gpt-5.5-pro
- gpt-5.5-pro-2026-04-23
- gpt-audio
- gpt-audio-1.5
- gpt-audio-2025-08-28
- gpt-audio-mini
- gpt-audio-mini-2025-10-06
- gpt-audio-mini-2025-12-15
- gpt-image-1
- gpt-image-1-mini
- gpt-image-1.5
- gpt-image-2
- gpt-image-2-2026-04-21
- gpt-realtime
- gpt-realtime-1.5
- gpt-realtime-2
- gpt-realtime-2025-08-28
- gpt-realtime-mini
- gpt-realtime-mini-2025-10-06
- gpt-realtime-mini-2025-12-15
- gpt-realtime-translate
- gpt-realtime-whisper
- o1
- o1-2024-12-17
- o1-pro
- o1-pro-2025-03-19
- o3
- o3-2025-04-16
- o3-mini
- o3-mini-2025-01-31
- o4-mini
- o4-mini-2025-04-16
- omni-moderation-2024-09-26
- omni-moderation-latest
- sora-2
- sora-2-pro
- text-embedding-3-large
- text-embedding-3-small
- text-embedding-ada-002
- tts-1
- tts-1-1106
- tts-1-hd
- tts-1-hd-1106
- whisper-1

## Models Analyzed

- **gpt-4.1**: 500 valid annotations
- **gpt-4o-mini**: 500 valid annotations
- **gpt-3.5-turbo**: 500 valid annotations
- **gpt-4o**: 500 valid annotations
- **gpt-4-turbo**: 500 valid annotations

## Per-Model Per-Subgroup Misclassification (Positive vs Non-Positive)

| subgroup     |   gpt-3.5-turbo |   gpt-4-turbo |   gpt-4.1 |   gpt-4o |   gpt-4o-mini |
|:-------------|----------------:|--------------:|----------:|---------:|--------------:|
| False_long   |          0      |        0      |    0      |   0      |        0      |
| False_medium |          0.1497 |        0.0749 |    0.1016 |   0.0963 |        0.0802 |
| False_short  |          0.1743 |        0.1743 |    0.1376 |   0.1284 |        0.1193 |
| True_long    |          0      |        0      |    0      |   0      |        0      |
| True_medium  |          0.328  |        0.224  |    0.2    |   0.176  |        0.216  |
| True_short   |          0.3478 |        0.1159 |    0.1739 |   0.1159 |        0.1304 |

## Per-Model Per-Subgroup Accuracy (3-class)

| subgroup     |   gpt-3.5-turbo |   gpt-4-turbo |   gpt-4.1 |   gpt-4o |   gpt-4o-mini |
|:-------------|----------------:|--------------:|----------:|---------:|--------------:|
| False_long   |          0.8333 |        0.8333 |    0.8333 |   0.8333 |        0.8333 |
| False_medium |          0.7059 |        0.738  |    0.6952 |   0.738  |        0.7594 |
| False_short  |          0.633  |        0.6606 |    0.6606 |   0.633  |        0.6606 |
| True_long    |          0.75   |        0.75   |    0.75   |   0.75   |        0.75   |
| True_medium  |          0.512  |        0.632  |    0.632  |   0.648  |        0.672  |
| True_short   |          0.5362 |        0.7246 |    0.6812 |   0.7681 |        0.7826 |

## FPR by Subgroup

| subgroup     |   gpt-3.5-turbo |   gpt-4-turbo |   gpt-4.1 |   gpt-4o |   gpt-4o-mini |
|:-------------|----------------:|--------------:|----------:|---------:|--------------:|
| False_long   |          0      |        0      |    0      |   0      |        0      |
| False_medium |          0.1429 |        0.0417 |    0.0536 |   0.0417 |        0.0417 |
| False_short  |          0.1798 |        0.0899 |    0.1011 |   0.0449 |        0.0562 |
| True_long    |          0      |        0      |    0      |   0      |        0      |
| True_medium  |          0.3776 |        0.2041 |    0.1939 |   0.0918 |        0.1939 |
| True_short   |          0.3929 |        0.1071 |    0.1429 |   0.0714 |        0.1071 |

## FNR by Subgroup

| subgroup     |   gpt-3.5-turbo |   gpt-4-turbo |   gpt-4.1 |   gpt-4o |   gpt-4o-mini |
|:-------------|----------------:|--------------:|----------:|---------:|--------------:|
| False_long   |          0      |        0      |    0      |   0      |        0      |
| False_medium |          0.2105 |        0.3684 |    0.5263 |   0.5789 |        0.4211 |
| False_short  |          0.15   |        0.55   |    0.3    |   0.5    |        0.4    |
| True_long    |          0      |        0      |    0      |   0      |        0      |
| True_medium  |          0.1481 |        0.2963 |    0.2222 |   0.4815 |        0.2963 |
| True_short   |          0.1538 |        0.1538 |    0.3077 |   0.3077 |        0.2308 |

## Delta-pi (max - min misclass rate across subgroups)

| Model | min | max | Δπ | Δπ > 0.05? |
|-------|-----|-----|----|------------|
| gpt-4.1 | 0.0000 | 0.2000 | 0.2000 | YES |
| gpt-4o-mini | 0.0000 | 0.2160 | 0.2160 | YES |
| gpt-3.5-turbo | 0.0000 | 0.3478 | 0.3478 | YES |
| gpt-4o | 0.0000 | 0.1760 | 0.1760 | YES |
| gpt-4-turbo | 0.0000 | 0.2240 | 0.2240 | YES |

## Consistency Analysis

**Highest misclassification subgroup per model:**

- gpt-4.1: `True_medium` (0.2000)
- gpt-4o-mini: `True_medium` (0.2160)
- gpt-3.5-turbo: `True_short` (0.3478)
- gpt-4o: `True_medium` (0.1760)
- gpt-4-turbo: `True_medium` (0.2240)

**Lowest misclassification subgroup per model:**

- gpt-4.1: `False_long` (0.0000)
- gpt-4o-mini: `False_long` (0.0000)
- gpt-3.5-turbo: `False_long` (0.0000)
- gpt-4o: `False_long` (0.0000)
- gpt-4-turbo: `False_long` (0.0000)

Most common worst subgroup: `True_medium` (4/5 models).

**Rank correlation of subgroup misclass rates between models:**

- gpt-4.1 vs gpt-4o-mini: ρ=1.000 (p=0.000)
- gpt-4.1 vs gpt-3.5-turbo: ρ=0.941 (p=0.005)
- gpt-4.1 vs gpt-4o: ρ=0.941 (p=0.005)
- gpt-4.1 vs gpt-4-turbo: ρ=0.941 (p=0.005)
- gpt-4o-mini vs gpt-3.5-turbo: ρ=0.941 (p=0.005)
- gpt-4o-mini vs gpt-4o: ρ=0.941 (p=0.005)
- gpt-4o-mini vs gpt-4-turbo: ρ=0.941 (p=0.005)
- gpt-3.5-turbo vs gpt-4o: ρ=0.824 (p=0.044)
- gpt-3.5-turbo vs gpt-4-turbo: ρ=0.824 (p=0.044)
- gpt-4o vs gpt-4-turbo: ρ=1.000 (p=0.000)

## Key Finding

**All 5 models show Δπ > 0.05**, confirming that subgroup-specific misclassification heterogeneity is not model-specific. The bias mechanism persists across diverse LLM architectures and sizes.
