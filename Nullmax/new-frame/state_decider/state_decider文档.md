<center><span style="font-size:2rem;font-weight:bold;">State Decider介绍</span></center>

<div style="page-break-after: always;"></div>

[toc]



<div style="page-break-after: always;"></div>

# 介绍

state_decider是nullmax时空联合高阶框架中的一环，主要负责的是当前状态state以及action的选择。

入口函数是在behavior_mcts_planner中的最后一个内容，semantic_forest_seach中的一环，主要的作用就是枚举出可能得action列表。然后给到下游决策做树搜索。

# 流程框架

```
```





# 具体函数介绍



