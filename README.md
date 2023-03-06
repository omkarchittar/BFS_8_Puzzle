# **BFS 8 Puzzle**

## **File Tree**

```text
proj1_omkar_chittar
+-final.py
+-nodePath.txt
+-Nodes.txt
+-NodesInfo.txt
+-plot_path.py
+-README.md
```

## **Installation and Running**

1. Download and extract the files.

2. Run the code final.py using the following command in your terminal
    ***python3 main.py***
    - Choose a test case from 1 or 2 to run by uncommenting the inputs OR change values for *nodeInitial* and *nodeGoal* for a custom test case 

3. To visualize the path taken from the initial_node to the goal_node, run
    ***python3 plot_path.py***

4. nodePath.txt : Displays the nodewise path taken to reach the goal_node

5. Nodes.txt : Displays all the nodes that were visited before finiding the goal_node

6. NodesInfo.txt : Displays all the nodes visited along with their node_number and their respective parent_node_number
    **format : [node_number, ParentNode, nodeState]**          
