class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        q = deque()
        zeros = 0

        for r in range(rows):
            if board[r][0] == "O":
                q.append([r,0])
            if board[r][cols - 1] == "O":
                q.append([r,cols-1])

        for c in range(cols):
            if board[0][c] == "O":
                q.append([0,c])
            if board[rows - 1][c] == "O":
                q.append([rows-1,c])
        
        while q:
            r, c = q.popleft()
            directions = [[0,1], [0,-1], [1,0], [-1,0]]
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (row in range(rows) and
                    col in range(cols) and
                    board[row][col] == "O"):
                    board[row][col] = "Z"
                    q.append([row,col])

        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "Z":
                    board[r][c] = "O"
