"""
Unit tests for src/find_ngrams.py.

Run with:  pytest
(from the repo root, with pandas/tabulate/openpyxl/pytest installed)
"""
import pandas as pd
import pytest

from find_ngrams import (
    splitline,
    sequence_cleaner,
    brute_sequence_matcher,
    pull_lines,
    sequence_matcher_to_dataframe,
    save_dataframe,
)


# ---------------------------------------------------------------------------
# splitline
# ---------------------------------------------------------------------------

def test_splitline_splits_on_default_separators():
    # "，" is one of the default Chinese separators
    assert splitline("你好，世界") == ["你好", "世界"]


def test_splitline_also_splits_on_plain_whitespace():
    # splitline finishes by splitting on ' ', so ordinary spaces
    # act as boundaries too, separator list or not
    assert splitline("hello world") == ["hello", "world"]


def test_splitline_drops_empty_tokens():
    # Two separators next to each other shouldn't produce empty strings
    assert splitline("，，") == []


def test_splitline_custom_separators():
    assert splitline("a|b|c", separators=["|"]) == ["a", "b", "c"]


# ---------------------------------------------------------------------------
# sequence_cleaner
# ---------------------------------------------------------------------------

def test_sequence_cleaner_removes_shorter_contained_sequences():
    result = sequence_cleaner(["ab", "abc", "xyz"])
    # "ab" is contained in "abc", so it should be dropped
    assert set(result) == {"abc", "xyz"}


def test_sequence_cleaner_keeps_equal_length_sequences():
    result = sequence_cleaner(["abc", "xyz"])
    assert set(result) == {"abc", "xyz"}


def test_sequence_cleaner_handles_no_overlap():
    result = sequence_cleaner(["foo", "bar", "baz"])
    assert set(result) == {"foo", "bar", "baz"}


# ---------------------------------------------------------------------------
# brute_sequence_matcher
# ---------------------------------------------------------------------------

def test_brute_sequence_matcher_returns_longest_non_overlapping_match():
    # From the README: AAABBB vs AAABB should return AAABB, not AA/AAB/etc.
    result = brute_sequence_matcher("AAABBB", "AAABB", 2)
    assert result == ["AAABB"]


def test_brute_sequence_matcher_respects_min_length():
    # No shared substring of length 4+ between these strings
    result = brute_sequence_matcher("AAABBB", "AAABB", 6)
    assert result == []


def test_brute_sequence_matcher_no_match_returns_empty_list():
    result = brute_sequence_matcher("abcdef", "ghijkl", 2)
    assert result == []


# ---------------------------------------------------------------------------
# pull_lines
# ---------------------------------------------------------------------------

def test_pull_lines_reads_file_and_maps_lineno_to_filename(tmp_path):
    f = tmp_path / "sample.txt"
    f.write_text("你好，世界\n\n1 this line starts with a digit, should be skipped\n再見\n")

    lines, line_to_file = pull_lines(str(f))

    assert lines == ["你好世界", "再見"]
    assert line_to_file == {0: "sample.txt", 1: "sample.txt"}


def test_pull_lines_accepts_single_filename_or_list(tmp_path):
    f1 = tmp_path / "a.txt"
    f1.write_text("abc\n")
    f2 = tmp_path / "b.txt"
    f2.write_text("def\n")

    lines_single, _ = pull_lines(str(f1))
    lines_list, map_list = pull_lines([str(f1), str(f2)])

    assert lines_single == ["abc"]
    assert lines_list == ["abc", "def"]
    assert map_list == {0: "a.txt", 1: "b.txt"}


# ---------------------------------------------------------------------------
# sequence_matcher_to_dataframe
# ---------------------------------------------------------------------------

def test_sequence_matcher_to_dataframe_finds_overlap(tmp_path):
    a_lines, a_map = pull_lines(_write(tmp_path, "a.txt", "AAABBB\n"))
    b_lines, b_map = pull_lines(_write(tmp_path, "b.txt", "AAABB\n"))

    df = sequence_matcher_to_dataframe(a_lines, b_lines, a_map, b_map, cutoff=2)

    assert list(df.columns) == ["a_file", "b_file", "match", "len"]
    assert len(df) == 1
    row = df.iloc[0]
    assert row["a_file"] == "a.txt"
    assert row["b_file"] == "b.txt"
    assert row["match"] == "AAABB"
    assert row["len"] == 5


def test_sequence_matcher_to_dataframe_empty_when_below_cutoff(tmp_path):
    a_lines, a_map = pull_lines(_write(tmp_path, "a.txt", "AAABBB\n"))
    b_lines, b_map = pull_lines(_write(tmp_path, "b.txt", "AAABB\n"))

    df = sequence_matcher_to_dataframe(a_lines, b_lines, a_map, b_map, cutoff=10)

    assert len(df) == 0


# ---------------------------------------------------------------------------
# save_dataframe
# ---------------------------------------------------------------------------

def test_save_dataframe_writes_csv(tmp_path):
    df = pd.DataFrame({"a": [1], "b": [2]})
    out = tmp_path / "out"
    save_dataframe(df, str(out), format="csv")

    result_file = tmp_path / "out.csv"
    assert result_file.exists()
    assert "a,b" in result_file.read_text()


def test_save_dataframe_writes_excel(tmp_path):
    df = pd.DataFrame({"a": [1], "b": [2]})
    out = tmp_path / "out"
    save_dataframe(df, str(out), format="excel")

    result_file = tmp_path / "out.xlsx"
    assert result_file.exists()
    reloaded = pd.read_excel(result_file)
    assert reloaded["a"].tolist() == [1]


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def _write(tmp_path, name, content):
    """Write `content` to tmp_path/name and return the path as a string."""
    path = tmp_path / name
    path.write_text(content)
    return str(path)
