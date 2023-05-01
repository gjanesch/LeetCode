 class Solution:
    """
    Maintains a list of the current closest points, then if one shows
    up that's closer than any others, replace the farthest-out point in
    the set with it.  Repeat until complete.
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k < len(points):
            closest_points = points[:k]
            closest_distances = [math.sqrt(p[0]**2 + p[1]**2) for p in points[:k]]
            largest_distance = max(closest_distances)
            for pt in points[k:]:
                current_distance = math.sqrt(pt[0]**2 + pt[1]**2)
                if current_distance < largest_distance:
                    replacement_index = closest_distances.index(largest_distance)
                    closest_points[replacement_index] = pt
                    closest_distances[replacement_index] = current_distance
                    largest_distance = max(closest_distances)
            return closest_points
        else:
            return points
