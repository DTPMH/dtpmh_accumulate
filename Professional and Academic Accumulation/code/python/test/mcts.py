import math
import random
import time
import matplotlib.pyplot as plt
from matplotlib import font_manager
# 设置中文字体（Windows 建议用微软雅黑）
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
from copy import deepcopy


# ---------- 游戏逻辑 ----------
class TicTacToe:
    """井字棋游戏类，负责游戏状态管理和逻辑判断"""
    
    def __init__(self):
        """初始化游戏棋盘（9个空位）和玩家（X先手）"""
        self.board = [" "] * 9
        self.current_player = "X"

    def clone(self):
        """克隆当前游戏状态，返回一个独立的游戏副本"""
        clone = TicTacToe()
        clone.board = self.board[:]
        clone.current_player = self.current_player
        return clone

    def available_moves(self):
        """返回棋盘上所有可用位置的列表（未被占据的位置）"""
        return [i for i in range(9) if self.board[i] == " "]

    def play_move(self, move):
        """在指定位置下棋，然后切换当前玩家"""
        self.board[move] = self.current_player
        self.current_player = "O" if self.current_player == "X" else "X"

    def winner(self):
        """检查是否有赢家，返回赢家标记（'X'或'O'）或None"""
        wins = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in wins:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return self.board[a]
        return None

    def is_terminal(self):
        """判断游戏是否结束（有赢家或棋盘满）"""
        return self.winner() is not None or " " not in self.board


# ---------- 可视化 ----------
def draw_board(state, highlight=None, title=""):
    """绘制井字棋盘
    
    参数:
        state: TicTacToe 游戏状态
        highlight: 需要高亮显示的位置索引
        title: 图表标题
    """
    plt.clf()
    plt.title(title)
    plt.xlim(-0.5, 2.5)
    plt.ylim(-0.5, 2.5)
    plt.xticks([])
    plt.yticks([])
    for i in range(1, 3):
        plt.axhline(i - 0.5, color="black", lw=2)
        plt.axvline(i - 0.5, color="black", lw=2)

    for i, mark in enumerate(state.board):
        r, c = divmod(i, 3)
        if mark == "X":
            color = "red"
        elif mark == "O":
            color = "blue"
        else:
            color = "gray"
        if highlight == i:
            plt.gca().add_patch(plt.Rectangle((c - 0.5, 2 - r - 0.5), 1, 1, color='yellow', alpha=0.3))
        if mark != " ":
            plt.text(c, 2 - r, mark, fontsize=48, ha='center', va='center', color=color)
    plt.pause(0.8)


# ---------- MCTS 节点 ----------
class Node:
    """MCTS 搜索树的节点类，管理节点状态、访问统计和子节点"""
    
    def __init__(self, state, parent=None, move=None):
        """初始化节点
        
        参数:
            state: 该节点对应的游戏状态
            parent: 父节点引用
            move: 从父节点到该节点的移动
        """
        self.state = state
        self.parent = parent
        self.move = move
        self.children = []
        self.visits = 0
        self.wins = 0
        self.untried_moves = state.available_moves()

    def is_fully_expanded(self):
        """判断该节点是否已完全展开（所有未尝试的移动都已尝试过）"""
        return len(self.untried_moves) == 0

    def best_child(self, c_param=1.4):
        """使用UCB（Upper Confidence Bound）算法选择最优子节点
        
        参数:
            c_param: 探索参数（默认1.4），控制探索vs利用的权衡
            
        返回:
            权重最高的子节点
        """
        weights = [
            (c.wins / (c.visits + 1e-8)) +
            c_param * math.sqrt(math.log(self.visits + 1) / (c.visits + 1e-8))
            for c in self.children
        ]
        return self.children[weights.index(max(weights))]

    def expand(self):
        """展开节点：从未尝试的移动中选择一个，创建新的子节点
        
        返回:
            新创建的子节点
        """
        move = self.untried_moves.pop()
        new_state = self.state.clone()
        new_state.play_move(move)
        child = Node(new_state, parent=self, move=move)
        self.children.append(child)
        return child

    def update(self, result):
        """更新节点的访问统计信息
        
        参数:
            result: 模拟结果（1表示X胜，0表示O胜或平局，0.5表示平局等）
        """
        self.visits += 1
        self.wins += result


# ---------- 随机模拟 ----------
def simulate(state):
    """从指定状态开始进行随机游玩，直到游戏结束，返回结果
    
    参数:
        state: 当前游戏状态
        
    返回:
        1: X胜利
        0: O胜利
        0.5: 平局
    """
    s = state.clone()
    while not s.is_terminal():
        moves = s.available_moves()
        s.play_move(random.choice(moves))
    winner = s.winner()
    if winner == "X": return 1
    elif winner == "O": return 0
    else: return 0.5


# ---------- 带动画的 MCTS ----------
def mcts_visual_steps(root_state, iter_limit=10):
    """执行 MCTS 搜索算法并显示动画演示
    
    MCTS四个阶段：
    1. Selection（选择）：沿着已建立的树向下选择，直到找到未完全展开的节点
    2. Expansion（展开）：向树中添加一个新的子节点
    3. Simulation（模拟）：从新节点进行随机游玩到游戏结束
    4. Backpropagation（回溯）：将游玩结果沿着树向上回溯，更新节点统计
    
    参数:
        root_state: 初始游戏状态
        iter_limit: 迭代次数（默认10）
    """
    root = Node(root_state)
    plt.ion()
    draw_board(root_state, title="初始局面")

    for i in range(iter_limit):
        node = root
        state = root_state.clone()

        # 1️⃣ Selection（选择阶段）：找到最有前景的未完全展开的节点
        while node.is_fully_expanded() and node.children:
            node = node.best_child()
            state.play_move(node.move)
            draw_board(state, highlight=node.move, title=f"选择阶段：扩展到节点 {node.move}")

        # 2️⃣ Expansion（展开阶段）：向未完全展开的节点添加一个新子节点
        if not node.is_fully_expanded() and not state.is_terminal():
            new_node = node.expand()
            state.play_move(new_node.move)
            draw_board(state, highlight=new_node.move, title=f"扩展阶段：新节点 {new_node.move}")
            node = new_node

        # 3️⃣ Simulation（模拟阶段）：从新节点进行随机游玩到游戏结束
        result_state = state.clone()
        draw_board(result_state, title="模拟阶段：随机游玩中")
        result = simulate(result_state)
        draw_board(result_state, title=f"模拟完成 → {'X胜' if result == 1 else 'O胜' if result == 0 else '平局'}")

        # 4️⃣ Backpropagation（回溯阶段）：将结果沿着树向上回溯，更新所有访问过的节点
        while node is not None:
            node.update(result if node.state.current_player == "O" else 1 - result)
            node = node.parent
        draw_board(state, title=f"第 {i+1} 次迭代完成 ✅")

    plt.ioff()
    draw_board(root_state, title="搜索结束")
    plt.show()


# ---------- 主程序 ----------
if __name__ == "__main__":
    game = TicTacToe()
    mcts_visual_steps(game, iter_limit=15)
