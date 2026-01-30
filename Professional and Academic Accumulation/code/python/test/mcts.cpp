#include <iostream>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <iomanip>

using namespace std;

// ---------- 游戏逻辑 ----------
class TicTacToe {
    /**
     * 井字棋游戏类，负责游戏状态管理和逻辑判断
     */
public:
    vector<char> board;      // 9个棋盘位置
    char current_player;     // 当前玩家（'X'或'O'）

    /**
     * 初始化游戏棋盘（9个空位）和玩家（X先手）
     */
    TicTacToe() {
        board = vector<char>(9, ' ');
        current_player = 'X';
    }

    /**
     * 克隆当前游戏状态，返回一个独立的游戏副本
     */
    TicTacToe clone() const {
        TicTacToe cloned;
        cloned.board = this->board;
        cloned.current_player = this->current_player;
        return cloned;
    }

    /**
     * 返回棋盘上所有可用位置的列表（未被占据的位置）
     */
    vector<int> available_moves() const {
        vector<int> moves;
        for (int i = 0; i < 9; i++) {
            if (board[i] == ' ') {
                moves.push_back(i);
            }
        }
        return moves;
    }

    /**
     * 在指定位置下棋，然后切换当前玩家
     */
    void play_move(int move) {
        board[move] = current_player;
        current_player = (current_player == 'X') ? 'O' : 'X';
    }

    /**
     * 检查是否有赢家，返回赢家标记（'X'或'O'）或'\0'（无赢家）
     */
    char winner() const {
        vector<vector<int>> lines = {
            {0, 1, 2}, {3, 4, 5}, {6, 7, 8},
            {0, 3, 6}, {1, 4, 7}, {2, 5, 8},
            {0, 4, 8}, {2, 4, 6}
        };
        
        for (const auto& line : lines) {
            int a = line[0], b = line[1], c = line[2];
            if (board[a] == board[b] && board[b] == board[c] && board[a] != ' ') {
                return board[a];
            }
        }
        return '\0';  // 无赢家
    }

    /**
     * 判断游戏是否结束（有赢家或棋盘满）
     */
    bool is_terminal() const {
        if (winner() != '\0') return true;
        for (char c : board) {
            if (c == ' ') return false;
        }
        return true;
    }

    /**
     * 打印棋盘到控制台
     */
    void print_board() const {
        cout << "\n";
        for (int i = 0; i < 3; i++) {
            cout << " " << board[i*3] << " | " << board[i*3+1] << " | " << board[i*3+2] << "\n";
            if (i < 2) cout << "-----------\n";
        }
        cout << "\n";
    }
};


// ---------- MCTS 节点 ----------
class Node {
    /**
     * MCTS 搜索树的节点类，管理节点状态、访问统计和子节点
     */
public:
    TicTacToe state;              // 该节点对应的游戏状态
    Node* parent;                 // 父节点引用
    int move;                     // 从父节点到该节点的移动
    vector<Node*> children;       // 子节点列表
    int visits;                   // 该节点被访问的次数
    double wins;                  // 该节点的胜利次数
    vector<int> untried_moves;    // 未被尝试的移动列表

    /**
     * 初始化节点
     * 参数:
     *   state: 该节点对应的游戏状态
     *   parent: 父节点引用
     *   move: 从父节点到该节点的移动
     */
    Node(const TicTacToe& state, Node* parent = nullptr, int move = -1)
        : state(state), parent(parent), move(move), visits(0), wins(0.0) {
        untried_moves = state.available_moves();
    }

    /**
     * 析构函数：递归删除所有子节点
     */
    ~Node() {
        for (Node* child : children) {
            delete child;
        }
    }

    /**
     * 判断该节点是否已完全展开（所有未尝试的移动都已尝试过）
     */
    bool is_fully_expanded() const {
        return untried_moves.empty();
    }

    /**
     * 使用UCB（Upper Confidence Bound）算法选择最优子节点
     * 参数:
     *   c_param: 探索参数（默认1.4），控制探索vs利用的权衡
     * 返回:
     *   权重最高的子节点
     */
    Node* best_child(double c_param = 1.4) const {
        double best_ucb = -1e9;
        Node* best = nullptr;

        for (Node* child : children) {
            double exploitation = child->wins / (child->visits + 1e-8);
            double exploration = c_param * sqrt(log(visits + 1) / (child->visits + 1e-8));
            double ucb = exploitation + exploration;

            if (ucb > best_ucb) {
                best_ucb = ucb;
                best = child;
            }
        }
        return best;
    }

    /**
     * 展开节点：从未尝试的移动中选择一个，创建新的子节点
     * 返回:
     *   新创建的子节点
     */
    Node* expand() {
        // 从未尝试的移动列表中移除并选择最后一个移动
        int move = untried_moves.back();
        untried_moves.pop_back();

        // 创建新的游戏状态
        TicTacToe new_state = state.clone();
        new_state.play_move(move);

        // 创建新的节点
        Node* child = new Node(new_state, this, move);
        children.push_back(child);
        return child;
    }

