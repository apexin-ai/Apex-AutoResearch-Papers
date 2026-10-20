"""Structural trace segmentation based on call subtrees, loop iterations, and exception chains.

Input: List[TraceEvent] from trace_collector.
Output: List[TraceSegment] with semantic boundaries (function calls, loops, exceptions).
"""
from __future__ import annotations

import logging
from typing import List

from dtd_types import TraceEvent, TraceSegment, estimate_tokens

logger = logging.getLogger(__name__)


class StructuralSegmenter:
    def __init__(self, max_recursion_depth: int = 10, min_segment_events: int = 2):
        self.max_recursion_depth = max_recursion_depth
        self.min_segment_events = min_segment_events

    def segment(self, events: List[TraceEvent]) -> List[TraceSegment]:
        call_subtrees = self._extract_call_subtrees(events)
        loop_iterations = self._extract_loop_iterations(events)
        exception_chains = self._extract_exception_chains(events)
        basic_blocks = self._extract_basic_blocks(events)
        merged = self._merge_and_deduplicate([exception_chains, call_subtrees, loop_iterations, basic_blocks])
        logger.info(
            "Segmented %d events into %d segments (calls=%d, loops=%d, exceptions=%d, blocks=%d)",
            len(events), len(merged), len(call_subtrees), len(loop_iterations), len(exception_chains), len(basic_blocks),
        )
        return merged

    def _extract_call_subtrees(self, events: List[TraceEvent]) -> List[TraceSegment]:
        segments = []
        i = 0
        n = len(events)
        call_stack: List[str] = []

        while i < n:
            ev = events[i]
            if ev.event_type == "call":
                start_depth = ev.call_depth
                start_idx = i
                fname = ev.function_name

                recursion_count = call_stack.count(fname)
                is_recursive = recursion_count > 0
                if recursion_count >= self.max_recursion_depth:
                    i += 1
                    continue

                call_stack.append(fname)
                j = i + 1
                while j < n:
                    ej = events[j]
                    if ej.event_type == "return" and ej.call_depth == start_depth:
                        j += 1
                        break
                    if ej.call_depth < start_depth:
                        break
                    j += 1

                call_stack.pop()
                subtree_events = events[start_idx:j]
                if len(subtree_events) >= self.min_segment_events:
                    seg = TraceSegment(
                        segment_type="call_subtree",
                        events=subtree_events,
                        start_idx=start_idx,
                        end_idx=j - 1,
                        metadata={
                            "function_name": fname,
                            "call_depth": start_depth,
                            "is_recursive": is_recursive,
                        },
                    )
                    segments.append(seg)
            i += 1
        return segments

    def _extract_loop_iterations(self, events: List[TraceEvent]) -> List[TraceSegment]:
        segments = []
        if not events:
            return segments

        iteration_start = 0
        loop_start_line = None
        current_func = None
        current_file = None

        for i in range(1, len(events)):
            ev = events[i]
            prev = events[i - 1]

            if ev.event_type != "line" or prev.event_type != "line":
                continue
            if ev.filename != prev.filename or ev.function_name != prev.function_name:
                continue

            is_back_jump = ev.lineno < prev.lineno

            if is_back_jump:
                if loop_start_line is None:
                    loop_start_line = ev.lineno
                    current_func = ev.function_name
                    current_file = ev.filename
                    iteration_start = i

                if (ev.function_name == current_func and ev.filename == current_file
                        and ev.lineno == loop_start_line):
                    iter_events = events[iteration_start:i]
                    if len(iter_events) >= self.min_segment_events:
                        seg = TraceSegment(
                            segment_type="loop_iteration",
                            events=iter_events,
                            start_idx=iteration_start,
                            end_idx=i - 1,
                            metadata={
                                "loop_start_line": loop_start_line,
                                "function_name": current_func,
                            },
                        )
                        segments.append(seg)
                    iteration_start = i

            if (ev.event_type == "line" and loop_start_line is not None
                    and (ev.function_name != current_func or ev.filename != current_file)):
                if i - iteration_start >= self.min_segment_events:
                    iter_events = events[iteration_start:i]
                    seg = TraceSegment(
                        segment_type="loop_iteration",
                        events=iter_events,
                        start_idx=iteration_start,
                        end_idx=i - 1,
                        metadata={
                            "loop_start_line": loop_start_line,
                            "function_name": current_func,
                        },
                    )
                    segments.append(seg)
                loop_start_line = None

        if loop_start_line is not None and len(events) - iteration_start >= self.min_segment_events:
            iter_events = events[iteration_start:]
            seg = TraceSegment(
                segment_type="loop_iteration",
                events=iter_events,
                start_idx=iteration_start,
                end_idx=len(events) - 1,
                metadata={
                    "loop_start_line": loop_start_line,
                    "function_name": current_func,
                },
            )
            segments.append(seg)

        return segments

    def _extract_exception_chains(self, events: List[TraceEvent]) -> List[TraceSegment]:
        segments = []
        visited = set()
        n = len(events)

        for i, ev in enumerate(events):
            if ev.event_type != "exception" or i in visited:
                continue

            start_idx = i
            exc_type = ev.exception_info[0] if ev.exception_info else "Unknown"
            raise_depth = ev.call_depth
            visited.add(i)

            current_min_depth = raise_depth
            j = i + 1
            while j < n:
                ej = events[j]
                if ej.event_type == "exception" and ej.call_depth < current_min_depth:
                    current_min_depth = ej.call_depth
                    visited.add(j)
                    j += 1
                    continue
                if ej.event_type == "return" and ej.call_depth >= current_min_depth:
                    j += 1
                    continue
                if ej.call_depth >= raise_depth:
                    j += 1
                    continue
                if ej.call_depth < current_min_depth and ej.event_type not in ("exception", "return"):
                    break
                if ej.event_type == "call" and ej.call_depth <= current_min_depth:
                    break
                j += 1

            chain_events = events[start_idx:j]
            if len(chain_events) >= self.min_segment_events:
                catch_depth = current_min_depth
                catch_line = events[j - 1].lineno if j > start_idx else None
                seg = TraceSegment(
                    segment_type="exception_chain",
                    events=chain_events,
                    start_idx=start_idx,
                    end_idx=j - 1,
                    metadata={
                        "exception_type": exc_type,
                        "raise_line": ev.lineno,
                        "raise_depth": raise_depth,
                        "catch_depth": catch_depth,
                        "catch_line": catch_line,
                        "propagation_depth": raise_depth - catch_depth,
                    },
                )
                segments.append(seg)
        return segments

    def _extract_basic_blocks(self, events: List[TraceEvent]) -> List[TraceSegment]:
        MIN_BLOCK_EVENTS = 5
        segments = []
        n = len(events)
        i = 0
        while i < n:
            ev = events[i]
            if ev.event_type != "line":
                i += 1
                continue
            block_start = i
            block_func = ev.function_name
            block_file = ev.filename
            block_depth = ev.call_depth
            prev_lineno = ev.lineno
            i += 1
            while i < n:
                ei = events[i]
                if ei.function_name != block_func or ei.filename != block_file:
                    break
                if ei.call_depth != block_depth:
                    break
                if ei.event_type in ("call", "return", "exception"):
                    break
                if ei.event_type == "line" and ei.lineno < prev_lineno:
                    break
                if ei.event_type == "line":
                    prev_lineno = ei.lineno
                i += 1
            block_events = events[block_start:i]
            if len(block_events) >= MIN_BLOCK_EVENTS:
                segments.append(TraceSegment(
                    segment_type="basic_block",
                    events=block_events,
                    start_idx=block_start,
                    end_idx=i - 1,
                    metadata={
                        "function_name": block_func,
                        "call_depth": block_depth,
                    },
                ))
        return segments

    def _merge_and_deduplicate(self, segments_list: List[List[TraceSegment]]) -> List[TraceSegment]:
        all_segments = []
        for sl in segments_list:
            all_segments.extend(sl)

        if not all_segments:
            return []

        max_idx = max(s.end_idx for s in all_segments) + 1
        covered = bytearray(max_idx)
        merged = []

        priority_order = ["exception_chain", "loop_iteration", "call_subtree", "basic_block"]
        for seg_type in priority_order:
            type_segs = [s for s in all_segments if s.segment_type == seg_type]
            type_segs.sort(key=lambda s: s.end_idx - s.start_idx)
            for seg in type_segs:
                total = seg.end_idx - seg.start_idx + 1
                overlap = sum(covered[seg.start_idx:seg.end_idx + 1])
                if overlap <= total * 0.3:
                    merged.append(seg)
                    for i in range(seg.start_idx, seg.end_idx + 1):
                        covered[i] = 1

        merged.sort(key=lambda s: s.start_idx)

        MAX_SEGMENTS = 20
        if len(merged) > MAX_SEGMENTS:
            step = len(merged) / MAX_SEGMENTS
            merged = [merged[int(i * step)] for i in range(MAX_SEGMENTS)]

        return merged


