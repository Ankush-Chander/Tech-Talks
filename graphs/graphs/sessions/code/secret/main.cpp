#include <iostream>
#include <queue>
#include <utility>
#include <vector>
#include <fstream>

using namespace::std;

int dfs(int node, vector<int>& allowed_time, vector<int>& adj[]) {

}


int main() {
    // Read input from standard input
    int nodes, edges;
    cin >> nodes >> edges;
    cout << "nodes: " << nodes << " edges: " << edges << endl;
    vector<int> adj[nodes+1];

    // process allowed_time
    vector<int> allowed_time(nodes+1);
    priority_queue<pair<int, int>> pq;
    for(int i = 0; i < nodes; ++i) {
        cin >> allowed_time[i+1];
        pq.push(make_pair(allowed_time[i+1], i+1));
    }

    // print allowed_time
    for(int i = 0; i <= nodes+1; ++i) {
        cout << i+1 << ": " << allowed_time[i+1] << " ";
    }
    // cout << endl;

    // Process input
    for(int i = 0; i < edges; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    // print adj
    for(int i = 1; i <= nodes; ++i) {
        cout << i << ": ";
        for(int j = 0; j < adj[i].size(); ++j) {
            cout << adj[i][j] << " ";
        }
        cout << endl;
    }


    std::cout << "" << std::endl;

    while(!pq.empty()) {
        pair<int, int> p = pq.top();
        int node = p.second;
        int time = p.first;

        pq.pop();
        # for each
        cout << "processing " << time << " " << node << endl;

    }
}