    /**
     * 更新节点的访问统计信息
     * 参数:
     *   result: 模拟结果（1.0表示X胜，0.0表示O胜或平局，0.5表示平局等）
     */
    void update(double result) {
        visits++;
        wins += result;
    }
};


// ---------- 随机模拟 ----------
/**
 * 从指定状态开始进行随机游玩，直到游戏结束，返回结果
 * 参数:
 *   state: 当前游戏状态
 * 返回:
 *   1.0: X胜利
 *   0.0: O胜利
 *   0.5: 平局
 */
double simulate(TicTacToe state) {
    while (!state.is_terminal()) {
        vector<int> moves = state.available_moves();
        int random_move = moves[rand() % moves.size()];
        state.play_move(random_move);
    }
    
    char win = state.winner();
    if (win == 'X') return 1.0;
    else if (win == 'O') return 0.0;
    else return 0.5;
}


// ---------- MCTS 算法 ----------
/**
 * 执行 MCTS 搜索算法
 * MCTS四个阶段：
 * 1. Selection（选择）：沿着已建立的树向下选择，直到找到未完全展开的节点
 * 2. Expansion（展开）：向树中添加一个新的子节点
 * 3. Simulation（模拟）：从新节点进行随机游玩到游戏结束
 * 4. Backpropagation（回溯）：将游玩结果沿着树向上回溯，更新节点统计
 * 
 * 参数:
 *   root_state: 初始游戏状态
 *   iter_limit: 迭代次数（默认300）
 * 返回:
 *   最优的移动位置
 */
int mcts(const TicTacToe& root_state, int iter_limit = 300) {
    Node* root = new Node(root_state);

    for (int i = 0; i < iter_limit; i++) {
        Node* node = root;
        TicTacToe state = root_state.clone();

        // 1️⃣ Selection（选择阶段）：找到最有前景的未完全展开的节点
        while (node->is_fully_expanded() && !node->children.empty()) {
            node = node->best_child();
            state.play_move(node->move);
        }

        // 2️⃣ Expansion（展开阶段）：向未完全展开的节点添加一个新子节点
        if (!node->is_fully_expanded() && !state.is_terminal()) {
            node = node->expand();
            state.play_move(node->move);
        }

        // 3️⃣ Simulation（模拟阶段）：从新节点进行随机游玩到游戏结束
        double result = simulate(state);

        // 4️⃣ Backpropagation（回溯阶段）：将结果沿着树向上回溯，更新所有访问过的节点
        while (node != nullptr) {
            // 根据当前玩家调整结果
            double adjusted_result = (node->state.current_player == 'O') ? result : (1.0 - result);
            node->update(adjusted_result);
            node = node->parent;
        }

        if ((i + 1) % 50 == 0) {
            cout << "迭代 " << (i + 1) << "/" << iter_limit << " 完成\n";
        }
    }

    // 找到访问次数最多的子节点（最优移动）
    Node* best_child = nullptr;
    int max_visits = -1;
    for (Node* child : root->children) {
        if (child->visits > max_visits) {
            max_visits = child->visits;
            best_child = child;
        }
    }

    // 输出搜索结果统计
    cout << "\n搜索完成！移动统计信息:\n";
    for (Node* child : root->children) {
        double win_rate = child->wins / (child->visits + 1e-8);
        cout << "移动 " << child->move << ": 访问次数=" << child->visits 
             << ", 胜率=" << fixed << setprecision(2) << win_rate << "\n";
    }

    int best_move = best_child->move;
    delete root;  // 释放整个搜索树
    return best_move;
}


// ---------- 主程序 ----------
int main() {
    srand(static_cast<unsigned>(time(0)));

    TicTacToe game;
    cout << "===== MCTS 井字棋游戏 =====\n";
    cout << "X: AI (MCTS算法)\n";
    cout << "O: 随机玩家\n\n";

    int move_count = 0;
    while (!game.is_terminal()) {
        game.print_board();
        cout << "当前玩家: " << game.current_player << "\n";

        int move;
        if (game.current_player == 'X') {
            cout << "MCTS 正在搜索最佳落子...\n";
            move = mcts(game, 400);
            cout << "MCTS 选择位置: " << move << "\n";
        } else {
            vector<int> available = game.available_moves();
            move = available[rand() % available.size()];
            cout << "随机玩家选择位置: " << move << "\n";
        }

        game.play_move(move);
        move_count++;

        // 检查游戏是否结束
        char win = game.winner();
        if (win != '\0') {
            game.print_board();
            cout << "🏆 " << win << " 获胜！ (经过 " << move_count << " 步)\n";
            break;
        }

        if (game.available_moves().empty()) {
            game.print_board();
            cout << "🤝 平局！(经过 " << move_count << " 步)\n";
            break;
        }
    }

    return 0;
}
