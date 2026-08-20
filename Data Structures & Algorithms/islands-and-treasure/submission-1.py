class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()
        dist = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if (
                        row not in range(ROWS)
                        or col not in range(COLS)
                        or (row, col) in visit
                        or grid[row][col] == -1
                    ):
                        continue
                    visit.add((row, col))
                    q.append([row, col])
            dist += 1
