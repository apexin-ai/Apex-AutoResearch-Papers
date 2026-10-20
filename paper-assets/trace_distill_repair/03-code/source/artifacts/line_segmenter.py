"""Line-level trace segmentation baseline.

Splits trace events into fixed-size windows or single-line segments.
Used as a comparison baseline against structural segmentation.
"""
from __future__ import annotations

import logging
from typing import List

from dtd_types import TraceEvent, TraceSegment

logger = logging.getLogger(__name__)


class LineSegmenter:
    def __init__(self, window_size: int = 5, stride: int = 5):
        self.window_size = window_size
        self.stride = stride

    def segment(self, events: List[TraceEvent]) -> List[TraceSegment]:
        segments = []
        n = len(events)
        window_index = 0

        i = 0
        while i < n:
            end = min(i + self.window_size, n)
            window_events = events[i:end]
            seg = TraceSegment(
                segment_type="line_window",
                events=window_events,
                start_idx=i,
                end_idx=end - 1,
                metadata={"window_size": self.window_size, "window_index": window_index},
            )
            segments.append(seg)
            window_index += 1
            i += self.stride

        logger.info("Line segmentation: %d events -> %d windows (size=%d, stride=%d)",
                     n, len(segments), self.window_size, self.stride)
        return segments

    def segment_single_line(self, events: List[TraceEvent]) -> List[TraceSegment]:
        segments = []
        for i, ev in enumerate(events):
            seg = TraceSegment(
                segment_type="line_window",
                events=[ev],
                start_idx=i,
                end_idx=i,
                metadata={"window_size": 1, "window_index": i},
            )
            segments.append(seg)
        logger.info("Single-line segmentation: %d events -> %d segments", len(events), len(segments))
        return segments


if __name__ == "__main__":
    import time
    from dtd_types import TraceEvent

    events = [
        TraceEvent("line", "func", "test.py", i, {"x": i}, 1, time.time())
        for i in range(12)
    ]

    segmenter = LineSegmenter(window_size=5, stride=5)
    segments = segmenter.segment(events)
    print(f"Window segments: {len(segments)}")
    for s in segments:
        print(f"  [{s.segment_type}] idx={s.start_idx}-{s.end_idx} events={len(s.events)} "
              f"meta={s.metadata}")

    single = segmenter.segment_single_line(events)
    print(f"\nSingle-line segments: {len(single)}")
