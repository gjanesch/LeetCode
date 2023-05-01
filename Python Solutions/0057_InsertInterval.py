class Solution:
    """
    This solution just iterates over the list of intervals while
    tracking whether overlaps have been found yet.  As such, the main
    while loop has essentially two states:
    1. If no overlap has been found, then intervals will just be added
    to the new interval list as appropriate.
    2. If an overlap has been found, then successive intervals from the
    original list that overlap with the merged interval will be added
    until either we've run through the original intervals or the next
    interval from the list doesn't overlap.
    """
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        new_intervals = []
        merged_interval = [None, None]
        overlap_found = False
        overlap_added = False
        while intervals:
            ival = intervals.pop(0)
            if not overlap_found:
                if ival[1] < newInterval[0]:
                    # interval from list is still fully below
                    # newInterval, so append ival
                    new_intervals.append(ival)
                elif ival[0] > newInterval[1]:
                    # interval from list is fully above newInterval, so
                    # append newInterval and the remaining intervals --
                    # and we're done since nothing can overlap anymore
                    new_intervals.append(newInterval)
                    new_intervals.append(ival)
                    new_intervals.extend(intervals)
                    return new_intervals
                else:
                    # there's an overlap, so merge and set the flag to
                    # move to the other mode of the while loop
                    overlap_found = True
                    merged_interval = [min(ival[0], newInterval[0]), max(ival[1], newInterval[1])]
            else:
                if ival[0] <= merged_interval[1]:
                    # if there's still overlap, merge
                    merged_interval[1] = max(merged_interval[1], ival[1])
                else:
                    # if there's no more overlap, add the merged
                    # interval and everything that remains
                    new_intervals.append(merged_interval)
                    new_intervals.append(ival)
                    new_intervals.extend(intervals)
                    return new_intervals

        if not overlap_found:
            new_intervals.append(newInterval)
        else:
            new_intervals.append(merged_interval)
        return new_intervals