if __name__ == "__main__":
    import time
    from dtd_types import TraceEvent

    events = [
        TraceEvent("call", "outer", "test.py", 10, {}, 1, time.time()),
        TraceEvent("line", "outer", "test.py", 11, {}, 1, time.time()),
        TraceEvent("call", "wrapper", "test.py", 30, {}, 2, time.time()),
        TraceEvent("line", "wrapper", "test.py", 31, {}, 2, time.time()),
        TraceEvent("call", "helper", "test.py", 20, {}, 3, time.time()),
        TraceEvent("line", "helper", "test.py", 21, {"x": 1}, 3, time.time()),
        TraceEvent("exception", "helper", "test.py", 21, {}, 3, time.time(),
                   exception_info=("TypeError", "bad type", "")),
        TraceEvent("return", "helper", "test.py", 21, {}, 3, time.time()),
        TraceEvent("exception", "wrapper", "test.py", 31, {}, 2, time.time(),
                   exception_info=("TypeError", "bad type", "")),
        TraceEvent("return", "wrapper", "test.py", 31, {}, 2, time.time()),
        TraceEvent("exception", "outer", "test.py", 11, {}, 1, time.time(),
                   exception_info=("TypeError", "bad type", "")),
        TraceEvent("line", "outer", "test.py", 12, {}, 1, time.time()),
        TraceEvent("return", "outer", "test.py", 12, {}, 1, time.time()),
    ]

    segmenter = StructuralSegmenter()
    segments = segmenter.segment(events)
    for s in segments:
        print(f"  [{s.segment_type}] idx={s.start_idx}-{s.end_idx} "
              f"events={len(s.events)} meta={s.metadata}")
